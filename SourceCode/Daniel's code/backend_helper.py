def load_and_clean_data(input_file, output_file):
    """
    Loads raw data, validates it, cleans it, and saves it.
    """

    df = pd.read_csv(input_file)

    if not validate_dataset(df, ["price", "volume"]):
        return None

    df = clean_financial_data(input_file, output_file)
    return df
