import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide", initial_sidebar_state="expanded")  # Adjusting page layout
    st.title("Dream 15")

    # Load data from CSV
    github_url = "https://raw.githubusercontent.com/paul270598/Dream15/main/players_list.csv"
    df = pd.read_csv(github_url)

    # Replace None values with 0
    df = df.fillna(0)

    # Calculate total points for each player
    df['Total Points'] = 0
    for i in range(1, 8):
        match_col = f'Match {i}'
        df['Total Points'] += df[match_col].astype(float) * df['Points']

    # Display leaderboard at the top with 100% width
    show_leaderboard(df)

    selected_owner = st.selectbox("Select Owner", df['Owner'].unique(), key='selectbox', format_func=lambda x: x.title(), help="Select owner from the list")

    # Display selected owner's total points
    selected_owner_points = df[df['Owner'] == selected_owner]['Total Points'].sum()
    st.write(f"Total Points for {selected_owner}: {selected_owner_points}")

    # Display leaderboard adjacent to dropdown
    st.write("", "")
    col1, col2, col3 = st.columns([1, 3, 1])  # Define col3
    with col1:
        pass  # No need to show leaderboard again here
    with col2:
        view_players(selected_owner, df)
    with col3:
        pass  # Empty column for spacing

def view_players(selected_owner, df):
    st.subheader(f"View Players Details for {selected_owner}")

    filtered_df = df[df['Owner'] == selected_owner].copy()  # Make a copy to avoid SettingWithCopyWarning

    # Add 'x' to every number in the 'Points' column
    filtered_df['Points'] = filtered_df['Points'].astype(str) + 'x'

    # Reset index and start index from 1 for each owner
    filtered_df = filtered_df.reset_index(drop=True)
    filtered_df.index += 1

    st.write(filtered_df, unsafe_allow_html=True)

    # CSS for styling
    st.markdown(
        f"""
        <style>
            /* Full-width table */
            .dataframe {{
                width: 100% !important;
            }}
            /* Background and box shadow */
            .stDataFrame {{
                background-color: #f0f0f0;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            /* Full-width container for the table */
            .stDataFrame div[data-baseweb="table-container"] {{
                width: 100% !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def show_leaderboard(df):
    # Calculate total points for each owner
    df['Total Points'] = 0
    for i in range(1, 8):
        match_col = f'Match {i}'
        df['Total Points'] += df[match_col].astype(float) * df['Points']

    # Calculate total points for each owner
    owners_total_points = df.groupby('Owner')['Total Points'].sum().reset_index()

    # Sort leaderboard based on most points to least points
    leaderboard = owners_total_points.sort_values(by='Total Points', ascending=False).reset_index(drop=True)

    # Reset index to start from 1
    leaderboard.index += 1

    # Display leaderboard at the top with 100% width
    st.subheader("Leaderboard")
    st.write(leaderboard, unsafe_allow_html=True)

    # CSS for styling
    st.markdown(
        f"""
        <style>
            /* Full-width table */
            .dataframe {{
                width: 100% !important;
            }}
            /* Background and box shadow */
            .stDataFrame {{
                background-color: #f0f0f0;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            /* Full-width container for the table */
            .stDataFrame div[data-baseweb="table-container"] {{
                width: 100% !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
