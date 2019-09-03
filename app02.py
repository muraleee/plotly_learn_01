import pandas as pd

import plotly.graph_objects as go



df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

selected_year = 1957

filtered_df = df[df.year == selected_year]

traces = []
for i in filtered_df.continent.unique():
    df_by_continent = filtered_df[filtered_df['continent'] == i]
    traces.append(go.Scatter(
        x=df_by_continent['gdpPercap'],
        y=df_by_continent['lifeExp'],
        text=df_by_continent['country'],
        mode='markers',
        opacity=0.7,
        marker={
            'size': 15,
            'line': {'width': 0.5, 'color': 'white'}
        },
        name=i
    ))

fig = go.Figure()

# fig.update_layout(
#         xaxis={'type': 'log', 'title': 'GDP Per Capita'},
#         yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
#         margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
#         legend={'x': 0, 'y': 1},
#         hovermode='closest'
#     )

fig.update_layout(
        xaxis={ 'title': 'GDP Per Capita', 'range':[0,120000]},
        yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
        legend={'x': 0, 'y': 1},
        hovermode='closest'
    )


[fig.add_trace(trace) for trace in traces]

print(fig.to_json())
fig.show()