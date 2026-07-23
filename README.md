# 🚨 AI Syllabus-to-Panic Calculator & Study Plan

> **Live Application URL:** [https://share.streamlit.io](https://share.streamlit.io) *(Replace with your Streamlit link once deployed)*

## 📌 Problem & Purpose
Students often face overwhelming exam stress when deadlines approach, making it hard to prioritize topics effectively under time pressure. The **AI Syllabus-to-Panic Calculator** turns last-minute panic into a clear, actionable game plan by calculating a real-time "Panic Index" and building a customized, hour-by-hour emergency study timeline.

## ✨ Key Features
* **Panic Index Score:** Instant percentage calculation indicating danger/stress levels based on remaining hours vs. topic volume.
* **Smart Prioritization:** Pinpoints core high-yield concepts required to pass/excel.
* **Hour-by-Hour Timeline:** A realistic study schedule broken down by exact topics.
* **Quick-Fire Survival Tips:** Actionable strategies to optimize last-minute study sessions.

## 🤖 The AI Engine & System Prompt
Powered by **Google Gemini API** (`gemini-1.5-flash`).

### System Instructions / Prompt
```text
You are a sharp, realistic, and highly motivating academic study planner.
The student is preparing for an exam in '{subject}'.
Topics to cover: {topics}
Time remaining until exam: {hours_left} hours.

Tasks:
1. Calculate a 'Panic Index Level' (percentage from 0% to 100%) based on topic count vs hours left.
2. Give a short, witty verdict on their current situation.
3. Provide an exact, realistic, hour-by-hour study timeline focusing ONLY on high-priority topics to ensure they pass/excel.
4. Give 3 actionable, quick-fire survival tips.
5.
