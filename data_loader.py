import json

def load_data():
    with open("tickets.json") as f:
        tickets = json.load(f)

    with open("orders.json") as f:
        orders = json.load(f)

    with open("customers.json") as f:
        customers = json.load(f)

    with open("products.json") as f:
        products = json.load(f)

    with open("knowledge-base.md") as f:
        kb = f.read()

    return tickets, orders, customers, products, kb