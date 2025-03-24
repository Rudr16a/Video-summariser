import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai

import time
from pathlib import Path
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure API
if API_KEY:
    genai.configure(api_key=API_KEY)

# Page Configuration
st.set_page_config(
    page_title="Multimodal AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("Phidata Multimodal AI Agent")
st.header("Powered by Gemini 2.0 🚀")

# Cache the agent initialization
@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

# Initialize the multimodal agent
multimodal_agent = initialize_agent()

# File Uploader
video_file = st.file_uploader(
    "Upload a video file", type=['mp4', 'mov', 'avi'], help="Upload a video for AI Analysis"
)

if video_file:
    # Create a temporary file for the uploaded video
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name  # Save temp file path

    # Display the uploaded video
    st.video(video_path, format="video/mp4", start_time=0)

    # User query input
    user_query = st.text_area(
        "What insights are you seeking from the video?",
        placeholder="Ask anything about the video content. The AI will analyze and summarize.",
        help="Provide specific questions or insights you want from the video"
    )

    # Analyze Video Button
    if st.button("🔍 Analyze Video", key="analyze_video_button"):
        if not user_query:
            st.warning("Please enter a question or insight to analyze the video.")
        else:
            try:
                with st.spinner("Processing video and gathering transcripts..."):
                    # Simulating video processing
                    time.sleep(1)

                    # Upload and process video file
                    processed_video = upload_file(video_path)

                # Prompt for AI analysis
                analysis_prompt = f"""
                Analyze the uploaded video for content and context.
                {user_query}

                Provide a detailed, user-friendly, and actionable response.
                """

                # AI Agent Execution
                response = multimodal_agent.run(analysis_prompt, videos=[processed_video])

                # Display the result
                st.subheader("Analysis Result")
                st.markdown(response.content)

            except Exception as error:
                st.error(f"An error occurred during analysis: {error}")
            finally:
                # Clean up temporary video file
                Path(video_path).unlink(missing_ok=True)

else:
    st.info("Upload a video file to begin analysis.")

# Customized Styling
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 100px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
