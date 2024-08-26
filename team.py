import streamlit as st
import webbrowser

def team_details():
    st.title("Our Team")

    team_members = [
        {
            "name": "Mohammed Musharraf",
            "role": "Founder & Developer",
            "description": "Mohammed Musharraf is dedicated to crafting innovative digital solutions. With a strong foundation in app and web development, he is passionate about utilizing technology to address real-world problems.",
            "gmail": "iammusharraf11@gmail.com",
            "usn": "SRN: PES2UG23CS915"
        }
    ]

    for member in team_members:
        st.header(member["name"])
        st.subheader(member["role"])
        st.write(member["description"])
        st.write(member["usn"])
        if st.button(f"Contact {member['name']} via Gmail"):
            webbrowser.open_new_tab(f"mailto:{member['gmail']}?subject=Regarding%20PawSome-AI%20App")

if __name__ == "__main__":
    team_details()
