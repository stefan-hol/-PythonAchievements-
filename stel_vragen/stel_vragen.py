print("hallo hoelang ben je in cm's?")
lengte = input()

print("wow " + lengte + " cm's dat is interesant waar kom je vandaan?")
locatie = input()

print("aaaah " + locatie + " ben je daar groot, klein of gemiddeld? [G]=groot [K]=klein [M]=gemiddeld")
ja_of_nee = input()

if(ja_of_nee == "M"):
	print("nou goed om te weten dat iedereen rond de " + lengte + "cm is in " + locatie + ".")

elif(ja_of_nee == "K"):
	print("ach het is niet erg om " + lengte + "cm te zijn niet iedereen kan een reus zijn in " + locatie + ".")

elif(ja_of_nee == "G"):
	print("ach het is niet erg om " + lengte + "cm te zijn " + locatie + " heefd toch een reus nodig.")