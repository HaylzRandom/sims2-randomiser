from globals import TURN_ONS_OFF
import inquirer


def get_turn_ons_off():
    turn_on_questions = [
        inquirer.Checkbox(
            "turn_ons", message="What are your turn ons?", choices=TURN_ONS_OFF
        )
    ]

    turn_on_answers = inquirer.prompt(turn_on_questions)

    turn_off_questions = [
        inquirer.List(
            "turn_offs", message="What is your turn off?", choices=TURN_ONS_OFF
        )
    ]

    turn_off_answer = inquirer.prompt(turn_off_questions)

    # Check if any input is None and handle it
    if turn_on_answers is None:
        turn_on_answers = {"turn_ons": []}
    if turn_off_answer is None:
        turn_off_answer = {"turn_offs": ""}

    return turn_on_answers, turn_off_answer


def get_trait_turn_off(turn_off, traits):
    # Turn Off
    match (turn_off):
        case "Adventurous":
            traits["absent-minded"] += 10
            traits["adventurous"] -= 10
            traits["ambitious"] -= 10
            traits["athletic"] -= 10
            traits["born salesman"] -= 10
            traits["brave"] -= 10
            traits["brooding"] += 10
            traits["charismatic"] -= 10
            traits["clumsy"] += 10
            traits["commitment issues"] += 10
            traits["couch potato"] += 10
            traits["coward"] += 10
            traits["daredevil"] -= 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["easily impressed"] += 10
            traits["evil"] -= 10
            traits["excitable"] -= 10
            traits["flirty"] += 10
            traits["friendly"] += 10
            traits["gatherer"] -= 10
            traits["grumpy"] += 10
            traits["hates the outdoors"] += 10
            traits["heavy sleeper"] += 10
            traits["hydrophobic"] += 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["irresistible"] += 10
            traits["kleptomaniac"] -= 10
            traits["light sleeper"] -= 10
            traits["loner"] += 10
            traits["loser"] += 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["lucky"] -= 10
            traits["neurotic"] += 10
            traits["never nude"] += 10
            traits["shy"] += 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["supernatural fan"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unlucky"] += 10
            traits["unstable"] += 10
        case "Alien":
            traits["absent-minded"] += 10
            traits["adventurous"] -= 10
            traits["ambitious"] -= 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["brave"] -= 10
            traits["brooding"] += 10
            traits["commitment issues"] += 10
            traits["coward"] -= 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["evil"] += 10
            traits["flirty"] += 10
            traits["grumpy"] += 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["irresistible"] += 10
            traits["mean-spirited"] += 10
            traits["night owl"] -= 10
            traits["proper"] += 10
            traits["rebellious"] += 10
            traits["shy"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["supernatural fan"] -= 10
            traits["supernatural sceptic"] += 10
        case "Animal Lover":
            traits["animal lover"] -= 10
            traits["cat person"] -= 10
            traits["dog person"] -= 10
            traits["equestrian"] -= 10
            traits["evil"] += 10
            traits["family-oriented"] -= 10
            traits["grumpy"] += 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["kleptomaniac"] += 10
            traits["neat"] += 10
            traits["socially awkward"] += 10
        case "Artistic":
            traits["absent-minded"] += 10
            traits["ambitious"] -= 10
            traits["artistic"] -= 10
            traits["avant garde"] -= 10
            traits["brooding"] += 10
            traits["can't stand art"] += 10
            traits["eccentric"] += 10
            traits["evil"] += 10
            traits["photographer's eye"] -= 10
            traits["savvy sculptor"] -= 10
            traits["star quality"] -= 10
            traits["virtuoso"] -= 10
        case "Athletic":
            traits["ambitious"] -= 10
            traits["athletic"] -= 10
            traits["daredevil"] -= 10
            traits["disciplined"] -= 10
            traits["equestrian"] -= 10
            traits["hydrophobic"] += 10
            traits["loves to swim"] -= 10
            traits["sailor"] -= 10
        case "Business Shark":
            traits["absent-minded"] += 10
            traits["ambitious"] -= 10
            traits["born salesman"] -= 10
            traits["easily impressed"] += 10
            traits["excitable"] += 10
            traits["family-oriented"] += 10
            traits["friendly"] += 10
            traits["good"] += 10
            traits["good sense of humour"] += 10
            traits["grumpy"] -= 10
            traits["heavy sleeper"] += 10
            traits["light sleeper"] -= 10
            traits["mean-spirited"] -= 10
            traits["nurturing"] += 10
            traits["schmoozer"] -= 10
            traits["shy"] += 10
            traits["snob"] -= 10
            traits["star quality"] -= 10
            traits["workaholic"] -= 10
        case "Charismatic":
            traits["brooding"] += 10
            traits["charismatic"] -= 10
            traits["diva"] -= 10
            traits["dramatic"] -= 10
            traits["excitable"] -= 10
            traits["flirty"] -= 10
            traits["friendly"] -= 10
            traits["good"] -= 10
            traits["good sense of humour"] -= 10
            traits["grumpy"] += 10
            traits["hopeless romantic"] -= 10
            traits["hot-headed"] += 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["irresistible"] -= 10
            traits["light sleeper"] -= 10
            traits["loner"] += 10
            traits["loser"] += 10
            traits["mean-spirited"] += 10
            traits["natural born performer"] -= 10
            traits["no sense of humour"] += 10
            traits["rebellious"] += 10
            traits["schmoozer"] -= 10
            traits["shy"] += 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["star quality"] -= 10
        case "Cultured":
            traits["absent-minded"] += 10
            traits["artistic"] -= 10
            traits["avant garde"] -= 10
            traits["bookworm"] -= 10
            traits["born salesman"] += 10
            traits["bot fan"] += 10
            traits["can't stand art"] += 10
            traits["couch potato"] -= 10
            traits["diva"] -= 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["photographer's eye"] -= 10
            traits["savvy sculptor"] -= 10
            traits["snob"] += 10
            traits["technophobe"] += 10
            traits["virtuoso"] -= 10
        case "Expressive":
            traits["adventurous"] -= 10
            traits["artistic"] -= 10
            traits["avant garde"] -= 10
            traits["bookworm"] += 10
            traits["brooding"] += 10
            traits["charismatic"] -= 10
            traits["childish"] -= 10
            traits["diva"] -= 10
            traits["dramatic"] -= 10
            traits["excitable"] -= 10
            traits["grumpy"] += 10
            traits["loner"] += 10
            traits["loser"] += 10
            traits["mean-spirited"] += 10
            traits["neurotic"] += 10
            traits["no sense of humour"] += 10
            traits["over-emotional"] -= 10
            traits["party animal"] -= 10
            traits["rebellious"] += 10
            traits["shy"] += 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
        case "Fatness":
            traits["adventurous"] += 10
            traits["athletic"] += 10
            traits["couch potato"] -= 10
            traits["disciplined"] += 10
            traits["equestrian"] += 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["hates the outdoors"] -= 10
            traits["heavy sleeper"] -= 10
            traits["light sleeper"] += 10
            traits["loves the outdoors"] += 10
            traits["loves to swim"] += 10
            traits["never nude"] -= 10
            traits["sailor"] += 10
            traits["slob"] -= 10
            traits["vegetarian"] += 10
        case "Fitness":
            traits["athletic"] -= 10
            traits["couch potato"] += 10
            traits["disciplined"] -= 10
            traits["hates the outdoors"] += 10
            traits["heavy sleeper"] += 10
            traits["hydrophobic"] += 10
            traits["light sleeper"] -= 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["loves to swim"] -= 10
            traits["sailor"] -= 10
            traits["vegetarian"] -= 10
        case "Foodie":
            traits["artistic"] -= 10
            traits["can't stand art"] += 10
            traits["clumsy"] += 10
            traits["evil"] += 10
            traits["family-oriented"] -= 10
            traits["grumpy"] += 10
            traits["hot-headed"] += 10
            traits["irresistible"] += 10
            traits["mean-spirited"] += 10
            traits["natural cook"] -= 10
            traits["neat"] -= 10
            traits["nurturing"] -= 10
            traits["rebellious"] += 10
            traits["slob"] += 10
            traits["snob"] -= 10
            traits["vegetarian"] -= 10
        case "Indoorsy":
            traits["adventurous"] += 10
            traits["angler"] += 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["computer whiz"] -= 10
            traits["couch potato"] -= 10
            traits["eco-friendly"] += 10
            traits["equestrian"] += 10
            traits["gatherer"] += 10
            traits["green thumb"] += 10
            traits["hates the outdoors"] -= 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["night owl"] -= 10
            traits["sailor"] += 10
            traits["shy"] -= 10
            traits["technophobe"] += 10
            traits["vehicle enthusiast"] += 10
        case "Infamous":
            traits["animal lover"] += 10
            traits["avant garde"] -= 10
            traits["charismatic"] += 10
            traits["childish"] += 10
            traits["commitment issues"] -= 10
            traits["coward"] += 10
            traits["daredevil"] -= 10
            traits["disciplined"] += 10
            traits["dislikes children"] -= 10
            traits["diva"] -= 10
            traits["dramatic"] -= 10
            traits["easily impressed"] += 10
            traits["evil"] -= 10
            traits["excitable"] -= 10
            traits["family-oriented"] += 10
            traits["friendly"] += 10
            traits["good"] += 10
            traits["hopeless romantic"] += 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["lucky"] += 10
            traits["mean-spirited"] -= 10
            traits["natural cook"] += 10
            traits["neat"] += 10
            traits["nurturing"] += 10
            traits["over-emotional"] += 10
            traits["perceptive"] += 10
            traits["perfectionist"] += 10
            traits["proper"] += 10
            traits["rebellious"] -= 10
            traits["shy"] += 10
            traits["supernatural fan"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unlucky"] -= 10
            traits["unstable"] -= 10
        case "Intellect":
            traits["absent-minded"] += 10
            traits["ambitious"] += 10
            traits["artistic"] += 10
            traits["bookworm"] -= 10
            traits["brooding"] -= 10
            traits["childish"] += 10
            traits["commitment issues"] += 10
            traits["computer whiz"] -= 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["easily impressed"] += 10
            traits["evil"] += 10
            traits["excitable"] += 10
            traits["genius"] -= 10
            traits["grumpy"] -= 10
            traits["hates the outdoors"] -= 10
            traits["hopeless romantic"] += 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["party animal"] += 10
            traits["perceptive"] -= 10
            traits["rebellious"] += 10
            traits["schmoozer"] += 10
            traits["shy"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["star quality"] += 10
            traits["supernatural fan"] -= 10
            traits["supernatural sceptic"] += 10
            traits["technophobe"] += 10
            traits["unflirty"] -= 10
            traits["unstable"] += 10
            traits["virtuoso"] += 10
            traits["workaholic"] += 10
        case "Introvert":
            traits["adventurous"] += 10
            traits["ambitious"] += 10
            traits["bookworm"] -= 10
            traits["born salesman"] += 10
            traits["bot fan"] -= 10
            traits["brave"] -= 10
            traits["brooding"] -= 10
            traits["cat person"] -= 10
            traits["charismatic"] += 10
            traits["commitment issues"] += 10
            traits["coward"] -= 10
            traits["diva"] += 10
            traits["dog person"] += 10
            traits["dramatic"] += 10
            traits["easily impressed"] += 10
            traits["excitable"] += 10
            traits["flirty"] += 10
            traits["genius"] += 10
            traits["good sense of humour"] += 10
            traits["grumpy"] -= 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] += 10
            traits["kleptomaniac"] += 10
            traits["loner"] -= 10
            traits["mooch"] += 10
            traits["natural born performer"] += 10
            traits["neurotic"] -= 10
            traits["never nude"] -= 10
            traits["night owl"] -= 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] += 10
            traits["rebellious"] += 10
            traits["shy"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["supernatural fan"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unflirty"] -= 10
            traits["workaholic"] += 10
        case "Laid Back":
            traits["adventurous"] += 10
            traits["athletic"] += 10
            traits["born salesman"] += 10
            traits["brave"] += 10
            traits["cat person"] -= 10
            traits["charismatic"] += 10
            traits["computer whiz"] -= 10
            traits["couch potato"] -= 10
            traits["diva"] += 10
            traits["dog person"] += 10
            traits["dramatic"] += 10
            traits["equestrian"] += 10
            traits["excitable"] += 10
            traits["gatherer"] += 10
            traits["green thumb"] += 10
            traits["handy"] += 10
            traits["hates the outdoors"] -= 10
            traits["hydrophobic"] -= 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["loves to swim"] += 10
            traits["mooch"] -= 10
            traits["natural born performer"] += 10
            traits["natural cook"] += 10
            traits["proper"] += 10
            traits["rebellious"] += 10
            traits["sailor"] += 10
            traits["slob"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["star quality"] += 10
            traits["technophobe"] += 10
            traits["vehicle enthusiast"] += 10
            traits["workaholic"] += 10
        case "Musical":
            traits["adventurous"] += 10
            traits["artistic"] += 10
            traits["avant garde"] += 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["brooding"] += 10
            traits["computer whiz"] += 10
            traits["couch potato"] += 10
            traits["diva"] -= 10
            traits["dramatic"] -= 10
            traits["eccentric"] += 10
            traits["evil"] += 10
            traits["genius"] += 10
            traits["irresistible"] -= 10
            traits["natural born performer"] -= 10
            traits["party animal"] -= 10
            traits["photographer's eye"] += 10
            traits["savvy sculptor"] += 10
            traits["star quality"] -= 10
            traits["virtuoso"] -= 10
            traits["workaholic"] += 10
        case "Occult":
            traits["absent-minded"] += 10
            traits["animal lover"] += 10
            traits["avant garde"] += 10
            traits["born salesman"] += 10
            traits["bot fan"] -= 10
            traits["brooding"] += 10
            traits["daredevil"] += 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["excitable"] += 10
            traits["grumpy"] += 10
            traits["hot-headed"] += 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["irresistible"] += 10
            traits["loser"] -= 10
            traits["night owl"] -= 10
            traits["nurturing"] += 10
            traits["proper"] += 10
            traits["schmoozer"] += 10
            traits["supernatural fan"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unlucky"] -= 10
            traits["unstable"] -= 10
            traits["workaholic"] += 10
        case "Outdoorsy":
            traits["absent-minded"] += 10
            traits["adventurous"] -= 10
            traits["angler"] -= 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["computer whiz"] += 10
            traits["couch potato"] += 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] -= 10
            traits["gatherer"] -= 10
            traits["green thumb"] -= 10
            traits["hates the outdoors"] += 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["loves to swim"] -= 10
            traits["sailor"] -= 10
            traits["shy"] += 10
            traits["technophobe"] -= 10
            traits["vehicle enthusiast"] -= 10
        case "Outgoing":
            traits["absent-minded"] += 10
            traits["ambitious"] -= 10
            traits["angler"] += 10
            traits["animal lover"] -= 10
            traits["bookworm"] += 10
            traits["born salesman"] -= 10
            traits["brave"] -= 10
            traits["brooding"] += 10
            traits["cat person"] += 10
            traits["charismatic"] -= 10
            traits["childish"] -= 10
            traits["clumsy"] += 10
            traits["commitment issues"] -= 10
            traits["coward"] += 10
            traits["diva"] -= 10
            traits["dog person"] -= 10
            traits["dramatic"] -= 10
            traits["excitable"] -= 10
            traits["flirty"] -= 10
            traits["genius"] += 10
            traits["good sense of humour"] -= 10
            traits["hopeless romantic"] -= 10
            traits["hot-headed"] += 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["irresistible"] -= 10
            traits["loner"] += 10
            traits["loser"] += 10
            traits["mean-spirited"] += 10
            traits["natural born performer"] -= 10
            traits["neurotic"] += 10
            traits["no sense of humour"] += 10
            traits["over-emotional"] -= 10
            traits["party animal"] -= 10
            traits["proper"] += 10
            traits["rebellious"] -= 10
            traits["schmoozer"] -= 10
            traits["shy"] += 10
            traits["snob"] += 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["star quality"] -= 10
            traits["unflirty"] += 10
            traits["unlucky"] += 10
            traits["unstable"] += 10
            traits["workaholic"] -= 10
        case "Plant Lover":
            traits["animal lover"] -= 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["cat person"] += 10
            traits["couch potato"] += 10
            traits["dog person"] -= 10
            traits["eco-friendly"] -= 10
            traits["gatherer"] -= 10
            traits["green thumb"] -= 10
            traits["hates the outdoors"] += 10
            traits["hydrophobic"] += 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["loves to swim"] -= 10
            traits["supernatural fan"] -= 10
            traits["supernatural sceptic"] += 10
            traits["vegetarian"] -= 10
        case "Rebellious":
            traits["absent-minded"] += 10
            traits["ambitious"] += 10
            traits["animal lover"] += 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["brooding"] += 10
            traits["cat person"] += 10
            traits["clumsy"] += 10
            traits["coward"] += 10
            traits["daredevil"] -= 10
            traits["diva"] -= 10
            traits["dog person"] += 10
            traits["dramatic"] -= 10
            traits["easily impressed"] += 10
            traits["eco-friendly"] += 10
            traits["equestrian"] += 10
            traits["evil"] -= 10
            traits["excitable"] += 10
            traits["flirty"] += 10
            traits["friendly"] += 10
            traits["frugal"] += 10
            traits["good"] += 10
            traits["good sense of humour"] += 10
            traits["grumpy"] -= 10
            traits["hot-headed"] -= 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["irresistible"] += 10
            traits["kleptomaniac"] -= 10
            traits["loner"] += 10
            traits["loser"] += 10
            traits["lucky"] += 10
            traits["natural born performer"] -= 10
            traits["neat"] += 10
            traits["proper"] += 10
            traits["rebellious"] -= 10
            traits["schmoozer"] -= 10
            traits["shy"] += 10
            traits["snob"] += 10
            traits["social butterfly"] += 10
            traits["socially awkward"] += 10
            traits["unflirty"] += 10
            traits["unlucky"] += 10
            traits["unstable"] -= 10
        case "Stylish":
            traits["absent-minded"] += 10
            traits["ambitious"] -= 10
            traits["angler"] += 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["charismatic"] -= 10
            traits["childish"] += 10
            traits["clumsy"] += 10
            traits["diva"] -= 10
            traits["dramatic"] -= 10
            traits["easily impressed"] += 10
            traits["eco-friendly"] += 10
            traits["evil"] -= 10
            traits["excitable"] += 10
            traits["family-oriented"] += 10
            traits["flirty"] -= 10
            traits["friendly"] += 10
            traits["frugal"] += 10
            traits["genius"] += 10
            traits["good"] += 10
            traits["hopeless romantic"] -= 10
            traits["irresistible"] -= 10
            traits["mooch"] += 10
            traits["natural born performer"] -= 10
            traits["over-emotional"] -= 10
            traits["party animal"] -= 10
            traits["perfectionist"] -= 10
            traits["photographer's eye"] -= 10
            traits["proper"] -= 10
            traits["schmoozer"] -= 10
            traits["shy"] += 10
            traits["snob"] -= 10
            traits["socially awkward"] += 10
            traits["star quality"] -= 10
            traits["unflirty"] += 10
            traits["unlucky"] += 10
            traits["workaholic"] += 10
        case "Technology":
            traits["ambitious"] += 10
            traits["artistic"] += 10
            traits["avant garde"] += 10
            traits["bookworm"] += 10
            traits["bot fan"] -= 10
            traits["brooding"] += 10
            traits["can't stand art"] -= 10
            traits["computer whiz"] -= 10
            traits["couch potato"] -= 10
            traits["green thumb"] += 10
            traits["grumpy"] += 10
            traits["handy"] -= 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["natural cook"] -= 10
            traits["photographer's eye"] -= 10
            traits["savvy sculptor"] += 10
            traits["technophobe"] += 10
            traits["vehicle enthusiast"] -= 10
            traits["virtuoso"] -= 10
        case "Tidy":
            traits["absent-minded"] += 10
            traits["angler"] += 10
            traits["animal lover"] += 10
            traits["cat person"] += 10
            traits["childish"] += 10
            traits["clumsy"] += 10
            traits["commitment issues"] += 10
            traits["dislikes children"] += 10
            traits["diva"] += 10
            traits["dog person"] -= 10
            traits["dramatic"] += 10
            traits["family-oriented"] -= 10
            traits["friendly"] -= 10
            traits["frugal"] -= 10
            traits["gatherer"] += 10
            traits["genius"] -= 10
            traits["green thumb"] += 10
            traits["grumpy"] += 10
            traits["heavy sleeper"] -= 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] += 10
            traits["kleptomaniac"] += 10
            traits["light sleeper"] += 10
            traits["lucky"] -= 10
            traits["mean-spirited"] += 10
            traits["mooch"] += 10
            traits["neat"] -= 10
            traits["never nude"] -= 10
            traits["night owl"] -= 10
            traits["nurturing"] -= 10
            traits["perfectionist"] -= 10
            traits["photographer's eye"] -= 10
            traits["proper"] -= 10
            traits["unlucky"] += 10
        case "Undead":
            traits["adventurous"] += 10
            traits["ambitious"] += 10
            traits["animal lover"] += 10
            traits["born salesman"] += 10
            traits["brave"] += 10
            traits["charismatic"] += 10
            traits["clumsy"] += 10
            traits["commitment issues"] += 10
            traits["coward"] += 10
            traits["disciplined"] += 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["easily impressed"] += 10
            traits["excitable"] += 10
            traits["flirty"] += 10
            traits["good sense of humour"] += 10
            traits["grumpy"] -= 10
            traits["hopeless romantic"] += 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["irresistible"] += 10
            traits["kleptomaniac"] -= 10
            traits["loner"] -= 10
            traits["loser"] -= 10
            traits["lucky"] += 10
            traits["night owl"] -= 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] += 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["supernatural fan"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unflirty"] -= 10
            traits["unlucky"] -= 10
        case "Well-Liked":
            traits["absent-minded"] -= 10
            traits["ambitious"] += 10
            traits["animal lover"] -= 10
            traits["brooding"] += 10
            traits["cat person"] -= 10
            traits["charismatic"] += 10
            traits["childish"] += 10
            traits["commitment issues"] += 10
            traits["daredevil"] += 10
            traits["dislikes children"] += 10
            traits["diva"] += 10
            traits["dog person"] -= 10
            traits["dramatic"] += 10
            traits["easily impressed"] -= 10
            traits["evil"] += 10
            traits["excitable"] -= 10
            traits["family-oriented"] -= 10
            traits["friendly"] -= 10
            traits["good"] -= 10
            traits["good sense of humour"] -= 10
            traits["grumpy"] += 10
            traits["hopeless romantic"] -= 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["irresistible"] += 10
            traits["kleptomaniac"] += 10
            traits["lucky"] += 10
            traits["mean-spirited"] += 10
            traits["mooch"] += 10
            traits["never nude"] -= 10
            traits["no sense of humour"] += 10
            traits["nurturing"] -= 10
            traits["proper"] -= 10
            traits["rebellious"] += 10
            traits["supernatural fan"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unflirty"] -= 10
            traits["unlucky"] -= 10


# def get_trait_turn_off_teen(turn_off, traits):
#     # Turn Off
#     match (turn_off):
#         case "Adventurous":
#             traits["coward"] -= 1
#             traits["loser"] -= 1
#         case "Alien":
#             traits["coward"] -= 1
#         case "Animal Lover":
#             print("Animal Lover")
#         case "Artistic":
#             traits["can't stand art"] -= 1
#             traits["eccentric"] -= 1
#             traits["handy"] -= 1
#             traits["vehicle enthusiast"] -= 1
#         case "Athletic":
#             traits["couch potato"] -= 1
#             traits["heavy sleeper"] -= 1
#             traits["never nude"] -= 1
#             traits["slob"] -= 1
#         case "Black Hair":
#             print("Black Hair")
#         case "Blonde Hair":
#             print("Blonde Hair")
#         case "Brown Hair":
#             print("Brown Hair")
#         case "Red Hair":
#             print("Red Hair")
#         case "Business Shark":
#             traits["bookworm"] -= 1
#             traits["disciplined"] -= 1
#             traits["easily impressed"] -= 1
#             traits["friendly"] -= 1
#             traits["great kisser"] -= 1
#             traits["natural cook"] -= 1
#             traits["nurturing"] -= 1
#             traits["virtuoso"] -= 1
#         case "Charismatic":
#             traits["angler"] -= 1
#             traits["bookworm"] -= 1
#             traits["computer whiz"] -= 1
#             traits["coward"] -= 1
#             traits["genius"] -= 1
#             traits["grumpy"] -= 1
#             traits["loner"] -= 1
#             traits["loser"] -= 1
#             traits["no sense of humour"] -= 1
#             traits["rebellious"] -= 1
#             traits["savvy sculptor"] -= 1
#             traits["shy"] -= 1
#             traits["unflirty"] -= 1
#             traits["unlucky"] -= 1
#         case "Cultured":
#             traits["absent-minded"] -= 1
#             traits["can't stand art"] -= 1
#             traits["inappropriate"] -= 1
#             traits["vehicle enthusiast"] -= 1
#         case "Expressive":
#             traits["angler"] -= 1
#             traits["computer whiz"] -= 1
#             traits["coward"] -= 1
#             traits["dislikes children"] -= 1
#             traits["evil"] -= 1
#             traits["frugal"] -= 1
#             traits["grumpy"] -= 1
#             traits["kleptomaniac"] -= 1
#             traits["light sleeper"] -= 1
#             traits["loner"] -= 1
#             traits["mean-spirited"] -= 1
#             traits["neurotic"] -= 1
#             traits["no sense of humour"] -= 1
#             traits["perceptive"] -= 1
#             traits["shy"] -= 1
#             traits["workaholic"] -= 1
#         case "Facial Hair":
#             print("Facial Hair")
#         case "Fatness":
#             traits["adventurous"] -= 1
#             traits["athletic"] -= 1
#             traits["disciplined"] -= 1
#             traits["light sleeper"] -= 1
#             traits["vegetarian"] -= 1
#         case "Fitness":
#             traits["couch potato"] -= 1
#             traits["hates the outdoors"] -= 1
#             traits["heavy sleeper"] -= 1
#             traits["never nude"] -= 1
#         case "Foodie":
#             print("Foodie")
#         case "Grey Hair":
#             print("Grey Hair")
#         case "Indoorsy":
#             traits["angler"] -= 1
#             traits["dramatic"] -= 1
#             traits["green thumb"] -= 1
#             traits["loves the outdoors"] -= 1
#         case "Infamous":
#             traits["artistic"] -= 1
#             traits["easily impressed"] -= 1
#             traits["eco-friendly"] -= 1
#             traits["family-oriented"] -= 1
#             traits["friendly"] -= 1
#             traits["good"] -= 1
#             traits["hopeless romantic"] -= 1
#             traits["lucky"] -= 1
#             traits["nurturing"] -= 1
#             traits["photographer's eye"] -= 1
#             traits["savvy sculptor"] -= 1
#             traits["vegetarian"] -= 1
#         case "Intellect":
#             traits["absent-minded"] -= 1
#             traits["easily impressed"] -= 1
#             traits["eco-friendly"] -= 1
#             traits["insane"] -= 1
#             traits["mooch"] -= 1
#             traits["star quality"] -= 1
#         case "Introvert":
#             traits["adventurous"] -= 1
#             traits["born salesman"] -= 1
#             traits["brave"] -= 1
#             traits["charismatic"] -= 1
#             traits["commitment issues"] -= 1
#             traits["daredevil"] -= 1
#             traits["dramatic"] -= 1
#             traits["eccentric"] -= 1
#             traits["excitable"] -= 1
#             traits["flirty"] -= 1
#             traits["good sense of humour"] -= 1
#             traits["great kisser"] -= 1
#             traits["hopeless romantic"] -= 1
#             traits["hot-headed"] -= 1
#             traits["inappropriate"] -= 1
#             traits["insane"] -= 1
#             traits["mooch"] -= 1
#             traits["over-emotional"] -= 1
#             traits["party animal"] -= 1
#             traits["schmoozer"] -= 1
#             traits["star quality"] -= 1
#         case "Laid Back":
#             traits["adventurous"] -= 1
#             traits["ambitious"] -= 1
#             traits["athletic"] -= 1
#             traits["born salesman"] -= 1
#             traits["brave"] -= 1
#             traits["charismatic"] -= 1
#             traits["daredevil"] -= 1
#             traits["disciplined"] -= 1
#             traits["green thumb"] -= 1
#             traits["handy"] -= 1
#             traits["light sleeper"] -= 1
#             traits["loves the outdoors"] -= 1
#             traits["natural cook"] -= 1
#             traits["neat"] -= 1
#             traits["perceptive"] -= 1
#             traits["perfectionist"] -= 1
#             traits["snob"] -= 1
#             traits["vegetarian"] -= 1
#             traits["workaholic"] -= 1
#         case "Musical":
#             traits["eccentric"] -= 1
#         case "Occult":
#             traits["coward"] -= 1
#             traits["hydrophobic"] -= 1
#         case "Outdoorsy":
#             traits["artistic"] -= 1
#             traits["hates the outdoors"] -= 1
#             traits["hydrophobic"] -= 1
#         case "Outgoing":
#             traits["ambitious"] -= 1
#             traits["kleptomaniac"] -= 1
#             traits["loner"] -= 1
#             traits["shy"] -= 1
#             traits["snob"] -= 1
#             traits["unflirty"] -= 1
#         case "Plant Lover":
#             traits["couch potato"] -= 1
#             traits["insane"] -= 1
#             traits["perfectionist"] -= 1
#             traits["snob"] -= 1
#         case "Rebellious":
#             traits["childish"] -= 1
#             traits["clumsy"] -= 1
#             traits["dramatic"] -= 1
#             traits["excitable"] -= 1
#             traits["genius"] -= 1
#             traits["good sense of humour"] -= 1
#             traits["green thumb"] -= 1
#             traits["natural cook"] -= 1
#             traits["neurotic"] -= 1
#             traits["nurturing"] -= 1
#             traits["over-emotional"] -= 1
#             traits["party animal"] -= 1
#             traits["perfectionist"] -= 1
#             traits["photographer's eye"] -= 1
#             traits["schmoozer"] -= 1
#             traits["vegetarian"] -= 1
#             traits["virtuoso"] -= 1
#         case "Stylish":
#             traits["frugal"] -= 1
#             traits["handy"] -= 1
#             traits["mooch"] -= 1
#             traits["unflirty"] -= 1
#             traits["vehicle enthusiast"] -= 1
#         case "Technology":
#             traits["eco-friendly"] -= 1
#             traits["technophobe"] -= 1
#         case "Tidy":
#             traits["clumsy"] -= 1
#             traits["couch potato"] -= 1
#             traits["slob"] -= 1
#             traits["unlucky"] -= 1
#         case "Undead":
#             traits["coward"] -= 1
#         case "Well-Liked":
#             traits["commitment issues"] -= 1
#             traits["dislikes children"] -= 1
#             traits["evil"] -= 1
#             traits["inappropriate"] -= 1
#             traits["kleptomaniac"] -= 1
#             traits["mean-spirited"] -= 1
#             traits["rebellious"] -= 1
#             traits["slob"] -= 1
#             traits["snob"] -= 1


# def get_trait_turn_off_adult(turn_off, traits):
#     # Turn Off
#     match (turn_off):
#         case "Adventurous":
#             traits["coward"] -= 1
#             traits["loser"] -= 1
#             traits["supernatural sceptic"] -= 1
#         case "Alien":
#             traits["coward"] -= 1
#             traits["supernatural sceptic"] -= 1
#         case "Animal Lover":
#             print("Animal Lover")
#         case "Artistic":
#             traits["can't stand art"] -= 1
#             traits["eccentric"] -= 1
#             traits["handy"] -= 1
#             traits["vehicle enthusiast"] -= 1
#         case "Athletic":
#             traits["couch potato"] -= 1
#             traits["heavy sleeper"] -= 1
#             traits["never nude"] -= 1
#             traits["slob"] -= 1
#             traits["unstable"] -= 1
#         case "Black Hair":
#             print("Black Hair")
#         case "Blonde Hair":
#             print("Blonde Hair")
#         case "Brown Hair":
#             print("Brown Hair")
#         case "Red Hair":
#             print("Red Hair")
#         case "Business Shark":
#             traits["bookworm"] -= 1
#             traits["cat person"] -= 1
#             traits["disciplined"] -= 1
#             traits["easily impressed"] -= 1
#             traits["equestrian"] -= 1
#             traits["friendly"] -= 1
#             traits["great kisser"] -= 1
#             traits["natural cook"] -= 1
#             traits["nurturing"] -= 1
#             traits["virtuoso"] -= 1
#         case "Charismatic":
#             traits["angler"] -= 1
#             traits["bookworm"] -= 1
#             traits["bot fan"] -= 1
#             traits["computer whiz"] -= 1
#             traits["coward"] -= 1
#             traits["genius"] -= 1
#             traits["grumpy"] -= 1
#             traits["loner"] -= 1
#             traits["loser"] -= 1
#             traits["night owl"] -= 1
#             traits["no sense of humour"] -= 1
#             traits["rebellious"] -= 1
#             traits["savvy sculptor"] -= 1
#             traits["shy"] -= 1
#             traits["socially awkward"] -= 1
#             traits["supernatural fan"] -= 1
#             traits["unflirty"] -= 1
#             traits["unlucky"] -= 1
#         case "Cultured":
#             traits["absent-minded"] -= 1
#             traits["can't stand art"] -= 1
#             traits["inappropriate"] -= 1
#             traits["vehicle enthusiast"] -= 1
#         case "Expressive":
#             traits["angler"] -= 1
#             traits["avant garde"] -= 1
#             traits["brooding"] -= 1
#             traits["computer whiz"] -= 1
#             traits["coward"] -= 1
#             traits["dislikes children"] -= 1
#             traits["evil"] -= 1
#             traits["frugal"] -= 1
#             traits["grumpy"] -= 1
#             traits["kleptomaniac"] -= 1
#             traits["light sleeper"] -= 1
#             traits["loner"] -= 1
#             traits["mean-spirited"] -= 1
#             traits["neurotic"] -= 1
#             traits["no sense of humour"] -= 1
#             traits["perceptive"] -= 1
#             traits["shy"] -= 1
#             traits["socially awkward"] -= 1
#             traits["supernatural sceptic"] -= 1
#             traits["workaholic"] -= 1
#         case "Facial Hair":
#             print("Facial Hair")
#         case "Fatness":
#             traits["adventurous"] -= 1
#             traits["athletic"] -= 1
#             traits["disciplined"] -= 1
#             traits["equestrian"] -= 1
#             traits["light sleeper"] -= 1
#             traits["sailor"] -= 1
#             traits["vegetarian"] -= 1
#         case "Fitness":
#             traits["couch potato"] -= 1
#             traits["hates the outdoors"] -= 1
#             traits["heavy sleeper"] -= 1
#             traits["never nude"] -= 1
#         case "Foodie":
#             print("Foodie")
#         case "Grey Hair":
#             print("Grey Hair")
#         case "Indoorsy":
#             traits["angler"] -= 1
#             traits["dramatic"] -= 1
#             traits["equestrian"] -= 1
#             traits["gatherer"] -= 1
#             traits["green thumb"] -= 1
#             traits["loves the heat"] -= 1
#             traits["loves the outdoors"] -= 1
#             traits["loves to swim"] -= 1
#             traits["sailor"] -= 1
#         case "Infamous":
#             traits["animal lover"] -= 1
#             traits["artistic"] -= 1
#             traits["dog person"] -= 1
#             traits["easily impressed"] -= 1
#             traits["eco-friendly"] -= 1
#             traits["equestrian"] -= 1
#             traits["family-oriented"] -= 1
#             traits["friendly"] -= 1
#             traits["good"] -= 1
#             traits["hopeless romantic"] -= 1
#             traits["lucky"] -= 1
#             traits["nurturing"] -= 1
#             traits["photographer's eye"] -= 1
#             traits["savvy sculptor"] -= 1
#             traits["social butterfly"] -= 1
#             traits["vegetarian"] -= 1
#         case "Intellect":
#             traits["absent-minded"] -= 1
#             traits["easily impressed"] -= 1
#             traits["eco-friendly"] -= 1
#             traits["insane"] -= 1
#             traits["irresistible"] -= 1
#             traits["mooch"] -= 1
#             traits["star quality"] -= 1
#         case "Introvert":
#             traits["adventurous"] -= 1
#             traits["animal lover"] -= 1
#             traits["born salesman"] -= 1
#             traits["brave"] -= 1
#             traits["charismatic"] -= 1
#             traits["commitment issues"] -= 1
#             traits["daredevil"] -= 1
#             traits["diva"] -= 1
#             traits["dog person"] -= 1
#             traits["dramatic"] -= 1
#             traits["eccentric"] -= 1
#             traits["excitable"] -= 1
#             traits["flirty"] -= 1
#             traits["good sense of humour"] -= 1
#             traits["great kisser"] -= 1
#             traits["hopeless romantic"] -= 1
#             traits["hot-headed"] -= 1
#             traits["inappropriate"] -= 1
#             traits["insane"] -= 1
#             traits["irresistible"] -= 1
#             traits["mooch"] -= 1
#             traits["natural born performer"] -= 1
#             traits["over-emotional"] -= 1
#             traits["party animal"] -= 1
#             traits["schmoozer"] -= 1
#             traits["social butterfly"] -= 1
#             traits["star quality"] -= 1
#         case "Laid Back":
#             traits["adventurous"] -= 1
#             traits["ambitious"] -= 1
#             traits["athletic"] -= 1
#             traits["avant garde"] -= 1
#             traits["born salesman"] -= 1
#             traits["brave"] -= 1
#             traits["charismatic"] -= 1
#             traits["daredevil"] -= 1
#             traits["disciplined"] -= 1
#             traits["equestrian"] -= 1
#             traits["green thumb"] -= 1
#             traits["handy"] -= 1
#             traits["irresistible"] -= 1
#             traits["light sleeper"] -= 1
#             traits["loves the heat"] -= 1
#             traits["loves the outdoors"] -= 1
#             traits["loves to swim"] -= 1
#             traits["natural born performer"] -= 1
#             traits["natural cook"] -= 1
#             traits["neat"] -= 1
#             traits["perceptive"] -= 1
#             traits["perfectionist"] -= 1
#             traits["proper"] -= 1
#             traits["sailor"] -= 1
#             traits["snob"] -= 1
#             traits["vegetarian"] -= 1
#             traits["workaholic"] -= 1
#         case "Musical":
#             traits["eccentric"] -= 1
#         case "Occult":
#             traits["coward"] -= 1
#             traits["diva"] -= 1
#             traits["hydrophobic"] -= 1
#             traits["supernatural sceptic"] -= 1
#         case "Outdoorsy":
#             traits["artistic"] -= 1
#             traits["bot fan"] -= 1
#             traits["hates the outdoors"] -= 1
#             traits["hydrophobic"] -= 1
#             traits["loves the cold"] -= 1
#             traits["night owl"] -= 1
#             traits["supernatural fan"] -= 1
#         case "Outgoing":
#             traits["ambitious"] -= 1
#             traits["cat person"] -= 1
#             traits["kleptomaniac"] -= 1
#             traits["loner"] -= 1
#             traits["shy"] -= 1
#             traits["snob"] -= 1
#             traits["unflirty"] -= 1
#         case "Plant Lover":
#             traits["couch potato"] -= 1
#             traits["gatherer"] -= 1
#             traits["insane"] -= 1
#             traits["perfectionist"] -= 1
#             traits["snob"] -= 1
#             traits["unstable"] -= 1
#         case "Rebellious":
#             traits["childish"] -= 1
#             traits["clumsy"] -= 1
#             traits["dog person"] -= 1
#             traits["dramatic"] -= 1
#             traits["excitable"] -= 1
#             traits["genius"] -= 1
#             traits["good sense of humour"] -= 1
#             traits["green thumb"] -= 1
#             traits["natural cook"] -= 1
#             traits["neurotic"] -= 1
#             traits["nurturing"] -= 1
#             traits["over-emotional"] -= 1
#             traits["party animal"] -= 1
#             traits["perfectionist"] -= 1
#             traits["photographer's eye"] -= 1
#             traits["schmoozer"] -= 1
#             traits["vegetarian"] -= 1
#             traits["virtuoso"] -= 1
#         case "Stylish":
#             traits["frugal"] -= 1
#             traits["handy"] -= 1
#             traits["mooch"] -= 1
#             traits["unflirty"] -= 1
#             traits["unstable"] -= 1
#             traits["vehicle enthusiast"] -= 1
#         case "Technology":
#             traits["eco-friendly"] -= 1
#             traits["technophobe"] += 1
#         case "Tidy":
#             traits["clumsy"] -= 1
#             traits["couch potato"] -= 1
#             traits["slob"] -= 1
#             traits["unlucky"] -= 1
#         case "Undead":
#             traits["coward"] -= 1
#             traits["diva"] -= 1
#             traits["proper"] -= 1
#             traits["supernatural sceptic"] -= 1
#         case "Well-Liked":
#             traits["commitment issues"] -= 1
#             traits["dislikes children"] -= 1
#             traits["diva"] -= 1
#             traits["evil"] -= 1
#             traits["inappropriate"] -= 1
#             traits["kleptomaniac"] -= 1
#             traits["mean-spirited"] -= 1
#             traits["rebellious"] -= 1
#             traits["slob"] -= 1
#             traits["snob"] -= 1


# TODO - Start Here
def get_trait_turn_on(turn_on, traits):
    # Turn On
    match (turn_on):
        case "Adventurous":
            traits["absent-minded"] -= 10
            traits["adventurous"] += 10
            traits["ambitious"] += 10
            traits["athletic"] += 10
            traits["born salesman"] += 10
            traits["brave"] += 10
            traits["brooding"] -= 10
            traits["charismatic"] += 10
            traits["clumsy"] -= 10
            traits["commitment issues"] -= 10
            traits["couch potato"] -= 10
            traits["coward"] -= 10
            traits["daredevil"] += 10
            traits["diva"] -= 10
            traits["dramatic"] -= 10
            traits["easily impressed"] -= 10
            traits["evil"] += 10
            traits["excitable"] += 10
            traits["flirty"] -= 10
            traits["friendly"] -= 10
            traits["gatherer"] += 10
            traits["grumpy"] -= 10
            traits["hates the outdoors"] -= 10
            traits["heavy sleeper"] -= 10
            traits["hydrophobic"] -= 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["irresistible"] -= 10
            traits["kleptomaniac"] += 10
            traits["light sleeper"] += 10
            traits["loner"] -= 10
            traits["loser"] -= 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["lucky"] += 10
            traits["neurotic"] -= 10
            traits["never nude"] -= 10
            traits["shy"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["supernatural fan"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unlucky"] -= 10
            traits["unstable"] -= 10
        case "Alien":
            traits["absent-minded"] -= 10
            traits["adventurous"] += 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["brave"] += 10
            traits["brooding"] -= 10
            traits["commitment issues"] -= 10
            traits["coward"] += 10
            traits["diva"] -= 10
            traits["dramatic"] -= 10
            traits["evil"] -= 10
            traits["flirty"] -= 10
            traits["grumpy"] -= 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["irresistible"] -= 10
            traits["night owl"] += 10
            traits["proper"] -= 10
            traits["rebellious"] -= 10
            traits["shy"] += 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["supernatural fan"] += 10
            traits["supernatural sceptic"] -= 10
        case "Animal Lover":
            traits["animal lover"] += 10
            traits["cat person"] += 10
            traits["dog person"] += 10
            traits["equestrian"] += 10
            traits["evil"] -= 10
            traits["family-oriented"] += 10
            traits["grumpy"] -= 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["kleptomaniac"] -= 10
            traits["neat"] -= 10
            traits["socially awkward"] -= 10
        case "Artistic":
            traits["absent-minded"] -= 10
            traits["ambitious"] += 10
            traits["artistic"] += 10
            traits["avant garde"] += 10
            traits["brooding"] -= 10
            traits["can't stand art"] -= 10
            traits["eccentric"] -= 10
            traits["evil"] -= 10
            traits["photographer's eye"] += 10
            traits["savvy sculptor"] += 10
            traits["star quality"] += 10
            traits["virtuoso"] += 10
        case "Athletic":
            traits["ambitious"] += 10
            traits["athletic"] += 10
            traits["daredevil"] += 10
            traits["disciplined"] += 10
            traits["equestrian"] += 10
            traits["hydrophobic"] -= 10
            traits["loves to swim"] += 10
            traits["sailor"] += 10
        case "Business Shark":
            traits["absent-minded"] -= 10
            traits["ambitious"] += 10
            traits["born salesman"] += 10
            traits["easily impressed"] -= 10
            traits["excitable"] -= 10
            traits["family-oriented"] -= 10
            traits["friendly"] -= 10
            traits["good"] -= 10
            traits["good sense of humour"] -= 10
            traits["grumpy"] += 10
            traits["heavy sleeper"] -= 10
            traits["light sleeper"] += 10
            traits["mean-spirited"] += 10
            traits["nurturing"] -= 10
            traits["schmoozer"] += 10
            traits["shy"] -= 10
            traits["snob"] += 10
            traits["star quality"] += 10
            traits["workaholic"] += 10
        case "Charismatic":
            traits["brooding"] -= 10
            traits["charismatic"] += 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["excitable"] += 10
            traits["flirty"] += 10
            traits["friendly"] += 10
            traits["good"] += 10
            traits["good sense of humour"] += 10
            traits["grumpy"] -= 10
            traits["hopeless romantic"] += 10
            traits["hot-headed"] -= 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["irresistible"] += 10
            traits["light sleeper"] += 10
            traits["loner"] -= 10
            traits["loser"] -= 10
            traits["mean-spirited"] -= 10
            traits["natural born performer"] += 10
            traits["no sense of humour"] -= 10
            traits["rebellious"] -= 10
            traits["schmoozer"] += 10
            traits["shy"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["star quality"] += 10
        case "Cultured":
            traits["absent-minded"] -= 10
            traits["artistic"] += 10
            traits["avant garde"] += 10
            traits["bookworm"] += 10
            traits["born salesman"] -= 10
            traits["bot fan"] -= 10
            traits["can't stand art"] -= 10
            traits["couch potato"] += 10
            traits["diva"] += 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["photographer's eye"] += 10
            traits["savvy sculptor"] += 10
            traits["snob"] -= 10
            traits["technophobe"] -= 10
            traits["virtuoso"] += 10
        case "Expressive":
            traits["adventurous"] += 10
            traits["artistic"] += 10
            traits["avant garde"] += 10
            traits["bookworm"] -= 10
            traits["brooding"] -= 10
            traits["charismatic"] += 10
            traits["childish"] += 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["excitable"] += 10
            traits["grumpy"] -= 10
            traits["loner"] -= 10
            traits["loser"] -= 10
            traits["mean-spirited"] -= 10
            traits["neurotic"] -= 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] += 10
            traits["rebellious"] -= 10
            traits["shy"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
        case "Fatness":
            traits["adventurous"] -= 10
            traits["couch potato"] += 10
            traits["disciplined"] -= 10
            traits["equestrian"] -= 10
            traits["hates the outdoors"] += 10
            traits["heavy sleeper"] += 10
            traits["light sleeper"] -= 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["loves to swim"] -= 10
            traits["never nude"] += 10
            traits["sailor"] -= 10
            traits["slob"] += 10
            traits["vegetarian"] -= 10
        case "Fitness":
            traits["couch potato"] -= 10
            traits["disciplined"] += 10
            traits["hates the outdoors"] -= 10
            traits["heavy sleeper"] -= 10
            traits["hydrophobic"] -= 10
            traits["light sleeper"] += 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["loves to swim"] += 10
            traits["sailor"] += 10
            traits["vegetarian"] += 10
        case "Foodie":
            traits["artistic"] += 10
            traits["can't stand art"] -= 10
            traits["clumsy"] -= 10
            traits["evil"] -= 10
            traits["family-oriented"] += 10
            traits["grumpy"] -= 10
            traits["hot-headed"] -= 10
            traits["irresistible"] -= 10
            traits["mean-spirited"] -= 10
            traits["natural cook"] += 10
            traits["neat"] += 10
            traits["nurturing"] += 10
            traits["rebellious"] -= 10
            traits["slob"] -= 10
            traits["snob"] += 10
            traits["vegetarian"] += 10
        case "Indoorsy":
            traits["adventurous"] -= 10
            traits["angler"] -= 10
            traits["bookworm"] += 10
            traits["bot fan"] += 10
            traits["computer whiz"] += 10
            traits["couch potato"] += 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] -= 10
            traits["gatherer"] -= 10
            traits["green thumb"] -= 10
            traits["hates the outdoors"] += 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["night owl"] += 10
            traits["sailor"] -= 10
            traits["shy"] += 10
            traits["technophobe"] -= 10
            traits["vehicle enthusiast"] -= 10
        case "Infamous":
            traits["animal lover"] -= 10
            traits["avant garde"] += 10
            traits["charismatic"] -= 10
            traits["childish"] -= 10
            traits["commitment issues"] += 10
            traits["coward"] -= 10
            traits["daredevil"] += 10
            traits["disciplined"] -= 10
            traits["dislikes children"] += 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["easily impressed"] -= 10
            traits["evil"] += 10
            traits["excitable"] += 10
            traits["family-oriented"] -= 10
            traits["friendly"] -= 10
            traits["good"] -= 10
            traits["good sense of humour"]
            traits["hopeless romantic"] -= 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["lucky"] -= 10
            traits["mean-spirited"] += 10
            traits["natural cook"] -= 10
            traits["neat"] -= 10
            traits["nurturing"] -= 10
            traits["over-emotional"] -= 10
            traits["perceptive"] -= 10
            traits["perfectionist"] -= 10
            traits["proper"] -= 10
            traits["rebellious"] += 10
            traits["shy"] -= 10
            traits["supernatural fan"] -= 10
            traits["supernatural sceptic"] += 10
            traits["unlucky"] += 10
            traits["unstable"] += 10
        case "Intellect":
            traits["absent-minded"] -= 10
            traits["ambitious"] -= 10
            traits["artistic"] -= 10
            traits["bookworm"] += 10
            traits["brooding"] += 10
            traits["childish"] -= 10
            traits["commitment issues"] -= 10
            traits["evil"] -= 10
            traits["excitable"] -= 10
            traits["genius"] += 10
            traits["grumpy"] += 10
            traits["hates the outdoors"] += 10
            traits["hopeless romantic"] -= 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["party animal"] -= 10
            traits["perceptive"] += 10
            traits["rebellious"] -= 10
            traits["schmoozer"] -= 10
            traits["shy"] += 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["star quality"] -= 10
            traits["supernatural fan"] += 10
            traits["supernatural sceptic"] -= 10
            traits["technophobe"] -= 10
            traits["unflirty"] += 10
            traits["unstable"] -= 10
            traits["virtuoso"] -= 10
            traits["workaholic"] -= 10
        case "Introvert":
            traits["adventurous"] -= 10
            traits["ambitious"] -= 10
            traits["bookworm"] += 10
            traits["born salesman"] -= 10
            traits["bot fan"] += 10
            traits["brave"] += 10
            traits["brooding"] += 10
            traits["cat person"] += 10
            traits["charismatic"] -= 10
            traits["commitment issues"] -= 10
            traits["coward"] += 10
            traits["diva"] -= 10
            traits["dog person"] -= 10
            traits["dramatic"] -= 10
            traits["easily impressed"] -= 10
            traits["excitable"] -= 10
            traits["flirty"] -= 10
            traits["genius"] -= 10
            traits["good sense of humour"] -= 10
            traits["grumpy"] += 10
            traits["hopeless romantic"] -= 10
            traits["irresistible"] -= 10
            traits["kleptomaniac"] -= 10
            traits["loner"] += 10
            traits["mooch"] -= 10
            traits["natural born performer"] -= 10
            traits["neurotic"] += 10
            traits["never nude"] += 10
            traits["night owl"] += 10
            traits["no sense of humour"] += 10
            traits["over-emotional"] -= 10
            traits["party animal"] -= 10
            traits["rebellious"] -= 10
            traits["shy"] += 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["supernatural fan"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unflirty"] += 10
            traits["workaholic"] -= 10
        case "Laid Back":
            traits["adventurous"] -= 10
            traits["athletic"] -= 10
            traits["born salesman"] -= 10
            traits["brave"] -= 10
            traits["cat person"] += 10
            traits["charismatic"] -= 10
            traits["computer whiz"] += 10
            traits["couch potato"] += 10
            traits["diva"] -= 10
            traits["dog person"] -= 10
            traits["dramatic"] -= 10
            traits["equestrian"] -= 10
            traits["excitable"] -= 10
            traits["gatherer"] -= 10
            traits["green thumb"] -= 10
            traits["handy"] -= 10
            traits["hates the outdoors"] += 10
            traits["hydrophobic"] += 10
            traits["loves the cold"] += 10
            traits["loves the heat"] -= 10
            traits["loves the outdoors"] -= 10
            traits["loves to swim"] -= 10
            traits["mooch"] += 10
            traits["natural born performer"] -= 10
            traits["natural cook"] -= 10
            traits["proper"] -= 10
            traits["rebellious"] -= 10
            traits["sailor"] -= 10
            traits["slob"] += 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["star quality"] -= 10
            traits["technophobe"] -= 10
            traits["vehicle enthusiast"] -= 10
            traits["workaholic"] -= 10
        case "Musical":
            traits["adventurous"] -= 10
            traits["artistic"] -= 10
            traits["avant garde"] -= 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["brooding"] -= 10
            traits["computer whiz"] -= 10
            traits["couch potato"] -= 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["eccentric"] -= 10
            traits["evil"] -= 10
            traits["genius"] -= 10
            traits["irresistible"] += 10
            traits["natural born performer"] += 10
            traits["party animal"] += 10
            traits["photographer's eye"] -= 10
            traits["savvy sculptor"] -= 10
            traits["star quality"] += 10
            traits["virtuoso"] += 10
            traits["workaholic"] -= 10
        case "Occult":
            traits["absent-minded"] -= 10
            traits["animal lover"] -= 10
            traits["avant garde"] -= 10
            traits["born salesman"] -= 10
            traits["bot fan"] += 10
            traits["brooding"] -= 10
            traits["daredevil"] -= 10
            traits["diva"] -= 10
            traits["dramatic"] -= 10
            traits["excitable"] -= 10
            traits["grumpy"] -= 10
            traits["hot-headed"] -= 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["irresistible"] -= 10
            traits["loser"] += 10
            traits["night owl"] += 10
            traits["nurturing"] -= 10
            traits["proper"] -= 10
            traits["schmoozer"] -= 10
            traits["supernatural fan"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unlucky"] += 10
            traits["unstable"] += 10
            traits["workaholic"] -= 10
        case "Outdoorsy":
            traits["absent-minded"] -= 10
            traits["adventurous"] += 10
            traits["angler"] += 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["computer whiz"] -= 10
            traits["couch potato"] -= 10
            traits["eco-friendly"] += 10
            traits["equestrian"] += 10
            traits["gatherer"] += 10
            traits["green thumb"] += 10
            traits["hates the outdoors"] -= 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["loves to swim"] += 10
            traits["sailor"] += 10
            traits["shy"] -= 10
            traits["technophobe"] += 10
            traits["vehicle enthusiast"] += 10
        case "Outgoing":
            traits["absent-minded"] -= 10
            traits["ambitious"] += 10
            traits["angler"] -= 10
            traits["animal lover"] += 10
            traits["bookworm"] -= 10
            traits["born salesman"] += 10
            traits["brave"] += 10
            traits["brooding"] -= 10
            traits["cat person"] -= 10
            traits["charismatic"] += 10
            traits["childish"] += 10
            traits["clumsy"] -= 10
            traits["commitment issues"] += 10
            traits["coward"] -= 10
            traits["diva"] += 10
            traits["dog person"] += 10
            traits["dramatic"] += 10
            traits["excitable"] += 10
            traits["flirty"] += 10
            traits["genius"] -= 10
            traits["good sense of humour"] += 10
            traits["hopeless romantic"] += 10
            traits["hot-headed"] -= 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["irresistible"] += 10
            traits["loner"] -= 10
            traits["loser"] -= 10
            traits["mean-spirited"] -= 10
            traits["natural born performer"] += 10
            traits["neurotic"] -= 10
            traits["no sense of humour"] -= 10
            traits["over-emotional"] += 10
            traits["party animal"] += 10
            traits["proper"] -= 10
            traits["rebellious"] += 10
            traits["schmoozer"] += 10
            traits["shy"] -= 10
            traits["snob"] -= 10
            traits["social butterfly"] += 10
            traits["socially awkward"] -= 10
            traits["star quality"] += 10
            traits["unflirty"] -= 10
            traits["unlucky"] -= 10
            traits["unstable"] -= 10
            traits["workaholic"] -= 10
        case "Plant Lover":
            traits["animal lover"] += 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["cat person"] -= 10
            traits["couch potato"] -= 10
            traits["dog person"] += 10
            traits["eco-friendly"] += 10
            traits["gatherer"] += 10
            traits["green thumb"] += 10
            traits["hates the outdoors"] -= 10
            traits["hydrophobic"] -= 10
            traits["loves the cold"] -= 10
            traits["loves the heat"] += 10
            traits["loves the outdoors"] += 10
            traits["loves to swim"] += 10
            traits["supernatural fan"] += 10
            traits["supernatural sceptic"] -= 10
            traits["vegetarian"] += 10
        case "Rebellious":
            traits["absent-minded"] -= 10
            traits["ambitious"] -= 10
            traits["animal lover"] -= 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["brooding"] -= 10
            traits["cat person"] -= 10
            traits["clumsy"] -= 10
            traits["coward"] -= 10
            traits["daredevil"] += 10
            traits["diva"] += 10
            traits["dog person"] -= 10
            traits["dramatic"] += 10
            traits["easily impressed"] -= 10
            traits["eco-friendly"] -= 10
            traits["equestrian"] -= 10
            traits["evil"] += 10
            traits["excitable"] -= 10
            traits["flirty"] -= 10
            traits["friendly"] -= 10
            traits["frugal"] -= 10
            traits["good"] -= 10
            traits["good sense of humour"] -= 10
            traits["grumpy"] += 10
            traits["hot-headed"] += 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["irresistible"] -= 10
            traits["kleptomaniac"] += 10
            traits["loner"] -= 10
            traits["loser"] -= 10
            traits["lucky"] -= 10
            traits["natural born performer"] += 10
            traits["neat"] -= 10
            traits["proper"] -= 10
            traits["rebellious"] += 10
            traits["schmoozer"] += 10
            traits["shy"] -= 10
            traits["snob"] -= 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] -= 10
            traits["unflirty"] -= 10
            traits["unlucky"] -= 10
            traits["unstable"] -= 10
        case "Stylish":
            traits["absent-minded"] -= 10
            traits["ambitious"] += 10
            traits["angler"] -= 10
            traits["bookworm"] -= 10
            traits["bot fan"] -= 10
            traits["charismatic"] += 10
            traits["childish"] -= 10
            traits["clumsy"] -= 10
            traits["diva"] += 10
            traits["dramatic"] += 10
            traits["easily impressed"] -= 10
            traits["eco-friendly"] -= 10
            traits["evil"] += 10
            traits["excitable"] -= 10
            traits["family-oriented"] -= 10
            traits["flirty"] += 10
            traits["friendly"] -= 10
            traits["frugal"] -= 10
            traits["genius"] -= 10
            traits["good"] -= 10
            traits["hopeless romantic"] += 10
            traits["irresistible"] += 10
            traits["mooch"] -= 10
            traits["natural born performer"] += 10
            traits["over-emotional"] += 10
            traits["party animal"] += 10
            traits["perfectionist"] += 10
            traits["photographer's eye"] += 10
            traits["proper"] += 10
            traits["schmoozer"] += 10
            traits["shy"] -= 10
            traits["snob"] += 10
            traits["socially awkward"] -= 10
            traits["star quality"] += 10
            traits["unflirty"] -= 10
            traits["unlucky"] -= 10
            traits["workaholic"] -= 10
        case "Technology":
            traits["ambitious"] -= 10
            traits["artistic"] -= 10
            traits["avant garde"] -= 10
            traits["bookworm"] -= 10
            traits["bot fan"] += 10
            traits["brooding"] -= 10
            traits["can't stand art"] += 10
            traits["computer whiz"] += 10
            traits["couch potato"] += 10
            traits["green thumb"] -= 10
            traits["grumpy"] -= 10
            traits["handy"] += 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["natural cook"] += 10
            traits["photographer's eye"] += 10
            traits["savvy sculptor"] -= 10
            traits["technophobe"] -= 10
            traits["vehicle enthusiast"] += 10
            traits["virtuoso"] += 10
        case "Tidy":
            traits["absent-minded"] -= 11
            traits["angler"] -= 10
            traits["animal lover"] -= 10
            traits["cat person"] -= 10
            traits["charismatic"]
            traits["childish"] -= 10
            traits["clumsy"] -= 10
            traits["commitment issues"] -= 10
            traits["dislikes children"] -= 10
            traits["diva"] -= 10
            traits["dog person"] -= 10
            traits["dramatic"] -= 10
            traits["family-oriented"] += 10
            traits["friendly"] += 10
            traits["frugal"] += 10
            traits["gatherer"] -= 10
            traits["genius"] += 10
            traits["green thumb"] -= 10
            traits["grumpy"] -= 10
            traits["heavy sleeper"] += 10
            traits["hopeless romantic"] -= 10
            traits["irresistible"] -= 10
            traits["kleptomaniac"] -= 10
            traits["light sleeper"] -= 10
            traits["lucky"] += 10
            traits["mean-spirited"] -= 10
            traits["mooch"] -= 10
            traits["neat"] += 10
            traits["never nude"] += 10
            traits["night owl"] += 10
            traits["nurturing"] += 10
            traits["perfectionist"] += 10
            traits["photographer's eye"] += 10
            traits["proper"] += 10
            traits["unlucky"] -= 10
        case "Undead":
            traits["adventurous"] -= 10
            traits["ambitious"] -= 10
            traits["animal lover"] -= 10
            traits["born salesman"] -= 10
            traits["brave"] -= 10
            traits["charismatic"] -= 10
            traits["clumsy"] -= 10
            traits["commitment issues"] -= 10
            traits["coward"] -= 10
            traits["disciplined"] -= 10
            traits["diva"] -= 10
            traits["dramatic"] -= 10
            traits["easily impressed"] -= 10
            traits["excitable"] -= 10
            traits["flirty"] -= 10
            traits["good sense of humour"] -= 10
            traits["grumpy"] += 10
            traits["hopeless romantic"] -= 10
            traits["inappropriate"] += 10
            traits["insane"] += 10
            traits["irresistible"] -= 10
            traits["kleptomaniac"] += 10
            traits["loner"] += 10
            traits["loser"] += 10
            traits["lucky"] -= 10
            traits["night owl"] += 10
            traits["no sense of humour"] += 10
            traits["over-emotional"] -= 10
            traits["party animal"] -= 10
            traits["social butterfly"] -= 10
            traits["socially awkward"] += 10
            traits["supernatural fan"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unflirty"] += 10
            traits["unlucky"] += 10
        case "Well-Liked":
            traits["absent-minded"] += 10
            traits["ambitious"] -= 10
            traits["animal lover"] += 10
            traits["brooding"] -= 10
            traits["cat person"] += 10
            traits["charismatic"] -= 10
            traits["childish"] -= 10
            traits["commitment issues"] -= 10
            traits["daredevil"] -= 10
            traits["dislikes children"] -= 10
            traits["diva"] -= 10
            traits["dog person"] += 10
            traits["dramatic"] -= 10
            traits["easily impressed"] += 10
            traits["evil"] -= 10
            traits["excitable"] += 10
            traits["family-oriented"] += 10
            traits["friendly"] += 10
            traits["good"] += 10
            traits["good sense of humour"] += 10
            traits["grumpy"] -= 10
            traits["hopeless romantic"] += 10
            traits["inappropriate"] -= 10
            traits["insane"] -= 10
            traits["irresistible"] -= 10
            traits["kleptomaniac"] -= 10
            traits["lucky"] -= 10
            traits["mean-spirited"] -= 10
            traits["mooch"] -= 10
            traits["never nude"] += 10
            traits["no sense of humour"] -= 10
            traits["nurturing"] += 10
            traits["proper"] += 10
            traits["rebellious"] -= 10
            traits["supernatural fan"] += 10
            traits["supernatural sceptic"] -= 10
            traits["unflirty"] += 10
            traits["unlucky"] += 10


# def get_trait_turn_on_teen(turn_on, traits):
#     # Turn On
#     match (turn_on):
#         case "Adventurous":
#             traits["adventurous"] += 1
#             traits["brave"] += 1
#             traits["daredevil"] += 1
#         case "Alien":
#             print("No Trait")
#         case "Animal Lover":
#             print("No Trait")
#         case "Artistic":
#             traits["artistic"] += 1
#             traits["loner"] += 1
#             traits["perceptive"] += 1
#             traits["photographer's eye"] += 1
#             traits["savvy sculptor"] += 1
#             traits["technophobe"] += 1
#         case "Athletic":
#             traits["adventurous"] += 1
#             traits["athletic"] += 1
#             traits["daredevil"] += 1
#             traits["disciplined"] += 1
#             traits["light sleeper"] += 1
#             traits["loves the outdoors"] += 1
#             traits["vegetarian"] += 1
#         case "Black Hair":
#             print("No Trait")
#         case "Blonde Hair":
#             print("No Trait")
#         case "Brown Hair":
#             print("No Trait")
#         case "Red Hair":
#             print("No Trait")
#         case "Business Shark":
#             traits["ambitious"] += 1
#             traits["born salesman"] += 1
#             traits["frugal"] += 1
#             traits["grumpy"] += 1
#             traits["hot-headed"] += 1
#             traits["mooch"] += 1
#             traits["schmoozer"] += 1
#             traits["workaholic"] += 1
#         case "Charismatic":
#             traits["ambitious"] += 1
#             traits["born salesman"] += 1
#             traits["charismatic"] += 1
#             traits["commitment issues"] += 1
#             traits["flirty"] += 1
#             traits["good sense of humour"] += 1
#             traits["great kisser"] += 1
#             traits["hopeless romantic"] += 1
#             traits["party animal"] += 1
#             traits["schmoozer"] += 1
#             traits["star quality"] += 1
#             traits["virtuoso"] += 1
#         case "Cultured":
#             traits["bookworm"] += 1
#             traits["eccentric"] += 1
#             traits["loner"] += 1
#             traits["over-emotional"] += 1
#             traits["savvy sculptor"] += 1
#         case "Expressive":
#             traits["artistic"] += 1
#             traits["charismatic"] += 1
#             traits["childish"] += 1
#             traits["daredevil"] += 1
#             traits["dramatic"] += 1
#             traits["easily impressed"] += 1
#             traits["eco-friendly"] += 1
#             traits["excitable"] += 1
#             traits["inappropriate"] += 1
#             traits["insane"] += 1
#             traits["lucky"] += 1
#             traits["natural cook"] += 1
#             traits["over-emotional"] += 1
#             traits["savvy sculptor"] += 1
#             traits["unlucky"] += 1
#         case "Facial Hair":
#             print("No Trait")
#         case "Fatness":
#             traits["couch potato"] += 1
#             traits["hates the outdoors"] += 1
#             traits["heavy sleeper"] += 1
#             traits["never nude"] += 1
#             traits["slob"] += 1
#         case "Fitness":
#             traits["athletic"] += 1
#             traits["brave"] += 1
#             traits["disciplined"] += 1
#             traits["excitable"] += 1
#             traits["light sleeper"] += 1
#             traits["loves the outdoors"] += 1
#             traits["party animal"] += 1
#         case "Foodie":
#             traits["absent-minded"] += 1
#             traits["family-oriented"] += 1
#             traits["friendly"] += 1
#             traits["good"] += 1
#             traits["natural cook"] += 1
#             traits["nurturing"] += 1
#             traits["perfectionist"] += 1
#             traits["photographer's eye"] += 1
#             traits["technophobe"] += 1
#         case "Grey Hair":
#             print("No Trait")
#         case "Indoorsy":
#             traits["bookworm"] += 1
#             traits["computer whiz"] += 1
#             traits["coward"] += 1
#             traits["eccentric"] += 1
#             traits["hates the outdoors"] += 1
#             traits["hydrophobic"] += 1
#             traits["loner"] += 1
#             traits["neat"] += 1
#             traits["perfectionist"] += 1
#             traits["slob"] += 1
#         case "Infamous":
#             traits["commitment issues"] += 1
#             traits["dislikes children"] += 1
#             traits["dramatic"] += 1
#             traits["evil"] += 1
#             traits["inappropriate"] += 1
#             traits["kleptomaniac"] += 1
#             traits["mean-spirited"] += 1
#             traits["rebellious"] += 1
#             traits["snob"] += 1
#         case "Intellect":
#             traits["bookworm"] += 1
#             traits["can't stand art"] += 1
#             traits["eccentric"] += 1
#             traits["genius"] += 1
#             traits["handy"] += 1
#             traits["no sense of humour"] += 1
#             traits["vehicle enthusiast"] += 1
#         case "Introvert":
#             traits["angler"] += 1
#             traits["clumsy"] += 1
#             traits["computer whiz"] += 1
#             traits["coward"] += 1
#             traits["genius"] += 1
#             traits["grumpy"] += 1
#             traits["hates the outdoors"] += 1
#             traits["kleptomaniac"] += 1
#             traits["loner"] += 1
#             traits["mean-spirited"] += 1
#             traits["neurotic"] += 1
#             traits["never nude"] += 1
#             traits["no sense of humour"] += 1
#             traits["perceptive"] += 1
#             traits["savvy sculptor"] += 1
#             traits["shy"] += 1
#             traits["unflirty"] += 1
#             traits["workaholic"] += 1
#         case "Laid Back":
#             traits["clumsy"] += 1
#             traits["couch potato"] += 1
#             traits["friendly"] += 1
#             traits["hates the outdoors"] += 1
#             traits["heavy sleeper"] += 1
#             traits["hydrophobic"] += 1
#             traits["loser"] += 1
#             traits["mooch"] += 1
#             traits["slob"] += 1
#             traits["unlucky"] += 1
#         case "Musical":
#             traits["star quality"] += 1
#             traits["virtuoso"] += 1
#         case "Occult":
#             traits["insane"] += 1
#             traits["lucky"] += 1
#         case "Outdoorsy":
#             traits["angler"] += 1
#             traits["can't stand art"] += 1
#             traits["eco-friendly"] += 1
#             traits["green thumb"] += 1
#             traits["light sleeper"] += 1
#             traits["loves the outdoors"] += 1
#             traits["technophobe"] += 1
#             traits["vegetarian"] += 1
#         case "Outgoing":
#             traits["absent-minded"] += 1
#             traits["charismatic"] += 1
#             traits["commitment issues"] += 1
#             traits["excitable"] += 1
#             traits["flirty"] += 1
#             traits["good sense of humour"] += 1
#             traits["great kisser"] += 1
#             traits["hopeless romantic"] += 1
#             traits["insane"] += 1
#             traits["light sleeper"] += 1
#             traits["mooch"] += 1
#             traits["over-emotional"] += 1
#             traits["party animal"] += 1
#             traits["schmoozer"] += 1
#             traits["star quality"] += 1
#             traits["virtuoso"] += 1
#         case "Plant Lover":
#             traits["eco-friendly"] += 1
#             traits["green thumb"] += 1
#             traits["loves the outdoors"] += 1
#             traits["vegetarian"] += 1
#         case "Rebellious":
#             traits["adventurous"] += 1
#             traits["commitment issues"] += 1
#             traits["dislikes children"] += 1
#             traits["evil"] += 1
#             traits["hot-headed"] += 1
#             traits["inappropriate"] += 1
#             traits["kleptomaniac"] += 1
#             traits["mean-spirited"] += 1
#             traits["rebellious"] += 1
#             traits["unflirty"] += 1
#             traits["workaholic"] += 1
#         case "Stylish":
#             traits["dramatic"] += 1
#             traits["perceptive"] += 1
#             traits["snob"] += 1
#         case "Technology":
#             traits["computer whiz"] += 1
#             traits["coward"] += 1
#             traits["eccentric"] += 1
#             traits["handy"] += 1
#             traits["hydrophobic"] += 1
#             traits["shy"] += 1
#             traits["vehicle enthusiast"] += 1
#         case "Tidy":
#             traits["disciplined"] += 1
#             traits["frugal"] += 1
#             traits["handy"] += 1
#             traits["lucky"] += 1
#             traits["neat"] += 1
#             traits["perfectionist"] += 1
#         case "Undead":
#             print("No Trait")
#         case "Well-Liked":
#             traits["childish"] += 1
#             traits["easily impressed"] += 1
#             traits["family-oriented"] += 1
#             traits["friendly"] += 1
#             traits["good"] += 1
#             traits["good sense of humour"] += 1
#             traits["lucky"] += 1
#             traits["natural cook"] += 1
#             traits["neat"] += 1
#             traits["nurturing"] += 1
#             traits["photographer's eye"] += 1
#             traits["shy"] += 1


# def get_trait_turn_on_adult(turn_on, traits):
#     # Turn On
#     match (turn_on):
#         case "Adventurous":
#             traits["adventurous"] += 1
#             traits["brave"] += 1
#             traits["daredevil"] += 1
#             traits["sailor"] += 1
#         case "Alien":
#             traits["supernatural fan"] += 1
#         case "Animal Lover":
#             traits["animal lover"] += 1
#             traits["cat person"] += 1
#             traits["dog person"] += 1
#             traits["equestrian"] += 1
#         case "Artistic":
#             traits["artistic"] += 1
#             traits["avant garde"] += 1
#             traits["loner"] += 1
#             traits["natural born performer"] += 1
#             traits["perceptive"] += 1
#             traits["photographer's eye"] += 1
#             traits["savvy sculptor"] += 1
#             traits["technophobe"] += 1
#         case "Athletic":
#             traits["adventurous"] += 1
#             traits["athletic"] += 1
#             traits["daredevil"] += 1
#             traits["disciplined"] += 1
#             traits["dog person"] += 1
#             traits["equestrian"] += 1
#             traits["light sleeper"] += 1
#             traits["loves the heat"] += 1
#             traits["loves the outdoors"] += 1
#             traits["loves to swim"] += 1
#             traits["sailor"] += 1
#             traits["vegetarian"] += 1
#         case "Black Hair":
#             print("No Trait")
#         case "Blonde Hair":
#             print("No Trait")
#         case "Brown Hair":
#             print("No Trait")
#         case "Red Hair":
#             print("No Trait")
#         case "Business Shark":
#             traits["ambitious"] += 1
#             traits["born salesman"] += 1
#             traits["frugal"] += 1
#             traits["grumpy"] += 1
#             traits["hot-headed"] += 1
#             traits["mooch"] += 1
#             traits["schmoozer"] += 1
#             traits["workaholic"] += 1
#         case "Charismatic":
#             traits["ambitious"] += 1
#             traits["born salesman"] += 1
#             traits["charismatic"] += 1
#             traits["commitment issues"] += 1
#             traits["flirty"] += 1
#             traits["good sense of humour"] += 1
#             traits["great kisser"] += 1
#             traits["hopeless romantic"] += 1
#             traits["irresistible"] += 1
#             traits["natural born performer"] += 1
#             traits["party animal"] += 1
#             traits["schmoozer"] += 1
#             traits["social butterfly"] += 1
#             traits["star quality"] += 1
#             traits["virtuoso"] += 1
#         case "Cultured":
#             traits["avant garde"] += 1
#             traits["bookworm"] += 1
#             traits["eccentric"] += 1
#             traits["loner"] += 1
#             traits["loves the cold"] += 1
#             traits["over-emotional"] += 1
#             traits["savvy sculptor"] += 1
#         case "Expressive":
#             traits["animal lover"] += 1
#             traits["artistic"] += 1
#             traits["charismatic"] += 1
#             traits["childish"] += 1
#             traits["daredevil"] += 1
#             traits["diva"] += 1
#             traits["dramatic"] += 1
#             traits["easily impressed"] += 1
#             traits["eco-friendly"] += 1
#             traits["excitable"] += 1
#             traits["inappropriate"] += 1
#             traits["insane"] += 1
#             traits["lucky"] += 1
#             traits["natural cook"] += 1
#             traits["over-emotional"] += 1
#             traits["savvy sculptor"] += 1
#             traits["social butterfly"] += 1
#             traits["unlucky"] += 1
#         case "Facial Hair":
#             print("No Trait")
#         case "Fatness":
#             traits["couch potato"] += 1
#             traits["hates the outdoors"] += 1
#             traits["heavy sleeper"] += 1
#             traits["never nude"] += 1
#             traits["slob"] += 1
#             traits["unstable"] += 1
#         case "Fitness":
#             traits["athletic"] += 1
#             traits["brave"] += 1
#             traits["disciplined"] += 1
#             traits["equestrian"] += 1
#             traits["excitable"] += 1
#             traits["light sleeper"] += 1
#             traits["loves the outdoors"] += 1
#             traits["loves to swim"] += 1
#             traits["party animal"] += 1
#             traits["sailor"] += 1
#         case "Foodie":
#             traits["absent-minded"] += 1
#             traits["family-oriented"] += 1
#             traits["friendly"] += 1
#             traits["good"] += 1
#             traits["natural cook"] += 1
#             traits["nurturing"] += 1
#             traits["perfectionist"] += 1
#             traits["photographer's eye"] += 1
#             traits["technophobe"] += 1
#         case "Grey Hair":
#             print("No Trait")
#         case "Indoorsy":
#             traits["bookworm"] += 1
#             traits["computer whiz"] += 1
#             traits["coward"] += 1
#             traits["eccentric"] += 1
#             traits["hates the outdoors"] += 1
#             traits["hydrophobic"] += 1
#             traits["loner"] += 1
#             traits["loves the cold"] += 1
#             traits["neat"] += 1
#             traits["perfectionist"] += 1
#             traits["slob"] += 1
#         case "Infamous":
#             traits["commitment issues"] += 1
#             traits["dislikes children"] += 1
#             traits["dramatic"] += 1
#             traits["evil"] += 1
#             traits["inappropriate"] += 1
#             traits["kleptomaniac"] += 1
#             traits["mean-spirited"] += 1
#             traits["rebellious"] += 1
#             traits["snob"] += 1
#             traits["socially awkward"] += 1
#             traits["supernatural sceptic"] += 1
#             traits["unstable"] += 1
#         case "Intellect":
#             traits["avant garde"] += 1
#             traits["bookworm"] += 1
#             traits["bot fan"] += 1
#             traits["can't stand art"] += 1
#             traits["eccentric"] += 1
#             traits["gatherer"] += 1
#             traits["genius"] += 1
#             traits["handy"] += 1
#             traits["no sense of humour"] += 1
#             traits["vehicle enthusiast"] += 1
#         case "Introvert":
#             traits["angler"] += 1
#             traits["bot fan"] += 1
#             traits["brooding"] += 1
#             traits["cat person"] += 1
#             traits["clumsy"] += 1
#             traits["computer whiz"] += 1
#             traits["coward"] += 1
#             traits["genius"] += 1
#             traits["grumpy"] += 1
#             traits["hates the outdoors"] += 1
#             traits["kleptomaniac"] += 1
#             traits["loner"] += 1
#             traits["mean-spirited"] += 1
#             traits["neurotic"] += 1
#             traits["never nude"] += 1
#             traits["night owl"] += 1
#             traits["no sense of humour"] += 1
#             traits["perceptive"] += 1
#             traits["savvy sculptor"] += 1
#             traits["shy"] += 1
#             traits["socially awkward"] += 1
#             traits["supernatural fan"] += 1
#             traits["unflirty"] += 1
#             traits["workaholic"] += 1
#         case "Laid Back":
#             traits["clumsy"] += 1
#             traits["couch potato"] += 1
#             traits["dog person"] += 1
#             traits["friendly"] += 1
#             traits["hates the outdoors"] += 1
#             traits["heavy sleeper"] += 1
#             traits["hydrophobic"] += 1
#             traits["loser"] += 1
#             traits["mooch"] += 1
#             traits["slob"] += 1
#             traits["unlucky"] += 1
#         case "Musical":
#             traits["natural born performer"] += 1
#             traits["star quality"] += 1
#             traits["virtuoso"] += 1
#         case "Occult":
#             traits["brooding"] += 1
#             traits["insane"] += 1
#             traits["lucky"] += 1
#             traits["supernatural fan"] += 1
#         case "Outdoorsy":
#             traits["angler"] += 1
#             traits["can't stand art"] += 1
#             traits["eco-friendly"] += 1
#             traits["equestrian"] += 1
#             traits["gatherer"] += 1
#             traits["green thumb"] += 1
#             traits["light sleeper"] += 1
#             traits["loves the heat"] += 1
#             traits["loves the outdoors"] += 1
#             traits["loves to swim"] += 1
#             traits["sailor"] += 1
#             traits["technophobe"] += 1
#             traits["vegetarian"] += 1
#         case "Outgoing":
#             traits["absent-minded"] += 1
#             traits["charismatic"] += 1
#             traits["commitment issues"] += 1
#             traits["diva"] += 1
#             traits["excitable"] += 1
#             traits["flirty"] += 1
#             traits["good sense of humour"] += 1
#             traits["great kisser"] += 1
#             traits["hopeless romantic"] += 1
#             traits["insane"] += 1
#             traits["irresistible"] += 1
#             traits["light sleeper"] += 1
#             traits["mooch"] += 1
#             traits["natural born performer"] += 1
#             traits["over-emotional"] += 1
#             traits["party animal"] += 1
#             traits["schmoozer"] += 1
#             traits["social butterfly"] += 1
#             traits["star quality"] += 1
#             traits["unstable"] += 1
#             traits["virtuoso"] += 1
#         case "Plant Lover":
#             traits["eco-friendly"] += 1
#             traits["green thumb"] += 1
#             traits["loves the heat"] += 1
#             traits["loves the outdoors"] += 1
#             traits["vegetarian"] += 1
#         case "Rebellious":
#             traits["adventurous"] += 1
#             traits["commitment issues"] += 1
#             traits["dislikes children"] += 1
#             traits["evil"] += 1
#             traits["hot-headed"] += 1
#             traits["inappropriate"] += 1
#             traits["kleptomaniac"] += 1
#             traits["mean-spirited"] += 1
#             traits["rebellious"] += 1
#             traits["supernatural sceptic"] += 1
#             traits["unflirty"] += 1
#             traits["workaholic"] += 1
#         case "Stylish":
#             traits["diva"] += 1
#             traits["dramatic"] += 1
#             traits["natural born performer"] += 1
#             traits["perceptive"] += 1
#             traits["proper"] += 1
#             traits["snob"] += 1
#         case "Technology":
#             traits["bot fan"] += 1
#             traits["computer whiz"] += 1
#             traits["coward"] += 1
#             traits["eccentric"] += 1
#             traits["handy"] += 1
#             traits["hydrophobic"] += 1
#             traits["night owl"] += 1
#             traits["shy"] += 1
#             traits["vehicle enthusiast"] += 1
#         case "Tidy":
#             traits["cat person"] += 1
#             traits["disciplined"] += 1
#             traits["frugal"] += 1
#             traits["handy"] += 1
#             traits["lucky"] += 1
#             traits["neat"] += 1
#             traits["perfectionist"] += 1
#             traits["proper"] += 1
#         case "Undead":
#             traits["supernatural fan"] += 1
#         case "Well-Liked":
#             traits["animal lover"] += 1
#             traits["childish"] += 1
#             traits["easily impressed"] += 1
#             traits["family-oriented"] += 1
#             traits["friendly"] += 1
#             traits["good"] += 1
#             traits["good sense of humour"] += 1
#             traits["lucky"] += 1
#             traits["natural cook"] += 1
#             traits["neat"] += 1
#             traits["nurturing"] += 1
#             traits["photographer's eye"] += 1
#             traits["proper"] += 1
#             traits["shy"] += 1
