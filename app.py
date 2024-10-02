import streamlit as st
import matplotlib.pyplot as plt

def plot_random_walk(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Date'], df['Value'])
    ax.set_title('Random Walk Visualization')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    st.pyplot(fig)

# In your main() function:
df = generate_data()
plot_random_walk(df)
