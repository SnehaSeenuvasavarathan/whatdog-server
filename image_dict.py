import os

# path = "/Users/sneha/dog-classifier/Images"

# Create an empty dictionary to store the dog names
dog_names = {0: 'silky terrier', 1: 'Scottish deerhound', 2: 'Chesapeake Bay retriever', 3: 'Ibizan hound', 4: 'wire', 5: 'Saluki', 6: 'cocker spaniel', 7: 'schipperke', 8: 'borzoi', 9: 'Pembroke', 10: 'komondor', 11: 'Staffordshire bullterrier', 12: 'standard poodle', 13: 'Eskimo dog', 14: 'English foxhound', 15: 'golden retriever', 16: 'Sealyham terrier', 17: 'Japanese spaniel', 18: 'miniature schnauzer', 19: 'malamute', 20: 'malinois', 21: 'Pekinese', 22: 'giant schnauzer', 23: 'Mexican hairless', 24: 'Doberman', 25: 'standard schnauzer', 26: 'dhole', 27: 'German shepherd', 28: 'Bouvier des Flandres', 29: 'Siberian husky', 30: 'Norwich terrier', 31: 'Irish terrier', 32: 'Norfolk terrier', 33: 'Saint Bernard', 34: 'Border terrier', 35: 'briard', 36: 'Tibetan mastiff', 37: 'bull mastiff', 38: 'Maltese dog', 39: 'Kerry blue terrier', 40: 'kuvasz', 41: 'Greater Swiss Mountain dog', 42: 'Lakeland terrier', 43: 'Blenheim spaniel', 44: 'basset', 45: 'West Highland white terrier', 46: 'Chihuahua', 47: 'Border collie', 48: 'redbone', 49: 'Irish wolfhound', 50: 'bluetick', 51: 'miniature poodle', 52: 'Cardigan', 53: 'EntleBucher', 54: 'Norwegian elkhound', 55: 'German short', 56: 'Bernese mountain dog', 57: 'papillon', 58: 'Tibetan terrier', 59: 'Gordon setter', 60: 'American Staffordshire terrier', 61: 'vizsla', 62: 'kelpie', 63: 'Weimaraner', 64: 'miniature pinscher', 65: 'boxer', 66: 'chow', 67: 'Old English sheepdog', 68: 'pug', 69: 'Rhodesian ridgeback', 70: 'Scotch terrier', 71: 'Shih', 72: 'affenpinscher', 73: 'whippet', 74: 'Sussex spaniel', 75: 'otterhound', 76: 'flat', 77: 'English setter', 78: 'Italian greyhound', 79: 'Labrador retriever', 80: 'collie', 81: 'cairn', 82: 'Rottweiler', 83: 'Australian terrier', 84: 'toy terrier', 85: 'Shetland sheepdog', 86: 'African hunting dog', 87: 'Newfoundland', 88: 'Walker hound', 89: 'Lhasa', 90: 'beagle', 91: 'Samoyed', 92: 'Great Dane', 93: 'Airedale', 94: 'bloodhound', 95: 'Irish setter', 96: 'keeshond', 97: 'Dandie Dinmont', 98: 'basenji', 99: 'Bedlington terrier', 100: 'Appenzeller', 101: 'clumber', 102: 'toy poodle', 103: 'Great Pyrenees', 104: 'English springer', 105: 'Afghan hound', 106: 'Brittany spaniel', 107: 'Welsh springer spaniel', 108: 'Boston bull', 109: 'dingo', 110: 'soft', 111: 'curly', 112: 'French bulldog', 113: 'Irish water spaniel', 114: 'Pomeranian', 115: 'Brabancon griffon', 116: 'Yorkshire terrier', 117: 'groenendael', 118: 'Leonberg', 119: 'black'}

# # Iterate over the subdirectories in the path
# i=0
# for subdir in os.listdir(path):
#     if subdir[0] == 'n':
#         # Extract the dog breed name from the directory name
#         breed_name = subdir.split("-")[1].replace("_", " ")
#         # Add the dog breed name to the dictionary with the corresponding directory name as the value
#         dog_names[i] = breed_name
#         i+=1
