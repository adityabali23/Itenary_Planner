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

**Rome Travel Itinerary (March 1st-7th, 2025)**

**Day 1: Arrival and Exploration of the Historic Center**

* 9:00 AM: Arrive at Rome's Leonardo da Vinci–Fiumicino Airport (FCO) 🛬
* 10:00 AM: Take the Leonardo Express train to Termini Station (€15, 30 minutes) 🚂
* 11:00 AM: Check-in to your hotel in the Historic Center and freshen up 🏨
* 12:00 PM: Visit the Pantheon (free admission) and explore the surrounding streets 🏯
* 1:00 PM: Enjoy lunch at a local trattoria, trying **Carbonara** and **Pizza Romana** 🍝
* 2:30 PM: Explore the Trevi Fountain and toss a coin into the water 💧
* 4:00 PM: Visit the Spanish Steps and enjoy the lively atmosphere 🏃‍♀️
* 7:00 PM: Enjoy an **Aperitivo** at a local enoteca, like Enoteca Ferrara 🍷
* 9:00 PM: Dine at a cozy restaurant in the Historic Center, trying **Trippa** and **Gelato** for dessert 🍴

**Day 2: Vatican City and Trastevere**

* 9:00 AM: Visit the Vatican Museums (tickets from €20) and explore the Sistine Chapel 🎨
* 12:00 PM: Enjoy lunch at a local osteria, trying **Supplì** and **Pizza al Taglio** 🍕
* 1:30 PM: Explore the charming neighborhood of Trastevere, visiting Santa Maria in Trastevere church 🏰
* 4:00 PM: Take a stroll along the Tiber Island, enjoying the scenic views 🌊
* 7:00 PM: Enjoy dinner at a romantic restaurant in Trastevere, trying **Risotto alla Romana** 🍝
* 9:00 PM: Explore the lively nightlife of Trastevere, visiting bars and clubs 🍻

**Day 3: Ancient Rome and Street Food**

* 9:00 AM: Visit the Colosseum (tickets from €12) and explore the ancient ruins 🏛️
* 11:00 AM: Explore the Roman Forum and Palatine Hill 🏯
* 1:00 PM: Visit Campo de' Fiori market square and try **Supplì** and **Pizza al Taglio** 🍕
* 2:30 PM: Explore the charming streets of the Historic Center, visiting the Piazza Navona 🏃‍♀️
* 7:00 PM: Enjoy dinner at a local restaurant, trying **Cacio e Pepe** and **Tiramisù** 🍝
* 9:00 PM: Take a leisurely stroll around the city, enjoying the evening atmosphere 🌃

**Day 4: Hidden Gems and Local Experiences**

* 9:00 AM: Visit the Capuchin Crypt (tickets from €8) and explore the fascinating site 💀
* 11:00 AM: Explore the Doria Pamphilj Gallery (tickets from €12) and admire the stunning art collection 🎨
* 1:00 PM: Enjoy lunch at a local enoteca, trying **Trippa** and **Gelato** 🍝
* 2:30 PM: Visit the Park of the Aqueducts and enjoy the peaceful atmosphere 🌳
* 4:00 PM: Take a guided tour of the Vatican Gardens (tickets from €20) 🌿
* 7:00 PM: Enjoy dinner at a local restaurant, trying **Risotto alla Romana** and **Panna Cotta** 🍝
* 9:00 PM: Explore the lively nightlife of the city, visiting bars and clubs 🍻

**Day 5: Festa della Donna and Departure**

* 9:00 AM: Celebrate International Women's Day at the Festa della Donna events around the city 🎉
* 11:00 AM: Visit the Museum of Castel Sant'Angelo (tickets from €14) and explore the stunning collection 🏰
* 1:00 PM: Enjoy lunch at a local trattoria, trying **Carbonara** and **Pizza Romana** 🍝
* 2:30 PM: Spend the afternoon shopping for souvenirs or exploring the city 🛍️
* 5:00 PM: Depart for the airport and fly back home 🛫️

**Buon viaggio!** 🇮🇹
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
