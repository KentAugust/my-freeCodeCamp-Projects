import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter("Year", "CSIRO Adjusted Sea Level", data=df, color="#41436A")

    # Create first line of best fit
    lin_rg = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    years_extended = pd.Series([n for n in range(df["Year"][0], 2051)])
    line = years_extended *lin_rg.slope + lin_rg.intercept
    
    ax.plot(years_extended, line, color="#F54768")

    # Create second line of best fit
    df_current = df[df["Year"] >= 2000]
    df_current.reset_index(inplace=True)
    
    lin_rg2 = linregress(df_current["Year"], df_current["CSIRO Adjusted Sea Level"])
    
    current_y_ext = pd.Series([n for n in range(df_current["Year"][0], 2051)])
    line2 = current_y_ext *lin_rg2.slope + lin_rg2.intercept
    
    ax.plot(current_y_ext, line2, color="#FF9677")
    
    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()