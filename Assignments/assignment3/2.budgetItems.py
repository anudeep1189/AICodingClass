# 2. Given a dictionary of item prices, ask the user for a budget and display which items can be bought within that budget.

itemPrices = {
    "laptop": 1200.56,
    "mouse": 25.00,
    "keyboard": 75.34,
    "monitor": 300,
    "webcam": 50,
    "headphones": 150
}

budget = float(input("Enter your budget: "))

items = []
for item, price in itemPrices.items():
    if price <= budget:
        items.append(item)

print(f"Items you can buy within your budget of {budget}: {items}")