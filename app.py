import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI Syllabus-to-Panic Calculator", page_icon="🚨", layout="centered")

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

            # System Prompt instructing AI
            prompt = f"""
            You are a sharp, realistic, and highly motivating academic study planner.
            The student is preparing for an exam in '{subject}'.
            Topics to cover: {topics}
            Time remaining until exam: {hours_left} hours.

            Tasks:
            1. Calculate a 'Panic Index Level' (percentage from 0% to 100%) based on topic count vs hours left.
            2. Give a short, witty verdict on their current situation (e.g., "78% Danger Zone - Put the coffee on!").
            3. Provide an exact, realistic, hour-by-hour study timeline focusing ONLY on high-priority topics to ensure they pass/excel.
            4. Give 3 actionable, quick-fire survival tips.

            Format the output clearly using Markdown headers, bullet points, and clean visual elements.
            """

            with st.spinner("Analyzing syllabus and calculating panic levels..."):
                response = model.generate_content(prompt)
                st.markdown("---")
                st.markdown(response.text)

        except Exception as e:
            st.error(f"Error generating plan: {e}")
