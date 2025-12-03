"""
prepare_data.py
-----------------
1. Load raw data.
2. Clean it (using src.data_cleaning).
3. Save cleaned data.
4. Split it into Train (80%) and Test (20%).
5. Save training and testing data.

This ensures all models use the EXACT same data split.
"""
import pandas as pd
from sklearn.model_selection import train_test_split  # type: ignore
from src.data_cleaning import (
    load_wallace_data, clean_wallace_data
)
from src.config import (
    WALLACE_RAW_PATH, WALLACE_CLEAN_PATH,
    TRAIN_DATA_PATH, TEST_DATA_PATH
)


def run() -> None:
    """Execute data preparation."""
    print("Loading and cleaning data...")
    wallace_raw: pd.DataFrame = load_wallace_data(WALLACE_RAW_PATH)
    wallace_clean: pd.DataFrame = clean_wallace_data(wallace_raw)

    wallace_clean.to_csv(WALLACE_CLEAN_PATH, index=False)

    print("Splitting data for training and testing...")
    train_set, test_set = train_test_split(
        wallace_clean,
        test_size=0.2,
        random_state=42,
        stratify=wallace_clean['new_contract_this_campaign']
    )

    train_set.to_csv(TRAIN_DATA_PATH, index=False)
    test_set.to_csv(TEST_DATA_PATH, index=False)
