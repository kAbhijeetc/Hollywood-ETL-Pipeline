"""
validate.py
-------------
Validates the transformed Hollywood dataset.
"""

import logging

# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_data(df):

    print("\n" + "=" * 50)
    print("VALIDATION PHASE STARTED")
    print("=" * 50)

    # -----------------------
    # Null Values
    # -----------------------
    null_values = df.isnull().sum().sum()

    print(f"\nNull Values : {null_values}")

    if null_values == 0:
        print("PASS : No Missing Values")
    else:
        print("FAIL : Missing Values Found")

    # -----------------------
    # Duplicate Rows
    # -----------------------
    duplicates = df.duplicated().sum()

    print(f"\nDuplicate Rows : {duplicates}")

    if duplicates == 0:
        print("PASS : No Duplicate Rows")
    else:
        print("FAIL : Duplicate Rows Found")

    # -----------------------
    # Audience Score Validation
    # -----------------------
    invalid_audience = df[
        (df["Audience  score %"] < 0) |
        (df["Audience  score %"] > 100)
    ]

    print(f"\nInvalid Audience Scores : {len(invalid_audience)}")

    # -----------------------
    # Rotten Tomatoes Validation
    # -----------------------
    invalid_rt = df[
        (df["Rotten Tomatoes %"] < 0) |
        (df["Rotten Tomatoes %"] > 100)
    ]

    print(f"Invalid Rotten Tomatoes Scores : {len(invalid_rt)}")

    # -----------------------
    # Worldwide Gross Validation
    # -----------------------
    invalid_gross = df[df["Worldwide Gross"] < 0]

    print(f"Negative Worldwide Gross : {len(invalid_gross)}")

    # -----------------------
    # Profitability Validation
    # -----------------------
    invalid_profit = df[df["Profitability"] < 0]

    print(f"Negative Profitability : {len(invalid_profit)}")

    logging.info("Validation Completed Successfully.")

    print("\nValidation Completed Successfully.")

    return True


# Test file independently
if __name__ == "__main__":

    from extract import extract_data
    from transform import transform_data

    df = extract_data()

    if df is not None:

        df = transform_data(df)

        validate_data(df)