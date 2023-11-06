from sampler import sample
from time import sleep

animals_names = {"🦤": "a dodo", "🦏": "a rhino", "🦬": "a bison", "🐖": "a pig", "🐄": "a cow", "🐃": "a water buffalo", "🐂": "an ox", 
                 "🦣": "a mammoth", "🦥": "a sloth", "🦖": "a tyrannosaurus", "🦕": "a sauropod", "🦑": "a squid", "🦐": "a shrimp", "🦃": "a turkey",
                 "🦞": "a lobster", "🦚": "a peacock", "🐧": "a penguin", "🐼": "a panda", "🦒": "a giraffe"}
animals = list(animals_names.keys())

print("Welcome to the Emoji Zoo!")
sleep(1)
print("Here you can enjoy a lovely sample of cute animals, perfect for cheering up your day!")
sleep(1)
n = input("How many animals did you see today? ")
try:
    n = int(n)
except ValueError:
    print("That was not a number! Please try visiting the zoo again.")
    exit()

if n < 0:
    print("Unless you saw something die, I am not sure that you can see a negative number of animals. Please try visiting the zoo again.")
    exit()
elif n == 0:
    print("You saw nothing today. That must have been disappointing. Please try visiting the zoo again.")
elif n > len(animals):
    print("There weren't that many animals at the zoo. You must not have visited. Please try visiting the zoo again.")
else:
    animals_sample = sample(animals, n)
    print((" 🌴 ").join(animals_sample))
    if n == 1:
        print(f"How exciting! When you visited the zoo today, you saw {animals_names[animals_sample[0]]}!")
    else:
        names = [animals_names[emoji] for emoji in animals_sample]
        print(f"How exciting! When you visited the zoo today, you saw {", ".join(names[:-1])}, and {names[-1]}!")