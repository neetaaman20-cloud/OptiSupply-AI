import pandas as pd
import numpy as np

def generate_data():
    date_rng = pd.date_range(start='2023-01-01', end='2025-01-01', freq='D')
    df = pd.DataFrame(date_rng, columns=['date'])
    df['sales'] = np.random.randint(50, 200, size=(len(date_rng))) + (df.index * 0.1)
    # Add seasonality (higher sales on weekends)
    df['is_weekend'] = df['date'].dt.dayofweek >= 5
    df.loc[df['is_weekend'], 'sales'] += 30
    df.to_csv('sales_data.csv', index=False)
    print("Dataset 'sales_data.csv' created!")

if __name__ == "__main__":
    generate_data()