# Edge-tts-API

## Overview

This script `Edge_tts.py` is a command-line tool that leverages the `edge-tts` library to convert text to speech and generate synchronized subtitle files (SRT). It's designed to be simple to use, taking a text file as input and producing an MP3 audio file and an SRT subtitle file, packaged together in a ZIP archive.

## Features

- **Text-to-Speech Conversion:** Converts text from an input file into speech using Microsoft Edge's text-to-speech service via the `edge-tts` library.
- **Subtitle Generation:** Automatically generates SRT subtitle files that are synchronized with the spoken words, making the audio content accessible and easier to follow.
- **Voice Customization:**  Allows customization of the voice used for text-to-speech. The default voice is set to `en-US-BrianMultilingualNeural`, but you can easily change it to any voice listed in `Voice-list.txt`.
- **Adjustable Speech Rate:**  Provides control over the speech rate, currently set to `"+7%"` for a slightly faster pace, which can be adjusted as needed.
- **Output Packaging:** Bundles the generated audio and subtitle files into a single ZIP archive for easy distribution and management.

## Prerequisites

Before using `Edge_tts.py`, ensure you have the following installed:

- **Python:** Python 3.7 or higher is required.

## Installation

1. **Install `edge-tts`:**
   Open your terminal and execute the following command to install the `edge-tts` library:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line, providing the path to your input text file as a command-line argument:

```bash
python Edge_tts.py <input_text_file>
```

- `<input_text_file>`:  Replace this with the path to the text file that contains the text you wish to convert to speech.

### Configuration

The script's behavior can be configured by modifying the following parameters directly within the `Edge_tts.py` file:

- **Voice Selection:**
  - To change the voice, locate the `asyncio.run(generator(...))` line within the `if __name__ == "__main__":` block.
  - Replace `"en-US-BrianMultilingualNeural"` with the name of your desired voice.
  - Refer to the `Voice-list.txt` file in the project directory for a list of available voices and their names.

- **Speech Rate:**
  - The speech rate is set using the `rate` parameter in the `generator` function. It's currently set to `"+7%"`.
  - Adjust this value to speed up or slow down the speech. For example, use `"+0%"` for normal speed, or higher positive percentages for faster speech, and negative percentages for slower speech.

- **Subtitle Timing (In Cue):**
  - The `in_cue` parameter in the `generator` function (currently set to `1`) affects subtitle generation timing. You can experiment with different integer values to adjust how subtitles are displayed.

### Voice List

A comprehensive list of supported voices is available in the `Voice-list.txt` file. This file is included in the repository and provides an extensive selection of voices in various languages and dialects, allowing you to choose the most appropriate voice for your text-to-speech needs.

### Output Files

Upon successful execution, the script will create an `Output/` directory (if it doesn't already exist) in the same directory where `Edge_tts.py` is located. Inside this directory, you will find the following output files:

- `audio.mp3`: The generated audio file in MP3 format.
- `audio.srt`: The subtitle file in SRT format, synchronized with the audio.
- `Results.zip`: A ZIP archive containing both `audio.mp3` and `audio.srt` for easy sharing and storage.

## Example Usage

Let's say you have a text file named `my_text.txt` in the same directory as `Edge_tts.py`, and it contains the text you want to convert to speech.

1. **Prepare your text:**
   Create a text file named `my_text.txt` and put your desired text content in it.

2. **Run the script:**
   Open your terminal, navigate to the directory containing `Edge_tts.py`, and run:
   ```bash
   python Edge_tts.py my_text.txt
   ```

3. **Locate the output:**
   After the script finishes running, navigate to the `Output/` directory. You will find `audio.mp3`, `audio.srt`, and `Results.zip` containing your converted speech and subtitles.

## Customization Examples

**Changing the Voice:**

To use the "en-GB-RyanNeural" voice, modify line 50 in `Edge_tts.py` from:

```python
asyncio.run(generator(text_content, "en-US-BrianMultilingualNeural", "+7%", 1))
```

to:

```python
asyncio.run(generator(text_content, "en-GB-RyanNeural", "+7%", 1))
```

**Adjusting Speech Rate:**

To set the speech rate to normal speed (0%), modify line 50 in `Edge_tts.py` from:

```python
asyncio.run(generator(text_content, "en-US-BrianMultilingualNeural", "+7%", 1))
```

to:

```python
asyncio.run(generator(text_content, "en-US-BrianMultilingualNeural", "+0%", 1))
```

## Troubleshooting

- **Voice not found:** Double-check the voice name against the `Voice-list.txt` file. Voice names are case-sensitive and must be entered exactly as listed.
- **Output directory issues:** Ensure that the script has write permissions in the directory where it is being run, or that it can create the `Output/` directory.

For further assistance or to report issues, please refer to the `edge-tts` library documentation or the repository.
