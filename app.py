import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="AI Syllabus-to-Panic Calculator", page_icon="📚")

# Hide Streamlit input instructions CSS
st.markdown("""
    <style>
    [data-testid="InputInstructions"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📚 AI Syllabus-to-Panic Calculator")
st.subheader("Calculate your panic level & get a custom study plan!")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

# Input Form
with st.form("study_form"):
    subject = st.text_input("Subject Name:")
    topics = st.text_area("Topics to Cover:")
    hours_left = st.number_input("Hours left until exam:", min_value=1, value=12)
    submitted = st.form_submit_button("Calculate Panic & Plan")

# Handle Submission
if submitted:
    if not api_key:
        st.error("Please enter a valid Gemini API Key in the sidebar!")
    elif not subject or not topics:
        st.warning("Please fill in all details before generating!")
    else:
        with st.spinner("Analyzing syllabus and calculating panic levels..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')

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

                response = model.generate_content(prompt)
                st.success("Plan Generated Successfully!")
                st.markdown("---")
                st.markdown(response.text)

            except Exception as e:
                # Fallback to gemini-pro if flash is unavailable
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(prompt)
                    st.success("Plan Generated Successfully!")
                    st.markdown("---")
                    st.markdown(response.text)
                except Exception as inner_error:
                    st.error(f"An error occurred: {e}")
