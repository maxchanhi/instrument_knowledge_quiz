
import streamlit as st
from topics import pick_topic
from data import fun_emoji_list
from streamlit_extras.let_it_rain import rain
from AI_feedback import provide_feedback
import random,os
ss=st.session_state
if "choosen_topic" not in ss:
    ss["choosen_topic"]=None
if "get_url" not in ss:
    ss["get_url"]=None
if "student_ans" not in ss:
    ss["student_ans"]=[]
if "pressed_kn" not in ss:
    ss["pressed_kn"]=True
if 'userpd'not in ss:
    ss['userpd']=None
    ss["pw_visiable"]=True
st.title('Music Quiz')
def main():
    topics= ['Reed', 'Transposing',"Clef","Voice types","Piano","Orniments","Inst. technique"]
    topics_selected = st.multiselect('Select topics to be quizzed on:',topics,default=topics)
    new_question = st.button('New question')
    if not topics_selected:
        st.warning('Please select at least one topic.')
    if new_question and topics_selected and ss["pressed_kn"]:
        ss["pressed_kn"]=False
        test_topic = random.choice(topics_selected)
        ss["choosen_topic"] = pick_topic(test_topic)
        choosen_topic = ss["choosen_topic"]
        if test_topic == "Orniments":
            ss["get_url"] = ss["choosen_topic"]["pic_url"]
        else:
            ss["get_url"] = None
    if ss["choosen_topic"]:
        choosen_topic = ss["choosen_topic"]
        st.subheader(choosen_topic['question'])
        if ss["get_url"]:
            st.image(ss["get_url"])
        reed_options = st.radio("Options:", choosen_topic['options'])
        if st.button('Check Answer',disabled=ss["pressed_kn"]):
            ss["pressed_kn"]=True
            if reed_options == choosen_topic['answer']:
                fun_emoji = random.choice(fun_emoji_list)
                st.success(f"Correct!{fun_emoji}")
                rain(emoji = fun_emoji,animation_length="1")
                st.balloons()
                ss["student_ans"].append([choosen_topic['question'],"student answer: "+reed_options,"correct"])
            else:
                st.error(f"Wrong! The correct answer is {choosen_topic['answer']}.")
                ss["student_ans"].append([choosen_topic['question'],"student answer: "+reed_options,"incorrect"])
            print(ss["student_ans"])
    ss['userpd'] = st.text_input('Enter your password for full access or find Max for password:',label_visibility=ss["pw_visiable"])
    
    if len(ss["student_ans"])>5:
        if st.button('You can get an AI feedback'):
            with st.spinner("Generating feedback..."):
                if os.environ['Password'] == ss['userpd']:
                    st.write("You now have full access to the feedback!")
                    feedback = provide_feedback(ss["student_ans"],128)
                    ss["pw_visiable"] = False
                else:
                    st.write("You can only preview!")
                    feedback = provide_feedback(ss["student_ans"], 32)
            st.success(feedback)
            ss["student_ans"]= []

if __name__ == '__main__':
    
    main()


