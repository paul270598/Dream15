import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide")  # Adjusting page layout
    st.title("Players Points Tracker")

    selected_owner = st.selectbox("Select Owner", ["Vaibhav", "Vishnu", "Vishal"])

    view_players(selected_owner)

def view_players(selected_owner):
    st.subheader(f"View Players Details for {selected_owner}")

    players_data = get_players_data(selected_owner)
    df = pd.DataFrame(players_data)
    df['Total Points'] = df.iloc[:, 2:].sum(axis=1)  # Calculate total points
    st.write(df)

def get_players_data(selected_owner):
    # Sample data
    players_data = {
        "Owner": [selected_owner]*15,
        "Player Name": get_player_names(selected_owner),
        "Match 1 Points": [10, 8, 6, 7, 9, 5, 4, 3, 2, 1, 0, 12, 14, 16, 11],
        "Match 2 Points": [5, 7, 9, 6, 8, 10, 4, 3, 2, 1, 0, 12, 14, 16, 11],
        "Match 3 Points": [8, 6, 5, 7, 9, 10, 4, 3, 2, 1, 0, 12, 14, 16, 11],
        "Match 4 Points": [6, 7, 8, 5, 9, 10, 4, 3, 2, 1, 0, 12, 14, 16, 11],
        "Match 5 Points": [9, 8, 6, 7, 5, 10, 4, 3, 2, 1, 0, 12, 14, 16, 11],
        "Match 6 Points": [10, 8, 6, 7, 9, 5, 4, 3, 2, 1, 0, 12, 14, 16, 11],
        "Match 7 Points": [10, 8, 6, 7, 9, 5, 4, 3, 2, 1, 0, 12, 14, 16, 11]
    }
    return players_data

def get_player_names(selected_owner):
    # Predefined player names
    if selected_owner == "Vaibhav":
        return [
            "John", "Jane", "Doe", "Alice", "Bob", "Emma", "Michael", "Sophia", "Liam", "Olivia",
            "William", "Ava", "James", "Charlotte", "Benjamin"
        ]
    elif selected_owner == "Vishnu":
        return [
            "David", "Mia", "Ethan", "Evelyn", "Alexander", "Amelia", "Daniel", "Harper", "Henry", "Abigail",
            "Sebastian", "Emily", "Matthew", "Ella", "Logan"
        ]
    elif selected_owner == "Vishal":
        return [
            "Lucas", "Scarlett", "Jackson", "Lily", "Aiden", "Grace", "Anthony", "Chloe", "Dylan", "Zoe",
            "Nicholas", "Madison", "Mason", "Sofia", "Elijah"
        ]
    else:
        return []

if __name__ == "__main__":
    main()
