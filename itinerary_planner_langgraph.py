
# itinerary_planner_langgraph.py

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = "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"

from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional

# Define state structure for LangGraph
class ItineraryState(TypedDict):
    inputs: dict
    location_data: Optional[str]
    guide_data: Optional[str]
    plan_data: Optional[str]

# Initialize Groq LLM
llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=os.environ.get("GROQ_API_KEY")
)

# Optional tool (not yet used)
search_tool = DuckDuckGoSearchResults(num_results=5)

# User inputs
user_inputs = {
    "from_city": "India",
    "destination_city": "Rome",
    "date_from": "1st March 2025",
    "date_to": "7th March 2025",
    "interests": "sightseeing and good food"
}

def init_state():
    return {"inputs": user_inputs, "location_data": None, "guide_data": None, "plan_data": None}

# Agent 1: Location Agent
location_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a travel logistics expert for the destination city."),
    ("human", "Provide travel and cultural insights for:
City: {destination_city}, Dates: {date_from} to {date_to}")
])
location_agent = location_prompt | llm | StrOutputParser()
def run_location_agent(state):
    inputs = state["inputs"]
    result = location_agent.invoke(inputs)
    return {**state, "location_data": result}

# Agent 2: Guide Agent
guide_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly local guide."),
    ("human", "Based on these interests ({interests}), recommend:
- Top local experiences
- Foods to try
- Hidden gems
in {destination_city}")
])
guide_agent = guide_prompt | llm | StrOutputParser()
def run_guide_agent(state):
    inputs = state["inputs"]
    result = guide_agent.invoke(inputs)
    return {**state, "guide_data": result}

# Agent 3: Planner Agent
planner_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior itinerary planner."),
    ("human", "Using the following:
Location Info: {location_data}
Guide Suggestions: {guide_data}
Create a 5-day itinerary in Markdown.")
])
planner_agent = planner_prompt | llm | StrOutputParser()
def run_planner_agent(state):
    result = planner_agent.invoke(state)
    return {**state, "plan_data": result}

# Build LangGraph
workflow = StateGraph(ItineraryState)
workflow.add_node("location_agent", RunnableLambda(run_location_agent))
workflow.add_node("guide_agent", RunnableLambda(run_guide_agent))
workflow.add_node("planner_agent", RunnableLambda(run_planner_agent))
workflow.set_entry_point("location_agent")
workflow.add_edge("location_agent", "guide_agent")
workflow.add_edge("guide_agent", "planner_agent")
workflow.add_edge("planner_agent", END)

# Run graph
app = workflow.compile()
final_state = app.invoke(init_state())

# Print final result
print("\n=== Final Travel Itinerary ===\n")
print(final_state["plan_data"])
