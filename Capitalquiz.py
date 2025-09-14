import streamlit as st
import random

# Dictionary of countries and capitals (top ~50 popular ones)
countries_capitals = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Brazil": "Brasilia",
    "Argentina": "Buenos Aires",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Bern",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Denmark": "Copenhagen",
    "Finland": "Helsinki",
    "Poland": "Warsaw",
    "Russia": "Moscow",
    "China": "Beijing",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "South Korea": "Seoul",
    "Australia": "Canberra",
    "New Zealand": "Wellington",
    "South Africa": "Pretoria",
    "Nigeria": "Abuja",
    "Egypt": "Cairo",
    "Turkey": "Ankara",
    "Saudi Arabia": "Riyadh",
    "United Arab Emirates": "Abu Dhabi",
    "Israel": "Jerusalem",
    "Thailand": "Bangkok",
    "Vietnam": "Hanoi",
    "Indonesia": "Jakarta",
    "Philippines": "Manila",
    "Pakistan": "Islamabad",
    "Bangladesh": "Dhaka",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Afghanistan": "Kabul",
    "Greece": "Athens",
    "Austria": "Vienna",
    "Ireland": "Dublin",
    "Singapore": "Singapore",
    "Malaysia": "Kuala Lumpur",
    "Kenya": "Nairobi",
    "Colombia": "Bogotá",
}

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(list(countries_capitals.items()), 10)
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.finished = False
    st.session_state.answered = False
    st.session_state.last_feedback = ""

st.title("🌍 Capital Cities Quiz")

if not st.session_state.finished:
    q_num = st.session_state.current_q + 1
    country, capital = st.session_state.questions[st.session_state.current_q]

    st.subheader(f"Question {q_num} of 10")
    user_answer = st.text_input(f"What is the capital of **{country}**?", key=f"q{q_num}")

    # Submit button → check correctness but don't move on yet
    if st.button("Submit Answer", key=f"submit{q_num}"):
        if user_answer.strip().lower() == capital.lower():
            st.session_state.last_feedback = "✅ Correct!"
            st.session_state.score += 1
        else:
            st.session_state.last_feedback = f"❌ Wrong! The correct answer is **{capital}**"
        st.session_state.answered = True
        st.rerun()

    # Show feedback if answered
    if st.session_state.answered:
        if st.session_state.last_feedback.startswith("✅"):
            st.success(st.session_state.last_feedback)
        else:
            st.error(st.session_state.last_feedback)

        # Next Question button (appears only after answering)
        if st.button("Next Question", key=f"next{q_num}"):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.last_feedback = ""
            if st.session_state.current_q >= 10:
                st.session_state.finished = True
            st.rerun()

else:
    st.subheader("🎉 Quiz Finished!")
    st.write(f"Your Score: **{st.session_state.score}/10**")

    # Intelligence message
    score = st.session_state.score
    if score == 10:
        st.success("🌟 You are very intelligent!")
    elif 5 <= score <= 7:
        st.info("🙂 You are moderately intelligent.")
    elif 3 <= score < 5:
        st.warning("😐 You are very average.")
    else:
        st.error("😞 Poor general knowledge.")

    # Reset button
    if st.button("Play Again"):
        for key in ["questions", "current_q", "score", "finished", "answered", "last_feedback"]:
            st.session_state.pop(key, None)
        st.rerun()
