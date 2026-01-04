def load_and_clean_data(input_file, output_file):
    """
    Loads raw data from a CSV file, checks that it contains
    the required columns, cleans the data, and saves the
    cleaned version to a new CSV file.
    """

    # Load the raw CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Check that the dataset contains the required columns
    # (e.g. 'price' and 'volume' are needed for analysis)
    # If the dataset is not valid, stop the process early
    if not validate_dataset(df, ["price", "volume"]):
        print("Data validation failed. Cleaning process stopped.")
        return None

    # Clean the data using the data cleaning function
    # This removes missing values and fixes data types
    df = clean_financial_data(input_file, output_file)

    # Return the cleaned DataFrame so it can be used later
    return df
