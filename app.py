import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Football-data-dashboard", initial_sidebar_state="expanded")

def show_rank_table(df, sort_col, display_cols, title, top_n=25):
    rank = (
        df.sort_values(sort_col, ascending=False)
        .reset_index(drop=True)
    )
    rank["RK"] = rank.index + 1

    st.subheader(title)
    st.dataframe(
        rank[display_cols].head(top_n),
        use_container_width=True,
        hide_index=True
    )

def main():
    df = pd.read_csv("data/player_stats_25.csv")
    
    st.title("Football Data Dashboard 24/25")

    with st.sidebar:
        st.header("About this project")
        st.write(
            """
            This dashboard analyzes attacking performances across
            Europe's top 5 football leagues (2024/2025 season).
            """
        )

        st.divider()

        st.header('Metrics Explained')
        st.markdown(
            """
            **Goals per 90**
            Average goals scored per full 90 minutes played.

            **Assists per 90**
            Average assists per full 90 minutes played.

            **Goals + Assists per 90(G/A per 90)**
            Combined attacking contribution per 90 minutes.

            These metrics help compare players with different playing time.
            """
        )
        
        st.divider()

        st.header("About Author")
        st.markdown(
            '''
            **Author:** Alec Rodriguez

            **Built with:**
            - Python
            - Streamlit
            - Pandas
            - Plotly Express

            **Focus:** Football data analysis & vizualization
            '''
        )

        st.divider()

        st.header("Data source")
        st.markdown(
            '''
            **Platform:** Kaggle
            **Dataset:** Football Players Stats (2024-2025)
            **Author:** Hubert Sidorowicz
            **License:** MIT

            Data originally sourced from **FBref** and updated weekly.
            '''
        )
        st.markdown(
            "[View dataset on Kaggle](https://www.kaggle.com/datasets/hubertsidorowicz/football-players-stats-2024-2025)"
        )

#----------------Columns------------------------------
    
    top_scorers_by_league_cols = ["Player", "MP", "Gls", "Squad", "Pos", "Age"]
    top_scorers_all_cols = ["Player", "MP", "Gls", "Squad", "Comp", "Pos", "Age"]

#------------Top scorers across all Top 5 leagues---------------

    disp_scorers = ["RK"] + top_scorers_all_cols

    show_rank_table(df[top_scorers_all_cols], 
        sort_col="Gls", 
        display_cols=disp_scorers, 
        title="Top 25 scorers across top 5 leagues", 
        top_n=25
    )

#-----------------Graph---------------------------------

    st.subheader("Top 10 scorers in top 5 leagues ")
    
    top10_all = df[top_scorers_all_cols].sort_values("Gls", ascending=False).head(10)
    
    fig1 = px.bar(top10_all, x="Player", y="Gls", color = "Player", title="Top 10 scorers")
    st.plotly_chart(fig1)
    st.divider()

#---------------League Selector---------------------

    leagues = sorted(df["Comp"].unique())
    selected_league = st.selectbox(
        "Select a league",
        leagues
    )

#--------------Top 25 scorers for selected leagues--------------

    filtered_league = df[df["Comp"] == selected_league]
    filtered_league_df = filtered_league[top_scorers_by_league_cols]
    
    display_cols = ["RK"] + top_scorers_by_league_cols

    show_rank_table(filtered_league_df, 
        sort_col="Gls", 
        display_cols=display_cols, 
        title=f"Top 25 scorers in {selected_league}", 
        top_n=25
    )

#-----------------Graph---------------------------------

    st.subheader(f"Top 10 scorers in {selected_league} ")
    
    top_10 = filtered_league_df.sort_values("Gls", ascending=False).head(10)
    
    fig2 = px.bar(top_10, x="Player", y="Gls", color = "Player", title="Top 10 scorers")
    st.plotly_chart(fig2)
    st.divider()

#--------------------Top 50 players stat per 90------------------- 

    selected_stat = st.selectbox(
        "Select a statistic",
        [
            "Goals per 90",
            "Assists per 90",
            "Goals + Assists per 90"
        ]
    )

    base_df = df[df["90s"] > 0].copy()

    if selected_stat == "Goals per 90":
        base_df["stat_value"] = (base_df["Gls"] / base_df["90s"]).round(2)
        title = "Top 50 players by Goals per 90"
        stat_label = "Goals per 90"
        display_cols = ["RK", "Player", "Min", "stat_value", "Gls", "Squad", "Comp", "Age"]
    
    elif selected_stat == "Assists per 90":
        base_df["stat_value"] = (base_df["Ast"] / base_df["90s"]).round(2)
        title = "Top 50 players by Assists per 90"
        stat_label = "Assists per 90"
        display_cols = ["RK", "Player", "Min", "stat_value", "Ast", "Squad", "Comp", "Age"]
    
    else:
        base_df["GA"] = base_df["Gls"] + base_df["Ast"]
        base_df["stat_value"] = (base_df["GA"] / base_df["90s"]).round(2)
        title = "Top 50 players by Goals + Assists per 90"
        stat_label = "Goals + Assists per 90"
        display_cols = ["RK", "Player", "Min", "stat_value", "Gls", "Ast", "Squad", "Comp", "Age"]

    base_df = base_df.rename(columns={"stat_value": stat_label})

    display_cols= ["RK", "Player", "Min", stat_label, "Gls", "Ast", "Squad", "Comp", "Age"]

    show_rank_table(
        df=base_df,
        sort_col=stat_label,
        display_cols=display_cols,
        title=title,
        top_n=50
    )
    
#----Do not touch----------
if __name__ == "__main__":
    main()