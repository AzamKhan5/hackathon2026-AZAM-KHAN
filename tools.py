import random

class Tools:
    def __init__(self, orders, customers, products, kb):
        self.orders = orders
        self.customers = customers
        self.products = products
        self.kb = kb

    def maybe_fail(self):
        if random.random() < 0.2:
            raise Exception("Tool timeout / malformed response")

    def get_customer(self, email):
        self.maybe_fail()
        return next((c for c in self.customers if c["email"] == email), None)

    def get_order(self, order_id):
        self.maybe_fail()
        return next((o for o in self.orders if o["order_id"] == order_id), None)

    def get_product(self, product_id):
        self.maybe_fail()
        return next((p for p in self.products if p["product_id"] == product_id), None)

    def search_knowledge_base(self, query):
        self.maybe_fail()
        return self.kb[:500]  # simulate semantic search

    def check_refund_eligibility(self, order_id):
        self.maybe_fail()
        return {"eligible": True, "reason": "Within policy"}

    def issue_refund(self, order_id, amount):
        self.maybe_fail()
        return f"Refund of ${amount} issued for {order_id}"

    def send_reply(self, ticket_id, message):
        return f"Reply sent to {ticket_id}: {message}"

    def escalate(self, ticket_id, summary, priority):
        return f"Escalated {ticket_id} with priority {priority}: {summary}"