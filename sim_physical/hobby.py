from globals import HOBBIES
import inquirer


# Hobbies - Arts & Crafts, Cuisine, Film & Literature, Fitness, Games, Music & Dance, Nature, Science, Sports, Tinkering
def get_hobby():

    hobby_question = [
        inquirer.List("hobby", message="What is the hobby?", choices=HOBBIES)
    ]

    hobby_answer = inquirer.prompt(hobby_question)

    if hobby_answer is None:
        hobby_answer = {"hobby": "None"}

    return hobby_answer["hobby"]


def hobby_traits(hobby, traits, age):

    if age == "toddler":
        # Hobby
        match (hobby):
            case "Arts & Crafts":
                traits["artistic"] += 1
                traits["can't stand art"] -= 1
            case "Cuisine":
                print("No Trait")
            case "Film & Literature":
                traits["couch potato"] += 1
            case "Fitness":
                traits["athletic"] += 1
                traits["disciplined"] += 1
                traits["light sleeper"] += 1
                traits["heavy sleeper"] -= 1
            case "Games":
                print("No Trait")
            case "Music & Dance":
                traits["clumsy"] += 1
                traits["virtuoso"] += 1
            case "Nature":
                traits["loves the outdoors"] += 1
                traits["hates the outdoors"] -= 1
            case "Science":
                traits["eccentric"] += 1
                traits["grumpy"] += 1
                traits["absent-minded"] -= 1
            case "Sports":
                traits["athletic"] += 1
            case "Tinkering":
                traits["eccentric"] += 1
            case _:
                print("No Trait")

    elif age == "child":
        # Hobby
        match (hobby):
            case "Arts & Crafts":
                traits["artistic"] += 1
                traits["photographer's eye"] += 1
                traits["can't stand art"] -= 1
            case "Cuisine":
                print("No Trait")
            case "Film & Literature":
                traits["bookworm"] += 1
                traits["couch potato"] += 1
                traits["over-emotional"] += 1
            case "Fitness":
                traits["athletic"] += 1
                traits["disciplined"] += 1
                traits["vegetarian"] += 1
                traits["light sleeper"] += 1
                traits["heavy sleeper"] -= 1
                traits["hydrophobic"] -= 1
                traits["never nude"] -= 1
            case "Games":
                traits["computer whiz"] += 1
                traits["technophobe"] -= 1
            case "Music & Dance":
                traits["clumsy"] += 1
                traits["virtuoso"] += 1
            case "Nature":
                traits["adventurous"] += 1
                traits["angler"] += 1
                traits["eco-friendly"] += 1
                traits["loves the outdoors"] += 1
                traits["hates the outdoors"] -= 1
            case "Science":
                traits["computer whiz"] += 1
                traits["eccentric"] += 1
                traits["absent-minded"] -= 1
                traits["grumpy"] += 1
            case "Sports":
                traits["athletic"] += 1
            case "Tinkering":
                traits["eccentric"] += 1
                traits["vehicle enthusiast"] += 1
    elif age == "teen":
        # Hobby
        match (hobby):
            case "Arts & Crafts":
                traits["artistic"] += 1
                traits["photographer's eye"] += 1
                traits["savvy sculptor"] += 1
                traits["can't stand art"] -= 1
            case "Cuisine":
                traits["natural cook"] += 1
            case "Film & Literature":
                traits["bookworm"] += 1
                traits["couch potato"] += 1
                traits["over-emotional"] += 1
            case "Fitness":
                traits["athletic"] += 1
                traits["disciplined"] += 1
                traits["vegetarian"] += 1
                traits["light sleeper"] += 1
                traits["heavy sleeper"] -= 1
                traits["hydrophobic"] -= 1
                traits["never nude"] -= 1
            case "Games":
                traits["childish"] += 1
                traits["computer whiz"] += 1
                traits["socially awkward"] += 1
                traits["technophobe"] -= 1
            case "Music & Dance":
                traits["clumsy"] += 1
                traits["dramatic"] += 1
                traits["virtuoso"] += 1
            case "Nature":
                traits["adventurous"] += 1
                traits["angler"] += 1
                traits["eco-friendly"] += 1
                traits["green thumb"] += 1
                traits["loves the outdoors"] += 1
                traits["hates the outdoors"] -= 1
            case "Science":
                traits["computer whiz"] += 1
                traits["eccentric"] += 1
                traits["handy"] += 1
                traits["absent-minded"] -= 1
                traits["grumpy"] += 1
            case "Sports":
                traits["athletic"] += 1
            case "Tinkering":
                traits["eccentric"] += 1
                traits["handy"] += 1
                traits["vehicle enthusiast"] += 1
            case _:
                print("No Trait")
    else:
        # Hobby
        match (hobby):
            case "Arts & Crafts":
                traits["artistic"] += 1
                traits["avant garde"] += 1
                traits["photographer's eye"] += 1
                traits["savvy sculptor"] += 1
                traits["can't stand art"] -= 1
            case "Cuisine":
                traits["natural cook"] += 1
            case "Film & Literature":
                traits["bookworm"] += 1
                traits["brooding"] += 1
                traits["couch potato"] += 1
                traits["over-emotional"] += 1
            case "Fitness":
                traits["athletic"] += 1
                traits["disciplined"] += 1
                traits["vegetarian"] += 1
                traits["light sleeper"] += 1
                traits["heavy sleeper"] -= 1
                traits["hydrophobic"] -= 1
                traits["never nude"] -= 1
            case "Games":
                traits["childish"] += 1
                traits["computer whiz"] += 1
                traits["socially awkward"] += 1
                traits["technophobe"] -= 1
            case "Music & Dance":
                traits["clumsy"] += 1
                traits["dramatic"] += 1
                traits["virtuoso"] += 1
            case "Nature":
                traits["adventurous"] += 1
                traits["angler"] += 1
                traits["eco-friendly"] += 1
                traits["gatherer"] += 1
                traits["green thumb"] += 1
                traits["loves the outdoors"] += 1
                traits["hates the outdoors"] -= 1
            case "Science":
                traits["bot fan"] += 1
                traits["computer whiz"] += 1
                traits["eccentric"] += 1
                traits["handy"] += 1
                traits["supernatural fan"] += 1
                traits["absent-minded"] -= 1
                traits["grumpy"] += 1
            case "Sports":
                traits["athletic"] += 1
            case "Tinkering":
                traits["eccentric"] += 1
                traits["handy"] += 1
                traits["vehicle enthusiast"] += 1
