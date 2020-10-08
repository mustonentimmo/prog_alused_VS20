nimi = input("Sisesta oma ees- ning perenimi!")
for osa_str in nimi.split(" "):
    print(osa_str.capitalize(), end= " ")