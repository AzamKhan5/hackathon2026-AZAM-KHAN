import re
import asyncio

class SupportAgent:

    def __init__(self, tools, model):
        self.tools = tools
        self.model = model

    # ---------------- SAFE TOOL CALL ----------------
    def safe_call(self, tool_name, *args, log=[]):
        try:
            tool = getattr(self.tools, tool_name)
            result = tool(*args)
            log.append({"tool": tool_name, "status": "success", "output": str(result)})
            return result
        except Exception as e:
            log.append({"tool": tool_name, "status": "failed", "error": str(e)})
            return None

    # ---------------- EXTRACT ORDER ID ----------------
    def extract_order_id(self, text):
        match = re.search(r"ORD-\d+", text)
        return match.group(0) if match else None

    # ---------------- REASONING ----------------
    def reason(self, ticket, customer, order, product, kb):
        reasons = []

        # SAFE fallback
        kb_text = kb.lower() if isinstance(kb, str) else ""

        if not customer:
            reasons.append("Customer not found")
            return {"action": "ask_info", "reasons": reasons}

        if not order:
            reasons.append("Order not found")
            return {"action": "ask_info", "reasons": reasons}

        if order.get("refund_status") == "refunded":
            reasons.append("Already refunded")
            return {"action": "inform", "reasons": reasons}

        body = (ticket.get("body") or "").lower()

        if "damaged" in body or "broken" in body:
            reasons.append("Damaged item")
            return {"action": "refund", "reasons": reasons}

        if "cancel" in body and order["status"] == "processing":
            reasons.append("Cancelable order")
            return {"action": "cancel", "reasons": reasons}

        # FIXED LINE
        if "warranty" in kb_text:
            reasons.append("Warranty case")
            return {"action": "escalate", "reasons": reasons}

        reasons.append("Default reply")
        return {"action": "reply", "reasons": reasons}

    # ---------------- EXECUTION ----------------
    async def execute(self, decision, ticket, order, log):

        if decision["action"] == "refund":

            # Tool 1
            eligibility = self.safe_call("check_refund_eligibility", order["order_id"], log=log)

            if not eligibility or not eligibility.get("eligible"):
                return self.safe_call("send_reply", ticket["ticket_id"],
                                      "Refund not eligible", log=log)

            # Tool 2
            self.safe_call("issue_refund", order["order_id"], order["amount"], log=log)

            # Tool 3
            return self.safe_call("send_reply", ticket["ticket_id"],
                                  "Your refund has been processed.", log=log)

        elif decision["action"] == "cancel":
            return self.safe_call("send_reply", ticket["ticket_id"],
                                  "Your order has been cancelled.", log=log)

        elif decision["action"] == "escalate":
            return self.safe_call("escalate",
                                  ticket["ticket_id"],
                                  "Warranty claim",
                                  "high",
                                  log=log)

        elif decision["action"] == "ask_info":
            return self.safe_call("send_reply", ticket["ticket_id"],
                                  "Please provide order ID.", log=log)

        elif decision["action"] == "inform":
            return self.safe_call("send_reply", ticket["ticket_id"],
                                  "Refund already processed. Please wait 5–7 days.", log=log)

        return self.safe_call("send_reply", ticket["ticket_id"],
                              "We are reviewing your request.", log=log)

    # ---------------- MAIN PIPELINE ----------------
    async def process_ticket(self, ticket):
        log = []

        customer = self.safe_call("get_customer", ticket["customer_email"], log=log)

        order_id = self.extract_order_id(ticket["body"] or "")
        order = self.safe_call("get_order", order_id, log=log) if order_id else None

        product = None
        if order:
            product = self.safe_call("get_product", order["product_id"], log=log)

        kb = self.safe_call("search_knowledge_base", ticket["subject"], log=log)

        decision = self.reason(ticket, customer, order, product, kb)

        result = await self.execute(decision, ticket, order, log)

        return {
            "ticket_id": ticket["ticket_id"],
            "decision": decision,
            "log": log,
            "result": result
        }


# ---------------- CONCURRENT PROCESSING ----------------
async def process_all(tickets, agent):
    tasks = [agent.process_ticket(t) for t in tickets]
    return await asyncio.gather(*tasks)