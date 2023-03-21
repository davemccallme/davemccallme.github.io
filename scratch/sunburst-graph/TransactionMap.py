import plotly.graph_objects as go

fig = go.Figure(go.Sunburst(
    ids=[item["id"] for item in data],
    parents=[item["parent"] for item in data],
    values=[item["value"] for item in data],
    branchvalues='total',
    textinfo='label+percent parent'
))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
fig.show()

