import streamlit as st
from streamlit import session_state as sess
from model import Chat

if 'model' not in sess:
    sess.model=Chat()

st.text_area('Describe the type of story you want...',key='story_description')
if st.button('Generate Story!'):
    with st.spinner('Generating a story for you...'):
        with st.expander('Story Generation'):
            st.write_stream(sess.model.stream_chat(sess.story_description))
    with st.expander('Story'):
        novel_content=sess.model.get_story()
        st.title(novel_content[0])
        for chapter in novel_content[1]:
            st.header(f"Chapter {chapter['number']}: {chapter['title']}")
            st.write(chapter['content'])
            st.markdown("---") 



        

