import streamlit as st
import webbrowser

def team_details():
    st.title("Our Team")

    team_members = [
        {
            "name": "Mohammadi Shifa",
            "role": "Lead Developer",
            "description": "Shifa is passionate about building innovative solutions and has a strong background in web development and AI.",
            "gmail": "shifamohammadi07@gmail.com",
            "usn": "USN: 1DT23CA025"
        },
        {
            "name": "Harsha",
            "role": "Data Scientist",
            "description": "Harsha specializes in machine learning algorithms and data analysis. She enjoys tackling complex problems.",
            "gmail": "harshasingh@gmail.com",
            "usn": "USN: B2345678"
        },
        {
            "name": "Kishitj",
            "role": "UI/UX Designer",
            "description": "Kishitj brings creativity to our team with a focus on user experience and interface design.",
            "gmail": "kishitj@gmail.com",
            "usn": "USN: C3456789"
        },
        {
            "name": "Fiona Ann Jacob",
            "role": "Data Scientist",
            "description": "Fiona specializes in machine learning algorithms and data analysis. She enjoys tackling complex problems.",
            "gmail": "fionaannjacob@gmail.com",
            "usn": "USN: 1DT23EC024"
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
