from inventory_utils import restock_quantity
import random

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity} = ${self.total_value():.2f}"


class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        base_value = super().total_value()
        if self.expiry_days < 5:
            return base_value * 0.8  # 20% discount
        return base_value

    def __repr__(self):
        return f"{self.name} (Perishable - {self.expiry_days} days) - ${self.price:.2f} x {self.quantity} = ${self.total_value():.2f}"


class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_inventory(self):
        for idx, item in enumerate(self.products, 1):
            print(f"{idx}. {item}")

    def search_by_name(self, term):
        results = list(filter(lambda p: term.lower() in p.name.lower(), self.products))
        return results

    def restock_all(self):
        for product in self.products:
            product.quantity += restock_quantity()

    def export_summary(self, filename="inventory_report.txt"):
        summary = {
            product.name: {
                "quantity": product.quantity,
                "total_value": round(product.total_value(), 2)
            }
            for product in self.products
        }

        with open(filename, "w") as f:
            f.write("Inventory Report\n")
            f.write("================\n")
            for name, info in summary.items():
                f.write(f"{name}: {info['quantity']} units - Total: ${info['total_value']}\n")

        print(f"Report saved to {filename}")


# Sample Usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Adding sample products
    manager.add_product(Product("Notebook", 3.5, 100))
    manager.add_product(PerishableProduct("Milk", 1.5, 50, 3))
    manager.add_product(PerishableProduct("Cheese", 2.0, 20, 7))
    manager.add_product(Product("Pen", 0.5, 200))

    print("\n📦 Inventory List:")
    manager.list_inventory()

    print("\n🔍 Search Results for 'milk':")
    results = manager.search_by_name("milk")
    for item in results:
        print(item)

    print("\n🔄 Restocking all items...")
    manager.restock_all()
    manager.list_inventory()

    print("\n📝 Exporting report...")
    manager.export_summary()
