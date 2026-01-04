import pandas as pd

def clean_financial_data(input_file, output_file):
    """
    Improved version of the data cleaning function.
    This version handles missing data more carefully
    and only attempts numeric conversion on suitable columns.
    """

    # Load the raw CSV data
    df = pd.read_csv(input_file)

    # Print original shape for reference
    print("Original data shape:", df.shape)

    # Make a copy of the data to avoid modifying the original directly
    cleaned_df = df.copy()

    # Drop rows only if important numeric values are missing
    # (example: price and volume are critical for analysis)
    important_columns = ["price", "volume"]
    existing_columns = [col for col in important_columns if col in cleaned_df.columns]

    if existing_columns:
        cleaned_df = cleaned_df.dropna(subset=existing_columns)

    # Convert only object (string) columns to numeric where possible
    for column in cleaned_df.select_dtypes(include=["object"]).columns:
        cleaned_df[column] = pd.to_numeric(cleaned_df[column], errors="ignore")

    # Reset index after cleaning
    cleaned_df = cleaned_df.reset_index(drop=True)

    # Print cleaned shape for reference
    print("Cleaned data shape:", cleaned_df.shape)

    # Save the cleaned data to a new CSV file
    cleaned_df.to_csv(output_file, index=False)

    print("Cleaned data saved to:", output_file)
