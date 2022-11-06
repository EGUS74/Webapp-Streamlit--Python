import streamlit as st
from streamlit_lottie import st_lottie
import requests as req
from PIL import Image


st.set_page_config(page_title="Kool Kraterzzz", page_icon=':simple_smile:', layout='wide')

def load_lottieURL(url):
    r = req.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieURL('https://assets3.lottiefiles.com/packages/lf20_ox5eapmh.json')
image_1 = Image.open('images/8DA08C3D-7C04-4FBD-8749-5CCC72B0AB22_1_105_c.jpeg')
image_2 = Image.open('images/72F591B0-FD36-488C-9E62-6DEEFEE8EA7C_1_105_c.jpeg')


with st.container():
    st.subheader('Yow... This is the gamers DEN! :wave:')
    st.title("Python KooL Kraterzzzz")
    st.write('ease off bruh...!')
    st.write('See me there....')
    st.write("[learn more about Kraterzz..](www.google.coolcraters.com)")


with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('what we do..')
        st.write('##') 
        st.write(
            '''
            When I SuS..
            we do code...
            when we not sus..
            we also do code... bruhhh!
            '''
        )  

        st.write('[our channel](www.youtube.com)')


    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')


# ---- Projects -------
with st.container():
        st.write('---')
        st.header('Kraterz work..')
        st.write('##')
        image_column, text_column = st.columns((1, 2))
       
        with image_column:
            st.image(image_1)
            st.image(image_2)

        with text_column:
            st.subheader('Some kool amination from kraterz\n')
            st.write(
                '''
                learn how to use lotties files in streamlit!\n
                Animation for kraterz Sussss....!!!!\n
                buckle up and enjoy the slide..!
                '''
            )
        st.markdown("[wantch out... ](https://youtube.com/shorts/YJxLKbWefKM?feature=share)")

with st.container():
    st.write('---')
    st.header('Wanna get in touch with a Kool Krater?!')
    st.subheader('don\'t say you were not warne ::ghost::\n')
    st.write('##')