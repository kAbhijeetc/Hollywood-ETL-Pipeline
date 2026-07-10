"""
extract.py
-----------
Extracts the Hollywood dataset from the data folder.
"""

import pandas as pd
import logging
from config import DATA_PATH, LOG_PATH

# Configure logging
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_data():
    """
    Reads the dataset from the CSV file.

    Returns:
        pandas.DataFrame : Dataset if successful
        None : If an error occurs
    """

    try:
        print("=" * 50)
        print("EXTRACT PHASE STARTED")
        print("=" * 50)

        print(f"\nReading dataset from:\n{DATA_PATH}\n")

        df = pd.read_csv(DATA_PATH)

        logging.info("Dataset extracted successfully.")

        print("Dataset Loaded Successfully!")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nFirst Five Records:")
        print(df.head())

        return df

    except FileNotFoundError:

        logging.error("Dataset file not found.")

        print("\nERROR: Dataset file not found.")
        print(DATA_PATH)

        return None

    except Exception as e:

        logging.error(f"Extraction Error : {e}")

        print("\nERROR:", e)

        return None


# Run only when extract.py is executed directly
if __name__ == "__main__":

    dataset = extract_data()

    if dataset is not None:
        print("\nExtraction Completed Successfully.")
    else:
        print("\nExtraction Failed.")