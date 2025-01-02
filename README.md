# Speech-to-Text Application

## Overview
The Speech-to-Text application is designed to convert audio files into text using pre-recorded samples. It includes functionalities for processing long and short audio files and provides a simple interface for transcription.

## Features
- **Speech-to-Text Conversion**: Converts speech from audio files (e.g., `.mp3`, `.wav`) into text.
- **Support for Long Audio**: Processes and transcribes longer audio files effectively.
- **Sample Data**: Includes sample audio files for testing and demonstration.

## Directory Structure
```
speech_to_text-main/
├── app_audio.py             # Handles audio processing logic
├── import.py                # Manages imports and preprocessing
├── long_audi 2.py           # Processes long audio files
├── main.py                  # Main entry point of the application
├── sample_audio/            # Contains sample audio files
│   ├── long_audio.mp3       # Sample long audio file
│   └── speech.wav           # Sample short audio file
```

## Prerequisites
- Python 3.8+
- Required Libraries:
  - SpeechRecognition
  - pydub
  - wave

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/speech_to_text.git
   cd speech_to_text-main
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Running the Application
To process and transcribe audio files:
```bash
python main.py
```

### 2. Handling Long Audio
For longer audio files, run the dedicated script:
```bash
python "long_audi 2.py"
```

### 3. Testing with Sample Audio
Use the provided sample audio files in the `sample_audio/` directory to test the transcription functionality.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes and push:
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact [ishaanvashista@gmail.com].

