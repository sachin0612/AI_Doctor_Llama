from gtts import gTTS
from pydub import AudioSegment
import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    mp3_temp_path = "temp_gtts_output.mp3"
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(mp3_temp_path)
    sound = AudioSegment.from_mp3(mp3_temp_path)
    sound.export(output_filepath, format="wav")
    os_name = platform.system()
    try:
        if os_name == "Darwin":  #macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  
            subprocess.run(['aplay', output_filepath])  
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

