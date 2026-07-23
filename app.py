import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="AI Syllabus-to-Panic Calculator", page_icon="📚")

# Hide Streamlit input instructions
st.markdown("""
<style>
[data-testid="InputInstructions"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 AI Syllabus-to-Panic Calculator")
st.subheader("Calculate your panic level & get a custom study plan!")

# Sidebar
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

# Form
with st.form("study_form"):
    subject = st.text_input("Subject Name:")
    topics = st.text_area("Topics to Cover:")
    hours_left = st.number_input("Hours left until exam:", min_value=1, value=12)
    submitted = st.form_submit_button("Calculate Panic & Plan")

if submitted:
    if not api_key:
        st.error("Please enter your Gemini API Key.")
    elif not subject or not topics:
        st.warning("Please fill in all details.")
    else:
        try:
            genai.configure(api_key=api_key)

            # Latest Gemini model
            model = genai.GenerativeModel("gemini-2.5-flash")

            prompt = f"""
You are a smart academic advisor.

Subject: {subject}
Topics to cover: {topics}
Hours remaining until exam: {hours_left}

Please provide:

1. Panic Level (Low / Medium / High / CRITICAL) with a funny explanation.
2. Hour-by-hour study plan.
3. Top 3 productivity tips.
"""

            response = model.generate_content(prompt)

            st.success("Plan Generated Successfully!")
            st.markdown("---")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
