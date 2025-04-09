import random

zbozi = ["čepice","rolák","kalhoty","tričko","šaty","ponožky"]

for i in range (10):
   nahodneZbozi1 = random.choice(zbozi)
   nahodneZbozi2 = random.choice(zbozi)
#    if nahodneZbozi1==nahodneZbozi2:
#       print("Ne, kupme jiný", nahodneZbozi2)
   print("Kupme", nahodneZbozi1)
   print("Ne, kupme", nahodneZbozi2)
  
