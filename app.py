# streamlit_app.py

import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Function to load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
local_css("style/style.css")

# Load Animation
animation_symbol = "🍂"

# Display the falling leaves animation
st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

# Define the start date of the anniversary
start_date = datetime(2023, 10, 21)

# Function to calculate the time difference in months, days, hours, and minutes
def get_anniversary_count():
    current_date = datetime.now()
    
    # Calculate the number of complete months between the dates
    months = relativedelta(current_date, start_date).months
    # Calculate the number of complete years and add them to months
    years = relativedelta(current_date, start_date).years
    months += years * 12
    
    # Calculate the time delta ignoring the full months to get exact days, hours, minutes
    month_adjusted_date = start_date + relativedelta(months=months)
    delta = current_date - month_adjusted_date
    
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60

    return months, days, hours, minutes

# Main function to run the Streamlit app
def main():
    months, days, hours, minutes = get_anniversary_count()
    st.markdown(
        f"<h1 style='text-align: center;'>Happy {months} Months, {days} Days, {hours} Hours, and {minutes} Minutes Anniversary Hunbun!!!</h1>", 
        unsafe_allow_html=True
    )
    st.image('love.gif', use_column_width=True)

    # Initialize session state for showing the kiss GIF and timestamp
    if 'show_kiss' not in st.session_state:
        st.session_state.show_kiss = False
    if 'kiss_start_time' not in st.session_state:
        st.session_state.kiss_start_time = None

    # Centering and styling the button using CSS
    st.markdown(
        """
        <style>
        .centered-button {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .kiss-button {
            padding: 20px 40px;
            font-size: 20px;
            background-color: #FF69B4;
            border: none;
            border-radius: 8px;
            color: white;
            cursor: pointer;
        }
        .kiss-button:hover {
            background-color: #FF1493;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create a centered button that triggers the kiss GIF
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio for centering
    with col2:
        if st.button("Kiss 💋", use_container_width=True, key="kiss_button"):
            st.session_state.show_kiss = True
            st.session_state.kiss_start_time = datetime.now()

    # Display the kiss GIF and manage its visibility
    if st.session_state.show_kiss:
        st.image('kiss_emoji.gif', use_column_width=True)
        # Check if 3 seconds have passed since the button was clicked
        if datetime.now() - st.session_state.kiss_start_time > timedelta(seconds=3):
            st.session_state.show_kiss = False  # Hide the GIF after 3 seconds
            st.session_state.kiss_start_time = None
            st.experimental_rerun()  # Force re-render to "delete" the GIF

# Run the app
if __name__ == "__main__":
    main()
