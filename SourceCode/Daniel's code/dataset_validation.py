def validate_dataset(df, required_columns):
    """
    This function checks whether a dataset contains all the columns
    that are required for the project to work correctly.
    """

    # Create an empty list to keep track of any missing columns
    missing_columns = []

    # Loop through each column name that we expect to be in the dataset
    for col in required_columns:
        # Check if the required column does NOT exist in the DataFrame
        if col not in df.columns:
            # If the column is missing, add it to the missing_columns list
            missing_columns.append(col)

    # After checking all required columns, see if any are missing
    if missing_columns:
        # Print the missing columns so the issue is clear
        print("Missing required columns:", missing_columns)

        # Return False to stop the pipeline from continuing
        # This prevents errors later in the project
        return False

    # If no columns are missing, print a success message
    print("Dataset validation passed")

    # Return True to confirm the dataset is valid and safe to use
    return True

