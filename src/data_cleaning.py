import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
WALLACE_PATH = os.path.join(
    current_dir, "..", "data", "wallacecommunications.csv")


def load_wallace_data(filepath: str = WALLACE_PATH) -> pd.DataFrame:
    """Loads raw data from a CSV file."""
    return pd.read_csv(filepath)


def clean_wallace_data(data: pd.DataFrame) -> pd.DataFrame:
    """Fix typos and inconsistencies."""
    clean_data: pd.DataFrame = data.copy()

    # Fix 'n' -> 'no' in 'has_tv_package'
    clean_data['has_tv_package'] = clean_data['has_tv_package'].replace(
        {'n': 'no'}
    )

    # Fix 'cell' -> 'cellular' in 'last_contact'
    clean_data['last_contact'] = clean_data['last_contact'].replace(
        {'cell': 'cellular'}
    )

    # Drop the single row with typo 'j' in month
    clean_data = clean_data[
        clean_data['last_contact_this_campaign_month'] != 'j'
    ]

    return clean_data
