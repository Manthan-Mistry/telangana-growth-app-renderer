# Modified code to start data bars from the minimum value
def data_bars(df, column, color):
    n_bins = 100
    # Calculate ranges starting from the minimum value
    min_value = df[column].min()
    max_value = df[column].max()
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    ranges = [
        (max_value - min_value) * i + min_value
        for i in bounds
    ]
    styles = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        max_bound_percentage = bounds[i] * 100
        styles.append({
            'if': {
                'filter_query': (
                    '{{{column}}} >= {min_bound}' +
                    (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                'column_id': column
            },
            'background': (
                """
                    linear-gradient(90deg,
                    {color} 0%,
                    {color} {max_bound_percentage}%,
                    white {max_bound_percentage}%,
                    white 100%)
                """.format( color = color ,max_bound_percentage=max_bound_percentage)
            ),
            'paddingBottom': 2,
            'paddingTop': 2
        })

    return styles
