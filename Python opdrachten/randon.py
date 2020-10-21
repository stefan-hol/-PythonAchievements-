import random

def woord(original):
	randomist = ''.join(random.sample(original, len(original)))
	return str(randomist)

print(woord("boterkoek"))
print(woord("bastonjekoek"))
print(woord("peperkoek"))
