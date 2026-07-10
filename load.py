"""
load.py
--------
Loads the cleaned dataset into the output folder.
"""

import logging
from config import OUTPUT_PATH

# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data(df):
    """
    Saves the transformed dataset.
    """

    print("\n" + "=" * 50)
    print("LOAD PHASE STARTED")
    print("=" * 50)

    try:

        df.to_csv(OUTPUT_PATH, index=False)

        print(f"\nDataset successfully saved to:\n{OUTPUT_PATH}")

        print(f"\nTotal Rows Saved    : {df.shape[0]}")
        print(f"Total Columns Saved : {df.shape[1]}")

        logging.info("Dataset loaded successfully.")

        print("\nLoad Phase Completed Successfully.")

    except Exception as e:

        logging.error(f"Load Error : {e}")

        print("\nError while saving dataset.")

        print(e)


# Test independently
if __name__ == "__main__":

    from extract import extract_data
    from transform import transform_data
    from validate import validate_data

    df = extract_data()

    if df is not None:

        df = transform_data(df)

        validate_data(df)

        load_data(df)