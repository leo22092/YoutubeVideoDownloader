import os
from pydub import AudioSegment

def reduce_volume(input_file, output_file, reduction_factor):
    sound = AudioSegment.from_file(input_file)
    normalized_sound = sound - reduction_factor
    normalized_sound.export(output_file, format='mp3')

# Example usage
input_file = "C:/Users/shitosu/Downloads/Kesariya.mp3"
output_file = 'output/Kesariya.mp3'
reduction_factor = 10  # Adjust the reduction factor as needed

# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(output_file), exist_ok=True)

reduce_volume(input_file, output_file, reduction_factor)
