import random
import string

#stap 1: Eerst het getal ophalen
try:
    invoer = input("Hoe lang moet het wachtwoord zijn?")
    lengte = int(invoer)
except ValueError:
    print(" Oeps! Dat is geen getal. Ik maak er voor nu maar 12 van.")
    lengte = 12

# Stap 2: De bron maken
bron = string.ascii_letters + string.digits + string.punctuation

#stap 3: Het wachtwoord bouwen
wachtwoord = "" 
for i in range(lengte):
# Hier komt de actie doe herhaald moet worden 
  gekozen_letter = random.choice(bron)
  wachtwoord = wachtwoord + gekozen_letter
  
# stap 4: printen
print("Resultaat:", wachtwoord)
