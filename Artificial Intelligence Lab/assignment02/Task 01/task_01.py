
orders = [
    ('Tea', 80, 4),
    ('Coffee', 200, 2),
    ('Cake', 350, 1),
    ('Tea', 80, 6),
    ('Coffee', 200, 3),
    ('Sandwich', 250, 2)
]

qty_total = {}
revenue_total = {}

for item, price, qty in orders:
    qty_total[item] = qty_total.get(item, 0) + qty
    revenue_total[item] = revenue_total.get(item, 0) + price * qty

leaderboard = sorted(
    revenue_total.items(),
    key=lambda kv: (-kv[1], kv[0])
)

print("Cafe Sales Leaderboard")

for rank, (item, revenue) in enumerate(leaderboard, start=1):
    print(f"{rank}. {item} - Revenue: {revenue}")

print("\nTotal Quantity:")
print(qty_total)

print("\nTotal Revenue:")
print(revenue_total)

above_500 = list(filter(lambda kv: kv[1] > 500, revenue_total.items()))

print("\nItems with revenue above 500:")
print(above_500)

names, revenues = zip(*leaderboard)

print("\nUnzipped Leaderboard:")
print("Names:", names)
print("Revenues:", revenues)

best_selling = max(qty_total.items(), key=lambda kv: kv[1])

print(f"\nBest selling item by quantity: {best_selling[0]}")
print(f"Quantity sold: {best_selling[1]}")




