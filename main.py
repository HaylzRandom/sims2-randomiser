import inquirer
from sim_personality.generator import generate_sim
from sim_physical.generate_young import generate_young
from sim_physical.generate_old import generate_old

print("Sims 2 Sim Tool")

choice = inquirer.list_input(
    "What would you like to do?",
    choices=["1. Generate a Sim", "2. Generate Traits for Sim"],
)

if choice == "1. Generate a Sim":
    generate_sim()
else:
    # What age is the sim?

    # Teen + Up - Include Turn Ons and Turn Off
    # Adventurous, Alien, Animal Lover, Artistic, Athletic, Black Hair, Blonde Hair, Brown Hair, Business Shark, Charismatic, Cultured, Expressive, Facial Hair, Fatness, Fitness, Foodie, Grey Hair, Indoorsy, Infamous, Intellect, Introvert, Laid Back, Musical, Occult, Outdoorsy, Outgoing, Plant Lover, Rebellious, Red Hair, Stylish, Technology, Tidy, Undead, Well-Liked

    # Get personality - Neat, Outgoing, Active, Playful, Nice

    # Get pre-destined hobby - Cuisine, Film & Literature, Tinkering, Sports, Music & Dance, Fitness, Arts & Crafts, Science, Games, Nature

    # Calculate Aspiration based on personality, interests and hobby

    # Calculate traits using personality, interests, hobby and turn ons/off

    # Aspirations - Family, Fortune, Romance, Popularity, Pleasure, Knowledge

    age = input("What age is the Sim? ").lower()

    if age in ["toddler", "child"]:
        generate_young(age)
    elif age in ["teen", "adult", "elder"]:
        generate_old(age)
