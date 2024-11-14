import streamlit as st
from video_to_text import video_to_text
import streamlit.components.v1 as components
import time 

st.set_page_config(layout="wide")
G_ID = st.secrets["Google_Analytics_Measuremen_ID"]

custom_head = """
<!DOCTYPE html>
<html>
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-WPTDRJYTTT"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
""" + f""" gtag('config', {G_ID});
    </script>
</head>
<body>
    <h1>Welcome to My Streamlit App</h1>
    <button onclick="showAlert()">Click Me</button>
</body>
</html>
"""

# Use Streamlit's HTML component to render the content
components.html(custom_head, height=300)

st.image(r"images/logo_path.png", width=150)
st.title("Welcome to PyTextify")

st.subheader("Upload Files for Transcription")
uploaded_file = st.file_uploader(label = " ", type=["mp4"])
if uploaded_file is not None:
    file_name = uploaded_file.name
    with open("uploaded_file/uploaded_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.video("uploaded_file/uploaded_video.mp4")  

    info_msg = st.info("Processing your video ...")
    transcription = video_to_text("uploaded_file/uploaded_video.mp4")
    info_msg.empty()
    msg = st.success("Transcription is now available")
    def stream_data():
        for word in transcription.split(" "):
            yield word + " "
            time.sleep(0.02)   

    with st.container(border=True):
        st.write_stream(stream_data)
# Footer or additional info
st.write("---")
st.write("PyTextify © 2024. Transcribe your videos.")

#################################################################################