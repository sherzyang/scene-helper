import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 30, 22]}
df = pd.DataFrame(data)
print(df)

# Calculate average age
average_age = df['Age'].mean()
print('Average Age:', average_age)