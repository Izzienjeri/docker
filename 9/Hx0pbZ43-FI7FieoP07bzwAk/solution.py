# Example usage
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2.5, 3.0, 4.5],
    'C': ['x', 'y', 'z', None]  # Non-numerical column
})

filled_df = fill_missing_values(df)