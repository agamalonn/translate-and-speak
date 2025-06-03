import pyperclip
from googletrans import Translator
import asyncio
import platform
from plyer import notification
import pyttsx3

translator = Translator()
last_text = ""

# Set up TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(text, lang='en'):
    # Try to select the voice based on language
    for voice in voices:
        if lang in voice.languages[0].decode().lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

async def main():
    global last_text
    while True:
        try:
            text = pyperclip.paste().strip()
            if text != last_text and text != "":
                print("you copy:", text)
                last_text = text

                # Translate
                translation_obj = translator.translate(text, dest='he')
                translation = translation_obj.text

                print("translation:", translation)
                pyperclip.copy(translation)

                # Notification (cross-platform)
                notification.notify(
                    title="📘 Translation",
                    message=f"{translation}\nof: {text}",
                    timeout=2
                )
                # Speech (cross-platform)
                speak(text, lang='en')
                speak(translation, lang='he')

            await asyncio.sleep(1.0)

        except Exception as e:
            print("error:", e)
            await asyncio.sleep(1.5)

asyncio.run(main())
