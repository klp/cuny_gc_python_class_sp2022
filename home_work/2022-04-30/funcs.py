def range_condition(df, column, min, max):
    condition = (df[column] >= min) & (df[column] <= max)
    return condition


# Running this function returns one boolean value