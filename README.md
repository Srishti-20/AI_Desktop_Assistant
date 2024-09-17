# AI-Powered Desktop Assistant

## Project Overview

This project involves developing an AI-powered desktop assistant using Python. The assistant is capable of recognizing voice commands to perform various tasks such as accessing Wikipedia, opening websites and on-device applications, providing the current time, and playing music via Spotify through Spotify API integration. This application enhances daily productivity by automating tasks using AI.

## Features

- **Voice Command Recognition**: Utilizes speech recognition to interpret user commands.
- **Web Interaction**: Opens specified websites and performs actions based on voice commands.
- **Application Control**: Launches and controls various applications installed on the desktop.
- **Time Inquiry**: Provides the current time when requested.
- **Music Playback**: Integrates with the Spotify API to play specific tracks.

## Installation

### Prerequisites

- Python 3.12 or higher
- Virtual environment (recommended)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Srishti-20/Desktop_Assistant.git
   cd your-repository

2. **Create and Activate Virtual Environment**
```bash
python3 -m venv assistant
source assistant/bin/activate
```

3. **Install Required Packages**
```
pip install -r requirements.txt
```
4. **Spotify API Setup**
- Create a Spotify developer account and register your application.
- Obtain the client_id, client_secret, and set up a redirect URI (e.g., http://localhost:8888/callback).
- Save these credentials in a file or environment variables.

5. **Configuration**
- Place your Spotify API credentials in config.json or set them as environment variables.

## Usage

1. **Start the Application**
```
python main.py
```
2. **Voice Commands**

- "Open [website]": Opens the specified website.
- "Play [artist]": Plays the specified artist's song on Spotify.
- "The time": Provides the current time.
- "Stop": Stops the current song playback.
- "Pause": Pauses the song.
- "Resume": Resumes the song from where it was paused.

## Testing
- Test voice command recognition by speaking commands clearly.
- Verify integration with Spotify by checking if songs play correctly.
- Ensure Flask server is running if using Spotify authentication.

## Known Issues
- Port 8888 might be in use; change to another port if needed.
- Ensure all dependencies are properly installed.

## Future Enhancements
- Add GUI for better user interaction.
- Integrate more advanced AI features for improved productivity.

## Acknowledgments
- Spotify API
- SpeechRecognition
- Flask


