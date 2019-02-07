def get_rows_columns(items, columns):
    rows = items // columns
    if items < columns:
        columns = items
    if rows * columns < items:
        rows += 1

    return rows, columns
