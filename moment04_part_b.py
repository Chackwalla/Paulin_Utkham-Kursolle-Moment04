# Inlämmningsuppgift moment 04

# Skapa en loop som bryter när användaren inte vill göra fler beräkningar
#?? stop = int(input("How many loops do you wanna do? "))

while True:
    f = input("Vill du göra en ny beräkning? (ja/nej): ")

  # Be användaren mata in rektangelns två sidor
    kort = int(input("Korta sidan: "))
  
    long = int(input("långa sidan: "))

  # Beräkna och skriv ut arean på rektangeln samt lagra i listan <-------
    area=kort*long

    print(area)

  # Om bägge sidorna är lika långa...
    if kort == long:

    # ... tala om att det är en kvadrat och skriv detta i listan <-----
        print("Detta är en kvadrat")

  # Loopa höjden från 1 till 10
    for j in range(1,10):
        volume = j*area  # Beräkna volymen och skriv ut den
        print(f"Volymen {j} av rektangeln är {volume}")

  # Fråga användaren om hen vill göra fler beräkningar


    # Om inte avryt loopen
    if f == "nej":
        break

# Skriv ut alla beräkningar