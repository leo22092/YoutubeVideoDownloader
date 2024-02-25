from pydub import AudioSegment
import os
os.environ["PATH"] += os.pathsep + r' c:\users\shitosu\desktop\prog\music_vol\virmu\lib\site-packages'

# define the desired output volume
target_dBFS = -20

file_path = r'C:\Users\shitosu\Downloads'
print("Hello")
for filename in os.listdir(file_path):
    if filename.endswith('.mp3'):
        print(filename)
        print("H?I")
        # open the audio file
        sound = AudioSegment.from_mp3(os.path.join(file_path, filename))
        # normalize the volume
        change_in_dBFS = target_dBFS - sound.dBFS
        normalized_sound = sound.apply_gain(change_in_dBFS)
        # save the normalized audio file
        normalized_sound.export(os.path.join('output', filename), format='mp3')