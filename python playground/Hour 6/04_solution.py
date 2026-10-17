# <details>
# <summary>10. Pet Food Recommendation
# </summary>
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# </details>
pet_species = input("What is your pet's species (Dog/Cat)? ").strip().lower()
pet_age = int(input("What is your pet's age in years? "))

if pet_species == "dog":
    if pet_age < 2:
        print("Recommend: Puppy food")
    else:
        print("Recommend: Adult dog food")
elif pet_species == "cat":
    if pet_age > 5:
        print("Recommend: Senior cat food")
    else:
        print("Recommend: Adult cat food")