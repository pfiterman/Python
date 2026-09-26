from util import get_required_env
from pathlib import Path
from datetime import datetime

from azure.identity import DefaultAzureCredential

# Try import azure.cognitiveservices.speech
try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)

# --------------------------------------------------------- 
# Azure Speech configuration 
# ---------------------------------------------------------
speech_key = get_required_env("SPEECH_KEY")
speech_region = get_required_env("SPEECH_REGION")
speech_endpoint = f"https://{speech_region}.api.cognitive.microsoft.com/"
speech_endpoint_with_custom_domain = get_required_env("FOUNDRY_ENDPOINT_CUSTOM_DOMAIN")

# --------------------------------------------------------- 
# Translation configuration 
# ---------------------------------------------------------
translation_config = speechsdk.translation.SpeechTranslationConfig( 
    subscription=speech_key, 
    endpoint=speech_endpoint, 
    speech_recognition_language="fa-IR", 
    target_languages=("en", "fr", "pt") 
) 

audio_config = speechsdk.audio.AudioConfig( 
    use_default_microphone=True 
)


# --------------------------------------------------------- 
# Translation output 
# ---------------------------------------------------------
root_dir = Path(__file__).resolve().parent 
translation_file = root_dir / "translations.txt"

def save_translation(
    persian: str,
    english: str,
    french: str,
    portuguese: str
):
    """Save a translation to translations.txt."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with translation_file.open("a", encoding="utf-8") as file:
        file.write(f"\n[{timestamp}]\n")
        file.write(f"Persian: {persian}\n")
        file.write(f"English: {english}\n")
        file.write(f"French: {french}\n")
        file.write(f"Portuguese: {portuguese}\n")
        file.write("-" * 60 + "\n")

# ---------------------------------------------------------
# Speech recognition callback
# ---------------------------------------------------------
def on_recognized(event):
    """Called whenever Azure recognizes a speech segment."""

    result = event.result

    if result.reason == speechsdk.ResultReason.TranslatedSpeech:

        # Get translations
        english = result.translations["en"]
        french = result.translations["fr"]
        portuguese = result.translations["pt"]

        # Display results
        print("\n" + "=" * 60)
        print(f"Persian:    {result.text}")
        print(f"English:    {english}")
        print(f"French:     {french}")
        print(f"Portuguese: {portuguese}")
        print("=" * 60)

        # Save to file
        save_translation(
            persian=result.text,
            english=english,
            french=french,
            portuguese=portuguese
        )

        print(f"Saved to: {translation_file}")

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print(
            "No speech could be recognized: "
            f"{result.no_match_details}"
        )

def on_canceled(event):
    """Called when the translation service is canceled."""

    cancellation = event.cancellation_details

    print(
        f"\nTranslation canceled: {cancellation.reason}"
    )

    if cancellation.reason == speechsdk.CancellationReason.Error:
        print(f"Error details: {cancellation.error_details}")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------
def main():
    """Continuously translate Persian speech from the microphone."""

    recognizer = speechsdk.translation.TranslationRecognizer(
        translation_config=translation_config,
        audio_config=audio_config
    )

    # Connect event handlers
    recognizer.recognized.connect(on_recognized)
    recognizer.canceled.connect(on_canceled)

    print("\nPersian speech translator started.")
    print("Speak into your microphone.")
    print("Press ENTER to stop.\n")

    # Start continuous recognition
    recognizer.start_continuous_recognition()

    try:
        input()
    except KeyboardInterrupt:
        print("\nStopping translator...")

    # Stop recognition
    recognizer.stop_continuous_recognition()

    print("Translator stopped.")


if __name__ == "__main__":
    main()
