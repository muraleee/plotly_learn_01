import plotly.graph_objects as go

def title_dict():
    fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
    #fig.update_layout(title_text="A Bar Chart",
    #                   title_font_size=30)
    fig.update_layout(title={"text":"A Bar Chart", "font":{"size":30}})
    fig.show()



fig = go.Figure(data=[
    go.Scatter(
        x=[1, 10, 20, 30, 40, 50, 60, 70, 80],
        y=[80, 70, 60, 50, 40, 30, 20, 10, 1]
    ),
    go.Scatter(
        x=[1, 10, 20, 30, 40, 50, 60, 70, 80],
        y=[1, 10, 20, 30, 40, 50, 60, 70, 80]
    )
])

#fig.update_xaxes(type="log")
#fig.update_yaxes(type="log")

fig.show()