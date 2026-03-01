import pandas as pd

# Load CSV file
df = pd.read_csv("expenses.csv")

# Remove missing values
df = df.dropna()

# Convert to JSON
df.to_json("expenses.json", orient="records", indent=4)

print("CSV converted to JSON successfully!")