# Assignment 3 – LLM Based AI Agent

## Overview

This assignment introduces an **LLM-driven AI agent** that uses a language model to decide which tool to use when answering a user query.

Unlike the previous assignment which used rule-based decision logic, this agent relies on a **Large Language Model (LLM)** to determine the appropriate action.

The system demonstrates the concept of **AI-driven tool selection**, which is an important component of modern **Agentic AI systems**.

---

# Objective

The goals of this assignment are:

* Integrate a **Large Language Model**
* Use the LLM to **select tools dynamically**
* Implement **tool execution**
* Maintain logs of agent activity

---

# Features

The agent supports three tools:

| Tool            | Description                        |
| --------------- | ---------------------------------- |
| Calculator      | Performs mathematical calculations |
| Weather         | Returns weather information        |
| Text Summarizer | Summarizes text using an LLM       |

If no tool is required, the agent directly queries the LLM.

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
├── assignment3_llm_agent/
│   ├── agent.py
│   ├── tools.py
│   ├── logger.py
│   ├── main.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

Clone repository

```
git clone <repo-url>
cd agentic-ai-lab
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Configure API Key

Create a `.env` file in the project root.

```
GROQ_API_KEY=your_api_key_here
```

---

# Running the Agent

```
python assignment3_llm_agent/main.py
```

---

# Example Usage

```
User > calculate 10 + 5
Agent > Result: 15

User > weather delhi
Agent > Weather in Delhi: 25°C, Clear sky

User > summarize Artificial intelligence is transforming industries worldwide.
Agent > Artificial intelligence is rapidly transforming industries by enabling machines to analyze data and automate tasks.

User > explain reinforcement learning
Agent > (LLM generated response)
```

---

# Code Explanation

## tools.py

Contains all external tools used by the agent.

* `calculator()` performs mathematical calculations
* `weather()` returns weather information
* `summarize_text()` summarizes text

---

## agent.py

Core component of the system.

Steps:

1. Receive user query
2. Ask the LLM which tool to use
3. Execute selected tool
4. Return the result
5. Log the interaction

---

## logger.py

Maintains a log file containing:

* User input
* Selected tool
* Output
* Timestamp

---

## main.py

Runs the interactive loop and handles user input.

---

# Learning Outcomes

Through this assignment we learn:

* Prompt-based decision making
* Integration of LLM APIs
* AI-based tool selection
* Logging and monitoring of agent decisions

---

# Future Improvements

Possible enhancements include:

* Adding more tools (web search, file reader, database query)
* Implementing LangChain tool agents
* Multi-agent collaboration
* Memory-based agents
