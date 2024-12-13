import streamlit as st
import yt_dlp
import tempfile
import os

def main():
    st.set_page_config(page_title="VidMate - YouTube Downloader", page_icon="🎥", layout="centered")
    st.title("🎥 VidMate - Download Videos Effortlessly")

    # App description
    st.markdown(
        """
        <style>
        .description {
            font-size: 18px;
            color: #444;
            text-align: center;
        }
        </style>
        <p class="description">Enter a YouTube video URL below to fetch details and download it in your preferred format.</p>
        """,
        unsafe_allow_html=True,
    )

    # Input for YouTube URL
    video_url = st.text_input("Paste YouTube Video URL here:", placeholder="https://www.youtube.com/watch?v=example")

    # Initialize session state for formats and selected format
    if "video_formats" not in st.session_state:
        st.session_state.video_formats = []
    if "selected_format" not in st.session_state:
        st.session_state.selected_format = None

    # Button to fetch video details
    if st.button("Fetch Video Details"):
        if video_url:
            try:
                # Fetch video information
                with yt_dlp.YoutubeDL() as ydl:
                    info_dict = ydl.extract_info(video_url, download=False)

                # Display video details
                st.write("### Video Details")
                st.markdown(
                    f"""
                    **Title:** {info_dict['title']}  
                    **Views:** {info_dict['view_count']}  
                    **Length:** {info_dict['duration']} seconds  
                    **Description:** {info_dict['description'][:200]}...
                    """, 
                    unsafe_allow_html=True
                )

                # Save available formats in session state
                formats = info_dict['formats']
                st.session_state.video_formats = [
                    (f"{fmt['format_note']} - {fmt['ext']}", fmt['format_id'])
                    for fmt in formats if fmt.get('format_note') and fmt.get('ext')
                ]
                st.session_state.title = info_dict["title"]

            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Show format selection and download button if formats are available
    if st.session_state.video_formats:
        selected_option = st.selectbox(
            "Select Format:",
            [opt[0] for opt in st.session_state.video_formats],
            key="selected_option"
        )

        # Get the selected format ID
        format_id = dict(st.session_state.video_formats).get(selected_option)

        if st.button("Download Video 🎬"):
            if format_id:
                try:
                    with st.spinner("Downloading your video, please wait..."):
                        # Use a temporary directory for download
                        with tempfile.TemporaryDirectory() as temp_dir:
                            output_path = f"{temp_dir}/{st.session_state.title}.%(ext)s"

                            ydl_opts = {
                                'format': format_id,
                                'outtmpl': output_path,
                            }

                            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([video_url])

                            # Find the downloaded file in the temporary directory
                            downloaded_file_path = None
                            for file in os.listdir(temp_dir):
                                if file.startswith(st.session_state.title):
                                    downloaded_file_path = os.path.join(temp_dir, file)
                                    break

                            # Check if the file exists and provide a download button
                            if downloaded_file_path and os.path.exists(downloaded_file_path):
                                st.success("Download complete! ✅")
                                with open(downloaded_file_path, "rb") as file:
                                    st.download_button(
                                        label="Click here to download the video 🎥",
                                        data=file,
                                        file_name=os.path.basename(downloaded_file_path),
                                        mime="video/mp4",
                                    )
                            else:
                                st.error("There was an error while saving the video.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
