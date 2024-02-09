import re

bestChar = ''
bestCharSpeed = 0

bestKart = ''
bestKartSpeed = 0

bestTire = ''
bestTireSpeed = 0

bestGlider = ''
bestGliderSpeed = 0

with open('characters') as file:
	for char in file:
		sanitizeChar = re.split(r'\s', char.strip())

		currentSpeed = float(sanitizeChar[-3])
		if currentSpeed > bestCharSpeed:
			bestChar = sanitizeChar[0] + sanitizeChar[1]
			bestCharSpeed = currentSpeed
		

with open('karts') as karts:
	for kart in karts:
		sanitizeKarts = re.split(r'\s', kart.strip())

		currentSpeed = float(sanitizeKarts[-3])
		if currentSpeed > bestKartSpeed:
					bestKart = sanitizeKarts[0]
					bestKartSpeed = currentSpeed

with open('tires') as tires:
	for tire in tires:
		sanitizeTires = re.split(r'\s', tire.strip())

		currentSpeed = float(sanitizeTires[-3])
		if currentSpeed > bestTireSpeed:
			bestTire = sanitizeTires[0]
			bestTireSpeed = currentSpeed
	
with open('gliders') as gliders:
	for glider in gliders:
		sanitizeGliders = re.split(r'\s', glider.strip())

		currentSpeed = float(sanitizeGliders[-2])
		if currentSpeed > bestGliderSpeed:
			bestGlider = sanitizeGliders[0]
			bestGliderSpeed = currentSpeed
			

print(f'Best Compo: {bestChar} {bestKart} {bestTire} {bestGlider}')
