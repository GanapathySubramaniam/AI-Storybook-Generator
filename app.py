import streamlit as st
from streamlit import session_state as sess
from model import Chat,image_gen_model

if 'model' not in sess:
    sess.model=Chat()

if 'image_gen' not in sess:
    sess.image_model=image_gen_model()

st.text_area('Describe the type of story you want...',key='story_description')
if st.button('Generate Story!'):
    with st.spinner('Generating a story for you...'):
        with st.expander('Story Generation'):
            st.write_stream(sess.model.stream_chat(sess.story_description))
    novel_content=sess.model.get_story()
    images=[]
    for chapter in novel_content[1]:
        images.append(sess.image_model.generate_image(chapter['content']))


    with st.expander('Story'):
        st.title(novel_content[0])
        for i,chapter in enumerate(novel_content[1]):
            st.header(f"Chapter {chapter['number']}: {chapter['title']}")
            st.image(images[i])
            st.write(chapter['content'])
            st.markdown("---") 



        

