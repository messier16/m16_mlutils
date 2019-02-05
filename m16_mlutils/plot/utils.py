def get_rows_columns(columns, elements):
    rows = elements // columns
    if elements < columns:
        columns = elements
    if rows * columns < len(elements):
        rows += 1

    return rows, columns
