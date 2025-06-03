import pyperclip
from googletrans import Translator
import os
import asyncio

translator = Translator()
last_text = ""

async def main():
    global last_text
    while True:
        try:
            text = pyperclip.paste().strip()
            if text != last_text and text != "":
                print("you copy:", text)
                last_text = text

                # המתן לתרגום
                translation_obj = await translator.translate(text, dest='he')
                translation = translation_obj.text

                print("translation:", translation)
                pyperclip.copy(translation)

                # שליחת התראה והשמעה
                os.system(f'''terminal-notifier -title "📘 Translation" -message "{translation}" -subtitle "of: {text}" -timeout 2''')
                os.system(f'say -v Samantha "{text}"')
                os.system(f'say -v Carmit "{translation}"')

            await asyncio.sleep(1.0)

        except Exception as e:
            print("error:", e)
            await asyncio.sleep(1.5)

asyncio.run(main())
