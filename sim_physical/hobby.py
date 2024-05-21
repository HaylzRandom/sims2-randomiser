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


def hobby_traits_all(hobby, traits):
    match (hobby):
        case "Arts & Crafts":
            traits["absent-minded"] -= 10
            traits["artistic"] += 10
            traits["athletic"] -= 10
            traits["brave"] -= 10
            traits["clumsy"] += 10
            traits["couch potato"] -= 10
            traits["disciplined"] -= 10
            traits["easily impressed"] += 10
            traits["eccentric"] -= 10
            traits["evil"] -= 10
            traits["excitable"] += 10
            traits["friendly"] += 10
            traits["genius"] -= 10
            traits["good"] += 10
            traits["grumpy"] -= 10
            traits["hates the outdoors"] += 10
            traits["heavy sleeper"] -= 10
            traits["insane"] -= 10
            traits["light sleeper"] += 10
            traits["loner"] -= 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["neurotic"] -= 10
            traits["perceptive"] += 10
            traits["sailor"] -= 10
            traits["slob"] -= 10
            traits["virtuoso"] -= 10
        case "Cuisine":
            traits["absent-minded"] -= 10
            traits["artistic"] -= 10
            traits["athletic"] -= 10
            traits["brave"] += 10
            traits["clumsy"] -= 10
            traits["couch potato"] += 10
            traits["disciplined"] -= 10
            traits["easily impressed"] -= 10
            traits["eccentric"] -= 10
            traits["evil"] -= 10
            traits["excitable"] -= 10
            traits["friendly"] += 10
            traits["genius"] += 10
            traits["good"] += 10
            traits["grumpy"] -= 10
            traits["hates the outdoors"] += 10
            traits["heavy sleeper"] += 10
            traits["insane"] -= 10
            traits["light sleeper"] -= 10
            traits["loner"] += 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["neurotic"] -= 10
            traits["perceptive"] += 10
            traits["sailor"] -= 10
            traits["slob"] -= 10
            traits["virtuoso"] -= 10
        case "Film & Literature":
            traits["absent-minded"] += 10
            traits["artistic"] -= 10
            traits["athletic"] -= 10
            traits["brave"] += 10
            traits["clumsy"] += 10
            traits["couch potato"] += 10
            traits["disciplined"] -= 10
            traits["easily impressed"] += 10
            traits["eccentric"] += 10
            traits["evil"] += 10
            traits["excitable"] += 10
            traits["friendly"] += 10
            traits["genius"] -= 10
            traits["good"] += 10
            traits["grumpy"] += 10
            traits["hates the outdoors"] += 10
            traits["heavy sleeper"] += 10
            traits["insane"] += 10
            traits["light sleeper"] -= 10
            traits["loner"] += 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["neurotic"] += 10
            traits["perceptive"] -= 10
            traits["sailor"] -= 10
            traits["slob"] += 10
            traits["virtuoso"] -= 10
        case "Fitness":
            traits["absent-minded"] -= 10
            traits["artistic"] -= 10
            traits["athletic"] += 10
            traits["brave"] += 10
            traits["clumsy"] -= 10
            traits["couch potato"] -= 10
            traits["disciplined"] += 10
            traits["easily impressed"] -= 10
            traits["eccentric"] -= 10
            traits["evil"] += 10
            traits["excitable"] -= 10
            traits["friendly"] -= 10
            traits["genius"] -= 10
            traits["good"] += 10
            traits["grumpy"] -= 10
            traits["hates the outdoors"] -= 10
            traits["heavy sleeper"] -= 10
            traits["insane"] += 10
            traits["light sleeper"] += 10
            traits["loner"] -= 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["neurotic"] -= 10
            traits["perceptive"] -= 10
            traits["sailor"] += 10
            traits["slob"] -= 10
            traits["virtuoso"] -= 10
        case "Games":
            traits["absent-minded"] += 10
            traits["artistic"] -= 10
            traits["athletic"] -= 10
            traits["brave"] -= 10
            traits["clumsy"] += 10
            traits["couch potato"] += 10
            traits["disciplined"] -= 10
            traits["easily impressed"] += 10
            traits["eccentric"] += 10
            traits["evil"] -= 10
            traits["excitable"] += 10
            traits["friendly"] += 10
            traits["genius"] += 10
            traits["good"] += 10
            traits["grumpy"] -= 10
            traits["hates the outdoors"] += 10
            traits["heavy sleeper"] += 10
            traits["insane"] += 10
            traits["light sleeper"] -= 10
            traits["loner"] -= 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["neurotic"] += 10
            traits["perceptive"] += 10
            traits["sailor"] -= 10
            traits["slob"] += 10
            traits["virtuoso"] -= 10
        case "Music & Dance":
            traits["absent-minded"] -= 10
            traits["artistic"] -= 10
            traits["athletic"] -= 10
            traits["brave"] += 10
            traits["clumsy"] += 10
            traits["couch potato"] -= 10
            traits["disciplined"] -= 10
            traits["easily impressed"] += 10
            traits["eccentric"] -= 10
            traits["evil"] -= 10
            traits["excitable"] += 10
            traits["friendly"] += 10
            traits["genius"] += 10
            traits["good"] += 10
            traits["grumpy"] -= 10
            traits["hates the outdoors"] -= 10
            traits["heavy sleeper"] -= 10
            traits["insane"] -= 10
            traits["light sleeper"] += 10
            traits["loner"] -= 10
            traits["loves the cold"] += 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["neurotic"] += 10
            traits["perceptive"] += 10
            traits["sailor"] -= 10
            traits["slob"] -= 10
            traits["virtuoso"] += 10
        case "Nature":
            traits["absent-minded"] += 10
            traits["artistic"] -= 10
            traits["athletic"] += 10
            traits["brave"] += 10
            traits["clumsy"] += 10
            traits["couch potato"] -= 10
            traits["disciplined"] += 10
            traits["easily impressed"] += 10
            traits["eccentric"] -= 10
            traits["evil"] -= 10
            traits["excitable"] += 10
            traits["friendly"] += 10
            traits["genius"] -= 10
            traits["good"] += 10
            traits["grumpy"] += 10
            traits["hates the outdoors"] -= 10
            traits["heavy sleeper"] -= 10
            traits["insane"] += 10
            traits["light sleeper"] += 10
            traits["loner"] += 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["neurotic"] -= 10
            traits["perceptive"] -= 10
            traits["sailor"] -= 10
            traits["slob"] += 10
            traits["virtuoso"] -= 10
        case "Science":
            traits["absent-minded"] -= 10
            traits["artistic"] -= 10
            traits["athletic"] -= 10
            traits["brave"] -= 10
            traits["clumsy"] -= 10
            traits["couch potato"] -= 10
            traits["disciplined"] += 10
            traits["easily impressed"] -= 10
            traits["eccentric"] += 10
            traits["evil"] += 10
            traits["excitable"] -= 10
            traits["friendly"] -= 10
            traits["genius"] += 10
            traits["good"] -= 10
            traits["grumpy"] += 10
            traits["hates the outdoors"] += 10
            traits["heavy sleeper"] -= 10
            traits["insane"] += 10
            traits["light sleeper"] += 10
            traits["loner"] += 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["neurotic"] += 10
            traits["perceptive"] += 10
            traits["sailor"] -= 10
            traits["slob"] -= 10
            traits["virtuoso"] -= 10
        case "Sports":
            traits["absent-minded"] += 10
            traits["artistic"] -= 10
            traits["athletic"] += 10
            traits["brave"] += 10
            traits["clumsy"] += 10
            traits["couch potato"] += 10
            traits["disciplined"] -= 10
            traits["easily impressed"] += 10
            traits["eccentric"] += 10
            traits["evil"] -= 10
            traits["excitable"] += 10
            traits["friendly"] += 10
            traits["genius"] -= 10
            traits["good"] += 10
            traits["grumpy"] -= 10
            traits["hates the outdoors"] -= 10
            traits["heavy sleeper"] += 10
            traits["insane"]
            traits["light sleeper"] -= 10
            traits["loner"] -= 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["neurotic"] -= 10
            traits["perceptive"] -= 10
            traits["sailor"] -= 10
            traits["slob"] += 10
            traits["virtuoso"] -= 10
        case "Tinkering":
            traits["absent-minded"] -= 10
            traits["artistic"] -= 10
            traits["athletic"] -= 10
            traits["brave"] -= 10
            traits["clumsy"] -= 10
            traits["couch potato"] -= 10
            traits["disciplined"] += 10
            traits["easily impressed"] -= 10
            traits["eccentric"] += 10
            traits["evil"] += 10
            traits["excitable"] -= 10
            traits["friendly"] -= 10
            traits["genius"] += 10
            traits["good"] -= 10
            traits["grumpy"] += 10
            traits["hates the outdoors"] -= 10
            traits["heavy sleeper"] += 10
            traits["insane"] += 10
            traits["light sleeper"] -= 10
            traits["loner"] += 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["neurotic"] += 10
            traits["perceptive"] -= 10
            traits["sailor"] -= 10
            traits["slob"] += 10
            traits["virtuoso"] -= 10


def hobby_traits_child(hobby, traits):
    traits["adventurous"]
    traits["ambitious"]
    traits["angler"]
    traits["animal lover"]
    traits["bookworm"]
    traits["bot fan"]
    traits["can't stand art"]
    traits["cat person"]
    traits["computer whiz"]
    traits["coward"]
    traits["daredevil"]
    traits["diva"]
    traits["dog person"]
    traits["eco-friendly"]
    traits["equestrian"]
    traits["family-oriented"]
    traits["frugal"]
    traits["good sense of humour"]
    traits["hot-headed"]
    traits["hydrophobic"]
    traits["inappropriate"]
    traits["kleptomaniac"]
    traits["loser"]
    traits["loves to swim"]
    traits["lucky"]
    traits["mean-spirited"]
    traits["mooch"]
    traits["neat"]
    traits["never nude"]
    traits["night owl"]
    traits["no sense of humour"]
    traits["over-emotional"]
    traits["party animal"]
    traits["perfectionist"]
    traits["photographer's eye"]
    traits["rebellious"]
    traits["shy"]
    traits["snob"]
    traits["star quality"]
    traits["supernatural fan"]
    traits["technophobe"]
    traits["unlucky"]
    traits["unstable"]
    traits["vegetarian"]
    traits["vehicle enthusiast"]
    traits["workaholic"]

    match (hobby):
        case "Arts & Crafts":
            traits["adventurous"] += 10
            traits["ambitious"] += 10
            traits["angler"] -= 10
            traits["animal lover"] += 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["can't stand art"] -= 10
            traits["cat person"] -= 10
            traits["computer whiz"] -= 10
            traits["coward"] -= 10
            traits["daredevil"] += 10
            traits["diva"] += 10
            traits["dog person"] -= 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] += 10
            traits["family-oriented"] -= 10
            traits["frugal"] += 10
            traits["good sense of humour"] += 10
            traits["hot-headed"] += 10
            traits["hydrophobic"] -= 10
            traits["inappropriate"] -= 10
            traits["kleptomaniac"] += 10
            traits["loser"] += 10
            traits["loves to swim"] += 10
            traits["lucky"] += 10
            traits["mean-spirited"] += 10
            traits["mooch"] += 10
            traits["neat"] -= 10
            traits["never nude"] -= 10
            traits["night owl"] += 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] += 10
            traits["perfectionist"] += 10
            traits["photographer's eye"] += 10
            traits["rebellious"] += 10
            traits["shy"] -= 10
            traits["snob"] += 10
            traits["star quality"] += 10
            traits["supernatural fan"] -= 10
            traits["technophobe"] += 10
            traits["unlucky"] -= 10
            traits["unstable"] += 10
            traits["vegetarian"] -= 10
            traits["vehicle enthusiast"] -= 10
            traits["workaholic"] += 10
        case "Cuisine":
            traits["adventurous"] += 10
            traits["ambitious"] -= 10
            traits["angler"] += 10
            traits["animal lover"] += 10
            traits["bookworm"] += 10
            traits["bot fan"] -= 10
            traits["can't stand art"] += 10
            traits["cat person"] += 10
            traits["computer whiz"] -= 10
            traits["coward"] += 10
            traits["daredevil"] -= 10
            traits["diva"] += 10
            traits["dog person"] += 10
            traits["eco-friendly"] += 10
            traits["equestrian"] -= 10
            traits["family-oriented"] += 10
            traits["frugal"] += 10
            traits["good sense of humour"] += 10
            traits["hot-headed"] -= 10
            traits["hydrophobic"] += 10
            traits["inappropriate"] -= 10
            traits["kleptomaniac"] -= 10
            traits["loser"] += 10
            traits["loves to swim"] -= 10
            traits["lucky"] -= 10
            traits["mean-spirited"] -= 10
            traits["mooch"] -= 10
            traits["neat"] += 10
            traits["never nude"] += 10
            traits["night owl"] -= 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] += 10
            traits["perfectionist"] += 10
            traits["photographer's eye"] += 10
            traits["rebellious"] -= 10
            traits["shy"] += 10
            traits["snob"] += 10
            traits["star quality"] += 10
            traits["supernatural fan"] += 10
            traits["technophobe"] -= 10
            traits["unlucky"] += 10
            traits["unstable"] -= 10
            traits["vegetarian"] += 10
            traits["vehicle enthusiast"] -= 10
            traits["workaholic"] -= 10
        case "Film & Literature":
            traits["adventurous"] -= 10
            traits["ambitious"] += 10
            traits["angler"] -= 10
            traits["animal lover"] += 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["can't stand art"] += 10
            traits["cat person"] += 10
            traits["computer whiz"] += 10
            traits["coward"] += 10
            traits["daredevil"] -= 10
            traits["diva"] += 10
            traits["dog person"] += 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] -= 10
            traits["family-oriented"] += 10
            traits["frugal"] += 10
            traits["good sense of humour"] += 10
            traits["hot-headed"] += 10
            traits["hydrophobic"] -= 10
            traits["inappropriate"] += 10
            traits["kleptomaniac"] += 10
            traits["loser"] += 10
            traits["loves to swim"] -= 10
            traits["lucky"] += 10
            traits["mean-spirited"] += 10
            traits["mooch"] -= 10
            traits["neat"] -= 10
            traits["never nude"] += 10
            traits["night owl"] += 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] -= 10
            traits["perfectionist"] -= 10
            traits["photographer's eye"] -= 10
            traits["rebellious"] -= 10
            traits["shy"] += 10
            traits["snob"] -= 10
            traits["star quality"] += 10
            traits["supernatural fan"] += 10
            traits["technophobe"] -= 10
            traits["unlucky"] -= 10
            traits["unstable"] -= 10
            traits["vegetarian"] -= 10
            traits["vehicle enthusiast"] -= 10
            traits["workaholic"] -= 10
        case "Fitness":
            traits["adventurous"] += 10
            traits["ambitious"] += 10
            traits["angler"] -= 10
            traits["animal lover"] -= 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["can't stand art"] -= 10
            traits["cat person"] -= 10
            traits["computer whiz"] -= 10
            traits["coward"] -= 10
            traits["daredevil"] += 10
            traits["diva"] += 10
            traits["dog person"] -= 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] += 10
            traits["family-oriented"] -= 10
            traits["frugal"] -= 10
            traits["good sense of humour"] -= 10
            traits["hot-headed"] += 10
            traits["hydrophobic"] -= 10
            traits["inappropriate"] += 10
            traits["kleptomaniac"] += 10
            traits["loser"] -= 10
            traits["loves to swim"] += 10
            traits["lucky"] += 10
            traits["mean-spirited"] += 10
            traits["mooch"] -= 10
            traits["neat"] -= 10
            traits["never nude"] -= 10
            traits["night owl"] -= 10
            traits["no sense of humour"] += 10
            traits["over-emotional"] -= 10
            traits["party animal"] += 10
            traits["perfectionist"] += 10
            traits["photographer's eye"] -= 10
            traits["rebellious"] += 10
            traits["shy"] -= 10
            traits["snob"] -= 10
            traits["star quality"] += 10
            traits["supernatural fan"] -= 10
            traits["technophobe"] += 10
            traits["unlucky"] -= 10
            traits["unstable"] += 10
            traits["vegetarian"] += 10
            traits["vehicle enthusiast"] -= 10
            traits["workaholic"] -= 10
        case "Games":
            traits["adventurous"] -= 10
            traits["ambitious"] -= 10
            traits["angler"] -= 10
            traits["animal lover"] += 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["can't stand art"] -= 10
            traits["cat person"] -= 10
            traits["computer whiz"] += 10
            traits["coward"] -= 10
            traits["daredevil"] += 10
            traits["diva"] -= 10
            traits["dog person"] += 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] -= 10
            traits["family-oriented"] += 10
            traits["frugal"] -= 10
            traits["good sense of humour"] += 10
            traits["hot-headed"] += 10
            traits["hydrophobic"] += 10
            traits["inappropriate"] += 10
            traits["kleptomaniac"] += 10
            traits["loser"] += 10
            traits["loves to swim"] -= 10
            traits["lucky"] -= 10
            traits["mean-spirited"] += 10
            traits["mooch"] -= 10
            traits["neat"] += 10
            traits["never nude"] += 10
            traits["night owl"] += 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] -= 10
            traits["party animal"] -= 10
            traits["perfectionist"] -= 10
            traits["photographer's eye"] -= 10
            traits["rebellious"] -= 10
            traits["shy"] += 10
            traits["snob"] -= 10
            traits["star quality"] -= 10
            traits["supernatural fan"] += 10
            traits["technophobe"] -= 10
            traits["unlucky"] += 10
            traits["unstable"] += 10
            traits["vegetarian"] -= 10
            traits["vehicle enthusiast"] -= 10
            traits["workaholic"] -= 10
        case "Music & Dance":
            traits["adventurous"] -= 10
            traits["ambitious"] += 10
            traits["angler"] -= 10
            traits["animal lover"] += 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["can't stand art"] -= 10
            traits["cat person"] -= 10
            traits["computer whiz"] -= 10
            traits["coward"] -= 10
            traits["daredevil"] += 10
            traits["diva"] += 10
            traits["dog person"] -= 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] += 10
            traits["family-oriented"] -= 10
            traits["frugal"] += 10
            traits["good sense of humour"] += 10
            traits["hot-headed"] += 10
            traits["hydrophobic"] -= 10
            traits["inappropriate"] += 10
            traits["kleptomaniac"] -= 10
            traits["loser"] -= 10
            traits["loves to swim"] -= 10
            traits["lucky"] += 10
            traits["mean-spirited"] -= 10
            traits["mooch"] -= 10
            traits["neat"] -= 10
            traits["never nude"] -= 10
            traits["night owl"] -= 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] += 10
            traits["perfectionist"] -= 10
            traits["photographer's eye"] -= 10
            traits["rebellious"] += 10
            traits["shy"] -= 10
            traits["snob"] += 10
            traits["star quality"] += 10
            traits["supernatural fan"] -= 10
            traits["technophobe"] += 10
            traits["unlucky"] -= 10
            traits["unstable"] += 10
            traits["vegetarian"] -= 10
            traits["vehicle enthusiast"] -= 10
            traits["workaholic"] -= 10
        case "Nature":
            traits["adventurous"] -= 10
            traits["ambitious"] -= 10
            traits["angler"] += 10
            traits["animal lover"] += 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["can't stand art"] += 10
            traits["cat person"] += 10
            traits["computer whiz"] -= 10
            traits["coward"] += 10
            traits["daredevil"] -= 10
            traits["diva"] -= 10
            traits["dog person"] += 10
            traits["eco-friendly"] += 10
            traits["equestrian"] += 10
            traits["family-oriented"] += 10
            traits["frugal"] -= 10
            traits["good sense of humour"] += 10
            traits["hot-headed"] -= 10
            traits["hydrophobic"] -= 10
            traits["inappropriate"] -= 10
            traits["kleptomaniac"] -= 10
            traits["loser"] += 10
            traits["loves to swim"] += 10
            traits["lucky"] -= 10
            traits["mean-spirited"] -= 10
            traits["mooch"] -= 10
            traits["neat"] -= 10
            traits["never nude"] -= 10
            traits["night owl"] -= 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] -= 10
            traits["perfectionist"] -= 10
            traits["photographer's eye"] -= 10
            traits["rebellious"] -= 10
            traits["shy"] += 10
            traits["snob"] -= 10
            traits["star quality"] -= 10
            traits["supernatural fan"] += 10
            traits["technophobe"] += 10
            traits["unlucky"] += 10
            traits["unstable"] += 10
            traits["vegetarian"] += 10
            traits["vehicle enthusiast"] -= 10
            traits["workaholic"] -= 10
        case "Science":
            traits["adventurous"] -= 10
            traits["ambitious"] -= 10
            traits["angler"] += 10
            traits["animal lover"] -= 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["can't stand art"] += 10
            traits["cat person"] += 10
            traits["computer whiz"] += 10
            traits["coward"] += 10
            traits["daredevil"] -= 10
            traits["diva"] -= 10
            traits["dog person"] -= 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] -= 10
            traits["family-oriented"] -= 10
            traits["frugal"] -= 10
            traits["good sense of humour"] -= 10
            traits["hot-headed"] += 10
            traits["hydrophobic"] += 10
            traits["inappropriate"] += 10
            traits["kleptomaniac"] += 10
            traits["loser"] += 10
            traits["loves to swim"] -= 10
            traits["lucky"] -= 10
            traits["mean-spirited"] += 10
            traits["mooch"] -= 10
            traits["neat"] += 10
            traits["never nude"] += 10
            traits["night owl"] += 10
            traits["no sense of humour"] += 10
            traits["over-emotional"] -= 10
            traits["party animal"] -= 10
            traits["perfectionist"] += 10
            traits["photographer's eye"] -= 10
            traits["rebellious"] -= 10
            traits["shy"] += 10
            traits["snob"] += 10
            traits["star quality"] -= 10
            traits["supernatural fan"] += 10
            traits["technophobe"] -= 10
            traits["unlucky"] += 10
            traits["unstable"] += 10
            traits["vegetarian"] -= 10
            traits["vehicle enthusiast"] += 10
            traits["workaholic"] -= 10
        case "Sports":
            traits["adventurous"] += 10
            traits["ambitious"] += 10
            traits["angler"] -= 10
            traits["animal lover"] += 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["can't stand art"] -= 10
            traits["cat person"] -= 10
            traits["computer whiz"] -= 10
            traits["coward"] -= 10
            traits["daredevil"] += 10
            traits["diva"] += 10
            traits["dog person"] += 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] += 10
            traits["family-oriented"] -= 10
            traits["frugal"] -= 10
            traits["good sense of humour"] += 10
            traits["hot-headed"] -= 10
            traits["hydrophobic"] -= 10
            traits["inappropriate"] += 10
            traits["kleptomaniac"] += 10
            traits["loser"] += 10
            traits["loves to swim"] += 10
            traits["lucky"] += 10
            traits["mean-spirited"] += 10
            traits["mooch"] -= 10
            traits["neat"] -= 10
            traits["never nude"] -= 10
            traits["night owl"] -= 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] += 10
            traits["perfectionist"] -= 10
            traits["photographer's eye"] -= 10
            traits["rebellious"] += 10
            traits["shy"] -= 10
            traits["snob"] -= 10
            traits["star quality"] -= 10
            traits["supernatural fan"] -= 10
            traits["technophobe"] -= 10
            traits["unlucky"] += 10
            traits["unstable"] += 10
            traits["vegetarian"] -= 10
            traits["vehicle enthusiast"] -= 10
            traits["workaholic"] -= 10
        case "Tinkering":
            traits["adventurous"] -= 10
            traits["ambitious"] -= 10
            traits["angler"] -= 10
            traits["animal lover"] -= 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["can't stand art"]
            traits["cat person"] += 10
            traits["computer whiz"] += 10
            traits["coward"] += 10
            traits["daredevil"] -= 10
            traits["diva"] -= 10
            traits["dog person"] += 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] -= 10
            traits["family-oriented"] += 10
            traits["frugal"] += 10
            traits["good sense of humour"] -= 10
            traits["hot-headed"] += 10
            traits["hydrophobic"] += 10
            traits["inappropriate"] -= 10
            traits["kleptomaniac"] += 10
            traits["loser"] += 10
            traits["loves to swim"] -= 10
            traits["lucky"] -= 10
            traits["mean-spirited"] -= 10
            traits["mooch"] -= 10
            traits["neat"] -= 10
            traits["never nude"] += 10
            traits["night owl"] -= 10
            traits["no sense of humour"] += 10
            traits["over-emotional"] -= 10
            traits["party animal"] -= 10
            traits["perfectionist"] += 10
            traits["photographer's eye"] -= 10
            traits["rebellious"] += 10
            traits["shy"] += 10
            traits["snob"] -= 10
            traits["star quality"] -= 10
            traits["supernatural fan"] -= 10
            traits["technophobe"] -= 10
            traits["unlucky"] += 10
            traits["unstable"] -= 10
            traits["vegetarian"] -= 10
            traits["vehicle enthusiast"] += 10
            traits["workaholic"] -= 10


def hobby_traits_teen(hobby, traits):
    traits["avant garde"]
    traits["born salesman"]
    traits["brooding"]
    traits["charismatic"]
    traits["childish"]
    traits["commitment issues"]
    traits["dislikes children"]
    traits["dramatic"]
    traits["flirty"]
    traits["gatherer"]
    traits["great kisser"]
    traits["green thumb"]
    traits["handy"]
    traits["hopeless romantic"]
    traits["irresistible"]
    traits["natural born performer"]
    traits["natural cook"]
    traits["nurturing"]
    traits["proper"]
    traits["savvy sculptor"]
    traits["schmoozer"]
    traits["social butterfly"]
    traits["socially awkward"]
    traits["supernatural sceptic"]
    traits["unflirty"]

    match (hobby):
        case "Arts & Crafts":
            traits["avant garde"] += 10
            traits["born salesman"] += 10
            traits["brooding"] += 10
            traits["charismatic"] += 10
            traits["childish"] -= 10
            traits["commitment issues"] += 10
            traits["dislikes children"] += 10
            traits["dramatic"] += 10
            traits["flirty"] += 10
            traits["gatherer"] -= 10
            traits["great kisser"] += 10
            traits["green thumb"] -= 10
            traits["handy"] -= 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] += 10
            traits["natural born performer"] -= 10
            traits["natural cook"] -= 10
            traits["nurturing"] -= 10
            traits["proper"] -= 10
            traits["savvy sculptor"] += 10
            traits["schmoozer"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] += 10
            traits["supernatural sceptic"] += 10
            traits["unflirty"] -= 10
        case "Cuisine":
            traits["avant garde"] -= 10
            traits["born salesman"] -= 10
            traits["brooding"] += 10
            traits["charismatic"] -= 10
            traits["childish"] -= 10
            traits["commitment issues"] += 10
            traits["dislikes children"] -= 10
            traits["dramatic"] -= 10
            traits["flirty"] += 10
            traits["gatherer"] += 10
            traits["great kisser"] -= 10
            traits["green thumb"] += 10
            traits["handy"] += 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] += 10
            traits["natural born performer"] -= 10
            traits["natural cook"] += 10
            traits["nurturing"] += 10
            traits["proper"] += 10
            traits["savvy sculptor"] -= 10
            traits["schmoozer"] -= 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unflirty"] += 10
        case "Film & Literature":
            traits["avant garde"] -= 10
            traits["born salesman"] -= 10
            traits["brooding"] -= 10
            traits["charismatic"] += 10
            traits["childish"] -= 10
            traits["commitment issues"] -= 10
            traits["dislikes children"] -= 10
            traits["dramatic"] += 10
            traits["flirty"] -= 10
            traits["gatherer"] -= 10
            traits["great kisser"] -= 10
            traits["green thumb"] -= 10
            traits["handy"] -= 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] -= 10
            traits["natural born performer"] += 10
            traits["natural cook"] -= 10
            traits["nurturing"] += 10
            traits["proper"] += 10
            traits["savvy sculptor"] -= 10
            traits["schmoozer"] += 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unflirty"] += 10
        case "Fitness":
            traits["avant garde"] -= 10
            traits["born salesman"] += 10
            traits["brooding"] -= 10
            traits["charismatic"] += 10
            traits["childish"] -= 10
            traits["commitment issues"] += 10
            traits["dislikes children"] += 10
            traits["dramatic"] += 10
            traits["flirty"] += 10
            traits["gatherer"] -= 10
            traits["great kisser"] += 10
            traits["green thumb"] -= 10
            traits["handy"] -= 10
            traits["hopeless romantic"] -= 10
            traits["irresistible"] += 10
            traits["natural born performer"] += 10
            traits["natural cook"] -= 10
            traits["nurturing"] -= 10
            traits["proper"] -= 10
            traits["savvy sculptor"] -= 10
            traits["schmoozer"] += 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unflirty"] -= 10
        case "Games":
            traits["avant garde"] -= 10
            traits["born salesman"] -= 10
            traits["brooding"] += 10
            traits["charismatic"] -= 10
            traits["childish"] += 10
            traits["commitment issues"] -= 10
            traits["dislikes children"] -= 10
            traits["dramatic"] -= 10
            traits["flirty"] -= 10
            traits["gatherer"] += 10
            traits["great kisser"] -= 10
            traits["green thumb"] -= 10
            traits["handy"] += 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] += 10
            traits["natural born performer"] -= 10
            traits["natural cook"] -= 10
            traits["nurturing"] += 10
            traits["proper"] += 10
            traits["savvy sculptor"] -= 10
            traits["schmoozer"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unflirty"] += 10
        case "Music & Dance":
            traits["avant garde"] -= 10
            traits["born salesman"] -= 10
            traits["brooding"] -= 10
            traits["charismatic"] += 10
            traits["childish"] += 10
            traits["commitment issues"] += 10
            traits["dislikes children"] += 10
            traits["dramatic"] += 10
            traits["flirty"] += 10
            traits["gatherer"] -= 10
            traits["great kisser"] += 10
            traits["green thumb"] -= 10
            traits["handy"] -= 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] += 10
            traits["natural born performer"] += 10
            traits["natural cook"] -= 10
            traits["nurturing"] -= 10
            traits["proper"] += 10
            traits["savvy sculptor"] -= 10
            traits["schmoozer"] += 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unflirty"] -= 10
        case "Nature":
            traits["avant garde"] -= 10
            traits["born salesman"] -= 10
            traits["brooding"] += 10
            traits["charismatic"] -= 10
            traits["childish"] += 10
            traits["commitment issues"] -= 10
            traits["dislikes children"] -= 10
            traits["dramatic"] -= 10
            traits["flirty"] -= 10
            traits["gatherer"] += 10
            traits["great kisser"] -= 10
            traits["green thumb"] += 10
            traits["handy"] += 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] -= 10
            traits["natural born performer"] -= 10
            traits["natural cook"] += 10
            traits["nurturing"] += 10
            traits["proper"] += 10
            traits["savvy sculptor"] -= 10
            traits["schmoozer"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unflirty"] += 10
        case "Science":
            traits["avant garde"] -= 10
            traits["born salesman"] -= 10
            traits["brooding"] += 10
            traits["charismatic"] -= 10
            traits["childish"] -= 10
            traits["commitment issues"] -= 10
            traits["dislikes children"] += 10
            traits["dramatic"] -= 10
            traits["flirty"] -= 10
            traits["gatherer"] += 10
            traits["great kisser"] -= 10
            traits["green thumb"] += 10
            traits["handy"] += 10
            traits["hopeless romantic"] -= 10
            traits["irresistible"] -= 10
            traits["natural born performer"] -= 10
            traits["natural cook"] += 10
            traits["nurturing"] -= 10
            traits["proper"] += 10
            traits["savvy sculptor"] -= 10
            traits["schmoozer"] -= 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unflirty"] += 10
        case "Sports":
            traits["avant garde"] -= 10
            traits["born salesman"] -= 10
            traits["brooding"] += 10
            traits["charismatic"] += 10
            traits["childish"] += 10
            traits["commitment issues"] += 10
            traits["dislikes children"] -= 10
            traits["dramatic"] -= 10
            traits["flirty"] -= 10
            traits["gatherer"] -= 10
            traits["great kisser"] += 10
            traits["green thumb"] -= 10
            traits["handy"] -= 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] += 10
            traits["natural born performer"] += 10
            traits["natural cook"] -= 10
            traits["nurturing"] += 10
            traits["proper"] -= 10
            traits["savvy sculptor"] -= 10
            traits["schmoozer"] += 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unflirty"] += 10
        case "Tinkering":
            traits["avant garde"] -= 10
            traits["born salesman"] += 10
            traits["brooding"] += 10
            traits["charismatic"] += 10
            traits["childish"] += 10
            traits["commitment issues"] -= 10
            traits["dislikes children"] -= 10
            traits["dramatic"] -= 10
            traits["flirty"] -= 10
            traits["gatherer"] += 10
            traits["great kisser"] -= 10
            traits["green thumb"] -= 10
            traits["handy"] += 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] += 10
            traits["natural born performer"] -= 10
            traits["natural cook"] -= 10
            traits["nurturing"] += 10
            traits["proper"] += 10
            traits["savvy sculptor"] -= 10
            traits["schmoozer"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unflirty"] += 10
