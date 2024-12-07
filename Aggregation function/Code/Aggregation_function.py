import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70, 80],
    'Weight': [1, 2, 3, 1, 2, 3, 1, 2]
}

df = pd.DataFrame(data)

# Define a custom weighted average aggregation function
def weighted_average(values, weights):
    return np.average(values, weights=weights)

# Apply the custom aggregation function with groupby
result = df.groupby('Category').apply(lambda x: weighted_average(x['Value'], x['Weight']))

print(result)
