import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

df_india = df[(df['country'] == 'India')]
df_china = df[(df['country'] == 'United States')]


traces =[]

traces.append(go.Scatter(
    x=df_india['year'],
    y=df_india['lifeExp'],
    text=df_india['country'],
    mode='lines+markers',
    opacity=0.7,
    marker={
        'size': 15,
        'line': {'width': 0.5, 'color': 'blue'}
    },
))

traces.append(go.Scatter(
    x=df_china['year'],
    y=df_china['lifeExp'],
    text=df_china['country'],
    mode='lines+markers',
    opacity=0.7,
    marker={
        'size': 15,
        'line': {'width': 0.5, 'color': 'red'}
    },
))

fig = go.Figure()
[fig.add_trace(trace) for trace in traces]
fig.show()