import pandas as pd

def extract():
    """Extract data (mock source)"""
    data = {
        "id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "salary": [50000, 60000, None, 55000]
    }
    df = pd.DataFrame(data)
    print("Extracted Data:")
    print(df)
    return df


def transform(df):
    """Transform data"""
    df["salary"] = df["salary"].fillna(0)
    df["salary_usd"] = df["salary"] * 1.1
    print("\nTransformed Data:")
    print(df)
    return df


def load(df):
    """Load data (save to CSV)"""
    df.to_csv("output.csv", index=False)
    print("\nData loaded to output.csv")


def main():
    df = extract()
    df_transformed = transform(df)
    load(df_transformed)


if __name__ == "__main__":
    main()
