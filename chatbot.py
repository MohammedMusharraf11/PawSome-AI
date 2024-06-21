def chatbot():
    # Importing all the modules
    import streamlit as st
    from PyPDF2 import PdfReader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    import os
    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    import google.generativeai as genai
    from langchain.vectorstores import FAISS
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.chains.question_answering import load_qa_chain
    from langchain.prompts import PromptTemplate
    from dotenv import load_dotenv
    import pyttsx3

    def speak_response(response_content):
        engine = pyttsx3.init()
        engine.say(response_content)
        engine.runAndWait()

    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)

    def get_pdf_text(pdf_docs):
        text = ""
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text

    def get_text_chunks(text):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        chunks = text_splitter.split_text(text)
        return chunks

    def get_vector_store(text_chunks):
        embedding_function = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embedding_function)
        vector_store.save_local("faiss_index")

    def get_conversational_chain():
        prompt_template = """
        Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
        provided context then go and find and provide the answer don't provide the wrong answer and your a expert in pet-care so make sure all your responses are within that.\n\n
        Context:\n {context}?\n
        Question: \n{question}\n

        Answer:
        """
        model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.3)
        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
        return chain

    def user_input(user_question):
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(user_question)
        chain = get_conversational_chain()
        response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
        return response["output_text"]

    # Main function for the chatbot
    st.title("Pet Care ChatBot 🐾")
    st.subheader("Your AI-Powered Pet Care Assistant")
    st.markdown("""
    Welcome to the Pet Care ChatBot! Ask any question related to pet care, and our AI-powered assistant will provide you with detailed and accurate answers.
    """)
    voice_response = st.checkbox("Click for Voice Response")

    if "messages" not in st.session_state:
        st.session_state.messages = []

# Uncomment if you want to add your own-custom pdf:
    # with st.form(key="uploader_form"):
    #     pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
    #     submit_button = st.form_submit_button(label="Submit & Process")
    # if submit_button:
    #     if pdf_docs:
    #         with st.spinner("Processing..."):
    #             raw_text = get_pdf_text(pdf_docs)
    #             text_chunks = get_text_chunks(raw_text)
    #             get_vector_store(text_chunks)
    #             st.success("Processing completed successfully.")
    #     else:
    #         st.warning("Please upload at least one PDF file.")

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Ask a question from the PDF files"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = user_input(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
            if voice_response:
                speak_response(response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
