import streamlit as st
import pandas as pd


def main():
    df = pd.read_csv("data/player_stats_25.csv")
    
    st.title("Football Data Dashboard 2024-2025")
    
#---------------League Selector---------------------

    leagues = (df["Comp"].unique())
    selected_league = st.selectbox(
        "Select a league",
        leagues
    )

#--------------Filtering Data for top scorers--------------

    filtered_league = df[df["Comp"] == selected_league]
    
    top_scorers_data = ["Player", "MP", "Gls", "Squad", "Pos", "Age"]
    filtered_league_df = filtered_league[top_scorers_data]

    top_scorers = (
        filtered_league_df
        .sort_values("Gls", ascending=False)
        .reset_index(drop=True)
        )
    
    top_scorers["RK"] = top_scorers.index + 1
    display_cols = ["RK"] + top_scorers_data

    st.subheader(f"Top 25 scorers in {selected_league}")
    st.dataframe(
        top_scorers[display_cols].head(25), 
        use_container_width=True,
        hide_index=True
        )

if __name__ == "__main__":
    main()