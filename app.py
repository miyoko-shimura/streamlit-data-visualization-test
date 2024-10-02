import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_random_walk(steps, start_value=0, drift=0, volatility=1):
    """Generate a random walk series."""
    random_steps = np.random.normal(loc=drift, scale=volatility, size=steps)
    return start_value + np.cumsum(random_steps)

def plot_random_walks(data, title):
    """Plot multiple random walks."""
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, walk in enumerate(data.T):
        ax.plot(walk, label=f'Walk {i+1}')
    ax.set_title(title)
    ax.set_xlabel('Steps')
    ax.set_ylabel('Value')
    ax.legend()
    return fig

def plot_histogram(data, title):
    """Plot histogram of final values."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data, bins=20, edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    return fig

def main():
    st.title('Random Walk Visualization App')
    st.write('Explore the properties of random walks and how different parameters affect them.')

    # Sidebar for parameters
    st.sidebar.header('Random Walk Parameters')
    num_walks = st.sidebar.slider('Number of Random Walks', 1, 10, 3)
    steps = st.sidebar.slider('Number of Steps', 10, 1000, 200)
    start_value = st.sidebar.number_input('Starting Value', value=0.0)
    drift = st.sidebar.number_input('Drift', value=0.0, help='Average change at each step')
    volatility = st.sidebar.number_input('Volatility', min_value=0.1, value=1.0, help='Standard deviation of changes')

    # Generate random walks
    walks = np.array([generate_random_walk(steps, start_value, drift, volatility) for _ in range(num_walks)])

    # Plotting random walks
    st.subheader('Random Walk Visualization')
    fig_walks = plot_random_walks(walks, 'Multiple Random Walks')
    st.pyplot(fig_walks)

    # Statistics
    st.subheader('Random Walk Statistics')
    final_values = walks[:, -1]
    st.write(f'Mean final value: {np.mean(final_values):.2f}')
    st.write(f'Standard deviation of final values: {np.std(final_values):.2f}')

    # Distribution of final values
    st.subheader('Distribution of Final Values')
    fig_hist = plot_histogram(final_values, 'Distribution of Final Values')
    st.pyplot(fig_hist)

    # Explain the concept
    st.subheader('Understanding Random Walks')
    st.write("""
    A random walk is a mathematical object that describes a path consisting of a succession of random steps. 
    It's often used to model various phenomena in physics, biology, and economics.

    Key components:
    - Starting Value: The initial point of the random walk.
    - Drift: A tendency for the walk to move in a particular direction.
    - Volatility: The degree of variation in the steps.

    Try adjusting these parameters and observe how they affect the random walks!
    """)

    # Additional educational content
    st.subheader('Properties of Random Walks')
    st.write("""
    1. Unpredictability: Each step is random, making long-term prediction difficult.
    2. Root Mean Square Distance: On average, the distance from the start grows with the square root of the number of steps.
    3. Scaling: Random walks often exhibit self-similarity when scaled properly.
    4. First Return Time: The probability of returning to the start decreases with time.

    These properties make random walks useful in modeling phenomena like Brownian motion, stock prices, and diffusion processes.
    """)

if __name__ == '__main__':
    main()
