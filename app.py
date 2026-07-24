import os
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Syllabus-to-Panic Calculator", page_icon="🚨"
)

st.title("🚨 AI Syllabus-to-Panic Calculator & Study Plan")
st.write(
    "Paste your course topics and see your panic level + custom study plan!"
)

# API Key handling
api_key = os.environ.get("GEMINI_API_KEY") or st.secrets.get(
    "GEMINI_API_KEY", ""
)

if not api_key:
  api_key = st.sidebar.text_input(
      "Enter your Gemini API Key:", type="password"
  )

syllabus_text = st.text_area(
    "Paste your course syllabus / exam topics here:", height=150
)
days_left = st.number_input(
    "Days left until exam:", min_value=1, max_value=30, value=3
)

if st.button("Calculate Panic Level & Plan 🚨"):
  if not api_key:
    st.error(
        "Please enter your Gemini API Key in the sidebar or set it in Streamlit"
        " Secrets!"
    )
  elif not syllabus_text.strip():
    st.warning("Please paste your syllabus first!")
  else:
    try:
      client = genai.Client(api_key=api_key)

      prompt = f"""
            You are a funny yet practical study coach.
            Analyze this syllabus and time left:
            Days Left: {days_left}
            Syllabus Topics: {syllabus_text}
            
            Provide:
            1. Panic Level Assessment (Low, Moderate, High, Critical) with a short humor-filled reasoning.
            2. Step-by-step study strategy divided across the remaining days.
            """

      response = client.models.generate_content(
          model="gemini-2.5-flash", contents=prompt
      )

      st.success("Analysis Complete!")
      st.markdown(response.text)

    except Exception as e:
      st.error(f"Error: {e}")
