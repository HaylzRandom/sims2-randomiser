from globals import (
    TODDLER_TRAITS,
    TODDLER_NUM_TRAITS,
    CHILD_TRAITS,
    CHILD_NUM_TRAITS,
    TEEN_TRAITS,
    TEEN_NUM_TRAITS,
    ADULT_TRAITS,
    ADULT_NUM_TRAITS,
    TODDLER_CONFLICTS,
    CHILD_CONFLICTS,
    TEEN_CONFLICTS,
    ADULT_CONFLICTS,
)
from .turn_ons_off import (
    get_trait_turn_off_adult,
    get_trait_turn_off_teen,
    get_trait_turn_on_adult,
    get_trait_turn_on_teen,
)

from .hobby import hobby_traits
from .personality import personality_traits
from .interests import interests_traits
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
        hobby_traits(hobby, traits, age)
        personality_traits(neat, outgoing, active, playful, nice, age, traits)
        interests_traits(
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
            age,
        )

        sorted_traits = sorted(traits.items(), key=lambda x: x[1], reverse=True)

        reordered_traits = {d: v for d, v in sorted_traits if v > 0}

        return reordered_traits
    else:
        traits = CHILD_TRAITS
        hobby_traits(hobby, traits, age)
        personality_traits(neat, outgoing, active, playful, nice, age, traits)
        interests_traits(
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
            age,
        )

        sorted_traits = sorted(traits.items(), key=lambda x: x[1], reverse=True)

        reordered_traits = {d: v for d, v in sorted_traits if v > 0}

        return reordered_traits


def get_traits_old(
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
):

    if age == "teen":
        traits = TEEN_TRAITS
        get_trait_turn_on_teen(turn_on_1, traits)
        get_trait_turn_on_teen(turn_on_2, traits)
        get_trait_turn_off_teen(turn_off, traits)
        hobby_traits(hobby, traits, age)
        personality_traits(neat, outgoing, active, playful, nice, age, traits)
        interests_traits(
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
            age,
        )
        aspiration_traits(aspirations, age, traits)

        sorted_traits = sorted(traits.items(), key=lambda x: x[1], reverse=True)

        reordered_traits = {d: v for d, v in sorted_traits if v > 0}

        return reordered_traits
    else:
        traits = ADULT_TRAITS
        get_trait_turn_on_adult(turn_on_1, traits)
        get_trait_turn_on_adult(turn_on_2, traits)
        get_trait_turn_off_adult(turn_off, traits)
        hobby_traits(hobby, traits, age)
        personality_traits(neat, outgoing, active, playful, nice, age, traits)
        interests_traits(
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
            age,
        )

        aspiration_traits(aspirations, age, traits)

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
