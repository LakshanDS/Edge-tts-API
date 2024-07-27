import asyncio
import edge_tts
import zipfile
import os

async def generator(text: str, voice: str, rate: str, in_cue: int):

    audio_file_path = "Output/audio.mp3"
    srt_file_path = "Output/audio.srt"
    zip_file_path = "Output/Results.zip"

    communicate = edge_tts.Communicate(text, voice, rate="+7%")
    submaker = edge_tts.SubMaker()
    
    with open(audio_file_path, "wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])
    
    vtt_file = [submaker.generate_subs(in_cue)]
    with open(srt_file_path,"w") as srt_file:
    
        for i in vtt_file:
            replaced = i.replace(".",",")
            lines = replaced.splitlines()

            if len(lines) >= 2:
                text = '\n'.join(lines[1:]).strip()
                srt_file.write(f"{text}\n\n")

    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        zipf.write(audio_file_path, os.path.basename(audio_file_path))
        zipf.write(srt_file_path, os.path.basename(srt_file_path))

    return zip_file_path

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_text_file>")
        sys.exit(1)
    
    input_text_file = sys.argv[1]

    with open(input_text_file, "r", encoding="utf-8") as file:
        text_content = file.read()
    
    asyncio.run(generator(text_content, "en-US-BrianMultilingualNeural", "+7%", 1))