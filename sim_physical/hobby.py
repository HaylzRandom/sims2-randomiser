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
            traits["absent-minded"] -= 20
            traits["artistic"] += 20
            traits["athletic"] -= 20
            traits["brave"] -= 20
            traits["clumsy"] += 20
            traits["couch potato"] -= 20
            traits["disciplined"] -= 20
            traits["easily impressed"] += 20
            traits["eccentric"] -= 20
            traits["evil"] -= 20
            traits["excitable"] += 20
            traits["friendly"] += 20
            traits["genius"] -= 20
            traits["good"] += 20
            traits["grumpy"] -= 20
            traits["hates the outdoors"] += 20
            traits["heavy sleeper"] -= 20
            traits["insane"] -= 20
            traits["light sleeper"] += 20
            traits["loner"] -= 20
            traits["loves the cold"] += 20
            traits["loves the heat"] -= 20
            traits["loves the outdoors"] -= 20
            traits["neurotic"] -= 20
            traits["perceptive"] += 20
            traits["sailor"] -= 20
            traits["slob"] -= 20
            traits["virtuoso"] -= 20
        case "Cuisine":
            traits["absent-minded"] -= 20
            traits["artistic"] -= 20
            traits["athletic"] -= 20
            traits["brave"] += 20
            traits["clumsy"] -= 20
            traits["couch potato"] += 20
            traits["disciplined"] -= 20
            traits["easily impressed"] -= 20
            traits["eccentric"] -= 20
            traits["evil"] -= 20
            traits["excitable"] -= 20
            traits["friendly"] += 20
            traits["genius"] += 20
            traits["good"] += 20
            traits["grumpy"] -= 20
            traits["hates the outdoors"] += 20
            traits["heavy sleeper"] += 20
            traits["insane"] -= 20
            traits["light sleeper"] -= 20
            traits["loner"] += 20
            traits["loves the cold"] += 20
            traits["loves the heat"] -= 20
            traits["loves the outdoors"] -= 20
            traits["neurotic"] -= 20
            traits["perceptive"] += 20
            traits["sailor"] -= 20
            traits["slob"] -= 20
            traits["virtuoso"] -= 20
        case "Film & Literature":
            traits["absent-minded"] += 20
            traits["artistic"] -= 20
            traits["athletic"] -= 20
            traits["brave"] += 20
            traits["clumsy"] += 20
            traits["couch potato"] += 20
            traits["disciplined"] -= 20
            traits["easily impressed"] += 20
            traits["eccentric"] += 20
            traits["evil"] += 20
            traits["excitable"] += 20
            traits["friendly"] += 20
            traits["genius"] -= 20
            traits["good"] += 20
            traits["grumpy"] += 20
            traits["hates the outdoors"] += 20
            traits["heavy sleeper"] += 20
            traits["insane"] += 20
            traits["light sleeper"] -= 20
            traits["loner"] += 20
            traits["loves the cold"] += 20
            traits["loves the heat"] -= 20
            traits["loves the outdoors"] -= 20
            traits["neurotic"] += 20
            traits["perceptive"] -= 20
            traits["sailor"] -= 20
            traits["slob"] += 20
            traits["virtuoso"] -= 20
        case "Fitness":
            traits["absent-minded"] -= 20
            traits["artistic"] -= 20
            traits["athletic"] += 20
            traits["brave"] += 20
            traits["clumsy"] -= 20
            traits["couch potato"] -= 20
            traits["disciplined"] += 20
            traits["easily impressed"] -= 20
            traits["eccentric"] -= 20
            traits["evil"] += 20
            traits["excitable"] -= 20
            traits["friendly"] -= 20
            traits["genius"] -= 20
            traits["good"] += 20
            traits["grumpy"] -= 20
            traits["hates the outdoors"] -= 20
            traits["heavy sleeper"] -= 20
            traits["insane"] += 20
            traits["light sleeper"] += 20
            traits["loner"] -= 20
            traits["loves the cold"] -= 20
            traits["loves the heat"] += 20
            traits["loves the outdoors"] += 20
            traits["neurotic"] -= 20
            traits["perceptive"] -= 20
            traits["sailor"] += 20
            traits["slob"] -= 20
            traits["virtuoso"] -= 20
        case "Games":
            traits["absent-minded"] += 20
            traits["artistic"] -= 20
            traits["athletic"] -= 20
            traits["brave"] -= 20
            traits["clumsy"] += 20
            traits["couch potato"] += 20
            traits["disciplined"] -= 20
            traits["easily impressed"] += 20
            traits["eccentric"] += 20
            traits["evil"] -= 20
            traits["excitable"] += 20
            traits["friendly"] += 20
            traits["genius"] += 20
            traits["good"] += 20
            traits["grumpy"] -= 20
            traits["hates the outdoors"] += 20
            traits["heavy sleeper"] += 20
            traits["insane"] += 20
            traits["light sleeper"] -= 20
            traits["loner"] -= 20
            traits["loves the cold"] += 20
            traits["loves the heat"] -= 20
            traits["loves the outdoors"] -= 20
            traits["neurotic"] += 20
            traits["perceptive"] += 20
            traits["sailor"] -= 20
            traits["slob"] += 20
            traits["virtuoso"] -= 20
        case "Music & Dance":
            traits["absent-minded"] -= 20
            traits["artistic"] -= 20
            traits["athletic"] -= 20
            traits["brave"] += 20
            traits["clumsy"] += 20
            traits["couch potato"] -= 20
            traits["disciplined"] -= 20
            traits["easily impressed"] += 20
            traits["eccentric"] -= 20
            traits["evil"] -= 20
            traits["excitable"] += 20
            traits["friendly"] += 20
            traits["genius"] += 20
            traits["good"] += 20
            traits["grumpy"] -= 20
            traits["hates the outdoors"] -= 20
            traits["heavy sleeper"] -= 20
            traits["insane"] -= 20
            traits["light sleeper"] += 20
            traits["loner"] -= 20
            traits["loves the cold"] += 20
            traits["loves the heat"] += 20
            traits["loves the outdoors"] += 20
            traits["neurotic"] += 20
            traits["perceptive"] += 20
            traits["sailor"] -= 20
            traits["slob"] -= 20
            traits["virtuoso"] += 20
        case "Nature":
            traits["absent-minded"] += 20
            traits["artistic"] -= 20
            traits["athletic"] += 20
            traits["brave"] += 20
            traits["clumsy"] += 20
            traits["couch potato"] -= 20
            traits["disciplined"] += 20
            traits["easily impressed"] += 20
            traits["eccentric"] -= 20
            traits["evil"] -= 20
            traits["excitable"] += 20
            traits["friendly"] += 20
            traits["genius"] -= 20
            traits["good"] += 20
            traits["grumpy"] += 20
            traits["hates the outdoors"] -= 20
            traits["heavy sleeper"] -= 20
            traits["insane"] += 20
            traits["light sleeper"] += 20
            traits["loner"] += 20
            traits["loves the cold"] -= 20
            traits["loves the heat"] += 20
            traits["loves the outdoors"] += 20
            traits["neurotic"] -= 20
            traits["perceptive"] -= 20
            traits["sailor"] -= 20
            traits["slob"] += 20
            traits["virtuoso"] -= 20
        case "Science":
            traits["absent-minded"] -= 20
            traits["artistic"] -= 20
            traits["athletic"] -= 20
            traits["brave"] -= 20
            traits["clumsy"] -= 20
            traits["couch potato"] -= 20
            traits["disciplined"] += 20
            traits["easily impressed"] -= 20
            traits["eccentric"] += 20
            traits["evil"] += 20
            traits["excitable"] -= 20
            traits["friendly"] -= 20
            traits["genius"] += 20
            traits["good"] -= 20
            traits["grumpy"] += 20
            traits["hates the outdoors"] += 20
            traits["heavy sleeper"] -= 20
            traits["insane"] += 20
            traits["light sleeper"] += 20
            traits["loner"] += 20
            traits["loves the cold"] += 20
            traits["loves the heat"] -= 20
            traits["loves the outdoors"] -= 20
            traits["neurotic"] += 20
            traits["perceptive"] += 20
            traits["sailor"] -= 20
            traits["slob"] -= 20
            traits["virtuoso"] -= 20
        case "Sports":
            traits["absent-minded"] += 20
            traits["artistic"] -= 20
            traits["athletic"] += 20
            traits["brave"] += 20
            traits["clumsy"] += 20
            traits["couch potato"] += 20
            traits["disciplined"] -= 20
            traits["easily impressed"] += 20
            traits["eccentric"] += 20
            traits["evil"] -= 20
            traits["excitable"] += 20
            traits["friendly"] += 20
            traits["genius"] -= 20
            traits["good"] += 20
            traits["grumpy"] -= 20
            traits["hates the outdoors"] -= 20
            traits["heavy sleeper"] += 20
            traits["insane"] += 20
            traits["light sleeper"] -= 20
            traits["loner"] -= 20
            traits["loves the cold"] -= 20
            traits["loves the heat"] += 20
            traits["loves the outdoors"] += 20
            traits["neurotic"] -= 20
            traits["perceptive"] -= 20
            traits["sailor"] -= 20
            traits["slob"] += 20
            traits["virtuoso"] -= 20
        case "Tinkering":
            traits["absent-minded"] -= 20
            traits["artistic"] -= 20
            traits["athletic"] -= 20
            traits["brave"] -= 20
            traits["clumsy"] -= 20
            traits["couch potato"] -= 20
            traits["disciplined"] += 20
            traits["easily impressed"] -= 20
            traits["eccentric"] += 20
            traits["evil"] += 20
            traits["excitable"] -= 20
            traits["friendly"] -= 20
            traits["genius"] += 20
            traits["good"] -= 20
            traits["grumpy"] += 20
            traits["hates the outdoors"] -= 20
            traits["heavy sleeper"] += 20
            traits["insane"] += 20
            traits["light sleeper"] -= 20
            traits["loner"] += 20
            traits["loves the cold"] -= 20
            traits["loves the heat"] += 20
            traits["loves the outdoors"] += 20
            traits["neurotic"] += 20
            traits["perceptive"] -= 20
            traits["sailor"] -= 20
            traits["slob"] += 20
            traits["virtuoso"] -= 20


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
            traits["adventurous"] += 20
            traits["ambitious"] += 20
            traits["angler"] -= 20
            traits["animal lover"] += 20
            traits["bookworm"] -= 20
            traits["bot fan"] -= 20
            traits["can't stand art"] -= 20
            traits["cat person"] -= 20
            traits["computer whiz"] -= 20
            traits["coward"] -= 20
            traits["daredevil"] += 20
            traits["diva"] += 20
            traits["dog person"] -= 20
            traits["eco-friendly"] -= 20
            traits["equestrian"] += 20
            traits["family-oriented"] -= 20
            traits["frugal"] += 20
            traits["good sense of humour"] += 20
            traits["hot-headed"] += 20
            traits["hydrophobic"] -= 20
            traits["inappropriate"] -= 20
            traits["kleptomaniac"] += 20
            traits["loser"] += 20
            traits["loves to swim"] += 20
            traits["lucky"] += 20
            traits["mean-spirited"] += 20
            traits["mooch"] += 20
            traits["neat"] -= 20
            traits["never nude"] -= 20
            traits["night owl"] += 20
            traits["no sense of humour"] -= 20
            traits["over-emotional"] += 20
            traits["party animal"] += 20
            traits["perfectionist"] += 20
            traits["photographer's eye"] += 20
            traits["rebellious"] += 20
            traits["shy"] -= 20
            traits["snob"] += 20
            traits["star quality"] += 20
            traits["supernatural fan"] -= 20
            traits["technophobe"] += 20
            traits["unlucky"] -= 20
            traits["unstable"] += 20
            traits["vegetarian"] -= 20
            traits["vehicle enthusiast"] -= 20
            traits["workaholic"] += 20
        case "Cuisine":
            traits["adventurous"] += 20
            traits["ambitious"] -= 20
            traits["angler"] += 20
            traits["animal lover"] += 20
            traits["bookworm"] += 20
            traits["bot fan"] -= 20
            traits["can't stand art"] += 20
            traits["cat person"] += 20
            traits["computer whiz"] -= 20
            traits["coward"] += 20
            traits["daredevil"] -= 20
            traits["diva"] += 20
            traits["dog person"] += 20
            traits["eco-friendly"] += 20
            traits["equestrian"] -= 20
            traits["family-oriented"] += 20
            traits["frugal"] += 20
            traits["good sense of humour"] += 20
            traits["hot-headed"] -= 20
            traits["hydrophobic"] += 20
            traits["inappropriate"] -= 20
            traits["kleptomaniac"] -= 20
            traits["loser"] += 20
            traits["loves to swim"] -= 20
            traits["lucky"] -= 20
            traits["mean-spirited"] -= 20
            traits["mooch"] -= 20
            traits["neat"] += 20
            traits["never nude"] += 20
            traits["night owl"] -= 20
            traits["no sense of humour"] -= 20
            traits["over-emotional"] += 20
            traits["party animal"] += 20
            traits["perfectionist"] += 20
            traits["photographer's eye"] += 20
            traits["rebellious"] -= 20
            traits["shy"] += 20
            traits["snob"] += 20
            traits["star quality"] += 20
            traits["supernatural fan"] += 20
            traits["technophobe"] -= 20
            traits["unlucky"] += 20
            traits["unstable"] -= 20
            traits["vegetarian"] += 20
            traits["vehicle enthusiast"] -= 20
            traits["workaholic"] -= 20
        case "Film & Literature":
            traits["adventurous"] -= 20
            traits["ambitious"] += 20
            traits["angler"] -= 20
            traits["animal lover"] += 20
            traits["bookworm"] += 20
            traits["bot fan"] += 20
            traits["can't stand art"] += 20
            traits["cat person"] += 20
            traits["computer whiz"] += 20
            traits["coward"] += 20
            traits["daredevil"] -= 20
            traits["diva"] += 20
            traits["dog person"] += 20
            traits["eco-friendly"] -= 20
            traits["equestrian"] -= 20
            traits["family-oriented"] += 20
            traits["frugal"] += 20
            traits["good sense of humour"] += 20
            traits["hot-headed"] += 20
            traits["hydrophobic"] -= 20
            traits["inappropriate"] += 20
            traits["kleptomaniac"] += 20
            traits["loser"] += 20
            traits["loves to swim"] -= 20
            traits["lucky"] += 20
            traits["mean-spirited"] += 20
            traits["mooch"] -= 20
            traits["neat"] -= 20
            traits["never nude"] += 20
            traits["night owl"] += 20
            traits["no sense of humour"] -= 20
            traits["over-emotional"] += 20
            traits["party animal"] -= 20
            traits["perfectionist"] -= 20
            traits["photographer's eye"] -= 20
            traits["rebellious"] -= 20
            traits["shy"] += 20
            traits["snob"] -= 20
            traits["star quality"] += 20
            traits["supernatural fan"] += 20
            traits["technophobe"] -= 20
            traits["unlucky"] -= 20
            traits["unstable"] -= 20
            traits["vegetarian"] -= 20
            traits["vehicle enthusiast"] -= 20
            traits["workaholic"] -= 20
        case "Fitness":
            traits["adventurous"] += 20
            traits["ambitious"] += 20
            traits["angler"] -= 20
            traits["animal lover"] -= 20
            traits["bookworm"] -= 20
            traits["bot fan"] -= 20
            traits["can't stand art"] -= 20
            traits["cat person"] -= 20
            traits["computer whiz"] -= 20
            traits["coward"] -= 20
            traits["daredevil"] += 20
            traits["diva"] += 20
            traits["dog person"] -= 20
            traits["eco-friendly"] -= 20
            traits["equestrian"] += 20
            traits["family-oriented"] -= 20
            traits["frugal"] -= 20
            traits["good sense of humour"] -= 20
            traits["hot-headed"] += 20
            traits["hydrophobic"] -= 20
            traits["inappropriate"] += 20
            traits["kleptomaniac"] += 20
            traits["loser"] -= 20
            traits["loves to swim"] += 20
            traits["lucky"] += 20
            traits["mean-spirited"] += 20
            traits["mooch"] -= 20
            traits["neat"] -= 20
            traits["never nude"] -= 20
            traits["night owl"] -= 20
            traits["no sense of humour"] += 20
            traits["over-emotional"] -= 20
            traits["party animal"] += 20
            traits["perfectionist"] += 20
            traits["photographer's eye"] -= 20
            traits["rebellious"] += 20
            traits["shy"] -= 20
            traits["snob"] -= 20
            traits["star quality"] += 20
            traits["supernatural fan"] -= 20
            traits["technophobe"] += 20
            traits["unlucky"] -= 20
            traits["unstable"] += 20
            traits["vegetarian"] += 20
            traits["vehicle enthusiast"] -= 20
            traits["workaholic"] -= 20
        case "Games":
            traits["adventurous"] -= 20
            traits["ambitious"] -= 20
            traits["angler"] -= 20
            traits["animal lover"] += 20
            traits["bookworm"] += 20
            traits["bot fan"] += 20
            traits["can't stand art"] -= 20
            traits["cat person"] -= 20
            traits["computer whiz"] += 20
            traits["coward"] -= 20
            traits["daredevil"] += 20
            traits["diva"] -= 20
            traits["dog person"] += 20
            traits["eco-friendly"] -= 20
            traits["equestrian"] -= 20
            traits["family-oriented"] += 20
            traits["frugal"] -= 20
            traits["good sense of humour"] += 20
            traits["hot-headed"] += 20
            traits["hydrophobic"] += 20
            traits["inappropriate"] += 20
            traits["kleptomaniac"] += 20
            traits["loser"] += 20
            traits["loves to swim"] -= 20
            traits["lucky"] -= 20
            traits["mean-spirited"] += 20
            traits["mooch"] -= 20
            traits["neat"] += 20
            traits["never nude"] += 20
            traits["night owl"] += 20
            traits["no sense of humour"] -= 20
            traits["over-emotional"] -= 20
            traits["party animal"] -= 20
            traits["perfectionist"] -= 20
            traits["photographer's eye"] -= 20
            traits["rebellious"] -= 20
            traits["shy"] += 20
            traits["snob"] -= 20
            traits["star quality"] -= 20
            traits["supernatural fan"] += 20
            traits["technophobe"] -= 20
            traits["unlucky"] += 20
            traits["unstable"] += 20
            traits["vegetarian"] -= 20
            traits["vehicle enthusiast"] -= 20
            traits["workaholic"] -= 20
        case "Music & Dance":
            traits["adventurous"] -= 20
            traits["ambitious"] += 20
            traits["angler"] -= 20
            traits["animal lover"] += 20
            traits["bookworm"] -= 20
            traits["bot fan"] -= 20
            traits["can't stand art"] -= 20
            traits["cat person"] -= 20
            traits["computer whiz"] -= 20
            traits["coward"] -= 20
            traits["daredevil"] += 20
            traits["diva"] += 20
            traits["dog person"] -= 20
            traits["eco-friendly"] -= 20
            traits["equestrian"] += 20
            traits["family-oriented"] -= 20
            traits["frugal"] += 20
            traits["good sense of humour"] += 20
            traits["hot-headed"] += 20
            traits["hydrophobic"] -= 20
            traits["inappropriate"] += 20
            traits["kleptomaniac"] -= 20
            traits["loser"] -= 20
            traits["loves to swim"] -= 20
            traits["lucky"] += 20
            traits["mean-spirited"] -= 20
            traits["mooch"] -= 20
            traits["neat"] -= 20
            traits["never nude"] -= 20
            traits["night owl"] -= 20
            traits["no sense of humour"] -= 20
            traits["over-emotional"] += 20
            traits["party animal"] += 20
            traits["perfectionist"] -= 20
            traits["photographer's eye"] -= 20
            traits["rebellious"] += 20
            traits["shy"] -= 20
            traits["snob"] += 20
            traits["star quality"] += 20
            traits["supernatural fan"] -= 20
            traits["technophobe"] += 20
            traits["unlucky"] -= 20
            traits["unstable"] += 20
            traits["vegetarian"] -= 20
            traits["vehicle enthusiast"] -= 20
            traits["workaholic"] -= 20
        case "Nature":
            traits["adventurous"] -= 20
            traits["ambitious"] -= 20
            traits["angler"] += 20
            traits["animal lover"] += 20
            traits["bookworm"] -= 20
            traits["bot fan"] -= 20
            traits["can't stand art"] += 20
            traits["cat person"] += 20
            traits["computer whiz"] -= 20
            traits["coward"] += 20
            traits["daredevil"] -= 20
            traits["diva"] -= 20
            traits["dog person"] += 20
            traits["eco-friendly"] += 20
            traits["equestrian"] += 20
            traits["family-oriented"] += 20
            traits["frugal"] -= 20
            traits["good sense of humour"] += 20
            traits["hot-headed"] -= 20
            traits["hydrophobic"] -= 20
            traits["inappropriate"] -= 20
            traits["kleptomaniac"] -= 20
            traits["loser"] += 20
            traits["loves to swim"] += 20
            traits["lucky"] -= 20
            traits["mean-spirited"] -= 20
            traits["mooch"] -= 20
            traits["neat"] -= 20
            traits["never nude"] -= 20
            traits["night owl"] -= 20
            traits["no sense of humour"] -= 20
            traits["over-emotional"] += 20
            traits["party animal"] -= 20
            traits["perfectionist"] -= 20
            traits["photographer's eye"] -= 20
            traits["rebellious"] -= 20
            traits["shy"] += 20
            traits["snob"] -= 20
            traits["star quality"] -= 20
            traits["supernatural fan"] += 20
            traits["technophobe"] += 20
            traits["unlucky"] += 20
            traits["unstable"] += 20
            traits["vegetarian"] += 20
            traits["vehicle enthusiast"] -= 20
            traits["workaholic"] -= 20
        case "Science":
            traits["adventurous"] -= 20
            traits["ambitious"] -= 20
            traits["angler"] += 20
            traits["animal lover"] -= 20
            traits["bookworm"] += 20
            traits["bot fan"] += 20
            traits["can't stand art"] += 20
            traits["cat person"] += 20
            traits["computer whiz"] += 20
            traits["coward"] += 20
            traits["daredevil"] -= 20
            traits["diva"] -= 20
            traits["dog person"] -= 20
            traits["eco-friendly"] -= 20
            traits["equestrian"] -= 20
            traits["family-oriented"] -= 20
            traits["frugal"] -= 20
            traits["good sense of humour"] -= 20
            traits["hot-headed"] += 20
            traits["hydrophobic"] += 20
            traits["inappropriate"] += 20
            traits["kleptomaniac"] += 20
            traits["loser"] += 20
            traits["loves to swim"] -= 20
            traits["lucky"] -= 20
            traits["mean-spirited"] += 20
            traits["mooch"] -= 20
            traits["neat"] += 20
            traits["never nude"] += 20
            traits["night owl"] += 20
            traits["no sense of humour"] += 20
            traits["over-emotional"] -= 20
            traits["party animal"] -= 20
            traits["perfectionist"] += 20
            traits["photographer's eye"] -= 20
            traits["rebellious"] -= 20
            traits["shy"] += 20
            traits["snob"] += 20
            traits["star quality"] -= 20
            traits["supernatural fan"] += 20
            traits["technophobe"] -= 20
            traits["unlucky"] += 20
            traits["unstable"] += 20
            traits["vegetarian"] -= 20
            traits["vehicle enthusiast"] += 20
            traits["workaholic"] -= 20
        case "Sports":
            traits["adventurous"] += 20
            traits["ambitious"] += 20
            traits["angler"] -= 20
            traits["animal lover"] += 20
            traits["bookworm"] -= 20
            traits["bot fan"] -= 20
            traits["can't stand art"] -= 20
            traits["cat person"] -= 20
            traits["computer whiz"] -= 20
            traits["coward"] -= 20
            traits["daredevil"] += 20
            traits["diva"] += 20
            traits["dog person"] += 20
            traits["eco-friendly"] -= 20
            traits["equestrian"] += 20
            traits["family-oriented"] -= 20
            traits["frugal"] -= 20
            traits["good sense of humour"] += 20
            traits["hot-headed"] -= 20
            traits["hydrophobic"] -= 20
            traits["inappropriate"] += 20
            traits["kleptomaniac"] += 20
            traits["loser"] += 20
            traits["loves to swim"] += 20
            traits["lucky"] += 20
            traits["mean-spirited"] += 20
            traits["mooch"] -= 20
            traits["neat"] -= 20
            traits["never nude"] -= 20
            traits["night owl"] -= 20
            traits["no sense of humour"] -= 20
            traits["over-emotional"] += 20
            traits["party animal"] += 20
            traits["perfectionist"] -= 20
            traits["photographer's eye"] -= 20
            traits["rebellious"] += 20
            traits["shy"] -= 20
            traits["snob"] -= 20
            traits["star quality"] -= 20
            traits["supernatural fan"] -= 20
            traits["technophobe"] -= 20
            traits["unlucky"] += 20
            traits["unstable"] += 20
            traits["vegetarian"] -= 20
            traits["vehicle enthusiast"] -= 20
            traits["workaholic"] -= 20
        case "Tinkering":
            traits["adventurous"] -= 20
            traits["ambitious"] -= 20
            traits["angler"] -= 20
            traits["animal lover"] -= 20
            traits["bookworm"] += 20
            traits["bot fan"] += 20
            traits["can't stand art"]
            traits["cat person"] += 20
            traits["computer whiz"] += 20
            traits["coward"] += 20
            traits["daredevil"] -= 20
            traits["diva"] -= 20
            traits["dog person"] += 20
            traits["eco-friendly"] -= 20
            traits["equestrian"] -= 20
            traits["family-oriented"] += 20
            traits["frugal"] += 20
            traits["good sense of humour"] -= 20
            traits["hot-headed"] += 20
            traits["hydrophobic"] += 20
            traits["inappropriate"] -= 20
            traits["kleptomaniac"] += 20
            traits["loser"] += 20
            traits["loves to swim"] -= 20
            traits["lucky"] -= 20
            traits["mean-spirited"] -= 20
            traits["mooch"] -= 20
            traits["neat"] -= 20
            traits["never nude"] += 20
            traits["night owl"] -= 20
            traits["no sense of humour"] += 20
            traits["over-emotional"] -= 20
            traits["party animal"] -= 20
            traits["perfectionist"] += 20
            traits["photographer's eye"] -= 20
            traits["rebellious"] += 20
            traits["shy"] += 20
            traits["snob"] -= 20
            traits["star quality"] -= 20
            traits["supernatural fan"] -= 20
            traits["technophobe"] -= 20
            traits["unlucky"] += 20
            traits["unstable"] -= 20
            traits["vegetarian"] -= 20
            traits["vehicle enthusiast"] += 20
            traits["workaholic"] -= 20


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
            traits["avant garde"] += 20
            traits["born salesman"] += 20
            traits["brooding"] += 20
            traits["charismatic"] += 20
            traits["childish"] -= 20
            traits["commitment issues"] += 20
            traits["dislikes children"] += 20
            traits["dramatic"] += 20
            traits["flirty"] += 20
            traits["gatherer"] -= 20
            traits["great kisser"] += 20
            traits["green thumb"] -= 20
            traits["handy"] -= 20
            traits["hopeless romantic"] += 20
            traits["irresistible"] += 20
            traits["natural born performer"] -= 20
            traits["natural cook"] -= 20
            traits["nurturing"] -= 20
            traits["proper"] -= 20
            traits["savvy sculptor"] += 20
            traits["schmoozer"] -= 20
            traits["social butterfly"] += 20
            traits["socially awkward"] += 20
            traits["supernatural sceptic"] += 20
            traits["unflirty"] -= 20
        case "Cuisine":
            traits["avant garde"] -= 20
            traits["born salesman"] -= 20
            traits["brooding"] += 20
            traits["charismatic"] -= 20
            traits["childish"] -= 20
            traits["commitment issues"] += 20
            traits["dislikes children"] -= 20
            traits["dramatic"] -= 20
            traits["flirty"] += 20
            traits["gatherer"] += 20
            traits["great kisser"] -= 20
            traits["green thumb"] += 20
            traits["handy"] += 20
            traits["hopeless romantic"] += 20
            traits["irresistible"] += 20
            traits["natural born performer"] -= 20
            traits["natural cook"] += 20
            traits["nurturing"] += 20
            traits["proper"] += 20
            traits["savvy sculptor"] -= 20
            traits["schmoozer"] -= 20
            traits["social butterfly"] -= 20
            traits["socially awkward"] += 20
            traits["supernatural sceptic"] -= 20
            traits["unflirty"] += 20
        case "Film & Literature":
            traits["avant garde"] -= 20
            traits["born salesman"] -= 20
            traits["brooding"] -= 20
            traits["charismatic"] += 20
            traits["childish"] -= 20
            traits["commitment issues"] -= 20
            traits["dislikes children"] -= 20
            traits["dramatic"] += 20
            traits["flirty"] -= 20
            traits["gatherer"] -= 20
            traits["great kisser"] -= 20
            traits["green thumb"] -= 20
            traits["handy"] -= 20
            traits["hopeless romantic"] += 20
            traits["irresistible"] -= 20
            traits["natural born performer"] += 20
            traits["natural cook"] -= 20
            traits["nurturing"] += 20
            traits["proper"] += 20
            traits["savvy sculptor"] -= 20
            traits["schmoozer"] += 20
            traits["social butterfly"] -= 20
            traits["socially awkward"] += 20
            traits["supernatural sceptic"] -= 20
            traits["unflirty"] += 20
        case "Fitness":
            traits["avant garde"] -= 20
            traits["born salesman"] += 20
            traits["brooding"] -= 20
            traits["charismatic"] += 20
            traits["childish"] -= 20
            traits["commitment issues"] += 20
            traits["dislikes children"] += 20
            traits["dramatic"] += 20
            traits["flirty"] += 20
            traits["gatherer"] -= 20
            traits["great kisser"] += 20
            traits["green thumb"] -= 20
            traits["handy"] -= 20
            traits["hopeless romantic"] -= 20
            traits["irresistible"] += 20
            traits["natural born performer"] += 20
            traits["natural cook"] -= 20
            traits["nurturing"] -= 20
            traits["proper"] -= 20
            traits["savvy sculptor"] -= 20
            traits["schmoozer"] += 20
            traits["social butterfly"] += 20
            traits["socially awkward"] -= 20
            traits["supernatural sceptic"] += 20
            traits["unflirty"] -= 20
        case "Games":
            traits["avant garde"] -= 20
            traits["born salesman"] -= 20
            traits["brooding"] += 20
            traits["charismatic"] -= 20
            traits["childish"] += 20
            traits["commitment issues"] -= 20
            traits["dislikes children"] -= 20
            traits["dramatic"] -= 20
            traits["flirty"] -= 20
            traits["gatherer"] += 20
            traits["great kisser"] -= 20
            traits["green thumb"] -= 20
            traits["handy"] += 20
            traits["hopeless romantic"] += 20
            traits["irresistible"] += 20
            traits["natural born performer"] -= 20
            traits["natural cook"] -= 20
            traits["nurturing"] += 20
            traits["proper"] += 20
            traits["savvy sculptor"] -= 20
            traits["schmoozer"] -= 20
            traits["social butterfly"] += 20
            traits["socially awkward"] += 20
            traits["supernatural sceptic"] -= 20
            traits["unflirty"] += 20
        case "Music & Dance":
            traits["avant garde"] -= 20
            traits["born salesman"] -= 20
            traits["brooding"] -= 20
            traits["charismatic"] += 20
            traits["childish"] += 20
            traits["commitment issues"] += 20
            traits["dislikes children"] += 20
            traits["dramatic"] += 20
            traits["flirty"] += 20
            traits["gatherer"] -= 20
            traits["great kisser"] += 20
            traits["green thumb"] -= 20
            traits["handy"] -= 20
            traits["hopeless romantic"] += 20
            traits["irresistible"] += 20
            traits["natural born performer"] += 20
            traits["natural cook"] -= 20
            traits["nurturing"] -= 20
            traits["proper"] += 20
            traits["savvy sculptor"] -= 20
            traits["schmoozer"] += 20
            traits["social butterfly"] += 20
            traits["socially awkward"] -= 20
            traits["supernatural sceptic"] += 20
            traits["unflirty"] -= 20
        case "Nature":
            traits["avant garde"] -= 20
            traits["born salesman"] -= 20
            traits["brooding"] += 20
            traits["charismatic"] -= 20
            traits["childish"] += 20
            traits["commitment issues"] -= 20
            traits["dislikes children"] -= 20
            traits["dramatic"] -= 20
            traits["flirty"] -= 20
            traits["gatherer"] += 20
            traits["great kisser"] -= 20
            traits["green thumb"] += 20
            traits["handy"] += 20
            traits["hopeless romantic"] += 20
            traits["irresistible"] -= 20
            traits["natural born performer"] -= 20
            traits["natural cook"] += 20
            traits["nurturing"] += 20
            traits["proper"] += 20
            traits["savvy sculptor"] -= 20
            traits["schmoozer"] -= 20
            traits["social butterfly"] += 20
            traits["socially awkward"] += 20
            traits["supernatural sceptic"] -= 20
            traits["unflirty"] += 20
        case "Science":
            traits["avant garde"] -= 20
            traits["born salesman"] -= 20
            traits["brooding"] += 20
            traits["charismatic"] -= 20
            traits["childish"] -= 20
            traits["commitment issues"] -= 20
            traits["dislikes children"] += 20
            traits["dramatic"] -= 20
            traits["flirty"] -= 20
            traits["gatherer"] += 20
            traits["great kisser"] -= 20
            traits["green thumb"] += 20
            traits["handy"] += 20
            traits["hopeless romantic"] -= 20
            traits["irresistible"] -= 20
            traits["natural born performer"] -= 20
            traits["natural cook"] += 20
            traits["nurturing"] -= 20
            traits["proper"] += 20
            traits["savvy sculptor"] -= 20
            traits["schmoozer"] -= 20
            traits["social butterfly"] -= 20
            traits["socially awkward"] += 20
            traits["supernatural sceptic"] -= 20
            traits["unflirty"] += 20
        case "Sports":
            traits["avant garde"] -= 20
            traits["born salesman"] -= 20
            traits["brooding"] += 20
            traits["charismatic"] += 20
            traits["childish"] += 20
            traits["commitment issues"] += 20
            traits["dislikes children"] -= 20
            traits["dramatic"] -= 20
            traits["flirty"] -= 20
            traits["gatherer"] -= 20
            traits["great kisser"] += 20
            traits["green thumb"] -= 20
            traits["handy"] -= 20
            traits["hopeless romantic"] += 20
            traits["irresistible"] += 20
            traits["natural born performer"] += 20
            traits["natural cook"] -= 20
            traits["nurturing"] += 20
            traits["proper"] -= 20
            traits["savvy sculptor"] -= 20
            traits["schmoozer"] += 20
            traits["social butterfly"] += 20
            traits["socially awkward"] -= 20
            traits["supernatural sceptic"] += 20
            traits["unflirty"] += 20
        case "Tinkering":
            traits["avant garde"] -= 20
            traits["born salesman"] += 20
            traits["brooding"] += 20
            traits["charismatic"] += 20
            traits["childish"] += 20
            traits["commitment issues"] -= 20
            traits["dislikes children"] -= 20
            traits["dramatic"] -= 20
            traits["flirty"] -= 20
            traits["gatherer"] += 20
            traits["great kisser"] -= 20
            traits["green thumb"] -= 20
            traits["handy"] += 20
            traits["hopeless romantic"] += 20
            traits["irresistible"] += 20
            traits["natural born performer"] -= 20
            traits["natural cook"] -= 20
            traits["nurturing"] += 20
            traits["proper"] += 20
            traits["savvy sculptor"] -= 20
            traits["schmoozer"] -= 20
            traits["social butterfly"] += 20
            traits["socially awkward"] -= 20
            traits["supernatural sceptic"] += 20
            traits["unflirty"] += 20
