def validate_dataset(df, required_columns):
    """
    Checks whether required columns exist in the dataset.
    Returns True if valid, False otherwise.
    """

    missing_columns = []

    for col in required_columns:
        if col not in df.columns:
            missing_columns.append(col)

    if missing_columns:
        print("Missing required columns:", missing_columns)
        return False

    print("Dataset validation passed")
    return True
