import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def generate_random_walk(steps, start=0, step_size=1):
    """Generate a random walk series."""
    random_steps = np.random.choice([-1, 1], size=steps) * step_size
    return np.cumsum(np.insert(random_steps, 0, start))

def main():
    st.title('Random Walk Explorer: An Educational App')
    st.write("""
    This app demonstrates the concept of a random walk using interactive visualizations.
    A random walk is a mathematical object that describes a path consisting of a succession of random steps.
    """)

    # Sidebar for user input
    st.sidebar.header("Parameters")
    steps = st.sidebar.slider("Number of steps", 100, 1000, 500)
    step_size = st.sidebar.slider("Step size", 0.1, 2.0, 1.0, 0.1)

    # Generate random walk data
    dates = pd.date_range(start='2023-01-01', periods=steps)
    values = generate_random_walk(steps, step_size=step_size)
    df = pd.DataFrame({'Date': dates, 'Value': values})

    # Display raw data
    st.subheader('Raw Data')
    st.write("This table shows the first few rows of our random walk data:")
    st.write(df.head())

    # Create a line plot
    st.subheader('Line Plot: The Path of a Random Walk')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Date'], df['Value'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title('Random Walk Over Time')
    st.pyplot(fig)
    st.write("""
    This line plot shows the path of our random walk over time. 
    Notice how it can drift up or down unpredictably, reflecting the random nature of each step.
    """)

    # Create a histogram
    st.subheader('Histogram: Distribution of Values')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Value'], bins=20, edgecolor='black')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Random Walk Values')
    st.pyplot(fig)
    st.write("""
    This histogram shows the distribution of values in our random walk.
    In a simple random walk, this distribution often approximates a normal (bell-curve) distribution,
    especially as the number of steps increases.
    """)

    # Create a scatter plot
    st.subheader('Scatter Plot: Step-by-Step View')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df.index, df['Value'], alpha=0.5)
    ax.set_xlabel('Step Number')
    ax.set_ylabel('Value')
    ax.set_title('Value at Each Step of the Random Walk')
    st.pyplot(fig)
    st.write("""
    This scatter plot shows the value at each step of the random walk.
    Each point represents a single step. You can see how the value changes with each step,
    sometimes moving up, sometimes down.
    """)

    # Create a box plot
    st.subheader('Box Plot: Monthly Distribution')
    fig, ax = plt.subplots(figsize=(10, 6))
    df['Month'] = df['Date'].dt.month
    sns.boxplot(x='Month', y='Value', data=df, ax=ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')
    ax.set_title('Distribution of Random Walk Values by Month')
    st.pyplot(fig)
    st.write("""
    This box plot shows the distribution of values for each month.
    In a true random walk, we wouldn't expect to see significant differences between months.
    Any patterns you might see are likely due to the random nature of this particular walk,
    rather than any underlying monthly trend.
    """)

    st.subheader('Experiment and Learn')
    st.write("""
    Try adjusting the number of steps and step size in the sidebar to see how they affect the random walk.
    - More steps will generally result in a smoother-looking walk and distribution.
    - Larger step sizes will lead to more dramatic changes between steps.
    
    Remember, each time you change these parameters, a new random walk is generated!
    """)

if __name__ == '__main__':
    main()
