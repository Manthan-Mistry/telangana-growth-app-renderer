def data_bars_diverging_final(df, column, color_above='#3D9970', color_below='#FF4136'):
    n_bins = 100
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    col_max = df[column].max()
    col_min = df[column].min()
    ranges = [
        ((col_max - col_min) * i) + col_min
        for i in bounds
    ]

    styles = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        min_bound_percentage = bounds[i - 1] * 100
        max_bound_percentage = bounds[i] * 100

        style = {
            'if': {
                'filter_query': (
                    '{{{column}}} >= {min_bound}' +
                    (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                'column_id': column
            },
            'paddingBottom': 2,
            'paddingTop': 2
        }

        if min_bound < 0 and max_bound > 0:
            background = (
                """
                    linear-gradient(90deg,
                    {color_below} 0%,
                    {color_below} 50%,
                    white 50%,
                    white 100%)
                """.format(
                    color_below=color_below
                )
            )
        elif max_bound >= 0:
            gradient_percentage = (abs(min_bound) / (col_max - col_min)) * 100
            background = (
                """
                    linear-gradient(90deg,
                    {color_above} 0%,
                    {color_above} {gradient_percentage}%,
                    white {gradient_percentage}%,
                    white 100%)
                """.format(
                    gradient_percentage=gradient_percentage,
                    color_above=color_above
                )
            )
        else:
            gradient_percentage = (abs(max_bound) / (col_max - col_min)) * 100
            background = (
                """
                    linear-gradient(90deg,
                    white 0%,
                    white {gradient_percentage}%,
                    {color_below} {gradient_percentage}%,
                    {color_below} 100%)
                """.format(
                    gradient_percentage=gradient_percentage,
                    color_below=color_below
                )
            )

        style['background'] = background
        styles.append(style)

    return styles