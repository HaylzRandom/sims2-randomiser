from globals import (
    TODDLER_TRAITS,
    CHILD_TRAITS,
    TEEN_OLDER_TRAITS,
)
from .turn_ons_off import (
    get_trait_turn_off,
    get_trait_turn_on,
)

from .hobby import hobby_traits_all, hobby_traits_child, hobby_traits_teen
from .personality import (
    personality_traits_all,
    personality_traits_child,
    personality_traits_teen,
)
from .interests import (
    interests_traits_all,
    interests_traits_child,
    interests_traits_teen,
)
from .aspiration import aspiration_traits


def get_traits_young(
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
):
    if age == "toddler":
        traits = TODDLER_TRAITS
        hobby_traits_all(hobby, traits)
        personality_traits_all(neat, outgoing, active, playful, nice, traits)
        interests_traits_all(
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
            traits,
        )

        sorted_traits = sorted(traits.items(), key=lambda x: x[1], reverse=True)

        reordered_traits = {d: v for d, v in sorted_traits if v > 0}

        return reordered_traits
    else:
        traits = CHILD_TRAITS

        hobby_traits_all(hobby, traits)
        hobby_traits_child(hobby, traits)

        personality_traits_all(neat, outgoing, active, playful, nice, traits)
        personality_traits_child(neat, outgoing, active, playful, nice, traits)

        interests_traits_all(
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
            traits,
        )
        interests_traits_child(
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
            traits,
        )

        sorted_traits = sorted(traits.items(), key=lambda x: x[1], reverse=True)

        reordered_traits = {d: v for d, v in sorted_traits if v > 0}

        return reordered_traits


def get_traits_old(
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
):

    traits = TEEN_OLDER_TRAITS

    get_trait_turn_on(turn_on_1, traits)
    get_trait_turn_on(turn_on_2, traits)
    get_trait_turn_off(turn_off, traits)

    hobby_traits_all(hobby, traits)
    hobby_traits_child(hobby, traits)
    hobby_traits_teen(hobby, traits)

    personality_traits_all(neat, outgoing, active, playful, nice, traits)
    personality_traits_child(neat, outgoing, active, playful, nice, traits)
    personality_traits_teen(neat, outgoing, active, playful, nice, traits)

    interests_traits_all(
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
        traits,
    )
    interests_traits_child(
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
        traits,
    )
    interests_traits_teen(
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
        traits,
    )
    aspiration_traits(aspirations, traits)

    sorted_traits = sorted(traits.items(), key=lambda x: x[1], reverse=True)

    reordered_traits = {d: v for d, v in sorted_traits if v > 0}

    return reordered_traits


def remove_conflicting_traits(traits, conflict_traits):
    # Make empty dict for final traits
    # Loop through traits
    # Loop through conflicts
    # Compare trait and conflict trait
    # If match, loop through traits and remove conflicting traits
    # Add trait to final traits dict
    # Return the final traits when completed

    final_traits = {}  # Make empty dict for final traits

    for trait, value in list(
        traits.items()
    ):  # Iterating over a copy to allow modification of original dictionary
        conflicts = [
            conflict
            for conflict_trait in conflict_traits
            if trait == conflict_trait["trait"]
            for conflict in conflict_trait.values()
            if conflict != trait
        ]

        if all(conflict not in final_traits for conflict in conflicts):
            final_traits[trait] = value
            del traits[trait]  # Remove the trait from the original dictionary

    return final_traits


def print_trait_list(traits):

    for i, (trait, value) in enumerate(traits, start=1):
        print(f"{i}. {trait.capitalize()} ({value})")
