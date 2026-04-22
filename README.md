# 🔥 AI Autonomous Task Agent

An intelligent AI agent that understands user tasks, breaks them into steps, and executes them using LLM-powered reasoning and tool calling.

---

## 🚀 Overview

This project demonstrates an **agentic AI system** that can:

* 🧠 Interpret natural language input
* 🪜 Decompose tasks into steps (planning)
* ⚙️ Execute actions via tools (booking, reminders)
* 🔄 Run multi-step workflows using a controlled execution loop

Built using **LangGraph + LLM (OpenRouter/Gemini)** with a **Streamlit UI**.

---

## 💡 Features

* 🧠 **Multi-step reasoning (Planner + Executor)**
* ⚙️ **Tool calling system**

  * Book appointments
  * Set reminders
* 🔄 **Workflow control using LangGraph**
* 🧠 **State management & memory**
* 📊 **Interactive UI with Streamlit**
* 🔐 **Secure API handling using `.env`**

---

## 🛠️ Tech Stack

* **Python**
* **LangGraph**
* **LLM (OpenRouter / Gemini)**
* **Streamlit**
* **dotenv**

---

## 📂 Project Structure

```
AI-Autonomous-Task-Agent/
│── agent/
│   ├── agent.py
│   ├── executor.py
│   ├── graph.py
│   ├── memory.py
│   ├── planner.py
│   ├── state.py
│   ├── tools.py
│
│── utils/
│   ├── llm.py
│
│── app.py
│── README.md
│── requirements.txt
│── .gitignore
```

---

## ▶️ How to Run Locally

```bash
# 1. Clone repo
git clone https://github.com/<YOUR_USERNAME>/AI-Autonomous-Task-Agent.git

# 2. Go to project folder
cd AI-Autonomous-Task-Agent

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run app
streamlit run app.py
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

⚠️ Do NOT upload `.env` to GitHub.

---

## 🎯 Example Inputs

* Book a doctor appointment for tomorrow
* Book doctor and remind me at 9 AM
* Set reminder for meeting

---

## 📸 Demo

*(Add your screenshot here)*

```
![App Screenshot](https://github.com/SinghPriya5/AI-Autonomous-Task-Agent/blob/main/ss.png)
```

---

## ⚠️ Limitations

* Limited domain (appointments & reminders)
* Uses mock tools (no real API integration yet)
* Planner may occasionally generate extra steps (controlled via prompt)

---

## 🚀 Future Improvements

* ✅ Real API integration (Google Calendar, Email)
* 🧠 Better memory (user preferences)
* 🤖 Fully autonomous tool selection (JSON-based agent)
* 🌐 Deployment (Streamlit Cloud / Render)

---

## 🧠 Key Learning

This project demonstrates:

* Agentic AI architecture
* Multi-step reasoning workflows
* LLM + tool integration
* State-driven execution using LangGraph

---

## 💼 Resume Line (Use This)

> Built an AI Autonomous Task Agent using LangGraph capable of multi-step reasoning, tool execution, and workflow-based task automation.

---

## 📌 Author

**Priya Singh**
Aspiring AI / Data Science Professional 🚀

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
