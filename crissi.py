import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def line_plot():
    # Generate some example data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Simple Line Plot')

    # Display the plot
    st.pyplot(fig)

def main():
    st.title('Line Plot App')
    st.write("Here's a simple Streamlit app that displays a line plot.")

    # Display the line plot
    line_plot()

if __name__ == '__main__':
    main()
