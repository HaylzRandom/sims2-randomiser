from globals import TEEN_OLDER_CONFLICTS, TEEN_NUM_TRAITS, ADULT_NUM_TRAITS
from .aspiration import generate_aspiration
from .turn_ons_off import get_turn_ons_off
from .traits import get_traits_old, remove_conflicting_traits, print_trait_list


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

    print(f"Aspirations for {age}:\n")
    for aspiration, value in aspiration_selection_combined:
        print(aspiration, value)

    if age == "teen":
        filtered_traits = remove_conflicting_traits(traits, TEEN_OLDER_CONFLICTS)
        teen_traits = list(filtered_traits.items())[:TEEN_NUM_TRAITS]
        print(f"\nTraits for {age}: ")
        print_trait_list(teen_traits)
    else:
        filtered_traits = remove_conflicting_traits(traits, TEEN_OLDER_CONFLICTS)
        adult_traits = list(filtered_traits.items())[:ADULT_NUM_TRAITS]
        print(f"\nTraits for {age}: ")
        print_trait_list(adult_traits)
