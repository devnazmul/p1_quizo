import streamlit as st
from api import generate_summary, generate_quiz, check_answer
from PIL import Image

with st.sidebar:
    st.subheader("Controls")

    # NOTE PICKER
    uploaded_notes = st.file_uploader("Upload your notes",type=["png","jpg","jpeg"],accept_multiple_files=True,max_upload_size=3)

    notes = []
    # IMAGE PREVIEW
    if(len(uploaded_notes)!=0):

        cols = st.columns(len(uploaded_notes))
        for i,note in enumerate(uploaded_notes):
            notes.append(Image.open(note))
            with cols[i]:
                # for i,note in enumerate(notes):
                st.image(note)

    # SELECTOR
    selected_defficality = st.selectbox("Select Difficality",("easy","medium","hard"),index=None)
    language = st.selectbox("Select Language",("English","Hindi","Bengali"),index=None)

    def get_status(selected_defficality):
        match selected_defficality:
            case "easy":
                st.markdown(f"Selected difficulty is: :green[**{selected_defficality.capitalize()}**]")
            case "medium":
                st.markdown(f"Selected difficulty is: :yellow[**{selected_defficality.capitalize()}**]")
            case "hard":
                st.markdown(f"Selected difficulty is: :red[**{selected_defficality.capitalize()}**]")

    if selected_defficality:
        get_status(selected_defficality)


    # SUBMIT
    is_submit_presed = st.button("Generate Notes",type="primary",use_container_width=True)

    # VALIDATION
    def validat():
        if is_submit_presed:
            if len(uploaded_notes) == 0:
                st.error("Please upload at least one note!")
            elif len(uploaded_notes) > 3:
                st.error("You can't upload more than 3 notes!")
            elif not selected_defficality:
                st.error("Please select a difficulty level!")
            else:
                return True



st.header("Qizo - AI Powered Quiz Generator",anchor=False)
st.text("Upload upto 3 images of your notes and we will generate quiz for you.")
st.divider()

if validat():
    with st.container(border=True):
        with st.spinner("Generating Summury..."):
            summary = generate_summary(notes, language)
            st.markdown(summary)

    with st.container(border=True):
        with st.spinner("Generating Quiz..."):
            quiz = generate_quiz(notes, language, selected_defficality)
            st.markdown(quiz)

    with st.expander("Check your answer"):
        with st.spinner("Checking your answer..."):
            result = check_answer(quiz)
            st.markdown(result)