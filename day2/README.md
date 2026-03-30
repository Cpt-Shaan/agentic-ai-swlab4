# Assignment 2 – Tool Using AI Agent

## Overview

This assignment extends the basic rule-based AI agent to support **tool usage**.
The agent can decide which tool to use based on user input and call the corresponding function.

This demonstrates the concept of **Agent + Tools**, which is a key component of **Agentic AI systems**.

---

# Objective

The goal of this assignment is to:

* Enable an AI agent to use **external tools**
* Implement **tool abstraction**
* Build a **modular agent architecture**

---

# Features

The agent supports three tools:

| Tool            | Description                             |
| --------------- | --------------------------------------- |
| Calculator      | Performs mathematical calculations      |
| Weather         | Returns weather information (mock data) |
| Text Summarizer | Summarizes text using an LLM            |

If the input does not match any tool, the agent queries the **Groq LLM** directly.

---

# Technologies Used

* Python 3.9+
* Groq API
* Llama-3.3-70B-Versatile model
* python-dotenv

---

# Project Structure

```
agentic-ai-lab/
│
├── assignment2_tool_agent/
│   ├── agent.py
│   ├── tools.py
│   ├── main.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

### Clone repository

```
git clone <repo-url>
cd agentic-ai-lab
```

### Create virtual environment

```
python -m venv venv
```

Activate:

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

### Install dependencies

```
pip install -r requirements.txt
```

---

# Configure API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

# Running the Program

```
python assignment2_tool_agent/main.py
```

---

# Example Usage

```
User > calculate 4 + 6
Agent > Result: 10

User > weather mumbai
Agent > Weather in Mumbai: 30°C, Humid

User > summarize Artificial intelligence enables machines to learn from data.
Agent > Artificial intelligence allows machines to analyze data and learn patterns to perform tasks.

User > explain neural networks
Agent > (LLM response)
```

---

# Code Explanation

## tools.py

Defines all tools used by the agent:

* `calculator()` – evaluates mathematical expressions
* `weather()` – returns mock weather data
* `summarize_text()` – summarizes text using Groq LLM

---

## agent.py

Contains the core **agent logic**.

Steps performed:

1. Receive user query
2. Detect intent
3. Select tool
4. Execute tool
5. Return result

---

## main.py

Acts as the **entry point** for the program and runs the interactive loop.

---

# Learning Outcomes

Through this assignment we learn:

* Tool abstraction in AI agents
* Function calling from agents
* Modular programming
* Integrating APIs with agents
* Building extensible agent systems

---

# Future Improvements

* Add more tools (Search API, File Reader, Web Scraper)
* Use LangChain Tool interface
* Implement automatic tool selection via LLM
* Build multi-agent systems
