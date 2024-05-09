from globals import ASPIRATION_MODEL
from .hobby import get_hobby
from .personality import get_personality
from .interests import get_interests


def generate_aspiration():
    aspiration_choice = dict(ASPIRATION_MODEL)
    sim_data = {}
    hobby = get_hobby()

    match hobby:
        case "Arts & Crafts":
            aspiration_choice["Popularity"] += 1
        case "Cuisine":
            aspiration_choice["Family"] += 1
        case "Film & Literature":
            aspiration_choice["Romance"] += 1
        case "Fitness":
            aspiration_choice["Popularity"] += 1
            aspiration_choice["Romance"] += 1
        case "Games":
            aspiration_choice["Family"] += 1
            aspiration_choice["Pleasure"] += 1
        case "Music & Dance":
            aspiration_choice["Pleasure"] += 1
            aspiration_choice["Fortune"] += 1
        case "Nature":
            aspiration_choice["Knowledge"] += 1
        case "Science":
            aspiration_choice["Knowledge"] += 1
        case "Sports":
            aspiration_choice["Popularity"] += 1
        case "Tinkering":
            aspiration_choice["Fortune"] += 1
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

    aspiration_choice["Family"] += school + toys + animals + food
    aspiration_choice["Fortune"] += crime + money + work + politics
    aspiration_choice["Knowledge"] += weather + paranormal + environment + sciFi
    aspiration_choice["Pleasure"] += food + entertainment + culture + travel
    aspiration_choice["Popularity"] += politics + sports + fashion + entertainment
    aspiration_choice["Romance"] += fashion + travel + health + culture

    sim_data = {
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
    if active >= 7:
        aspirations["Pleasure"] += 5
    if active >= 6:
        aspirations["Popularity"] += 5
    if active == 4:
        aspirations["Pleasure"] -= 5
    if active <= 3:
        aspirations["Popularity"] -= 5

    # Neat
    if neat > 6:
        aspirations["Family"] += 5
        aspirations["Knowledge"] += 5
    if neat < 6 and neat > 3:
        aspirations["Knowledge"] -= 5
    if neat <= 3:
        aspirations["Family"] -= 5

    # Nice
    if nice >= 7:
        aspirations["Family"] += 5
        aspirations["Popularity"] += 5
        aspirations["Fortune"] -= 5
    if nice >= 6:
        aspirations["Romance"] -= 5
    if nice == 4:
        aspirations["Fortune"] += 5
        aspirations["Romance"] += 5
    if nice <= 3:
        aspirations["Family"] -= 5
        aspirations["Popularity"] -= 5

    # Outgoing
    if outgoing >= 9:
        aspirations["Popularity"] += 5
    if outgoing == 7:
        aspirations["Fortune"] += 5
        aspirations["Pleasure"] += 5
        aspirations["Romance"] += 5
        aspirations["Family"] -= 5
    if outgoing > 5:
        aspirations["Knowledge"] -= 5
    if outgoing == 4:
        aspirations["Family"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Pleasure"] -= 5
        aspirations["Romance"] -= 5
    if outgoing <= 3:
        aspirations["Popularity"] -= 5

    # Playful
    if playful > 6:
        aspirations["Pleasure"] += 5
        aspirations["Romance"] += 5
        aspirations["Fortune"] -= 5
    if playful == 5:  # 5?
        aspirations["Knowledge"] -= 5
    if playful == 4:  # 4?
        aspirations["Fortune"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Romance"] -= 5
    if playful <= 3:
        aspirations["Knowledge"] += 5


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
                traits["social awkward"] += 1
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
