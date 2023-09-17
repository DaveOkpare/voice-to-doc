import os
from tempfile import NamedTemporaryFile

import assemblyai as aai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

transcriber = aai.Transcriber()

audio = st.file_uploader("Upload an audio file", type=["mp3"])

if audio is not None:
    with NamedTemporaryFile(suffix="mp3") as temp:
        temp.write(audio.getvalue())
        temp.seek(0)
        transcript = transcriber.transcribe(temp.name)
        st.write(transcript.text)



