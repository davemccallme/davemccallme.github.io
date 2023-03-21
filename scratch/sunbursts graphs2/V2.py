#V2
import plotly.graph_objects as go
# Sample data
data = [    ["A", "A1", "A1a", "A1a1"],
    ["A", "A1", "A1a", "A1a2"],
    ["A", "A1", "A1a", "A1a3"],
    ["A", "A1", "A1b", "A1b1"],
    ["A", "A1", "A1b", "A1b2"],
    ["A", "A1", "A1c", "A1c1"],
    ["A", "A2", "A2a", "A2a1"],
    ["A", "A2", "A2a", "A2a2"],
]

# Create a dictionary to store the index of each label in the labels list
label_index = {}

# Loop through the data list to populate the label_index dictionary
for i, d in enumerate(data):
    for label in d:
        if label not in label_index:
            label_index[label] = len(label_index)

# Create a list of parents for each label based on its position in the data list
parents = [None] * len(data) + [0] * (len(label_index) - len(data))
for i, d in enumerate(data):
    parent = None
    for label in d:
        index = label_index[label]
        parents[index] = parent
        parent = index

# Create a sunburst graph
fig = go.Figure(go.Sunburst(
    labels=list(label_index.keys()),
    parents=parents,
    values=[1] * len(label_index),
))

# Update layout
fig.update_layout(
    title="Simple Sunburst Graph",
    sunburstcolorway=["#f7b267", "#fc529d", "#4974a5", "#57c4ad"],
    extendsunburstcolors=True,
)

# Show the plot
fig.show()
