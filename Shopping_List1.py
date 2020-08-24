print("Lista zakupów")
shopping_dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
print(shopping_dict)

for keys, values in shopping_dict.items():
    print(f"Idę do {keys.title()} i kupuję tam: {str(values).title()}")

produkty = sum(shopping_dict.values(), [])
print(f"W sumie kupuję {len(produkty)} produktów")
   