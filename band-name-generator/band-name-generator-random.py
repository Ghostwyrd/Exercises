# program to generate band name randomly from lists of adjectives and animals

import random

# random.choice(list_name) selects random value from a list

#randomly selects adj from list
adj_list = ["Lost", "Giddy", "Mischievous", "Soaked", "Impatient", "Hungry, Hungry", "Bored", "Jealous", "Guilty", "Ecstatic", "Relaxed", "Suspicious", "Cunning", "Flexible", "Loyal", "Unloyal", "Content", "Speedy", "Triumphant", "Invincible", "Arctic", "River", "Confident", "Reliable", "Crafty", "Invisible", "Legendary"]
adj = random.choice(adj_list)

#randomly selects animal from list
animal_list = ["Dogs", "Cats", "Foxes", "Ferrets", "Narwhals", "Hippos", "Cephalopods", "Yaks", "Llamas", "Mustangs", "Cheetahs", "Lions", "Wolverines", "Honey Badgers", "Kookaburras", "Penguins", "Bears", "Pacyderms", "Dinosaurs", "Shepherds", "Koalas", "Pythons", "Bovines", "Dairy Cows", "Sheep", "Goats", "Gorillas", "Earthworms"]
animal = random.choice(animal_list)


print("Your band name is: The " + adj + " " + animal + ".")

