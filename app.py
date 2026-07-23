import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI Syllabus-to-Panic Calculator", page_icon="🚨", layout="centered")

# Hide Streamlit's default "Press Ctrl+Enter to submit form" text
st.markdown("""
    <style>
    div[data-testid="InputInstructions"] {display: none !important;}
    </style>
""", unsafe_allow_html=True)

st.title("🚨 AI Syllabus-to-Panic Calculator")
st.subheader("Turn exam panic into a step-by-step action plan!")

# User Inputs
with st.form("exam_form"):
    subject = st.text_input("Subject Name", placeholder="e.g., Object-Oriented Programming")
    topics = st.text_area("Topics/Syllabus to Cover", placeholder="e.g., Classes & Objects, Inheritance, Polymorphism, Pointers, File I/O", help="Enter your topics here")
    hours_left = st.number_input("Hours Remaining Until Exam", min_value=1, max_value=168, value=12)
    api_key = st.text_input("Enter your Gemini API Key", type="password")

    submitted = st.form_submit_button("Calculate Panic & Generate Plan 🚀")

if submitted:
    if not api_key:
        st.error("Please enter a valid Gemini API Key!")
    elif not subject or not topics:
        st.warning("Please fill in all details before generating!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')

            prompt = f"""
            You are a smart academic advisor. A student needs help planning their study schedule.
            
            Subject: {subject}
            Topics to cover: {topics}
            Hours remaining until exam: {hours_left} hours

            Please provide:
            1. Panic Level (Low / Medium / High / CRITICAL) with a brief funny explanation.
            2. A realistic hour-by-hour study plan customized for the remaining time.
            3. Top 3 quick tips to maximize productivity and avoid burnout.
            """

            with st.spinner("Analyzing syllabus and calculating panic levels..."):
                response = model.generate_content(prompt)
                
            st.success("Plan Generated Successfully!")
            st.markdown("---")
            st.write(response.text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
