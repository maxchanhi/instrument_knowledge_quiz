import streamlit as st
from topics import pick_topic
from data import fun_emoji_list
from streamlit_extras.let_it_rain import rain
import random

ss=st.session_state
if "choosen_topic" not in ss:
    ss["choosen_topic"]=None
if "get_url" not in ss:
    ss["get_url"]=None
if "pressed" not in ss:
    ss["pressed"]=False
st.title('Music Quiz')
topics= ['Reed', 'Transposing',"Clef","Voice types","Piano","Ornaments","Inst. technique"]
topics_selected = st.multiselect('Select topics to be quizzed on:',topics,default=topics)
new_question = st.button('New question')
if not topics_selected:
    st.warning('Please select at least one topic.')
if new_question and topics_selected:
    ss["pressed"]=False
    test_topic = random.choice(topics_selected)
    ss["choosen_topic"] = pick_topic(test_topic)
    if test_topic == "Ornaments":
        ss["get_url"] = ss["choosen_topic"]["pic_url"]
    else:
        ss["get_url"] = None

if ss["choosen_topic"]:
    st.subheader(ss["choosen_topic"]['question'])
    if ss["get_url"]:
        st.image(ss["get_url"])
    reed_options = st.radio("Options:", ss["choosen_topic"]['options'])
    if st.button('Check Answer', disabled=ss["pressed"]):
        ss["pressed"]=True 
        if reed_options == ss["choosen_topic"]['answer']:
            fun_emoji = random.choice(fun_emoji_list)
            st.success(f"Correct!{fun_emoji}")
            rain(emoji = fun_emoji,animation_length="1")
            st.balloons()
        else:
            ans =ss["choosen_topic"]['answer']
            st.error(f"Wrong! The correct answer is {ans}.")

