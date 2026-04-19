import streamlit as st
import asyncio
import google.generativeai as genai

import os
from data_loader import load_data
from tools import Tools
from agent import SupportAgent, process_all
from dotenv import load_dotenv
load_dotenv()


# -------- GEMINI SETUP --------
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# -------- LOAD DATA --------
tickets, orders, customers, products, kb = load_data()

tools = Tools(orders, customers, products, kb)
agent = SupportAgent(tools, model)

# -------- PAGE --------
st.set_page_config(page_title="Support Agent", layout="wide")

st.title("🤖 ShopWave Support Agent")

# -------- SIDEBAR --------
st.sidebar.header("Options")

ticket_ids = [t["ticket_id"] for t in tickets]
selected = st.sidebar.multiselect(
    "Select Tickets",
    ticket_ids,
    default=ticket_ids[:5]  # smaller default
)

run = st.sidebar.button("Run Agent")

# -------- STATUS HELPER --------
def get_status(result):
    if "Escalated" in str(result):
        return "Escalated"
    elif "Reply sent" in str(result) or "Refund" in str(result):
        return "Resolved"
    return "Other"

# -------- MAIN --------
if run:

    selected_tickets = [t for t in tickets if t["ticket_id"] in selected]

    st.write("### Processing Tickets...")

    results = asyncio.run(process_all(selected_tickets, agent))

    # -------- SUMMARY --------
    st.write("### Summary")

    total = len(results)
    resolved = sum(get_status(r["result"]) == "Resolved" for r in results)
    escalated = sum(get_status(r["result"]) == "Escalated" for r in results)

    st.write(f"Total: {total}")
    st.write(f"Resolved: {resolved}")
    st.write(f"Escalated: {escalated}")

    st.divider()

    # -------- RESULTS --------
    for res in results:

        st.subheader(res["ticket_id"])

        st.write("**Decision:**", res["decision"]["action"])
        st.write("**Reason:**", ", ".join(res["decision"]["reasons"]))

        st.write("**Result:**", res["result"])

        with st.expander("View Logs"):
            st.json(res["log"])

        st.divider()

else:
    st.write("Select tickets from sidebar and click 'Run Agent'")