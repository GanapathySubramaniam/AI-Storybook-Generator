import streamlit as st
from streamlit import session_state as sess
from model import Chat,image_gen_model,tts

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
    text=novel_content[0]
    with st.spinner('Generating Images...'):
        for chapter in novel_content[1]:
            text+=f"\nChapter {chapter['number']}: {chapter['title']}\n"
            text+=chapter['content']
            images.append(sess.image_model.generate_image(chapter['content']))

    with st.spinner('Generating Audiobook...'):
        audio_file=tts(text)
    
    with st.expander('Audio Book'):
        st.audio(audio_file)
        
    st.title(novel_content[0])
    for i,chapter in enumerate(novel_content[1]):
        st.header(f"Chapter {chapter['number']}: {chapter['title']}")
        st.image(images[i])
        st.write(chapter['content'])
        st.markdown("---") 
    



        

