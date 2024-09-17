# AI-Powered Desktop Assistant

## Project Overview

This project involves developing an AI-powered desktop assistant using Python. The assistant is capable of recognizing voice commands to perform various tasks such as accessing Wikipedia, opening websites and on-device applications, providing the current time, and playing music via Spotify through Spotify API integration. Additionally, it includes face recognition for enhanced security and customization.

## Features

- **Voice Command Recognition**: Utilizes speech recognition to interpret user commands.
- **Web Interaction**: Opens specified websites and performs actions based on voice commands.
- **Application Control**: Launches and controls various applications installed on the desktop.
- **Time Inquiry**: Provides the current time when requested.
- **Music Playback**: Integrates with the Spotify API to play specific tracks.
- **Face Recognition**: Uses OpenCV to detect and recognize faces for security purposes and personalized interactions.
- **Wikipedia Access**: Retrieves information from Wikipedia based on voice queries for quick reference.
- **Customizable Wake Word**: Implements wake word detection to activate the assistant using a custom trigger word.

## Installation

### Prerequisites

- Python 3.12 or higher
- Virtual environment (recommended)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Srishti-20/Desktop_Assistant.git
   cd Desktop_Assistant

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

6. **Face Recognition Setup**
- Install OpenCV: ```pip install opencv-python```
- Ensure your webcam drivers are up-to-date.

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
- "Search Wikipedia for [query]": Retrieves information from Wikipedia based on the query.
- "Detect face": Activates the face recognition feature to identify users or for security checks.

## Testing
- Test voice command recognition by speaking commands clearly.
- Verify integration with Spotify by checking if songs play correctly.
- Ensure Flask server is running if using Spotify authentication.

## Known Issues
- Port 8888 might be in use; change to another port if needed.
- Ensure all dependencies are properly installed.
- Face recognition may require fine-tuning for accuracy based on lighting and camera quality.

## Future Enhancements
- **GUI Integration**: Add a graphical user interface for better user interaction and control.
- **Advanced AI Features**: Integrate more sophisticated AI models for improved accuracy and functionality, such as natural language understanding or personalized recommendations.
- **Cross-Platform Compatibility**: Adapt the application for different operating systems and platforms.
- **Extended Voice Commands**: Add more complex voice command capabilities and contextual understanding.

## Acknowledgments
- **Spotify API**: For music playback functionality.
- **SpeechRecognition**: For voice command recognition.
- **Flask**: For handling authentication and server-side logic.
- **OpenCV**: For face recognition functionality.
