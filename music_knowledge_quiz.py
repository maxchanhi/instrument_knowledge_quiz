
import streamlit as st
from topics import pick_topic
import random
ss=st.session_state
if "choosen_topic" not in ss:
    ss["choosen_topic"]=None
st.title('Music Quiz')
choosen_topic = ss["choosen_topic"]
topics= ['Reed', 'Transposing',"Clef","Voice types","Piano"]
topics_selected = st.multiselect('Select topics to be quizzed on:',topics,default=topics)
new_question = st.button('New question')
if new_question:
    test_topic = random.choice(topics_selected)
    ss["choosen_topic"] = pick_topic(test_topic)
    print(choosen_topic,topics_selected)
    st.rerun()
if choosen_topic:
    st.subheader(choosen_topic['question'])
    reed_options = st.radio("Options:", choosen_topic['options'],index=None)
    if st.button('Check Answer'):
        if reed_options == choosen_topic['answer']:
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is {choosen_topic['answer']}.")


