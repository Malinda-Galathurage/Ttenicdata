import pandas as pd

data_url = 'https://drive.google.com/uc?export=download&id=1AwtQq1DIrGNyD-UfOE4BbtmI9GiiZTqJ'
df = pd.read_csv(data_url)


df.to_csv('../data/malinda_data.csv', index=False)
print("Data collection completed by Malinda")

