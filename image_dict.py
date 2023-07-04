import os

path = "data/"

# Create an empty dictionary to store the dog names
dog_names = {}

# Iterate over the subdirectories in the path
def populate_dog_names():
    i=0
    for subdir in os.listdir(path):
        if subdir[0] == 'n':
            # Extract the dog breed name from the directory name
            breed_name = subdir.split("-")[1].replace("_", " ")
            # Add the dog breed name to the dictionary with the corresponding directory name as the value
            dog_names[i] = breed_name
            i+=1

# populate_dog_names()
