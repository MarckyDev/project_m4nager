from GenerativeAI import Borus as b
from whisper_mic import WhisperMic as w



borus = b.Borus()

whisper = w(model="tiny.en")
if __name__ == "__main__":
    print("Listening...")
    speech = whisper.listen()
    print(speech)
