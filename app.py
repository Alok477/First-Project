from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":upside_down_face:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")        
    

lottie_coding1 = load_lottieurl("https://lottie.host/9dfab803-6079-4f53-ae19-cf34688b122e/C3d8dKQ8Tp.json")
lottie_coding = load_lottieurl("https://lottie.host/25d15a88-76ad-4bfa-9dc0-14a3d3b5cf8a/bowbEeSo3j.json")

img_contact_form = Image.open("C:/Users/PRITAM/Desktop/webpage/images/img 1.jpg")
img_lottie_animation = Image.open("C:/Users/PRITAM/Desktop/webpage/images/img 2.jpg")

with st. container():
    st.subheader("Hi, I am Alok:wave:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title(" First project ")
        st.write(" This is my first ever website suppositely made for fun . But it's definately not fun just looking at an awkward webpage made by a Bigenner. So, you can go watch some anime instead")
        st.write("[Go check some more useful stuff>](https://www.youtube.com/)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding1")

with st. container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who even am I:face_with_raised_eyebrow:")
        st.write("I am a computer science student. I like to learn new things using coding and try new games . But why did I create this webite? Who cares. I sure like to watch anime alot.The link below contains some good anime suggestions you can go check if you want ")
        st.write("[Some Fun Topics >](https://gamerant.com/best-isekai-anime-to-watch-ranked/)")

    with right_column:
        st_lottie(lottie_coding1, height=300, key="coding")



with st.container():
    st.write("---")
    st.header("My Projects:shushing_face:")
    st.write("Previously I havent done any projects to begain with So, her are some other topics because WHY THE HELL NOT ")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_contact_form)

    with text_column:
        st.subheader("Tower Of God Season 2| ANNOUNCEMENT TRAILER")
        st.write("""Tower of God, the acclaimed anime series, has been greenlit for its highly anticipated second season, set to release in July 2024.
 The teaser for season 2 suggests that it will adapt the Return Of The Prince and Workshop Battle arcs, potentially spanning 24 episodes split into 2 cours.
 Tower of God's success paves the way for more Korean manhwa adaptations in the anime industry, increasing exposure and excitement among fans. """)

        st.markdown("[Watch Video...](https://youtu.be/QZNIqX7aMUg)")

with st.container():
     image_column, text_column = st.columns((1,2))

with image_column:
        st.image(img_lottie_animation)
      
with text_column:
        st.subheader("Teyvat Chapter Storyline Preview: Travail | Genshin Impact (Contains spoilers)")
        st.write("""Teyvat Chapter Storyline Preview: Travail was a video released by official Genshin Impact media on September 27, 2020. It teased the storyline of the Archon Quests, as well as characters that are expected to appear in each nation. """)

        st.markdown("[Watch Video...](https://youtu.be/TAlKhARUcoY)")


#contact#

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/alokdelhiind@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form> """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
                   
