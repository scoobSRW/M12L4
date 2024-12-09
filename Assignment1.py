class OrderQueue:
    def __init__(self):
        self.orders = []

    def post_order(self, order):
        """Adds an order to the end of the queue."""
        self.orders.append(order)

    def delete_order(self):
        """Removes and returns the first order from the queue."""
        if not self.is_empty():
            return self.orders.pop(0)

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.orders) == 0

    def size(self):
        """Returns the number of orders in the queue."""
        return len(self.orders)

    def display_orders(self):
        """Display all orders categorized into Antipasti, Primi, Secondi, Contorni, Dolci, and Bevande."""
        if self.is_empty():
            print("No orders in the queue.")
            return

        print("Orders in the queue by category:")
        categories = ["Antipasti", "Primi", "Secondi", "Contorni", "Dolci", "Bevande"]
        categorized_orders = {category: [] for category in categories}

        for order in self.orders:
            category = order.get("category", "Uncategorized")
            if category in categorized_orders:
                categorized_orders[category].append(order)
            else:
                categorized_orders["Uncategorized"] = categorized_orders.get("Uncategorized", []) + [order]

        for category, orders in categorized_orders.items():
            print(f"\n{category}:")
            if orders:
                for order in orders:
                    print(
                        f"- {order['table']} with {order['guest_num']} guests ordered: {order['order']} @ {order['timestamp']}")
            else:
                print("  No orders in this category.")


order_queue = OrderQueue()

order_queue.post_order({
    "id": 1,
    "table": "table1",
    "guest_num": 2,
    "order": "Zuppa di Fagioli, Ribeye Steak, a glass of Chianti",
    "timestamp": "2024-12-09 18:00",
    "category": "Primi"
})

order_queue.post_order({
    "id": 2,
    "table": "table2",
    "guest_num": 3,
    "order": "Tiramisu, Espresso",
    "timestamp": "2024-12-09 18:15",
    "category": "Dolci"
})

order_queue.post_order({
    "id": 3,
    "table": "table3",
    "guest_num": 1,
    "order": "Caesar Salad, a glass of Prosecco",
    "timestamp": "2024-12-09 18:20",
    "category": "Antipasti"
})

order_queue.display_orders()

print("\nProcessing the first order...")
order_queue.delete_order()
order_queue.display_orders()
