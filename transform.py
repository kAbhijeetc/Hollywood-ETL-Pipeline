"""
transform.py
-------------
Transforms and cleans the Hollywood dataset.
"""

import logging
import pandas as pd

# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def transform_data(df):
    """
    Cleans and transforms the dataset.
    """

    print("\n" + "=" * 50)
    print("TRANSFORM PHASE STARTED")
    print("=" * 50)

    # -----------------------------
    # Remove duplicate rows
    # -----------------------------
    before = df.shape[0]
    df.drop_duplicates(inplace=True)
    after = df.shape[0]

    print(f"Duplicates Removed : {before - after}")
    logging.info(f"Duplicates Removed : {before - after}")

    # -----------------------------
    # Convert numeric columns
    # -----------------------------
    numeric_cols = [
        "Audience  score %",
        "Profitability",
        "Rotten Tomatoes %",
        "Worldwide Gross"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print("Numeric columns converted.")
    logging.info("Numeric conversion completed.")

    # -----------------------------
    # Handle missing values
    # -----------------------------
    missing = df.isnull().sum().sum()

    print(f"Missing Values Found : {missing}")

    df.fillna({
        "Audience  score %": df["Audience  score %"].mean(),
        "Profitability": df["Profitability"].mean(),
        "Rotten Tomatoes %": df["Rotten Tomatoes %"].mean(),
        "Worldwide Gross": df["Worldwide Gross"].mean()
    }, inplace=True)

    logging.info("Missing values handled.")

    # -----------------------------
    # Clean text columns
    # -----------------------------
    df["Film"] = df["Film"].str.strip()
    df["Genre"] = df["Genre"].str.strip()
    df["Lead Studio"] = df["Lead Studio"].str.strip()

    print("Text cleaned.")
    logging.info("Text columns cleaned.")

    # -----------------------------
    # Create Profit Category
    # -----------------------------
    df["Profit Category"] = pd.cut(
        df["Profitability"],
        bins=[0, 2, 5, float("inf")],
        labels=["Low", "Medium", "High"]
    )

    print("Profit Category created.")
    logging.info("Profit Category created.")

    # -----------------------------
    # Display dataset info
    # -----------------------------
    print("\nDataset Shape :", df.shape)

    print("\nFirst Five Rows")
    print(df.head())

    print("\nTransformation Completed Successfully.")

    logging.info("Transformation completed successfully.")

    return df


# Test file independently
if __name__ == "__main__":

    from extract import extract_data

    df = extract_data()

    if df is not None:
        df = transform_data(df)