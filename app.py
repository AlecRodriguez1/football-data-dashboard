import streamlit as st
import pandas as pd


def main():
    df = pd.read_csv("data/player_stats_25.csv")
    
    st.title("Football Data Dashboard 2024-2025")
    st.subheader("Dataset preview")
    st.dataframe(df.head(20), use_container_width=True)


if __name__ == "__main__":
    main()