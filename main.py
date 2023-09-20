import os
from tempfile import NamedTemporaryFile

import assemblyai as aai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
transcriber = aai.Transcriber()

audio = st.file_uploader("Upload an audio file", type=["mp3"])


def get_transcript():
    with NamedTemporaryFile(suffix="mp3") as temp:
        temp.write(audio.getvalue())
        temp.seek(0)
        transcript = transcriber.transcribe(temp.name)
        return transcript


def process_download(dataframe):
    doctype = st.radio("Choose file format", ["CSV (.csv)", "JSON (.json)"])
    if doctype == "CSV (.csv)":
        file = dataframe.to_csv(index=False)
        st.download_button("Download", data=file, file_name="streamlit_download.csv")
    elif doctype == "JSON (.json)":
        file = dataframe.to_json(orient="records")
        st.download_button("Download", data=file, file_name="streamlit_download.json")




