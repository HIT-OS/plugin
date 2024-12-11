from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema import Data
from pathlib import Path
from platformdirs import user_cache_dir
import os
import speech_recognition as sr

class SpeechToTextComponent(Component):
    display_name = "Speech to Text"
    description = "Converts speech input from the microphone to text."
    documentation: str = "http://docs.langflow.org/components/custom"
    icon = "microphone"

    inputs = [
        MessageTextInput(name="save_path", display_name="Save Path", value=str(Path(user_cache_dir("langflow")) / "speech_output.txt")),
    ]

    outputs = [
        Output(display_name="Output", name="output", method="build_output"),
    ]

    def build_output(self) -> Data:
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        try:
            with microphone as source:
                print("Listening...")
                audio = recognizer.listen(source)
                print("Recognizing...")
                text_input = recognizer.recognize_google(audio)
                print(f"Recognized Text: {text_input}")

            save_path = self.input_value
            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            # Open the file in write mode and save the text
            with open(save_path, 'w') as file:
                file.write(text_input)
        except Exception as e:
            raise e

        data = Data(value=text_input)
        self.status = data
        return data