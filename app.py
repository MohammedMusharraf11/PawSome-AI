import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="PawSome-AI", 
    page_icon="🐾", 
    layout="centered", 
    initial_sidebar_state="auto"
)

# Display your logo at the top of the main page
# Adjust the path to your logo image

# st.header("Welcome to PawSome AI")

with st.sidebar:
    selected = option_menu(
        'PawSome AI',
        ['Welcome', 'Disease & Breed Detection', 'Petcare ChatBot', 'Prescription-Analyzer', 'Team Details', 'Feedback'],
        icons=['house-door-fill', 'search', 'chat-right-fill', 'file-earmark-break-fill', 'info', 'star'],
        menu_icon="🐶",
        default_index=0
    )

if selected == 'Welcome':
    import welcome
    welcome.welcome()

if selected == 'Disease & Breed Detection':
    import model
    model.model()

if selected == 'Petcare ChatBot':
    import chatbot
    chatbot.chatbot()

if selected == 'Prescription-Analyzer':
    import prescription
    prescription.presc_analyze()

if selected == 'Feedback':
    import feedback
    feedback.feedback()
if selected == 'Team Details':
    import team
    team.team_details()
