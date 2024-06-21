import streamlit as st
import pandas as pd
from datetime import datetime

def feedback():
    st.title("Feedback")
    st.write("We value your feedback to help us improve PawSome-AI!")

    # Feedback form
    with st.form(key='feedback_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        feedback_type = st.selectbox("Type of Feedback", ["Suggestion", "Issue", "Other"])
        message = st.text_area("Your Feedback")
        submit_button = st.form_submit_button(label="Submit")

    # After the user clicks the submit button
    if submit_button:
        feedback_data = {
            "name": [name],
            "email": [email],
            "feedback_type": [feedback_type],
            "message": [message],
            "timestamp": [datetime.now()]
        }
        feedback_df = pd.DataFrame(feedback_data)

        # Save the feedback to a CSV file
        try:
            existing_feedback_df = pd.read_csv("feedback.csv")
            feedback_df = pd.concat([existing_feedback_df, feedback_df], ignore_index=True)
        except FileNotFoundError:
            pass

        feedback_df.to_csv("feedback.csv", index=False)

        st.success("Thank you for your feedback! We'll get back to you shortly.")

    st.write("If you need immediate assistance, please contact us at: ")
    st.markdown("[contact.pawsomeai@gmail.com](mailto:contact.pawsomeai@gmail.com)")
