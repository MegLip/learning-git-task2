print("Lista codziennych zakupów") #1 commit Change name
shopping_dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
print(shopping_dict)

for keys, values in shopping_dict.items():
    print(f"Idę do {keys.title()} i kupuję tam: {str(values).title()}")

produkty = sum(shopping_dict.values(), [])
print(f"W sumie kupuję {len(produkty)} produktów")

print(f"Mój ulubiony sklep to: {keys}, a najbardziej lubię jeść: {values[0:3]}") #2 commit Add ulubione

print((str(shopping_dict.items())).upper()) #3 commit Add upper

print("***Special regards from Meg***") #4 commit Add regards