import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "HollywoodsMostProfitableStories.csv"
)

OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "output",
    "Hollywood_Cleaned.csv"
)

LOG_PATH = os.path.join(
    BASE_DIR,
    "logs",
    "pipeline.log"
)
print(DATA_PATH)
print(OUTPUT_PATH)
print(LOG_PATH)