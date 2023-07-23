## python3 transcriptions.py  で実行できます
## jsshort.m4a にサウンドが入っています

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
## File uploads are currently limited to 25 MB

import openai
audio_file= open("jsshort.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript["text"])
audio_file= open("jsshort.m4a", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript["text"])


