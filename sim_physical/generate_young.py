from globals import (
    TODDLER_CONFLICTS,
    TODDLER_NUM_TRAITS,
    CHILD_CONFLICTS,
    CHILD_NUM_TRAITS,
)
from .hobby import get_hobby
from .personality import get_personality
from .interests import get_interests
from .traits import get_traits_young, remove_conflicting_traits, print_trait_list


def generate_young(age):
    hobby = get_hobby()

    neat, outgoing, active, playful, nice = get_personality()

    (
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
    ) = get_interests()

    traits = get_traits_young(
        age,
        neat,
        outgoing,
        active,
        playful,
        nice,
        hobby,
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
    )

    if age == "toddler":
        filtered_traits = remove_conflicting_traits(traits, TODDLER_CONFLICTS)
        toddler_traits = list(filtered_traits.items())[:TODDLER_NUM_TRAITS]
        print(f"\nTraits for {age}: ")
        print_trait_list(toddler_traits)
    else:
        filtered_traits = remove_conflicting_traits(traits, CHILD_CONFLICTS)
        child_traits = list(filtered_traits.items())[:CHILD_NUM_TRAITS]
        print(f"\nTraits for {age}: ")
        print_trait_list(child_traits)
