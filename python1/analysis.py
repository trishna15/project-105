import csv
import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv("data107.csv")

std = df.loc[df["student_id"]=="TRL_987"]



fig = go.Figure(go.Bar(
    x = std.groupby("level")["attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    oreintation = 'h'
))

fig.show()