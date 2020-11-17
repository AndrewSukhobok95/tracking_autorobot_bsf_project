import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

def plot_interactive_lines(df: pd.DataFrame,
                           xcol:str,
                           ycol:list,
                           title:str,
                           xaxis_name:str=None,
                           labels:list=None,
                           html_name:str="plot.html"):
    fig = go.Figure()

    for i in range(len(ycol)):
        col_name = ycol[i]
        
        if col_name!=xcol:
            label = ycol[i]
            
            if labels is not None:
                label = labels[i]
            
            scatter = go.Scatter(x=df[xcol], y=df[col_name], name=label, mode='lines+markers')
            fig.add_trace(scatter)

    xaxis_title = xaxis_name if xaxis_name else xcol 
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title='Value')
    plotly.offline.plot(fig, filename=html_name)
    # fig.show()

