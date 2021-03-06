from datetime import datetime

# Save current time in variable date
date = datetime.now()

# Read input from User

jahr = input("Wann bist du geboren? ")
wohnort = input("Wo wohnst du? ")
farbe = input("Was ist deine Lieblingsfarbe? ")
essen = input("Was ist dein Lieblingsessen? ")
getraenk = input("Was ist dein Lieblingsgetraenk? ")


# Print out the input decorated with ASCII-Code
# calculate the current age of the user

print("† Du bist: " , int(date.year) - int(jahr))
print("Du wohnst in: " , wohnort)

print("       #")
print("         #")
print("        #")
print("       #")
print("       _")
print("     _|=|__________")
print("    /              \\")
print("   /                \\")
print("  /__________________\\")
print("   ||  || /--\ ||  ||")
print("   ||[]|| | .| ||[]||")
print(" ()||__||_|__|_||__||()")
print("^^^^^^^^^^====^^^^^^^^^^^")
print()


print("Deine Lieblingsfarbe ist: " , farbe)

print()

print("Am liebsten speist du: " , essen)

print("                   _")
print("                  / )")
print("            |||| / /")
print("            ||||/ /")
print("            \\__(_/")
print("            ||//")
print("            ||/")
print("            ||")
print("           (||")
print("            """)

print("Am liebsten schlürfst du: " , getraenk)

print('''   
  .
 . .
  ...
\~~~~~/
 \   /
  \ /
   V
   |
   |
  ---''')

print("_" *30)
