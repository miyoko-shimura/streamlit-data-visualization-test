import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum()
    return pd.DataFrame({'Date': dates, 'Value': values})

def main():
    st.title('Simple Data Visualization App')

    # Add a button to generate new data
    if 'data' not in st.session_state:
        st.session_state.data = generate_data()

    if st.button('Generate New Data'):
        st.session_state.data = generate_data()

    # Use the generated data
    df = st.session_state.data

    # Display raw data
    st.subheader('Raw Data')
    st.write(df)

    # Create a line plot
    st.subheader('Line Plot')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Date'], df['Value'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title('Cumulative Random Walk')
    st.pyplot(fig)

    # Create a histogram
    st.subheader('Histogram')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Value'], bins=20)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Values')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
