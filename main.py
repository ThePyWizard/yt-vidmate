import streamlit as st
import yt_dlp
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

    # Button to trigger video details fetching
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

                # Available formats
                formats = info_dict['formats']
                format_options = [
                    (f"{fmt['format_note']} - {fmt['ext']}", fmt['format_id'])
                    for fmt in formats if fmt.get('format_note')
                ]

                selected_format = st.selectbox("Select Format:", [opt[0] for opt in format_options])
                format_id = dict(format_options)[selected_format]

                if st.button("Download Video 🎬"):
                    with st.spinner("Downloading your video, please wait..."):
                        download_dir = os.path.join(os.getcwd(), "downloads")
                        os.makedirs(download_dir, exist_ok=True)  # Ensure the directory exists
                        
                        ydl_opts = {
                            'format': format_id,
                            'outtmpl': os.path.join(download_dir, f"{info_dict['title']}.%(ext)s"),
                        }
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([video_url])

                        # Provide a download link
                        downloaded_file_path = os.path.join(download_dir, f"{info_dict['title']}.{info_dict['formats'][0]['ext']}")
                        
                        if os.path.exists(downloaded_file_path):
                            st.success("Download complete! ✅")
                            st.markdown(f"Click [here](/{downloaded_file_path}) to download the video.")
                        else:
                            st.error("There was an error while saving the video.")

            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
