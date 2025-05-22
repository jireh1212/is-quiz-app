import streamlit as st

st.set_page_config(page_title="IS this a major?", page_icon="💻")

st.title("💻 IS this a major?")
st.write("Answer O (True) or X (False) to the following questions about Information Systems!")

questions = [
    ("Information Systems majors study both business and technology.", "O"),
    ("IS majors are eligible for a 3-year OPT after graduation.", "O"),
    ("If you major in IS, you don’t need to take classes in accounting, finance, or marketing.", "X"),
    ("You can start the IS major without knowing any coding.", "O"),
    ("Information Systems focuses more on solving real-world problems than Computer Science.", "O"),
    ("IS majors can work in app development, data analysis, cybersecurity, and more.", "O"),
]

score = 0
for i, (q, correct) in enumerate(questions, 1):
    user_answer = st.radio(f"Q{i}. {q}", ["O", "X"], key=f"q{i}")
    if user_answer == correct:
        score += 1

st.markdown("---")
if st.button("Submit Quiz"):
    st.success(f"✅ You scored {score} out of {len(questions)}!")
