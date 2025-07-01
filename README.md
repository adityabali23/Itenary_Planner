# Itenary_Planner
# ✈️ AI-Powered Travel Itinerary Planner (Groq + LangGraph)

This project is a multi-agent AI itinerary planner built using **LangGraph**, **LangChain**, and **Groq's LLaMA 3 model** (`llama3-70b-8192`). It creates a customized, day-wise travel itinerary based on your inputs — such as origin, destination, dates, and interests — using intelligent prompt agents.

---

## 🚀 Features

* **Multi-Agent Architecture** powered by `LangGraph`:

  * 🧭 `Location Agent`: Provides travel logistics, cultural info, and weather insights
  * 🗺️ `Guide Agent`: Recommends top experiences, foods, and attractions
  * 📋 `Planner Agent`: Compiles a full 5-day itinerary with time slots and highlights

* Uses **Groq LLaMA 3 (70B)** for blazing fast, high-quality natural language generation

* Modular and extendable using **LangChain** components

* Output is formatted with **emojis and Markdown**, ready for export or sharing

---

## 🛠 Tech Stack

* [LangChain](https://www.langchain.com/) – for prompt chaining, output parsing
* [LangGraph](https://docs.langgraph.dev/) – to design and run multi-agent flows
* [Groq](https://console.groq.com/) – inference backend (LLaMA 3)
* Python – scripting and orchestration
* dotenv – environment variable management
* *(Optional)* DuckDuckGo search tool

---

## 📦 Project Structure

```
├── itinerary_planner_langgraph.py   # Main multi-agent planner script
├── .env                             # Store your GROQ_API_KEY securely
├── README.md                        # Project documentation
└── requirements.txt                 # Required Python packages
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ai-itinerary-planner.git
cd ai-itinerary-planner
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up your API key** in a `.env` file:

```
GROQ_API_KEY=your-api-key-here
```

4. **Run the script**

```bash
python itinerary_planner_langgraph.py
```

---

## 📤 Sample Output

```
=== Final Travel Itinerary ===

🇮🇹 Welcome to Rome! Here's your personalized 5-day itinerary...
- 🏛️ Day 1: Colosseum, Roman Forum...
- 🍝 Food: Cacio e Pepe, Gelato...
...
```

---

## 🔮 Future Enhancements

* Export itinerary as `.md`, `.pdf`, or `.json`
* Add real-time event search via DuckDuckGo
* Budget planner or accommodation recommendation agent
* Streamlit UI for end-user interaction

---

## 🧠 Credits

Built using LangGraph, LangChain, and Groq.

---

## 📜 License

MIT License – free to use, modify, and distribute.
