import tarfile

# open the tar.gz file
tar = tarfile.open("C:/Users/shitosu/Downloads/ffmpeg-6.0.tar.xz", "r:xz")

# extract all files to the current directory
tar.extractall()


# close the file
tar.close()