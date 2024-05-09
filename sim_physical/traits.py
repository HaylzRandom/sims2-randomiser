from globals import (
    TODDLER_TRAITS,
    TODDLER_NUM_TRAITS,
    CHILD_TRAITS,
    CHILD_NUM_TRAITS,
    TEEN_TRAITS,
    TEEN_NUM_TRAITS,
    ADULT_TRAITS,
    ADULT_NUM_TRAITS,
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

# def get_traits_young(
#     age,
#     neat,
#     outgoing,
#     active,
#     playful,
#     nice,
#     hobby,
#     politics,
#     crime,
#     food,
#     sports,
#     work,
#     school,
#     money,
#     entertainment,
#     health,
#     paranormal,
#     weather,
#     toys,
#     environment,
#     culture,
#     fashion,
#     travel,
#     animals,
#     sciFi,
# ):
#     if age == "toddler":
#         traits = TODDLER_TRAITS
#         hobby_traits(hobby, traits, age)
#         personality_traits(neat, outgoing, active, playful, nice, age, traits)
#         interests_traits(
#             politics,
#             crime,
#             food,
#             sports,
#             work,
#             school,
#             money,
#             entertainment,
#             health,
#             paranormal,
#             weather,
#             toys,
#             environment,
#             culture,
#             fashion,
#             travel,
#             animals,
#             sciFi,
#             traits,
#             age,
#         )

#         top_toddler_traits = sorted(
#             traits.items(), key=lambda item: item[1], reverse=True
#         )[: TODDLER_NUM_TRAITS + 1]
#         toddler_traits_combined = [(key, value) for key, value in top_toddler_traits]

#         return toddler_traits_combined
#     else:
#         traits = CHILD_TRAITS
#         hobby_traits(hobby, traits, age)
#         personality_traits(neat, outgoing, active, playful, nice, age, traits)
#         interests_traits(
#             politics,
#             crime,
#             food,
#             sports,
#             work,
#             school,
#             money,
#             entertainment,
#             health,
#             paranormal,
#             weather,
#             toys,
#             environment,
#             culture,
#             fashion,
#             travel,
#             animals,
#             sciFi,
#             traits,
#             age,
#         )

#         top_child_traits = sorted(
#             traits.items(), key=lambda item: item[1], reverse=True
#         )[: CHILD_NUM_TRAITS + 1]
#         child_traits_combined = [(key, value) for key, value in top_child_traits]

#         return child_traits_combined


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

        top_teen_traits = sorted(
            traits.items(), key=lambda item: item[1], reverse=True
        )[: TEEN_NUM_TRAITS + 1]
        teen_traits_combined = [(key, value) for key, value in top_teen_traits]

        return teen_traits_combined
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

        top_adult_traits = sorted(
            traits.items(), key=lambda item: item[1], reverse=True
        )[: ADULT_NUM_TRAITS + 1]
        adult_traits_combined = [(key, value) for key, value in top_adult_traits]

        return adult_traits_combined
