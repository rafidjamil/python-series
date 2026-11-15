import pandas as pd

data = {
    'name': ['Ali', 'Sara', 'Usman', 'Ayesha', 'Bilal', 'Hina', 'Zain', 'Fatima'],
    'department': ['CS', 'CS', 'EE', 'CS', 'BBA', 'EE', 'BBA', 'CS'],
    'semester': [4, 6, 4, 2, 6, 8, 2, 8],
    'cgpa': [3.45, 3.82, 2.95, 3.15, 3.60, 3.30, 2.80, 2.90]
}
df = pd.DataFrame(data)

print("1. CS Students with CGPA above 3.0:")
print(df[(df['department'] == 'CS') & (df['cgpa'] > 3.0)])

print("\n2. Average CGPA of every department:")
print(df.groupby('department')['cgpa'].mean().round(2))

print("\n3. Top 3 students by CGPA:")
print(df.sort_values(by='cgpa', ascending=False).head(3))
