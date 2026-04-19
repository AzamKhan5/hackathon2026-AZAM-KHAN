# 🤖 ShopWave Autonomous Support Agent

> An AI-powered system that **resolves customer support tickets end-to-end** using tool-based reasoning, policy awareness, and autonomous decision-making.

---

## 🚀 Live Demo

- 🌐 **Streamlit App**: https://hackathon2026-azam-khan.streamlit.app/  
- 💻 **GitHub Repo**:  https://github.com/AzamKhan5/hackathon2026-AZAM-KHAN.git 
- 🎥 **Demo Video**:  
https://github.com/user-attachments/assets/12f07612-992c-45d4-a358-d15fedf95461

---

## 🧠 Problem

ShopWave receives hundreds of daily support tickets.  
Most are repetitive, yet all require manual handling.

This leads to:
- ⏳ Slow response times  
- 💰 High operational cost  
- ❌ Inconsistent decisions  

---

## 💡 Solution

This project builds an **Autonomous Support Resolution Agent** that:

- Understands customer queries  
- Fetches relevant data (orders, customers, products)  
- Applies company policies  
- Takes real actions (refunds, cancellations, escalation)  

👉 It doesn’t just classify — it **resolves**.

---

## ⚙️ Key Features

- 🔗 **Multi-step Tool Chaining** (≥3 calls per ticket)
- ⚡ **Concurrent Processing** (async execution)
- 🛡️ **Failure Resilience** (timeouts, missing data)
- 🧠 **Policy-Aware Decisions** via knowledge base
- 📊 **Full Audit Logging** (transparent reasoning)
- 🤖 **Autonomous Execution** (refunds, replies, escalation)

---

## 🏗️ Architecture

<img width="797" height="720" alt="Image" src="https://github.com/user-attachments/assets/328bd305-c984-4715-b990-11c0bc56fed3" />

## 🔄 Agent Workflow

### Example Flow

1. Extract order ID  
2. Fetch customer + order  
3. Retrieve product + policy  
4. Decide action  
5. Execute:
   - Refund
   - Cancel
   - Reply
   - Escalate  

---

## 🧰 Tech Stack

| Layer | Technology |
|------|-----------|
| Language | Python |
| LLM | Gemini API |
| UI | Streamlit |
| Concurrency | AsyncIO |
| Data | JSON |
| Logic | Rule + LLM Hybrid |

---

## 📂 Project Structure
shopwave-agent/
├── app.py
├── agent.py
├── tools.py
├── data_loader.py
├── tickets.json
├── orders.json
├── customers.json
├── products.json
├── knowledge-base.md
├── architecture.png
├── audit_log.json
├── failure_modes.md


---

## 📊 Observability

Each ticket logs:

Tool calls
Failures
Decisions
Final action

### 👉 See: audit_log.json

## ⚠️ Failure Handling

### Handled scenarios include:

Tool timeouts
Missing order ID
Invalid requests
Policy conflicts

### 👉 See: failure_modes.md

## 🧠 Key Insight

Data tells the agent what happened.
Policy tells it what to do.

## 🚀 Future Improvements
Function-calling LLM agent
Vector DB for knowledge retrieval
Retry & backoff strategies
Real-time streaming reasoning
Metrics dashboard
🏁 Conclusion

This project demonstrates how AI agents can:

Think
Act
Recover
Scale

## 👉 Moving beyond chatbots → toward real autonomous systems

## 👤 Author
# AZAM KHAN
