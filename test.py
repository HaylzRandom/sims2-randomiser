from sim_physical.aspiration import generate_aspiration
from sim_physical.turn_ons_off import get_turn_ons_off
from sim_physical.traits import get_traits_old, remove_conflicting_traits

from globals import (
    TODDLER_CONFLICTS,
    CHILD_CONFLICTS,
    TEEN_CONFLICTS,
    ADULT_CONFLICTS,
    TODDLER_NUM_TRAITS,
    CHILD_NUM_TRAITS,
    TEEN_NUM_TRAITS,
    ADULT_NUM_TRAITS,
)

# What age is the sim?

# Teen + Up - Include Turn Ons and Turn Off
# Adventurous, Alien, Animal Lover, Artistic, Athletic, Black Hair, Blonde Hair, Brown Hair, Business Shark, Charismatic, Cultured, Expressive, Facial Hair, Fatness, Fitness, Foodie, Grey Hair, Indoorsy, Infamous, Intellect, Introvert, Laid Back, Musical, Occult, Outdoorsy, Outgoing, Plant Lover, Rebellious, Red Hair, Stylish, Technology, Tidy, Undead, Well-Liked

# Get personality - Neat, Outgoing, Active, Playful, Nice

# Get pre-destined hobby - Cuisine, Film & Literature, Tinkering, Sports, Music & Dance, Fitness, Arts & Crafts, Science, Games, Nature

# Calculate Aspiration based on personality, interests and hobby

# Calculate traits using personality, interests, hobby and turn ons/off

# Aspirations - Family, Fortune, Romance, Popularity, Pleasure, Knowledge

# def generate_young(age):
#     hobby = get_hobby()

#     neat, outgoing, active, playful, nice = get_personality()

#     (
#         politics,
#         crime,
#         food,
#         sports,
#         work,
#         school,
#         money,
#         entertainment,
#         health,
#         paranormal,
#         weather,
#         toys,
#         environment,
#         culture,
#         fashion,
#         travel,
#         animals,
#         sciFi,
#     ) = get_interests()

#     traits = get_traits_young(
#         age,
#         neat,
#         outgoing,
#         active,
#         playful,
#         nice,
#         hobby,
#         politics,
#         crime,
#         food,
#         sports,
#         work,
#         school,
#         money,
#         entertainment,
#         health,
#         paranormal,
#         weather,
#         toys,
#         environment,
#         culture,
#         fashion,
#         travel,
#         animals,
#         sciFi,
#     )

#     print(f"\nTraits for {age}:\n")
#     for trait, value in traits:
#         print(trait.capitalize(), value)


def generate_old(age):

    data_aspiration, aspirations = generate_aspiration()

    (
        hobby,
        neat,
        outgoing,
        active,
        playful,
        nice,
        politics,
        crime,
        food,
        sports,
        work,
        school,
        money,
        entertainment,
        health,
        paranormal,
        weather,
        toys,
        environment,
        culture,
        fashion,
        travel,
        animals,
        sciFi,
    ) = data_aspiration.values()

    data = get_turn_ons_off()

    turn_on_1, turn_on_2 = data[0]["turn_ons"][0], data[0]["turn_ons"][1]
    turn_off = data[1]["turn_offs"]

    traits = get_traits_old(
        age,
        neat,
        outgoing,
        active,
        playful,
        nice,
        hobby,
        turn_on_1,
        turn_on_2,
        turn_off,
        politics,
        crime,
        food,
        sports,
        work,
        school,
        money,
        entertainment,
        health,
        paranormal,
        weather,
        toys,
        environment,
        culture,
        fashion,
        travel,
        animals,
        sciFi,
        aspirations,
    )

    aspiration_selection = sorted(
        aspirations.items(), key=lambda item: item[1], reverse=True
    )
    aspiration_selection_combined = [
        (key, value) for key, value in aspiration_selection
    ]

    print(f"\nAspirations for {age}:\n")
    for aspiration, value in aspiration_selection_combined:
        print(aspiration, value)


    if age == "teen":
        filtered_traits = remove_conflicting_traits(traits, TEEN_CONFLICTS)
        #print(f"\nFiltered Traits: {filtered_traits}")
        teen_traits = list(filtered_traits.items())[:TEEN_NUM_TRAITS]
        print(f"Final Traits: {teen_traits}")
    else:
        filtered_traits = remove_conflicting_traits(traits, ADULT_CONFLICTS)
        #print(f"Filtered Traits: {filtered_traits}")
        adult_traits = list(filtered_traits.items())[:ADULT_NUM_TRAITS]
        print(f"Final Traits: {adult_traits}")


age = input("\nWhat age is the Sim? ").lower()

# if age in ["toddler", "child"]:
#     generate_young(age)
# elif age in ["teen", "adult", "elder"]:
generate_old(age)
