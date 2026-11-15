import pandas as pd

sales = pd.DataFrame({
    "city": ["Karachi", "Lahore", "Karachi", "Lahore", "Karachi"],
    "amount": [100, 200, 150, 50, 300]
})

total_sales = sales.groupby("city")["amount"].sum()

print("Total Sales:")
print(total_sales)

print("\nCity with Highest Sales:")
print(total_sales.idxmax())




import pandas as pd

employees = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ali", "Sara", "Omar"]
})

salaries = pd.DataFrame({
    "id": [1, 2, 3],
    "salary": [50000, 60000, 45000]
})

result = pd.merge(employees, salaries, on="id")

print("Merged Employee Data:")
print(result)