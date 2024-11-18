from melo.api import TTS

# Initialize TTS with English
tts = TTS(language='EN')

# Get available speakers
speaker_ids = tts.hps.data.spk2id
print("Available speakers:", list(speaker_ids.keys()))

# Test text-to-speech with the first available speaker
text = "Hello, this is a test of MeloTTS with Python 3.12.7."
speaker = list(speaker_ids.keys())[0]
output_file = "test_output.wav"

print(f"Generating speech for text: {text}")
print(f"Using speaker: {speaker}")

# Generate speech
tts.tts_to_file(
    text=text,
    speaker_id=speaker_ids[speaker],
    output_path=output_file
)

print(f"Speech generated and saved to: {output_file}")
