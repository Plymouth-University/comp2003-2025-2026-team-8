import pandas as pd

def clean_financial_data(input_file, output_file):
    """
    Very simple data cleaning function.
    Loads raw data, removes missing values,
    and saves cleaned data to a new file.
    """

    # Load raw data
    df = pd.read_csv(input_file)

    # Print original shape (for debugging)
    print("Original data shape:", df.shape)

    # Remove rows with any missing values (inefficient but simple)
    df = df.dropna()

    # Loop through columns and try to convert to numeric
    for column in df.columns:
        try:
            df[column] = pd.to_numeric(df[column])
        except:
            # If conversion fails, leave column as is
            pass

    # Reset index after cleaning
    df = df.reset_index(drop=True)

    # Print cleaned shape
    print("Cleaned data shape:", df.shape)

    # Save cleaned data
    df.to_csv(output_file, index=False)

    print("Cleaned data saved to:", output_file)
