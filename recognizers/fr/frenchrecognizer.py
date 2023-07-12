import speech_recognition as sr
import moviepy.editor as mp
import assemblyai as aai
import json

class FrenchRecognizer:
    def recognize(self, path):
        r = sr.Recognizer()
        audio_file = mp.AudioFileClip(path)
        audio_file.write_audiofile("out/voice.wav");
        with sr.AudioFile("../../out/voice.wav") as source:
            audio = r.record(source)
        result = r.recognize_vosk(audio, language="fr")
        return json.loads(result)['text']

    def recognize_assembly(self, path):
        audio_file = mp.AudioFileClip(path)
        audio_file.write_audiofile("out/voice.wav");
        aai.settings.api_key = "c623f21a00114c67a8e737f051c459ad"
        transcriber = aai.Transcriber()
        response = transcriber.transcribe("out/voice.wav")
        return response.text