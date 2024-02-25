import os
from pydub import AudioSegment

def normalize_audio(input_file, output_file, target_dBFS):
    sound = AudioSegment.from_file(input_file)
    normalized_sound = sound.normalize(target_dBFS)
    normalized_sound.export(output_file, format='mp3')

# Example usage
input_folder = "C:/Users/shitosu/Downloads/"
output_folder = 'output'
target_dBFS = -20

# Create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each audio file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.mp3'):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        normalize_audio(input_file, output_file, target_dBFS)
