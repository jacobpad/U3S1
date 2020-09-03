def ten_x(n):
    """
    Param n is a number
    Function will enlarge the number by 10
    """
    return n * 100


def replace_spaces_with_underscore_in_column_names_and_make_lowercase(df):
    """
    Accepts a dataframe.
    Alters column names- replacing spaces with '_' and column names lowercase.
    Returns a dataframe.
    """
    labels = list(df.columns)
    for i in range(len(df.columns)):
        labels[i] = labels[i].replace(" ", "_")
        labels[i] = labels[i].lower()
        df.columns = labels
    return df


if __name__ == "__main__":
    print(enlarge(5))
