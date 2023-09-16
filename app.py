import streamlit as st
from streamlit_option_menu import option_menu 
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout='wide')
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
def local_css(file_name):
      with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

lottie_profile = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_h5wdcgrm.json")
lottie_contact = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_px0ntw70.json")    
lottie_coder = "https://lottie.host/c475733d-c417-4fd6-b65a-e0f224cffa2c/M6YMdoaCc3.json"

image = Image.open(r"Untitled.png")
image2 = Image.open(r"aidict.png")
image3 = Image.open(r"banknote auth.jpg")




st.write('##')
st.subheader("Hey guys :wave:")

st.title('My Portfolio Website')
st.write("""
Hello! I'm Manas Rai, a third-year B.Tech student at KIET Group of Institutions. 
I'm an enthusiastic learner with a focus on machine learning and backend development.
 I have practical experience with frameworks like Django, Flask, and FastAPI, as well as Linux and MySQL database management. I'm eager to take on challenging projects and make a meaningful impact in the tech world.
 """)

st.write('---')

with st.container():
    selected = option_menu(
        menu_title=None,
        options =['About','Projects','Contact'],
        icons = ['person','code-slash','chat-left-text-fill'],
        orientation = 'horizontal'
    )

if selected == 'About':

    with st.container():
        col1,col2 =st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Manas Rai")
            st.title("Undergrad at KIET")
        with col2:
            st_lottie(lottie_coder)
        st.write('---')
        with st.container():
            col3,col4 = st.columns(2)
            with col3:
                st.subheader("""
                EDUCATION
                - kiet
                   - Bachelor of Technology - Computer Science
                   - Grade: 8.3
                - St. Mary's Convent School
                   - XIIth (PCM)
                   - Grade: 91.2%
                - St. Mary's Convent School
                   - Xth
                   - Grade: 93.8%
                """
                )
            with col4:
                st.subheader(""" 
                Certifications
                - Deep Learning Specialisation
                    - Course1 -> Neural Networks and Deep Learning
                - Full stack Web-Development with FLASK - LinkedIN Learning
                - Building Restful APIs with FLASK

                """)
if selected == "Projects":
    with st.container():
            st.header("MY PROJECTS")
            st.write("##")
            col_l, col_r = st.columns((1,2))
            with col_l:
                  st.image(image)
            with col_r:
                  st.subheader("LUNA APP FOR WOMEN  ")
                  st.write("""

                  A period awareness app which not only helps women to effectively manage their menstrual cycle
                  but also predicts the potential risk of pcod(Poly-cystic ovary syndrome) and provides them with
                  optimal solutions.
                  """)
                  st.markdown("[Visit Github Repo >](https://github.com/manasrai1406/luna")
            col_l1, col_r1 = st.columns((1,2))
            with col_l1:
                  st.image(image2)
            with col_r1:
                  st.subheader("AI Dictionary")
                  st.write("""

                  Sometimes while reading a complex research paper or a technicsl newsletter you might wonder 
                  what they actually mean so just paste the text or paragraph into this application and generate meaning
                  of all technical terms related to Artificial Intelligence and Machine Learning.
                  """)
                  st.markdown("[Visit Github Repo >](https://github.com/manasrai1406/project")

            col_l2, col_r2 = st.columns((1,2))
            with col_l2:
                  st.image(image3)
            with col_r2:
                  st.subheader("Banknote Authentication System")
                  st.write("""

                  A banknote authentication system to check for a fake note well-trained on machine learning model
                  used latest FAST-API framework to build the project thus improving the performance manyfold  of the machine learning
                  api as compared to conventional flask framework which was way too slow.
                  """)
                  st.markdown("[Visit Github Repo >](https://github.com/manasrai1406/banknote-authentication")

if selected == "Contact":
      st.header("Get In Touch With Me!")
      st.write("##")
      st.write("##")

      contact_form = """
      <form action="https://formsubmit.co/mrai73759@gmail.com" method="POST">
      <input type = "hidden" name ="_captcha" value = "false">
      <input type="text" name="name" placeholder = "Your name" required>
      <input type="email" name="email" placeholder = "Your email" required>
      <textarea name = "message" placeholder = "Your message" required></textarea>
      <button type="submit">Send</button>
      </form>
    """
      left_col, right_col = st.columns((2,1))
      with left_col:
            st.markdown(contact_form, unsafe_allow_html= True)
      with right_col:
            st_lottie(lottie_contact,height=245,width=450)

        
              

