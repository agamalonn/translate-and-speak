import pyperclip
from googletrans import Translator
import os
import time
import subprocess

translator = Translator()
last_text = ""

def main():
    global last_text
    while True:
        try:
            text = pyperclip.paste().strip().lower()
            if text != last_text and text != "" and len(text)<100:
                print("you copy:", text)
                last_text = text

                translation_obj = translator.translate(text, dest='he')
                translation = translation_obj.text

                print("translation:", translation)
                pyperclip.copy(translation)

                # Show notification with a Skip button
                notifier_cmd = [
                    'terminal-notifier',
                    '-title', '📘 Translation',
                    '-message', translation,
                    '-subtitle', f'of: {text}',
                    '-timeout', '5',
                    '-actions', 'Skip'
                ]
            
                os.system(f'''terminal-notifier -title "📘 Translation" -message "{translation}" -subtitle "of: {text}" -timeout 2''')
                os.system(f'say -v Samantha "{text}"')
                #os.system(f'say -v Carmit "{translation}"')

            time.sleep(1.0)

        except Exception as e:
            print("error:", e)
            time.sleep(1.5)

if __name__ == "__main__":
    main()
