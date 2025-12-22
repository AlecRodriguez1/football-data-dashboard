import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    df = pd.read_csv("data/player_stats_25.csv")
    
    st.title("Football Data Dashboard 2024-2025")
    
    
#----------------Columns------------------------------
    
    top_scorers_by_league_cols = ["Player", "MP", "Gls", "Squad", "Pos", "Age"]
    top_scorers_all_cols = ["Player", "MP", "Gls", "Squad", "Comp", "Pos", "Age"]

#------------Top scorers across all Top 5 leagues---------------

    five_league_scorers = (
        df[top_scorers_all_cols]
        .sort_values("Gls", ascending=False)
        .reset_index(drop=True)
        )

    five_league_scorers["RK"] = five_league_scorers.index + 1
    disp_scorers = ["RK"] + top_scorers_all_cols

    st.subheader("Top 25 scorers across top 5 leagues")
    st.dataframe(
        five_league_scorers[disp_scorers].head(25),
        use_container_width=True,
        hide_index=True
    )

#-----------------Graph---------------------------------

    st.subheader("Top 10 scorers in top 5 leagues ")
    
    top10_all = five_league_scorers.head(10)
    
    fig1 = px.bar(top10_all, x="Player", y="Gls", color = "Player", title="Top 10 scorers")
    st.plotly_chart(fig1)

#---------------League Selector---------------------

    leagues = (df["Comp"].unique())
    selected_league = st.selectbox(
        "Select a league",
        leagues
    )

#--------------Top scorers for selected leagues--------------

    filtered_league = df[df["Comp"] == selected_league]
    
    filtered_league_df = filtered_league[top_scorers_by_league_cols]

    top_scorers = (
        filtered_league_df
        .sort_values("Gls", ascending=False)
        .reset_index(drop=True)
        )
    
    top_scorers["RK"] = top_scorers.index + 1
    display_cols = ["RK"] + top_scorers_by_league_cols

    st.subheader(f"Top 25 scorers in {selected_league}")
    st.dataframe(
        top_scorers[display_cols].head(25), 
        use_container_width=True,
        hide_index=True
        )

#-----------------Graph---------------------------------

    st.subheader(f"Top 10 scorers in {selected_league} ")
    
    top10 = top_scorers.head(10)
    
    fig2 = px.bar(top10, x="Player", y="Gls", color = "Player", title="Top 10 scorers")
    st.plotly_chart(fig2)

#--------------------Top 50 players goals per 90------------------- 

    g90_df = df[df["90s"] > 0].copy()
    g90_df["goals_per_90"] = (g90_df["Gls"] / g90_df["90s"]).round(2)
    
    top_g90 = (
        g90_df
        .sort_values("goals_per_90", ascending=False)
        .reset_index(drop=True)
    )
    
    top_g90["RK"] = top_g90.index + 1

    st.subheader("Top 50 players with best goals per 90 ratio")
    st.dataframe(
        top_g90[["RK", "Player", "Min", "goals_per_90", "Gls", "Squad", "Comp", "Age"]].head(50),
        use_container_width=True,
        hide_index=True
    )

if __name__ == "__main__":
    main()