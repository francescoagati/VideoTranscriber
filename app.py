import streamlit as st
from utils.audio_processing import extract_audio
from utils.transcription import transcribe_audio
from utils.summarization import summarize_text
from utils.validation import validate_environment
from pathlib import Path

def main():
    st.title("🎥 OBS Recording Transcriber")
    st.caption("Process your OBS recordings with AI transcription and summarization")

    # Allow the user to select a base folder
    st.sidebar.header("Folder Selection")
    base_folder = st.sidebar.text_input(
        "Enter the base folder path:",
        value=str(Path.home())
    )

    base_path = Path(base_folder)

    # Validate environment
    env_errors = validate_environment(base_path)
    if env_errors:
        st.error("## Environment Issues")
        for error in env_errors:
            st.markdown(f"- {error}")
        return

    # File selection
    recordings = list(base_path.glob("*.mp4"))
    if not recordings:
        st.warning(f"📂 No recordings found in the folder: {base_folder}!")
        return

    selected_file = st.selectbox("Choose a recording", recordings)

    if st.button("🚀 Start Processing"):
        try:
            transcript, summary = transcribe_audio(selected_file)
            if transcript:
                st.subheader("🖍 Summary")
                st.write(summary)
                st.subheader("📜 Full Transcript")
                with st.expander("View transcript content"):
                    st.text(transcript)
                st.download_button(
                    label="💾 Download Transcript",
                    data=transcript,
                    file_name=f"{Path(selected_file).stem}_transcript.txt",
                    mime="text/plain"
                )
            else:
                st.error("❌ Failed to process recording")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.write(e)  # This will show the traceback in the Streamlit app
if __name__ == "__main__":
    main()
