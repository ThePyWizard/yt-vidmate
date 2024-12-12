import streamlit as st
import yt_dlp
import os

def main():
    # Set up the app title and layout
    st.set_page_config(page_title="StreamEase - YouTube Downloader", page_icon="🎥", layout="centered")
    st.title("🎥 StreamEase - Download Videos Effortlessly")

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
    video_url = st.text_input(
        "Paste YouTube Video URL here:", placeholder="https://www.youtube.com/watch?v=example"
    )

    if video_url:
        try:
            # Fetch video information
            with yt_dlp.YoutubeDL() as ydl:
                info_dict = ydl.extract_info(video_url, download=False)

            # Display video details
            st.write("### Video Details")
            st.markdown(
                f"""<style>.details {{ font-size: 16px; }}</style>
                <div class="details">
                **Title:** {info_dict['title']}<br>
                **Views:** {info_dict['view_count']}<br>
                **Length:** {info_dict['duration']} seconds<br>
                **Description:** {info_dict['description'][:200]}...
                </div>""",
                unsafe_allow_html=True,
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
                    ydl_opts = {
                        'format': format_id,
                        'outtmpl': os.path.join(os.getcwd(), f"{info_dict['title']}.%(ext)s"),
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video_url])
                    st.success("Download complete! ✅")
                    st.markdown(f"File saved as: **{info_dict['title']}** in the current directory.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
