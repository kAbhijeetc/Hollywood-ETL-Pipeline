"""
dashboard.py
-------------
Generates charts from the cleaned Hollywood dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import logging

from config import OUTPUT_PATH

# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def create_dashboard():

    print("\n" + "=" * 50)
    print("DASHBOARD PHASE STARTED")
    print("=" * 50)

    try:

        df = pd.read_csv(OUTPUT_PATH)

        plt.style.use("ggplot")

        # ---------------------------------
        # Dashboard Layout
        # ---------------------------------

        fig, axs = plt.subplots(2, 2, figsize=(14, 10))

        # ---------------------------------
        # Chart 1
        # Movies by Genre
        # ---------------------------------

        genre = df["Genre"].value_counts()

        axs[0, 0].bar(
            genre.index,
            genre.values
        )

        axs[0, 0].set_title("Movies by Genre")
        axs[0, 0].set_xlabel("Genre")
        axs[0, 0].set_ylabel("Count")
        axs[0, 0].tick_params(axis='x', rotation=30)

        # ---------------------------------
        # Chart 2
        # Audience Score Distribution
        # ---------------------------------

        axs[0, 1].hist(
            df["Audience  score %"],
            bins=10
        )

        axs[0, 1].set_title("Audience Score Distribution")
        axs[0, 1].set_xlabel("Audience Score")
        axs[0, 1].set_ylabel("Frequency")

        # ---------------------------------
        # Chart 3
        # Audience vs Rotten Tomatoes
        # ---------------------------------

        axs[1, 0].scatter(
            df["Audience  score %"],
            df["Rotten Tomatoes %"]
        )

        axs[1, 0].set_title("Audience vs Rotten Tomatoes")
        axs[1, 0].set_xlabel("Audience Score")
        axs[1, 0].set_ylabel("Rotten Tomatoes")

        # ---------------------------------
        # Chart 4
        # Genre Pie Chart
        # ---------------------------------

        axs[1, 1].pie(
            genre.values,
            labels=genre.index,
            autopct="%1.1f%%",
            startangle=90
        )

        axs[1, 1].set_title("Genre Distribution")

        plt.tight_layout()

        dashboard_path = os.path.join("output", "dashboard.png")

        plt.savefig(dashboard_path)

        plt.show()

        print(f"\nDashboard saved to:\n{dashboard_path}")

        logging.info("Dashboard created successfully.")

    except Exception as e:

        logging.error(f"Dashboard Error : {e}")

        print(e)


if __name__ == "__main__":

    create_dashboard()