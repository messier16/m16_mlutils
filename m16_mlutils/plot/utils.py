def get_rows_columns(items, columns):
    """
    A helper to use subplots. Pass the number of items and the number of columns that you want to use to display them.
    :param items:
    :param columns:
    :return: a tuple with the number of rows and columns necessary to present all your data.
    """
    rows = items // columns
    if items < columns:
        columns = items
    if rows * columns < items:
        rows += 1

    return rows, columns
