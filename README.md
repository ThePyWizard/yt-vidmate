# VidMate - YouTube Video Downloader

VidMate is a simple and efficient web application built with Streamlit that allows users to fetch details of YouTube videos and download them in their preferred resolution and format. It is designed for ease of use and seamless interaction.

## Features

- Fetch YouTube video details including:
  - Title
  - Views
  - Duration
- Download videos in various resolutions and formats.
- User-friendly interface for effortless navigation.

## Tech Stack

- **Streamlit**: For the web app interface.
- **yt-dlp**: To extract video information and handle downloading.
- **Python**: The backbone of the application.

## Installation

Follow these steps to run VidMate on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/vidmate.git
   cd vidmate
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

## How to Use

1. Paste the YouTube video URL into the input field.
2. Click "Fetch Video Details" to retrieve information about the video.
3. Select your preferred resolution and format from the dropdown menu.
4. Click "Download Video" to start the download.

## Project Structure

```
vidmate/
├── app.py             # Main Streamlit app file
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Dependencies

The project requires the following dependencies:

- **Streamlit**
- **yt-dlp**

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## Screenshots

Coming soon...

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

## Contact

For any questions or feedback, feel free to reach out:
- LinkedIn: [Jishnu M M](https://linkedin.com/in/thepywizard)
- Email: jishnumm4312@gmail.com
