import pandas as pd
import re
import os

# File path configuration
FILE_PATH = "/Users/bjacobe/Desktop/fabu_attributes.xlsx"
OUTPUT_FILE_PATH = "/Users/bjacobe/Desktop/fabu_attributes_fixed.xlsx"

# Ensure file exists before proceeding
if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(f"File not found: {FILE_PATH}")

# Load dataset
df = pd.read_excel(FILE_PATH)

# Validate column existence
if "LogData" not in df.columns:
    raise ValueError("Expected column 'LogData' not found. Verify dataset structure.")

# Precompiled regex for performance
ATTRIBUTE_STATUS_CHANGE_REGEX = re.compile(
    r'(\d{1,2}/\d{1,2}/\d{4})\s+\d{1,2}:\d{2}:\d{2}\s*(?:AM|PM)?\s+\w+\s+(AttributeStatus|Attribute Status)\s+.+-».+'
)

def get_first_status_transition_date(logdata: str) -> str:
    """
    Identifies the earliest date where 'AttributeStatus' or 'Attribute Status' is modified.

    Args:
        logdata (str): Multi-line log data for a single attribute.

    Returns:
        str: The first detected date (MM/DD/YYYY) when a state transition occurred, else None.
    """
    if pd.isna(logdata):  
        return None  # Handle missing values
    
    matches = ATTRIBUTE_STATUS_CHANGE_REGEX.findall(logdata)
    
    return matches[0][0] if matches else None  # Return first detected transition date

# Apply function to dataset
df["first_status_change_date"] = df["LogData"].apply(get_first_status_transition_date)

# Ensure DataFrame is not empty before saving
if df.empty:
    raise ValueError("⚠️ Processed DataFrame is empty. Verify input file integrity.")

# Persist results
df.to_excel(OUTPUT_FILE_PATH, index=False, engine='openpyxl')

print(f"Process completed successfully. Output saved to: {OUTPUT_FILE_PATH}")