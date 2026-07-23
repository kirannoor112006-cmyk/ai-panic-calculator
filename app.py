if submitted:
    if not api_key:
        st.error("Please enter a valid Gemini API Key!")
    elif not subject or not topics:
        st.warning("Please fill in all details before generating!")
    else:
        with st.spinner("Analyzing syllabus and calculating panic levels..."):
            try:
                genai.configure(api_key=api_key)
                
                # Standard syntax for Google Generative AI library
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
                # Fallback if model version mismatch occurs on Streamlit Cloud
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(prompt)
                    st.success("Plan Generated Successfully!")
                    st.markdown("---")
                    st.markdown(response.text)
                except Exception as inner_error:
                    st.error(f"An error occurred: {e}")
