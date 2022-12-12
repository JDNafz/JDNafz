#open AI code rename files within the same directory.
import os

# Get the list of files in the directory
files = os.listdir()

# Iterate over the files and rename them
for i, file in enumerate(files):
    # Generate the new file name
    new_name = str(i+1) + '.jpg'

    # Rename the file
    os.rename(file, new_name)
