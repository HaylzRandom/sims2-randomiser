from globals import ASPIRATION_MODEL
from .hobby import get_hobby
from .personality import get_personality
from .interests import get_interests, interests_aspiration


def generate_aspiration():
    aspiration_choice = dict(ASPIRATION_MODEL)
    sim_data = {}
    hobby = get_hobby()

    match hobby:
        case "Arts & Crafts":
            aspiration_choice["Family"] += 10
            aspiration_choice["Fortune"] -= 10
            aspiration_choice["Knowledge"] -= 10
            aspiration_choice["Pleasure"] -= 10
            aspiration_choice["Popularity"] += 10
            aspiration_choice["Romance"] += 10
        case "Cuisine":
            aspiration_choice["Family"] += 10
            aspiration_choice["Fortune"] -= 10
            aspiration_choice["Knowledge"] -= 10
            aspiration_choice["Pleasure"] += 10
            aspiration_choice["Popularity"] -= 10
            aspiration_choice["Romance"] += 10
        case "Film & Literature":
            aspiration_choice["Family"] -= 10
            aspiration_choice["Fortune"] -= 10
            aspiration_choice["Knowledge"] -= 10
            aspiration_choice["Popularity"] += 10
            aspiration_choice["Romance"] += 10
            aspiration_choice["Pleasure"] += 10
        case "Fitness":
            aspiration_choice["Family"] -= 10
            aspiration_choice["Fortune"] += 10
            aspiration_choice["Knowledge"] -= 10
            aspiration_choice["Pleasure"] -= 10
            aspiration_choice["Popularity"] += 10
            aspiration_choice["Romance"] += 10
        case "Games":
            aspiration_choice["Family"] += 10
            aspiration_choice["Fortune"] -= 10
            aspiration_choice["Knowledge"] -= 10
            aspiration_choice["Pleasure"] += 10
            aspiration_choice["Popularity"] += 10
            aspiration_choice["Romance"] -= 10
        case "Music & Dance":
            aspiration_choice["Family"] += 10
            aspiration_choice["Fortune"] -= 10
            aspiration_choice["Knowledge"] -= 10
            aspiration_choice["Pleasure"] += 10
            aspiration_choice["Popularity"] += 10
            aspiration_choice["Romance"] += 10
        case "Nature":
            aspiration_choice["Family"] += 10
            aspiration_choice["Fortune"] -= 10
            aspiration_choice["Knowledge"] += 10
            aspiration_choice["Pleasure"] -= 10
            aspiration_choice["Popularity"] += 10
            aspiration_choice["Romance"] -= 10
        case "Science":
            aspiration_choice["Family"] += 10
            aspiration_choice["Fortune"] += 10
            aspiration_choice["Knowledge"] += 10
            aspiration_choice["Pleasure"] -= 10
            aspiration_choice["Popularity"] -= 10
            aspiration_choice["Romance"] -= 10
        case "Sports":
            aspiration_choice["Family"] -= 10
            aspiration_choice["Fortune"] += 10
            aspiration_choice["Knowledge"] -= 10
            aspiration_choice["Pleasure"] -= 10
            aspiration_choice["Popularity"] += 10
            aspiration_choice["Romance"] += 10
        case "Tinkering":
            aspiration_choice["Family"] += 10
            aspiration_choice["Fortune"] += 10
            aspiration_choice["Knowledge"] += 10
            aspiration_choice["Pleasure"] -= 10
            aspiration_choice["Popularity"] -= 10
            aspiration_choice["Romance"] -= 10
        case _:
            print("Unknown Hobby at this time!")

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

    personality_aspiration(neat, outgoing, active, playful, nice, aspiration_choice)

    interests_aspiration(
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
        aspiration_choice,
    )

    sim_data = {
        "hobby": hobby,
        "neat": neat,
        "outgoing": outgoing,
        "active": active,
        "playful": playful,
        "nice": nice,
        "politics": politics,
        "crime": crime,
        "food": food,
        "sports": sports,
        "work": work,
        "school": school,
        "money": money,
        "entertainment": entertainment,
        "health": health,
        "paranormal": paranormal,
        "weather": weather,
        "toys": toys,
        "environment": environment,
        "culture": culture,
        "fashion": fashion,
        "travel": travel,
        "animals": animals,
        "sciFi": sciFi,
    }

    return sim_data, aspiration_choice


def personality_aspiration(neat, outgoing, active, playful, nice, aspirations):
    # Active
    if active >= 8:
        aspirations["Knowledge"] -= 10
        aspirations["Popularity"] += 10
    if active >= 5 and active < 8:
        aspirations["Family"] -= 10
        aspirations["Fortune"] += 10
        aspirations["Pleasure"] -= 10
        aspirations["Romance"] += 10
    if active >= 3 and active < 5:
        aspirations["Family"] += 10
        aspirations["Fortune"] -= 10
        aspirations["Pleasure"] += 10
        aspirations["Romance"] -= 10
    if active <= 2:
        aspirations["Knowledge"] += 10
        aspirations["Popularity"] -= 10

    # Neat
    if neat >= 8:
        aspirations["Family"] += 10
        aspirations["Knowledge"] += 10
    if neat >= 5 and neat < 8:
        aspirations["Fortune"] += 10
        aspirations["Pleasure"] -= 10
        aspirations["Popularity"] -= 10
        aspirations["Romance"] -= 10
    if neat >= 3 and neat < 5:
        aspirations["Fortune"] -= 10
        aspirations["Popularity"] += 10
        aspirations["Romance"] += 10
    if neat <= 2:
        aspirations["Family"] -= 10
        aspirations["Knowledge"] -= 10
        aspirations["Pleasure"] += 10

    # Nice
    if nice >= 8:
        aspirations["Family"] += 10
        aspirations["Knowledge"] -= 10
        aspirations["Popularity"] += 10
    if nice >= 5 and nice < 8:
        aspirations["Fortune"] -= 10
        aspirations["Pleasure"] += 10
        aspirations["Romance"] -= 10
    if nice >= 3 and nice < 5:
        aspirations["Fortune"] += 10
        aspirations["Pleasure"] -= 10
        aspirations["Romance"] += 10
    if nice <= 2:
        aspirations["Family"] -= 10
        aspirations["Knowledge"] += 10
        aspirations["Popularity"] -= 10

    # Outgoing
    if outgoing >= 8:
        aspirations["Knowledge"] -= 10
        aspirations["Popularity"] += 10
        aspirations["Romance"] += 10
    if outgoing >= 5 and outgoing < 8:
        aspirations["Family"] -= 10
        aspirations["Fortune"] += 10
        aspirations["Pleasure"] += 10
    if outgoing >= 3 and outgoing < 5:
        aspirations["Family"] += 10
        aspirations["Fortune"] -= 10
        aspirations["Pleasure"] -= 10
    if outgoing <= 2:
        aspirations["Knowledge"] += 10
        aspirations["Popularity"] -= 10
        aspirations["Romance"] -= 10

    # Playful
    if playful >= 8:
        aspirations["Fortune"] -= 10
        aspirations["Knowledge"] -= 10
        aspirations["Pleasure"] += 10
    if playful >= 5 and playful < 8:
        aspirations["Family"] += 10
        aspirations["Popularity"] -= 10
        aspirations["Romance"] += 10
    if playful >= 3 and playful < 5:
        aspirations["Family"] -= 10
        aspirations["Popularity"] += 10
        aspirations["Romance"] -= 10
    if playful <= 2:
        aspirations["Fortune"] += 10
        aspirations["Knowledge"] += 10
        aspirations["Pleasure"] -= 10

def aspiration_traits(aspirations, age, traits):

    if age == "teen":
        for key, value in aspirations.items():

            if key == "Family" and value >= 15:
                traits["adventurous"] -= 1
                traits["ambitious"] -= 1
                traits["brave"] += 1
                traits["childish"] += 1
                traits["clumsy"] += 1
                traits["commitment issues"] -= 1
                traits["computer whiz"] += 1
                traits["couch potato"] += 1
                traits["coward"] += 1
                traits["daredevil"] -= 1
                traits["dislikes children"] -= 1
                traits["dramatic"] -= 1
                traits["eccentric"] -= 1
                traits["eco-friendly"] += 1
                traits["evil"] -= 1
                traits["excitable"] += 1
                traits["family-oriented"] += 1
                traits["friendly"] += 1
                traits["frugal"] += 1
                traits["good"] += 1
                traits["green thumb"] += 1
                traits["hot-headed"] -= 1
                traits["inappropriate"] -= 1
                traits["insane"] -= 1
                traits["kleptomaniac"] -= 1
                traits["light sleeper"] += 1
                traits["loves the outdoors"] += 1
                traits["mean-spirited"] -= 1
                traits["mooch"] -= 1
                traits["natural cook"] += 1
                traits["neat"] += 1
                traits["nurturing"] += 1
                traits["perfectionist"] += 1
                traits["rebellious"] -= 1
                traits["snob"] -= 1
                traits["technophobe"] -= 1
            if key == "Fortune" and value >= 15:
                traits["absent-minded"] -= 1
                traits["adventurous"] -= 1
                traits["ambitious"] += 1
                traits["angler"] -= 1
                traits["charismatic"] += 1
                traits["childish"] -= 1
                traits["clumsy"] -= 1
                traits["commitment issues"] += 1
                traits["computer whiz"] -= 1
                traits["coward"] -= 1
                traits["daredevil"] += 1
                traits["dislikes children"] += 1
                traits["dramatic"] -= 1
                traits["easily impressed"] -= 1
                traits["eco-friendly"] -= 1
                traits["evil"] += 1
                traits["excitable"] -= 1
                traits["family-oriented"] += 1
                traits["friendly"] -= 1
                traits["frugal"] += 1
                traits["hates the outdoors"] += 1
                traits["heavy sleeper"] -= 1
                traits["hot-headed"] += 1
                traits["insane"] -= 1
                traits["kleptomaniac"] += 1
                traits["light sleeper"] += 1
                traits["loser"] -= 1
                traits["mean-spirited"] += 1
                traits["mooch"] += 1
                traits["no sense of humour"] += 1
                traits["perceptive"] += 1
                traits["perfectionist"] += 1
                traits["schmoozer"] += 1
                traits["snob"] += 1
            if key == "Knowledge" and value >= 15:
                traits["absent-minded"] -= 1
                traits["angler"] += 1
                traits["can't stand art"] += 1
                traits["charismatic"] -= 1
                traits["childish"] -= 1
                traits["clumsy"] -= 1
                traits["commitment issues"] -= 1
                traits["computer whiz"] += 1
                traits["coward"] -= 1
                traits["daredevil"] -= 1
                traits["disciplined"] += 1
                traits["dislikes children"] -= 1
                traits["dramatic"] -= 1
                traits["eccentric"] += 1
                traits["evil"] += 1
                traits["excitable"] -= 1
                traits["family-oriented"] += 1
                traits["frugal"] += 1
                traits["genius"] += 1
                traits["good"] += 1
                traits["good sense of humour"] -= 1
                traits["great kisser"] -= 1
                traits["green thumb"] += 1
                traits["grumpy"] += 1
                traits["handy"] += 1
                traits["hates the outdoors"] += 1
                traits["hot-headed"] += 1
                traits["insane"] -= 1
                traits["loner"] += 1
                traits["mean-spirited"] += 1
                traits["natural cook"] -= 1
                traits["neat"] += 1
                traits["no sense of humour"] += 1
                traits["party animal"] -= 1
                traits["perceptive"] += 1
                traits["perfectionist"] += 1
                traits["rebellious"] -= 1
                traits["schmoozer"] -= 1
                traits["star quality"] -= 1
                traits["technophobe"] -= 1
                traits["unflirty"] += 1
            if key == "Pleasure" and value >= 15:
                traits["absent-minded"] += 1
                traits["angler"] -= 1
                traits["brave"] -= 1
                traits["childish"] += 1
                traits["clumsy"] += 1
                traits["commitment issues"] += 1
                traits["computer whiz"] += 1
                traits["couch potato"] += 1
                traits["coward"] += 1
                traits["daredevil"] += 1
                traits["dislikes children"] += 1
                traits["dramatic"] += 1
                traits["easily impressed"] += 1
                traits["eccentric"] += 1
                traits["eco-friendly"] -= 1
                traits["evil"] -= 1
                traits["excitable"] += 1
                traits["family-oriented"] += 1
                traits["flirty"] += 1
                traits["frugal"] -= 1
                traits["genius"] -= 1
                traits["good sense of humour"] += 1
                traits["great kisser"] += 1
                traits["handy"] -= 1
                traits["hates the outdoors"] -= 1
                traits["heavy sleeper"] += 1
                traits["hopeless romantic"] += 1
                traits["inappropriate"] += 1
                traits["insane"] += 1
                traits["kleptomaniac"] -= 1
                traits["light sleeper"] -= 1
                traits["loser"] += 1
                traits["loves the outdoors"] += 1
                traits["neat"] -= 1
                traits["no sense of humour"] -= 1
                traits["party animal"] += 1
                traits["perceptive"] -= 1
                traits["perfectionist"] -= 1
                traits["rebellious"] += 1
                traits["star quality"] += 1
                traits["unflirty"] -= 1
            if key == "Popularity" and value >= 15:
                traits["adventurous"] += 1
                traits["brave"] += 1
                traits["can't stand art"] -= 1
                traits["charismatic"] += 1
                traits["childish"] += 1
                traits["commitment issues"] -= 1
                traits["computer whiz"] -= 1
                traits["couch potato"] -= 1
                traits["coward"] += 1
                traits["daredevil"] += 1
                traits["disciplined"] -= 1
                traits["dislikes children"] -= 1
                traits["dramatic"] += 1
                traits["eco-friendly"] += 1
                traits["evil"] -= 1
                traits["excitable"] += 1
                traits["family-oriented"] += 1
                traits["flirty"] += 1
                traits["friendly"] += 1
                traits["frugal"] -= 1
                traits["good"] += 1
                traits["good sense of humour"] += 1
                traits["green thumb"] += 1
                traits["grumpy"] -= 1
                traits["heavy sleeper"] += 1
                traits["hopeless romantic"] += 1
                traits["hot-headed"] -= 1
                traits["kleptomaniac"] += 1
                traits["loner"] -= 1
                traits["loves the outdoors"] += 1
                traits["mean-spirited"] -= 1
                traits["natural cook"] += 1
                traits["neat"] -= 1
                traits["no sense of humour"] -= 1
                traits["party animal"] += 1
                traits["perfectionist"] -= 1
                traits["rebellious"] += 1
                traits["schmoozer"] += 1
                traits["star quality"] += 1
                traits["technophobe"] += 1
                traits["unflirty"] -= 1
            if key == "Romance" and value >= 15:
                traits["angler"] -= 1
                traits["can't stand art"] -= 1
                traits["clumsy"] += 1
                traits["commitment issues"] += 1
                traits["computer whiz"] -= 1
                traits["couch potato"] -= 1
                traits["coward"] -= 1
                traits["daredevil"] -= 1
                traits["dislikes children"] += 1
                traits["dramatic"] += 1
                traits["eccentric"] -= 1
                traits["eco-friendly"] -= 1
                traits["evil"] += 1
                traits["excitable"] -= 1
                traits["family-oriented"] -= 1
                traits["flirty"] += 1
                traits["frugal"] -= 1
                traits["great kisser"] += 1
                traits["handy"] -= 1
                traits["hopeless romantic"] += 1
                traits["inappropriate"] += 1
                traits["kleptomaniac"] += 1
                traits["light sleeper"] -= 1
                traits["nurturing"] -= 1
                traits["unflirty"] -= 1
    else:
        for key, value in aspirations.items():
            if key == "Family" and value >= 15:
                traits["adventurous"] -= 1
                traits["ambitious"] -= 1
                traits["brave"] += 1
                traits["cat person"] += 1
                traits["childish"] += 1
                traits["clumsy"] += 1
                traits["commitment issues"] -= 1
                traits["computer whiz"] += 1
                traits["couch potato"] += 1
                traits["coward"] += 1
                traits["daredevil"] -= 1
                traits["dislikes children"] -= 1
                traits["diva"] -= 1
                traits["dog person"] += 1
                traits["dramatic"] -= 1
                traits["eccentric"] -= 1
                traits["eco-friendly"] += 1
                traits["equestrian"] -= 1
                traits["evil"] -= 1
                traits["excitable"] += 1
                traits["family-oriented"] += 1
                traits["friendly"] += 1
                traits["frugal"] += 1
                traits["good"] += 1
                traits["green thumb"] += 1
                traits["hot-headed"] -= 1
                traits["inappropriate"] -= 1
                traits["insane"] -= 1
                traits["kleptomaniac"] -= 1
                traits["light sleeper"] += 1
                traits["loves the cold"] += 1
                traits["loves the outdoors"] += 1
                traits["mean-spirited"] -= 1
                traits["mooch"] -= 1
                traits["natural cook"] += 1
                traits["neat"] += 1
                traits["night owl"] -= 1
                traits["nurturing"] += 1
                traits["perfectionist"] += 1
                traits["rebellious"] -= 1
                traits["snob"] -= 1
                traits["supernatural fan"] += 1
                traits["supernatural sceptic"] -= 1
                traits["technophobe"] -= 1
            if key == "Fortune" and value >= 15:
                traits["absent-minded"] -= 1
                traits["adventurous"] -= 1
                traits["ambitious"] += 1
                traits["angler"] -= 1
                traits["charismatic"] += 1
                traits["childish"] -= 1
                traits["clumsy"] -= 1
                traits["commitment issues"] += 1
                traits["computer whiz"] -= 1
                traits["coward"] -= 1
                traits["daredevil"] += 1
                traits["dislikes children"] += 1
                traits["diva"] += 1
                traits["dog person"] -= 1
                traits["dramatic"] -= 1
                traits["easily impressed"] -= 1
                traits["eco-friendly"] -= 1
                traits["equestrian"] += 1
                traits["evil"] += 1
                traits["excitable"] -= 1
                traits["family-oriented"] += 1
                traits["friendly"] -= 1
                traits["frugal"] += 1
                traits["gatherer"] += 1
                traits["hates the outdoors"] += 1
                traits["heavy sleeper"] -= 1
                traits["hot-headed"] += 1
                traits["insane"] -= 1
                traits["kleptomaniac"] += 1
                traits["light sleeper"] += 1
                traits["loser"] -= 1
                traits["mean-spirited"] += 1
                traits["mooch"] += 1
                traits["no sense of humour"] += 1
                traits["perceptive"] += 1
                traits["perfectionist"] += 1
                traits["schmoozer"] += 1
                traits["snob"] += 1
                traits["supernatural fan"] -= 1
                traits["supernatural sceptic"] += 1
            if key == "Knowledge" and value >= 15:
                traits["absent-minded"] -= 1
                traits["angler"] += 1
                traits["can't stand art"] += 1
                traits["cat person"] += 1
                traits["charismatic"] -= 1
                traits["childish"] -= 1
                traits["clumsy"] -= 1
                traits["commitment issues"] -= 1
                traits["computer whiz"] += 1
                traits["coward"] -= 1
                traits["daredevil"] -= 1
                traits["disciplined"] += 1
                traits["dislikes children"] -= 1
                traits["diva"] -= 1
                traits["dog person"] -= 1
                traits["dramatic"] -= 1
                traits["eccentric"] += 1
                traits["equestrian"] -= 1
                traits["evil"] += 1
                traits["excitable"] -= 1
                traits["family-oriented"] += 1
                traits["frugal"] += 1
                traits["gatherer"] += 1
                traits["genius"] += 1
                traits["good"] += 1
                traits["good sense of humour"] -= 1
                traits["great kisser"] -= 1
                traits["green thumb"] += 1
                traits["grumpy"] += 1
                traits["handy"] += 1
                traits["hates the outdoors"] += 1
                traits["hot-headed"] += 1
                traits["insane"] -= 1
                traits["loner"] += 1
                traits["loves the cold"] += 1
                traits["loves the heat"] -= 1
                traits["mean-spirited"] += 1
                traits["natural born performer"] -= 1
                traits["natural cook"] -= 1
                traits["neat"] += 1
                traits["no sense of humour"] += 1
                traits["party animal"] -= 1
                traits["perceptive"] += 1
                traits["perfectionist"] += 1
                traits["rebellious"] -= 1
                traits["schmoozer"] -= 1
                traits["social butterfly"] -= 1
                traits["socially awkward"] += 1
                traits["star quality"] -= 1
                traits["supernatural fan"] += 1
                traits["supernatural sceptic"] -= 1
                traits["technophobe"] -= 1
                traits["unflirty"] += 1
            if key == "Pleasure" and value >= 15:
                traits["absent-minded"] += 1
                traits["angler"] -= 1
                traits["brave"] -= 1
                traits["cat person"] -= 1
                traits["childish"] += 1
                traits["clumsy"] += 1
                traits["commitment issues"] += 1
                traits["computer whiz"] += 1
                traits["couch potato"] += 1
                traits["coward"] += 1
                traits["daredevil"] += 1
                traits["dislikes children"] += 1
                traits["dramatic"] += 1
                traits["easily impressed"] += 1
                traits["eccentric"] += 1
                traits["eco-friendly"] -= 1
                traits["equestrian"] += 1
                traits["evil"] -= 1
                traits["excitable"] += 1
                traits["family-oriented"] += 1
                traits["flirty"] += 1
                traits["frugal"] -= 1
                traits["gatherer"] -= 1
                traits["genius"] -= 1
                traits["good sense of humour"] += 1
                traits["great kisser"] += 1
                traits["handy"] -= 1
                traits["hates the outdoors"] -= 1
                traits["heavy sleeper"] += 1
                traits["hopeless romantic"] += 1
                traits["inappropriate"] += 1
                traits["insane"] += 1
                traits["irresistible"] += 1
                traits["kleptomaniac"] -= 1
                traits["light sleeper"] -= 1
                traits["loser"] += 1
                traits["loves the outdoors"] += 1
                traits["natural born performer"] += 1
                traits["neat"] -= 1
                traits["night owl"] += 1
                traits["no sense of humour"] -= 1
                traits["party animal"] += 1
                traits["perceptive"] -= 1
                traits["perfectionist"] -= 1
                traits["rebellious"] += 1
                traits["social butterfly"] += 1
                traits["socially awkward"] -= 1
                traits["star quality"] += 1
                traits["supernatural fan"] -= 1
                traits["supernatural sceptic"] += 1
                traits["unflirty"] -= 1
            if key == "Popularity" and value >= 15:
                traits["adventurous"] += 1
                traits["brave"] += 1
                traits["can't Stand Art"] -= 1
                traits["charismatic"] += 1
                traits["childish"] += 1
                traits["commitment issues"] -= 1
                traits["computer whiz"] -= 1
                traits["couch potato"] -= 1
                traits["coward"] += 1
                traits["daredevil"] += 1
                traits["disciplined"] -= 1
                traits["dislikes children"] -= 1
                traits["diva"] += 1
                traits["dog person"] += 1
                traits["dramatic"] += 1
                traits["eco-friendly"] += 1
                traits["equestrian"] += 1
                traits["evil"] -= 1
                traits["excitable"] += 1
                traits["family-oriented"] += 1
                traits["flirty"] += 1
                traits["friendly"] += 1
                traits["frugal"] -= 1
                traits["good"] += 1
                traits["good sense of humour"] += 1
                traits["green thumb"] += 1
                traits["grumpy"] -= 1
                traits["heavy sleeper"] += 1
                traits["hopeless romantic"] += 1
                traits["hot-headed"] -= 1
                traits["irresistible"] += 1
                traits["kleptomaniac"] += 1
                traits["loner"] -= 1
                traits["loves the cold"] -= 1
                traits["loves the heat"] += 1
                traits["loves the outdoors"] += 1
                traits["mean-spirited"] -= 1
                traits["natural born performer"] += 1
                traits["natural cook"] += 1
                traits["neat"] -= 1
                traits["no sense of humour"] -= 1
                traits["party animal"] += 1
                traits["perfectionist"] -= 1
                traits["rebellious"] += 1
                traits["schmoozer"] += 1
                traits["social butterfly"] += 1
                traits["socially awkward"] -= 1
                traits["star quality"] += 1
                traits["supernatural fan"] += 1
                traits["supernatural sceptic"] -= 1
                traits["technophobe"] += 1
                traits["unflirty"] -= 1
            if key == "Romance" and value >= 15:
                traits["angler"] -= 1
                traits["can't stand art"] -= 1
                traits["clumsy"] += 1
                traits["commitment issues"] += 1
                traits["computer whiz"] -= 1
                traits["couch potato"] -= 1
                traits["coward"] -= 1
                traits["daredevil"] -= 1
                traits["dislikes children"] += 1
                traits["diva"] += 1
                traits["dog person"] += 1
                traits["dramatic"] += 1
                traits["eccentric"] -= 1
                traits["eco-friendly"] -= 1
                traits["equestrian"] += 1
                traits["evil"] += 1
                traits["excitable"] -= 1
                traits["family-oriented"] -= 1
                traits["flirty"] += 1
                traits["frugal"] -= 1
                traits["gatherer"] -= 1
                traits["great kisser"] += 1
                traits["handy"] -= 1
                traits["hopeless romantic"] += 1
                traits["inappropriate"] += 1
                traits["irresistible"] += 1
                traits["kleptomaniac"] += 1
                traits["light sleeper"] -= 1
                traits["loves the heat"] += 1
                traits["natural born performer"] += 1
                traits["night owl"] += 1
                traits["nurturing"] -= 1
                traits["supernatural fan"] -= 1
                traits["supernatural sceptic"] += 1
                traits["unflirty"] -= 1
