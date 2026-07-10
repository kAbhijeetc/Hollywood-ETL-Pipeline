"""
run_pipeline.py
----------------
Main ETL Pipeline
"""

import logging

from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data
from dashboard import create_dashboard


# Configure Logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():

    print("=" * 60)
    print("HOLLYWOOD MOVIES ETL PIPELINE")
    print("=" * 60)

    # -----------------------------
    # Extract
    # -----------------------------
    df = extract_data()

    if df is None:
        print("Extraction Failed.")
        return

    # -----------------------------
    # Transform
    # -----------------------------
    df = transform_data(df)

    # -----------------------------
    # Validate
    # -----------------------------
    validation = validate_data(df)

    if validation:

        # -----------------------------
        # Load
        # -----------------------------
        load_data(df)

        # -----------------------------
        # Dashboard
        # -----------------------------
        create_dashboard()

        print("\n" + "=" * 60)
        print("ETL PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)

        logging.info("ETL Pipeline Completed Successfully.")

    else:

        print("Validation Failed.")

        logging.error("Validation Failed.")


if __name__ == "__main__":

    run_pipeline()