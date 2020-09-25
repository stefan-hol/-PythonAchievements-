# hoger lager maken spelletje
import random

willekeur = random.randrange(1,11)
nieuw  = random.randrange(1,11) 

	
print("het getal van 1 / 10 is momenteel ", willekeur)
print("word het volgende getal hoger [H] of lager [L]?")

antwoord = input()

print(nieuw)

if willekeur < nieuw and antwoord == "L":
	print("dat is fout")
	print("game over")	
	
elif willekeur > nieuw and antwoord == "H":
	print("dat is fout")
	print("game over")
     

elif willekeur == nieuw:
	print ("je hebt massel het is hetzelfde")
	print("kijken of je der nog 1 kan?")
		
elif (willekeur < nieuw and antwoord == "H"):	
	print("goedzo")
	print("kijken of je der nog 1 kan?")
    
elif (willekeur > nieuw and antwoord == "L"):
	print("goedzo")
	print("kijken of je der nog 1 kan?")
	
while((willekeur > nieuw and antwoord == "L")or(willekeur < nieuw and antwoord == "H")or(willekeur == nieuw)):	
	willekeur = random.randrange(1,11)
	nieuw  = random.randrange(1,11) 
	
	print("het getal van 1 / 10 is momenteel ", willekeur)
	print("word het volgende getal hoger [H] of lager [L]?")


	antwoord = input()

	print(nieuw)


	if willekeur < nieuw and antwoord == "L":
		print("dat is fout")
		print("game over")	
	
	elif willekeur > nieuw and antwoord == "H":
		print("dat is fout")
		print("game over")
     

	elif willekeur == nieuw:
		print ("je hebt massel het is hetzelfde")
		print("kijken of je der nog 1 kan?")
		
	elif (willekeur < nieuw and antwoord == "H"):	
		print("goedzo")
		print("kijken of je der nog 1 kan?")
	
	elif (willekeur > nieuw and antwoord == "L"):
		print("goedzo")
		print("kijken of je der nog 1 kan?")
		
		
		
		