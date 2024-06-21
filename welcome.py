import streamlit as st

def welcome():
    # Logo and main heading
    st.image("logo-hd.png", width=200)
    st.title("Welcome to PawSome-AI 🐾")
    st.write("Your AI-Powered Pet Care Assistant")
    st.markdown("---")  # Horizontal line

    # Main layout with two columns
    col1, col2 = st.columns(2)

    # Key Features section centered (Column 1)
    with col1:
        st.markdown("""
        <div style="background-color:#e5f7fa; padding:20px; border-radius:10px; text-align:center;">
        <h3 style="color:#007a87;">Key Features</h3>
        <p style="color:#333333;">Explore the capabilities that PawSome-AI offers to enhance your pet care experience:</p>
        <ul style="text-align:left;">
        <li><strong>Dog Breed Identification and Disease Detection</strong><br>
        Upload images to identify your dog's breed and detect diseases. Get detailed information on symptoms, precautions, and treatments.</li><br>

        <li><strong>Pet Care Chatbot</strong><br>
        Interactive chatbot for pet-care-related queries and advice. Receive personalized recommendations on nutrition, grooming, behavior, and more.</li><br>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # Additional Key Features (Column 2)
    with col2:
        st.markdown("""
        <div style="background-color:#e5f7fa; padding:20px; border-radius:10px;">
        <h3 style="color:#007a87;">Additional Key Features</h3>
        <ul style="text-align:left;">
        <li><strong>Prescription Analyzer</strong><br>
         Upload veterinary prescriptions to manage your pet's medications effectively
         Get detailed information about medications listed in the prescription. 
         <br>
                  
         
        <li><strong>Contact and Feedback</strong><br>
        Contact form for inquiries and feedback collection. Reach out to us for any questions or suggestions.</li><br>

        <li><strong>Future Features</strong><br>
        Planned enhancements to further assist pet owners. Suggestions are welcomed. </li><br>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # How to Use section centered (Spanning both columns)
    st.markdown("""
    <div style="background-color:#f9f9f9; padding:20px; border-radius:10px; text-align:center;">
    <h3 style="color:#4d4d4d;">How to Use</h3>
    <ul style="text-align:left;">
    <li>Navigate through the app using the sidebar menu on the left.</li>
    <li>Upload an image to detect dog breeds and diseases.</li>
    <li>Interact with the chatbot for personalized pet care advice.</li>
    <li>Use the Prescription Analyzer to manage your pet's medications.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
