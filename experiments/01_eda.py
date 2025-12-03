"""
Exploratory Data Analysis (EDA) Script.

USAGE:
    Run interactively in VS Code:
    Highlight the lines to run then "Shift+Enter" to view data and charts.
"""
# autopep8: off
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))

from src.data_cleaning import (
    load_wallace_data
)
# autopep8: on

# Get the data
wallace = load_wallace_data()
wallace.head()
wallace.info()

# Viewing categorical columns
wallace["town"].value_counts()
wallace["country"].value_counts()
wallace["job"].value_counts()
wallace["married"].value_counts()
wallace["education"].value_counts()
wallace["arrears"].value_counts()
wallace["housing"].value_counts()

# Some have 'n' instead of 'no' in 'has_tv_package'
wallace["has_tv_package"].value_counts()

# Some have 'cell' instead of 'cellular' in 'last_contact'
wallace["last_contact"].value_counts()

# One record has 'j' instead of an actual month
wallace["last_contact_this_campaign_month"].value_counts()

wallace["outcome_previous_campaign"].value_counts()
wallace["new_contract_this_campaign"].value_counts()
