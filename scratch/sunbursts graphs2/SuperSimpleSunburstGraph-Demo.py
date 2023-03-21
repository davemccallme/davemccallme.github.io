import plotly.graph_objects as go

# Sample data
data = [
    ["A", "A1", "A1a", "A1a1"],
    ["A", "A1", "A1a", "A1a2"],
    ["A", "A1", "A1a", "A1a3"],
    ["A", "A1", "A1b", "A1b1"],
    ["A", "A1", "A1b", "A1b2"],
    ["A", "A1", "A1c", "A1c1"],
    ["A", "A2", "A2a", "A2a1"],
    ["A", "A2", "A2a", "A2a2"],
    # Add more data points here (up to a total of 100)...
]

# Create a sunburst graph
fig = go.Figure(go.Sunburst(
    labels=[item for sublist in data for item in sublist],
    parents=[None, "A", "A1", "A1a"] * len(data),
    values=[1] * len(data),
))

# Update layout
fig.update_layout(
    title="Simple Sunburst Graph",
    sunburstcolorway=["#f7b267", "#fc529d", "#4974a5", "#57c4ad"],
    extendsunburstcolors=True,
)

# Show the plot
fig.show()
