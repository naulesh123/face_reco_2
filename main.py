import streamlit as st
import time
from deepface import DeepFace
import cv2
import threading
from streamlit_webrtc import webrtc


############## reference images #################
reference1=cv2.imread("reference.jpeg")
reference2=cv2.imread("reference_3.jpeg")
event=threading.Event()



############# functions  ########################

face_match=False

def match(image_to_check):
    try:
        result1=DeepFace.verify(reference1,image_to_check)
        if result1["verified"]:
            global face_match
            face_match=True

    except ValueError as e:
        pass


def match2(image_to_check):
    try:
        result2=DeepFace.verify(reference2,image_to_check)
        if result2["verified"]:
            global face_match
            face_match=True

    except ValueError as e:
        pass











#################################################





st.set_page_config(layout="wide")
st.header("My all projects combined in this single project")


################################################################################
################################################################################
col21,col22=st.columns(2,gap="small")


with col21:
    ################################################################################
    ################################################################################

    cap = cv2.VideoCapture(0)

    if st.button("Use Face recognition", use_container_width=True):

        counter = 0

        while True:
            ret, frame = cap.read()
            # cv2.imshow("Frame", frame)

            if ret:
                if counter % 30 == 0:
                    t1 = threading.Thread(target=match, args=[frame.copy()])
                    t2 = threading.Thread(target=match2, args=[frame.copy()])

                    t1.start()
                    t2.start()
                    t1.join()
                    t2.join()

                    if face_match:
                        st.header("**Welcome NIKHIL KUMAR !!!**")
                        break
                    else:
                        st.write("not matching")

                counter += 1

            pass

        pass

    cap.release()
    cv2.destroyAllWindows()

# password_button=st.empty()
# # password_button=st.button("Use Password instead")
# # password="1221"
# # if password_button:
# if password_button.button("Use Password instead",use_container_width=True):
#     password_button.empty()
#
#
#     user_input = st.text_input("Enter the password",type="password")
#
#     print(user_input)
#     # Display the input
#     if user_input:
#
#
#         st.write("You entered:", user_input)

with col22:
    with st.form("my_form"):
        st.write("")
        slider_val = st.slider("Use the number in the CV to slide in this sliding bar")
        # checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            pass
            # st.write("slider", slider_val)

###########################################################
###########################################################

placeholder=st.empty()









############################################################
############################################################
if slider_val==99 or face_match==True:


    st.write(" ")
    st.write(" " )

    col1, col2 = st.columns(2, gap='small')
    with col1:
        pass

        col11,col12=st.columns(2,gap="small")
        with col11:
            st.write("**NAME : NIKHIL KUMAR**")
            st.write("**BRANCH : CHEMICAL ENGINEERING**")
            st.write("**ROLL NUMBER : 120CH0099**")
            st.write("**PROGRAMME : B.TECH.**")
            st.write("**COLLEGE NAME : NIT ROURKELA**")
        with col12:
            st.image("reference_3.jpeg",width=200)





    with col2:
        # st.write("hello")
        pass

    st.write(" ")
    st.write(" ")
    col41,col42,col43,col44=st.columns(4,gap="small")
    with col41:
        # st.write("gg")
        st.write("***Movie Recommendation system***")
        # st.image()

        st.write("A full stack website developed using streamlit framework python’s natural language toolkit module , which recommends movie based on the keywords provided by user and similar type of movies, developed using")
        st.write("")
        st.write("**python, Natural language toolkit, Streamlit, Pandas, Numpy**")
        st.write("")

        gg11,gg12=st.columns(2,gap="small")

        with gg11:
            st.link_button("Project Link", "https://movierecommendation-ejiehzusjsntbjau5wt3wc.streamlit.app/")
        with gg12:
            st.link_button("Github repo Link","https://github.com/naulesh123/movie_recommendation")


        pass
    with col42:
        # st.write("gg")
        st.write("***Continent analysis***")

        st.write("Build a website for analysis of continents on the basis of GDP per capita , GDP growth rate , population etc")
        st.image("continent_analysis.png")
        st.write("**python, pandas, Streamlit,plotly_chart**")
        gg21,gg22=st.columns(2,gap="small")
        with gg21:
            st.link_button("Project Link","https://countriesdashboardusingapp-9y5uqe8ejvgllqcuur7jvw.streamlit.app/")
        with gg22:
            st.link_button("Github repo Link","https://github.com/naulesh123/countries_dashboard_using_streamlit")





        pass
    with col43:
        # st.write("gg")
        st.write("***House price prediction using Flask & Decision Tree***")
        st.write("Developed a fullstack website for house price prediction using **python's scikit learn** flask framework , bootstrap , used axios for data transfer between frontend and backend")
        st.image("hp_pred.png")
        st.write("**Python, Flask, Scikit‐learn’s Decision Tree, Numpy, Pandas, axios, HTML, CSS,Javascript**")
        gg31,gg32=st.columns(2,gap="small")
        with gg31:
            st.link_button("Github repo Link","https://github.com/naulesh123/house_price_predict2")


        pass
    with col44:
        # st.write("gg")
        st.write("***Marketing intern in IOCL Divisional office Barauni***")
        st.write("Worked as a marketing analyst intern at Indian Oil corporation(IOCL), managed IOCL Barauni divisional audits under Assistant Manager of Begusarai division")
        st.image("iocl_barauni_do.png",width=150)

        gg41,gg42=st.columns(2,gap="small")

        with gg41:
            st.link_button("certificate from DO","https://drive.google.com/file/d/1RLFjRxTGc8LJZjVaYBtbVog3LZgtXKrn/view?usp=drive_link")
        with gg42:
            st.link_button("Official Certificate from IOCL","https://drive.google.com/file/d/1k3vm76_RMflHwXTlYKWk3ieeOz-YM9pq/view?usp=drive_link")














        pass



    pass

# st.write("Outside the form")

# css_style = """
# <style>
# .custom-button {
#     background-color: rgb(204, 49, 49);
# }
# </style>
# """
#
# st.markdown(css_style, unsafe_allow_html=True)
#
# # Create a specific button with the custom CSS class
# st.markdown('<button class="custom-button">Custom Button</button>', unsafe_allow_html=True)




