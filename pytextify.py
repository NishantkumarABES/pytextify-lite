import streamlit as st
from video_to_text import video_to_text
import streamlit.components.v1 as components
import time 

# Set page configuration
st.set_page_config(layout="wide")

# Inject Google Analytics JavaScript in the <head> section
components.html(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-YF606H6E0K"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-YF606H6E0K');
    </script>
    """,
    height=0,  # Set height to 0 to avoid visible space
)

# App content
st.image(r"images/logo_path.png", width=150)
st.title("Welcome to PyTextify")
st.subheader("Upload Files for Transcription")

# File uploader for video transcription
uploaded_file = st.file_uploader(label=" ", type=["mp4"])
if uploaded_file is not None:
    file_name = uploaded_file.name
    with open("uploaded_file/uploaded_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.video("uploaded_file/uploaded_video.mp4")

    info_msg = st.info("Processing your video ...")
    transcription = video_to_text("uploaded_file/uploaded_video.mp4")
    info_msg.empty()
    st.success("Transcription is now available")

    # Streaming transcription output
    def stream_data():
        for word in transcription.split(" "):
            yield word + " "
            time.sleep(0.02)

    with st.container():
        st.write_stream(stream_data)

# Footer or additional info
st.write("---")
st.write("PyTextify © 2024. Transcribe your videos.")
