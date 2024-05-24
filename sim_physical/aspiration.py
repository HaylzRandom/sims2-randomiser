from globals import ASPIRATION_MODEL
from .hobby import get_hobby
from .personality import get_personality
from .interests import get_interests, interests_aspiration


def generate_aspiration(turn_on_1, turn_on_2, turn_off):
    aspiration_choice = dict(ASPIRATION_MODEL)
    sim_data = {}
    print("")
    hobby = get_hobby()

    match hobby:
        case "Arts & Crafts":
            aspiration_choice["Family"] += 20
            aspiration_choice["Fortune"] -= 20
            aspiration_choice["Knowledge"] -= 20
            aspiration_choice["Pleasure"] -= 20
            aspiration_choice["Popularity"] += 20
            aspiration_choice["Romance"] += 20
        case "Cuisine":
            aspiration_choice["Family"] += 20
            aspiration_choice["Fortune"] -= 20
            aspiration_choice["Knowledge"] -= 20
            aspiration_choice["Pleasure"] += 20
            aspiration_choice["Popularity"] -= 20
            aspiration_choice["Romance"] += 20
        case "Film & Literature":
            aspiration_choice["Family"] -= 20
            aspiration_choice["Fortune"] -= 20
            aspiration_choice["Knowledge"] -= 20
            aspiration_choice["Popularity"] += 20
            aspiration_choice["Romance"] += 20
            aspiration_choice["Pleasure"] += 20
        case "Fitness":
            aspiration_choice["Family"] -= 20
            aspiration_choice["Fortune"] += 20
            aspiration_choice["Knowledge"] -= 20
            aspiration_choice["Pleasure"] -= 20
            aspiration_choice["Popularity"] += 20
            aspiration_choice["Romance"] += 20
        case "Games":
            aspiration_choice["Family"] += 20
            aspiration_choice["Fortune"] -= 20
            aspiration_choice["Knowledge"] -= 20
            aspiration_choice["Pleasure"] += 20
            aspiration_choice["Popularity"] += 20
            aspiration_choice["Romance"] -= 20
        case "Music & Dance":
            aspiration_choice["Family"] += 20
            aspiration_choice["Fortune"] -= 20
            aspiration_choice["Knowledge"] -= 20
            aspiration_choice["Pleasure"] += 20
            aspiration_choice["Popularity"] += 20
            aspiration_choice["Romance"] += 20
        case "Nature":
            aspiration_choice["Family"] += 20
            aspiration_choice["Fortune"] -= 20
            aspiration_choice["Knowledge"] += 20
            aspiration_choice["Pleasure"] -= 20
            aspiration_choice["Popularity"] += 20
            aspiration_choice["Romance"] -= 20
        case "Science":
            aspiration_choice["Family"] += 20
            aspiration_choice["Fortune"] += 20
            aspiration_choice["Knowledge"] += 20
            aspiration_choice["Pleasure"] -= 20
            aspiration_choice["Popularity"] -= 20
            aspiration_choice["Romance"] -= 20
        case "Sports":
            aspiration_choice["Family"] -= 20
            aspiration_choice["Fortune"] += 20
            aspiration_choice["Knowledge"] -= 20
            aspiration_choice["Pleasure"] -= 20
            aspiration_choice["Popularity"] += 20
            aspiration_choice["Romance"] += 20
        case "Tinkering":
            aspiration_choice["Family"] += 20
            aspiration_choice["Fortune"] += 20
            aspiration_choice["Knowledge"] += 20
            aspiration_choice["Pleasure"] -= 20
            aspiration_choice["Popularity"] -= 20
            aspiration_choice["Romance"] -= 20
        case _:
            print("Unknown Hobby at this time!")

    turn_on_aspiration(turn_on_1, aspiration_choice)
    turn_on_aspiration(turn_on_2, aspiration_choice)
    turn_off_aspiration(turn_off, aspiration_choice)

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
        aspirations["Knowledge"] -= 20
        aspirations["Popularity"] += 20
    if active >= 5 and active < 8:
        aspirations["Family"] -= 20
        aspirations["Fortune"] += 20
        aspirations["Pleasure"] -= 20
        aspirations["Romance"] += 20
    if active >= 3 and active < 5:
        aspirations["Family"] += 20
        aspirations["Fortune"] -= 20
        aspirations["Pleasure"] += 20
        aspirations["Romance"] -= 20
    if active <= 2:
        aspirations["Knowledge"] += 20
        aspirations["Popularity"] -= 20

    # Neat
    if neat >= 8:
        aspirations["Family"] += 20
        aspirations["Knowledge"] += 20
    if neat >= 5 and neat < 8:
        aspirations["Fortune"] += 20
        aspirations["Pleasure"] -= 20
        aspirations["Popularity"] -= 20
        aspirations["Romance"] -= 20
    if neat >= 3 and neat < 5:
        aspirations["Fortune"] -= 20
        aspirations["Popularity"] += 20
        aspirations["Romance"] += 20
    if neat <= 2:
        aspirations["Family"] -= 20
        aspirations["Knowledge"] -= 20
        aspirations["Pleasure"] += 20

    # Nice
    if nice >= 8:
        aspirations["Family"] += 20
        aspirations["Knowledge"] -= 20
        aspirations["Popularity"] += 20
    if nice >= 5 and nice < 8:
        aspirations["Fortune"] -= 20
        aspirations["Pleasure"] += 20
        aspirations["Romance"] -= 20
    if nice >= 3 and nice < 5:
        aspirations["Fortune"] += 20
        aspirations["Pleasure"] -= 20
        aspirations["Romance"] += 20
    if nice <= 2:
        aspirations["Family"] -= 20
        aspirations["Knowledge"] += 20
        aspirations["Popularity"] -= 20

    # Outgoing
    if outgoing >= 8:
        aspirations["Knowledge"] -= 20
        aspirations["Popularity"] += 20
        aspirations["Romance"] += 20
    if outgoing >= 5 and outgoing < 8:
        aspirations["Family"] -= 20
        aspirations["Fortune"] += 20
        aspirations["Pleasure"] += 20
    if outgoing >= 3 and outgoing < 5:
        aspirations["Family"] += 20
        aspirations["Fortune"] -= 20
        aspirations["Pleasure"] -= 20
    if outgoing <= 2:
        aspirations["Knowledge"] += 20
        aspirations["Popularity"] -= 20
        aspirations["Romance"] -= 20

    # Playful
    if playful >= 8:
        aspirations["Fortune"] -= 20
        aspirations["Knowledge"] -= 20
        aspirations["Pleasure"] += 20
    if playful >= 5 and playful < 8:
        aspirations["Family"] += 20
        aspirations["Popularity"] -= 20
        aspirations["Romance"] += 20
    if playful >= 3 and playful < 5:
        aspirations["Family"] -= 20
        aspirations["Popularity"] += 20
        aspirations["Romance"] -= 20
    if playful <= 2:
        aspirations["Fortune"] += 20
        aspirations["Knowledge"] += 20
        aspirations["Pleasure"] -= 20


def turn_on_aspiration(turn_on, aspirations):
    match (turn_on):
        case "Adventurous":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] += 20
        case "Alien":
            aspirations["Family"] += 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Animal Lover":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] -= 20
        case "Artistic":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] += 20
        case "Athletic":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] += 20
        case "Business Shark":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] += 20
        case "Charismatic":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] += 20
        case "Cultured":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] -= 20
        case "Expressive":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] -= 20
        case "Fatness":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Fitness":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] += 20
        case "Foodie":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Indoorsy":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Infamous":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] += 20
        case "Intellect":
            aspirations["Family"] += 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Introvert":
            aspirations["Family"] += 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Laid Back":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Musical":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] -= 20
        case "Occult":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Outdoorsy":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] += 20
        case "Outgoing":
            aspirations["Family"] -= 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] += 20
        case "Plant Lover":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] -= 20
        case "Rebellious":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] += 20
        case "Stylish":
            aspirations["Family"] -= 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] += 20
        case "Technology":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Tidy":
            aspirations["Family"] += 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Undead":
            aspirations["Family"] += 20
            aspirations["Fortune"] += 20
            aspirations["Knowledge"] += 20
            aspirations["Pleasure"] -= 20
            aspirations["Popularity"] -= 20
            aspirations["Romance"] -= 20
        case "Well-Liked":
            aspirations["Family"] += 20
            aspirations["Fortune"] -= 20
            aspirations["Knowledge"] -= 20
            aspirations["Pleasure"] += 20
            aspirations["Popularity"] += 20
            aspirations["Romance"] -= 20


def turn_off_aspiration(turn_off, aspirations):
    match (turn_off):
        case "Adventurous":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] -= 50
        case "Alien":
            aspirations["Family"] -= 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Animal Lover":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] += 50
        case "Artistic":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] -= 50
        case "Athletic":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] -= 50
        case "Business Shark":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] -= 50
        case "Charismatic":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] -= 50
        case "Cultured":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] += 50
        case "Expressive":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] += 50
        case "Fatness":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Fitness":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] -= 50
        case "Foodie":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Indoorsy":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Infamous":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] -= 50
        case "Intellect":
            aspirations["Family"] -= 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Introvert":
            aspirations["Family"] -= 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Laid Back":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Musical":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] += 50
        case "Occult":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Outdoorsy":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] -= 50
        case "Outgoing":
            aspirations["Family"] += 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] -= 50
        case "Plant Lover":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] += 50
        case "Rebellious":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] -= 50
        case "Stylish":
            aspirations["Family"] += 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] -= 50
        case "Technology":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Tidy":
            aspirations["Family"] -= 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Undead":
            aspirations["Family"] -= 50
            aspirations["Fortune"] -= 50
            aspirations["Knowledge"] -= 50
            aspirations["Pleasure"] += 50
            aspirations["Popularity"] += 50
            aspirations["Romance"] += 50
        case "Well-Liked":
            aspirations["Family"] -= 50
            aspirations["Fortune"] += 50
            aspirations["Knowledge"] += 50
            aspirations["Pleasure"] -= 50
            aspirations["Popularity"] -= 50
            aspirations["Romance"] += 50


def aspiration_traits(aspirations, traits):

    for key, value in aspirations.items():
        print(f"Value: {value}")
        if key == "Family":
            if value >= 80:
                traits["adventurous"] += 20
                traits["ambitious"] -= 20
                traits["animal lover"] += 20
                traits["athletic"] -= 20
                traits["born salesman"] -= 20
                traits["brave"] += 20
                traits["childish"] += 20
                traits["clumsy"] += 20
                traits["commitment issues"] -= 20
                traits["coward"] -= 20
                traits["daredevil"] -= 20
                traits["disciplined"] += 20
                traits["dislikes children"] -= 20
                traits["diva"] -= 20
                traits["dog person"] += 20
                traits["eco-friendly"] += 20
                traits["equestrian"] -= 20
                traits["evil"] -= 20
                traits["family-oriented"] += 20
                traits["friendly"] += 20
                traits["gatherer"] += 20
                traits["good"] += 20
                traits["green thumb"] += 20
                traits["handy"] += 20
                traits["hopeless romantic"] += 20
                traits["inappropriate"] -= 20
                traits["insane"] -= 20
                traits["kleptomaniac"] -= 20
                traits["mean-spirited"] -= 20
                traits["mooch"] -= 20
                traits["natural cook"] += 20
                traits["neat"] += 20
                traits["nurturing"] += 20
                traits["party animal"] -= 20
                traits["perfectionist"] += 20
                traits["proper"] += 20
                traits["shy"] += 20
                traits["slob"] -= 20
                traits["social butterfly"] += 20
                traits["supernatural fan"] += 20
                traits["supernatural sceptic"] -= 20
                traits["unstable"] -= 20
                traits["workaholic"] -= 20
            if value >= 50 and value < 80:
                traits["absent-minded"] += 20
                traits["angler"] += 20
                traits["artistic"] -= 20
                traits["avant garde"] -= 20
                traits["bookworm"] += 20
                traits["bot fan"] -= 20
                traits["brooding"] -= 20
                traits["can't stand art"] += 20
                traits["cat person"] += 20
                traits["charismatic"] += 20
                traits["computer whiz"] += 20
                traits["couch potato"] += 20
                traits["dramatic"] -= 20
                traits["easily impressed"] += 20
                traits["eccentric"] -= 20
                traits["excitable"] += 20
                traits["flirty"] -= 20
                traits["frugal"] += 20
                traits["genius"] += 20
                traits["good sense of humour"] += 20
                traits["great kisser"] -= 20
                traits["grumpy"] -= 20
                traits["hates the outdoors"] -= 20
                traits["heavy sleeper"] -= 20
                traits["hot-headed"] -= 20
                traits["hydrophobic"] += 20
                traits["irresistible"] -= 20
                traits["light sleeper"] += 20
                traits["loner"] += 20
                traits["loser"] -= 20
                traits["loves the cold"] -= 20
                traits["loves the heat"] += 20
                traits["loves the outdoors"] += 20
                traits["lucky"] += 20
                traits["natural born performer"] -= 20
                traits["neurotic"] -= 20
                traits["never nude"] -= 20
                traits["night owl"] -= 20
                traits["no sense of humour"] -= 20
                traits["over-emotional"] += 20
                traits["perceptive"] += 20
                traits["photographer's eye"] -= 20
                traits["rebellious"] -= 20
                traits["sailor"] -= 20
                traits["savvy sculptor"] -= 20
                traits["schmoozer"] -= 20
                traits["snob"] += 20
                traits["socially awkward"] += 20
                traits["star quality"] -= 20
                traits["technophobe"] -= 20
                traits["unflirty"] += 20
                traits["unlucky"] -= 20
                traits["vegetarian"] += 20
                traits["vehicle enthusiast"] += 20
                traits["virtuoso"] -= 20
            if value >= 30 and value < 50:
                traits["absent-minded"] -= 20
                traits["angler"] -= 20
                traits["artistic"] += 20
                traits["avant garde"] += 20
                traits["bookworm"] -= 20
                traits["bot fan"] += 20
                traits["brooding"] += 20
                traits["can't stand art"] -= 20
                traits["cat person"] -= 20
                traits["charismatic"] -= 20
                traits["computer whiz"] -= 20
                traits["couch potato"] -= 20
                traits["dramatic"] += 20
                traits["easily impressed"] -= 20
                traits["eccentric"] += 20
                traits["excitable"] -= 20
                traits["flirty"] += 20
                traits["frugal"] -= 20
                traits["genius"] -= 20
                traits["good sense of humour"] -= 20
                traits["great kisser"] += 20
                traits["grumpy"] += 20
                traits["hates the outdoors"] += 20
                traits["heavy sleeper"] += 20
                traits["hot-headed"] += 20
                traits["hydrophobic"] -= 20
                traits["irresistible"] += 20
                traits["light sleeper"] -= 20
                traits["loner"] -= 20
                traits["loser"] += 20
                traits["loves the cold"] += 20
                traits["loves the heat"] -= 20
                traits["loves the outdoors"] -= 20
                traits["lucky"] -= 20
                traits["natural born performer"] += 20
                traits["neurotic"] += 20
                traits["never nude"] += 20
                traits["night owl"] += 20
                traits["no sense of humour"] += 20
                traits["over-emotional"] -= 20
                traits["perceptive"] -= 20
                traits["photographer's eye"] += 20
                traits["rebellious"] += 20
                traits["sailor"] += 20
                traits["savvy sculptor"] += 20
                traits["schmoozer"] += 20
                traits["snob"] -= 20
                traits["socially awkward"] -= 20
                traits["star quality"] += 20
                traits["technophobe"] += 20
                traits["unflirty"] -= 20
                traits["unlucky"] += 20
                traits["vegetarian"] -= 20
                traits["vehicle enthusiast"] -= 20
                traits["virtuoso"] += 20
            if value <= 0:
                traits["adventurous"] -= 20
                traits["ambitious"] += 20
                traits["animal lover"] -= 20
                traits["athletic"] += 20
                traits["born salesman"] += 20
                traits["brave"] -= 20
                traits["childish"] -= 20
                traits["clumsy"] -= 20
                traits["commitment issues"] += 20
                traits["coward"] += 20
                traits["daredevil"] += 20
                traits["disciplined"] -= 20
                traits["dislikes children"] += 20
                traits["diva"] += 20
                traits["dog person"] -= 20
                traits["eco-friendly"] -= 20
                traits["equestrian"] += 20
                traits["evil"] += 20
                traits["family-oriented"] -= 20
                traits["friendly"] -= 20
                traits["gatherer"] -= 20
                traits["good"] -= 20
                traits["green thumb"] -= 20
                traits["handy"] -= 20
                traits["hopeless romantic"] -= 20
                traits["inappropriate"] += 20
                traits["insane"] += 20
                traits["kleptomaniac"] += 20
                traits["mean-spirited"] += 20
                traits["mooch"] += 20
                traits["natural cook"] -= 20
                traits["neat"] -= 20
                traits["nurturing"] -= 20
                traits["party animal"] += 20
                traits["perfectionist"] -= 20
                traits["proper"] -= 20
                traits["shy"] -= 20
                traits["slob"] += 20
                traits["social butterfly"] -= 20
                traits["supernatural fan"] -= 20
                traits["supernatural sceptic"] += 20
                traits["unstable"] += 20
                traits["workaholic"] += 20
        if key == "Fortune":
            if value >= 80:
                traits["absent-minded"] -= 20
                traits["adventurous"] += 20
                traits["ambitious"] += 20
                traits["artistic"] += 20
                traits["avant garde"] += 20
                traits["born salesman"] += 20
                traits["brooding"] += 20
                traits["can't stand art"] -= 20
                traits["childish"] -= 20
                traits["clumsy"] -= 20
                traits["computer whiz"] -= 20
                traits["daredevil"] += 20
                traits["disciplined"] -= 20
                traits["dislikes children"] += 20
                traits["diva"] += 20
                traits["easily impressed"] -= 20
                traits["eco-friendly"] -= 20
                traits["equestrian"] += 20
                traits["evil"] += 20
                traits["excitable"] -= 20
                traits["frugal"] += 20
                traits["good"] -= 20
                traits["good sense of humour"] -= 20
                traits["grumpy"] += 20
                traits["handy"] += 20
                traits["heavy sleeper"] -= 20
                traits["hopeless romantic"] -= 20
                traits["hot-headed"] += 20
                traits["kleptomaniac"] += 20
                traits["light sleeper"] += 20
                traits["loser"] -= 20
                traits["lucky"] += 20
                traits["mean-spirited"] += 20
                traits["mooch"] += 20
                traits["natural born performer"] += 20
                traits["night owl"] -= 20
                traits["no sense of humour"] += 20
                traits["over-emotional"] -= 20
                traits["perceptive"] += 20
                traits["perfectionist"] += 20
                traits["photographer's eye"] += 20
                traits["proper"] += 20
                traits["savvy sculptor"] += 20
                traits["schmoozer"] += 20
                traits["snob"] += 20
                traits["socially awkward"] -= 20
                traits["supernatural fan"] -= 20
                traits["supernatural sceptic"] += 20
                traits["technophobe"] += 20
                traits["unlucky"] -= 20
                traits["vegetarian"] -= 20
                traits["vehicle enthusiast"] += 20
                traits["workaholic"] += 20
            if value >= 50 and value < 80:
                traits["angler"] -= 20
                traits["animal lover"] -= 20
                traits["athletic"] += 20
                traits["bookworm"] += 20
                traits["bot fan"] += 20
                traits["brave"] += 20
                traits["cat person"] += 20
                traits["charismatic"] += 20
                traits["commitment issues"] += 20
                traits["couch potato"] -= 20
                traits["coward"] -= 20
                traits["dog person"] -= 20
                traits["dramatic"] += 20
                traits["eccentric"] += 20
                traits["family-oriented"] -= 20
                traits["flirty"] += 20
                traits["friendly"] -= 20
                traits["gatherer"] -= 20
                traits["genius"] -= 20
                traits["great kisser"] -= 20
                traits["green thumb"] += 20
                traits["hates the outdoors"] += 20
                traits["hydrophobic"] -= 20
                traits["inappropriate"] += 20
                traits["insane"] += 20
                traits["irresistible"] += 20
                traits["loner"] += 20
                traits["loves the cold"] += 20
                traits["loves the heat"] -= 20
                traits["loves the outdoors"] -= 20
                traits["natural cook"] -= 20
                traits["neat"] += 20
                traits["neurotic"] += 20
                traits["never nude"] += 20
                traits["nurturing"] -= 20
                traits["party animal"] -= 20
                traits["rebellious"] += 20
                traits["sailor"] -= 20
                traits["shy"] -= 20
                traits["slob"] -= 20
                traits["social butterfly"] += 20
                traits["star quality"] += 20
                traits["unflirty"] -= 20
                traits["unstable"] += 20
                traits["virtuoso"] += 20
            if value >= 30 and value < 50:
                traits["angler"] += 20
                traits["animal lover"] += 20
                traits["athletic"] -= 20
                traits["bookworm"] -= 20
                traits["bot fan"] -= 20
                traits["brave"] -= 20
                traits["cat person"] -= 20
                traits["charismatic"] -= 20
                traits["commitment issues"] -= 20
                traits["couch potato"] += 20
                traits["coward"] += 20
                traits["dog person"] += 20
                traits["dramatic"] -= 20
                traits["eccentric"] -= 20
                traits["family-oriented"] += 20
                traits["flirty"] -= 20
                traits["friendly"] += 20
                traits["gatherer"] += 20
                traits["genius"] += 20
                traits["great kisser"] += 20
                traits["green thumb"] -= 20
                traits["hates the outdoors"] -= 20
                traits["hydrophobic"] += 20
                traits["inappropriate"] -= 20
                traits["insane"] -= 20
                traits["irresistible"] -= 20
                traits["loner"] -= 20
                traits["loves the cold"] -= 20
                traits["loves the heat"] += 20
                traits["loves the outdoors"] += 20
                traits["natural cook"] += 20
                traits["neat"] -= 20
                traits["neurotic"] -= 20
                traits["never nude"] -= 20
                traits["nurturing"] += 20
                traits["party animal"] += 20
                traits["rebellious"] -= 20
                traits["sailor"] += 20
                traits["shy"] += 20
                traits["slob"] += 20
                traits["social butterfly"] -= 20
                traits["star quality"] -= 20
                traits["unflirty"] += 20
                traits["unstable"] -= 20
                traits["virtuoso"] -= 20
            if value <= 0:
                traits["absent-minded"] += 20
                traits["adventurous"] -= 20
                traits["ambitious"] -= 20
                traits["artistic"] -= 20
                traits["avant garde"] -= 20
                traits["born salesman"] -= 20
                traits["brooding"] -= 20
                traits["can't stand art"] += 20
                traits["childish"] += 20
                traits["clumsy"] += 20
                traits["computer whiz"] += 20
                traits["daredevil"] -= 20
                traits["disciplined"] += 20
                traits["dislikes children"] -= 20
                traits["diva"] -= 20
                traits["easily impressed"] += 20
                traits["eco-friendly"] += 20
                traits["equestrian"] -= 20
                traits["evil"] -= 20
                traits["excitable"] += 20
                traits["frugal"] -= 20
                traits["good"] += 20
                traits["good sense of humour"] += 20
                traits["grumpy"] -= 20
                traits["handy"] -= 20
                traits["heavy sleeper"] += 20
                traits["hopeless romantic"] += 20
                traits["hot-headed"] -= 20
                traits["kleptomaniac"] -= 20
                traits["light sleeper"] -= 20
                traits["loser"] += 20
                traits["lucky"] -= 20
                traits["mean-spirited"] -= 20
                traits["mooch"] -= 20
                traits["natural born performer"] -= 20
                traits["night owl"] += 20
                traits["no sense of humour"] -= 20
                traits["over-emotional"] += 20
                traits["perceptive"] -= 20
                traits["perfectionist"] -= 20
                traits["photographer's eye"] -= 20
                traits["proper"] -= 20
                traits["savvy sculptor"] -= 20
                traits["schmoozer"] -= 20
                traits["snob"] -= 20
                traits["socially awkward"] += 20
                traits["supernatural fan"] += 20
                traits["supernatural sceptic"] -= 20
                traits["technophobe"] -= 20
                traits["unlucky"] += 20
                traits["vegetarian"] += 20
                traits["vehicle enthusiast"] -= 20
                traits["workaholic"] -= 20
        if key == "Knowledge":
            if value >= 80:
                traits["adventurous"] += 20
                traits["angler"] += 20
                traits["artistic"] -= 20
                traits["avant garde"] -= 20
                traits["bookworm"] += 20
                traits["bot fan"] += 20
                traits["brooding"] += 20
                traits["cat person"] += 20
                traits["charismatic"] -= 20
                traits["commitment issues"] -= 20
                traits["computer whiz"] += 20
                traits["daredevil"] -= 20
                traits["disciplined"] += 20
                traits["dramatic"] -= 20
                traits["easily impressed"] -= 20
                traits["eccentric"] += 20
                traits["equestrian"] -= 20
                traits["evil"] += 20
                traits["flirty"] -= 20
                traits["gatherer"] += 20
                traits["genius"] += 20
                traits["good sense of humour"] -= 20
                traits["great kisser"] -= 20
                traits["green thumb"] += 20
                traits["grumpy"] += 20
                traits["handy"] += 20
                traits["hates the outdoors"] += 20
                traits["heavy sleeper"] -= 20
                traits["hot-headed"] += 20
                traits["hydrophobic"] += 20
                traits["irresistible"] -= 20
                traits["light sleeper"] += 20
                traits["loner"] += 20
                traits["loves the cold"] += 20
                traits["loves the heat"] -= 20
                traits["loves the outdoors"] -= 20
                traits["natural born performer"] -= 20
                traits["neat"] += 20
                traits["neurotic"] += 20
                traits["never nude"] += 20
                traits["night owl"] += 20
                traits["no sense of humour"] += 20
                traits["over-emotional"] -= 20
                traits["party animal"] -= 20
                traits["perceptive"] += 20
                traits["perfectionist"] += 20
                traits["photographer's eye"] -= 20
                traits["proper"] += 20
                traits["rebellious"] -= 20
                traits["savvy sculptor"] -= 20
                traits["shy"] += 20
                traits["slob"] -= 20
                traits["snob"] += 20
                traits["socially awkward"] += 20
                traits["supernatural fan"] += 20
                traits["supernatural sceptic"] -= 20
                traits["technophobe"] -= 20
                traits["unflirty"] += 20
                traits["virtuoso"] -= 20
            if value >= 50 and value < 80:
                traits["absent-minded"] -= 20
                traits["ambitious"] += 20
                traits["animal lover"] -= 20
                traits["athletic"] -= 20
                traits["born salesman"] -= 20
                traits["brave"] += 20
                traits["can't stand art"] += 20
                traits["childish"] += 20
                traits["clumsy"] -= 20
                traits["couch potato"] += 20
                traits["coward"] -= 20
                traits["dislikes children"] -= 20
                traits["diva"] -= 20
                traits["dog person"] -= 20
                traits["eco-friendly"] += 20
                traits["excitable"] -= 20
                traits["family-oriented"] += 20
                traits["friendly"] += 20
                traits["frugal"] += 20
                traits["good"] += 20
                traits["hopeless romantic"] += 20
                traits["inappropriate"] += 20
                traits["insane"] += 20
                traits["kleptomaniac"] += 20
                traits["loser"] += 20
                traits["lucky"] -= 20
                traits["mean-spirited"] += 20
                traits["mooch"] -= 20
                traits["natural cook"] += 20
                traits["nurturing"] += 20
                traits["sailor"] -= 20
                traits["schmoozer"] -= 20
                traits["social butterfly"] -= 20
                traits["star quality"] -= 20
                traits["unlucky"] += 20
                traits["unstable"] += 20
                traits["vegetarian"] -= 20
                traits["vehicle enthusiast"] += 20
                traits["workaholic"] += 20
            if value >= 30 and value < 50:
                traits["absent-minded"] += 20
                traits["ambitious"] -= 20
                traits["animal lover"] += 20
                traits["athletic"] += 20
                traits["born salesman"] += 20
                traits["brave"] -= 20
                traits["can't stand art"] -= 20
                traits["childish"] -= 20
                traits["clumsy"] += 20
                traits["couch potato"] -= 20
                traits["coward"] += 20
                traits["dislikes children"] += 20
                traits["diva"] += 20
                traits["dog person"] += 20
                traits["eco-friendly"] -= 20
                traits["excitable"] += 20
                traits["family-oriented"] -= 20
                traits["friendly"] -= 20
                traits["frugal"] -= 20
                traits["good"] -= 20
                traits["hopeless romantic"] -= 20
                traits["inappropriate"] -= 20
                traits["insane"] -= 20
                traits["kleptomaniac"] -= 20
                traits["loser"] -= 20
                traits["lucky"] += 20
                traits["mean-spirited"] -= 20
                traits["mooch"] += 20
                traits["natural cook"] -= 20
                traits["nurturing"] -= 20
                traits["sailor"] += 20
                traits["schmoozer"] += 20
                traits["social butterfly"] += 20
                traits["star quality"] += 20
                traits["unlucky"] -= 20
                traits["unstable"] -= 20
                traits["vegetarian"] += 20
                traits["vehicle enthusiast"] -= 20
                traits["workaholic"] -= 20
            if value <= 0:
                traits["adventurous"] -= 20
                traits["angler"] -= 20
                traits["artistic"] += 20
                traits["avant garde"] += 20
                traits["bookworm"] -= 20
                traits["bot fan"] -= 20
                traits["brooding"] -= 20
                traits["cat person"] -= 20
                traits["charismatic"] += 20
                traits["commitment issues"] += 20
                traits["computer whiz"] -= 20
                traits["daredevil"] += 20
                traits["disciplined"] -= 20
                traits["dramatic"] += 20
                traits["easily impressed"] += 20
                traits["eccentric"] -= 20
                traits["equestrian"] += 20
                traits["evil"] -= 20
                traits["flirty"] += 20
                traits["gatherer"] -= 20
                traits["genius"] -= 20
                traits["good sense of humour"] += 20
                traits["great kisser"] += 20
                traits["green thumb"] -= 20
                traits["grumpy"] -= 20
                traits["handy"] -= 20
                traits["hates the outdoors"] -= 20
                traits["heavy sleeper"] += 20
                traits["hot-headed"] -= 20
                traits["hydrophobic"] -= 20
                traits["irresistible"] += 20
                traits["light sleeper"] -= 20
                traits["loner"] -= 20
                traits["loves the cold"] -= 20
                traits["loves the heat"] += 20
                traits["loves the outdoors"] += 20
                traits["natural born performer"] += 20
                traits["neat"] -= 20
                traits["neurotic"] -= 20
                traits["never nude"] -= 20
                traits["night owl"] -= 20
                traits["no sense of humour"] -= 20
                traits["over-emotional"] += 20
                traits["party animal"] += 20
                traits["perceptive"] -= 20
                traits["perfectionist"] -= 20
                traits["photographer's eye"] += 20
                traits["proper"] -= 20
                traits["rebellious"] += 20
                traits["savvy sculptor"] += 20
                traits["shy"] -= 20
                traits["slob"] += 20
                traits["snob"] -= 20
                traits["socially awkward"] -= 20
                traits["supernatural fan"] -= 20
                traits["supernatural sceptic"] += 20
                traits["technophobe"] += 20
                traits["unflirty"] -= 20
                traits["virtuoso"] += 20
        if key == "Pleasure":
            if value >= 80:
                traits["absent-minded"] += 20
                traits["adventurous"] += 20
                traits["ambitious"] -= 20
                traits["animal lover"] += 20
                traits["bookworm"] -= 20
                traits["bot fan"] -= 20
                traits["brooding"] -= 20
                traits["can't stand art"] -= 20
                traits["charismatic"] += 20
                traits["childish"] += 20
                traits["computer whiz"] += 20
                traits["couch potato"] += 20
                traits["coward"] += 20
                traits["dislikes children"] -= 20
                traits["easily impressed"] += 20
                traits["equestrian"] += 20
                traits["evil"] -= 20
                traits["excitable"] += 20
                traits["flirty"] += 20
                traits["friendly"] += 20
                traits["genius"] -= 20
                traits["good"] += 20
                traits["good sense of humour"] += 20
                traits["great kisser"] += 20
                traits["grumpy"] -= 20
                traits["handy"] += 20
                traits["heavy sleeper"] += 20
                traits["hopeless romantic"] += 20
                traits["hydrophobic"] -= 20
                traits["light sleeper"] -= 20
                traits["loser"] += 20
                traits["lucky"] -= 20
                traits["natural born performer"] += 20
                traits["night owl"] += 20
                traits["no sense of humour"] -= 20
                traits["over-emotional"] += 20
                traits["perfectionist"] -= 20
                traits["proper"] -= 20
                traits["schmoozer"] += 20
                traits["slob"] += 20
                traits["social butterfly"] += 20
                traits["socially awkward"] -= 20
                traits["star quality"] += 20
                traits["technophobe"] -= 20
                traits["unflirty"] -= 20
                traits["unlucky"] -= 20
                traits["vehicle enthusiast"] += 20
                traits["workaholic"] -= 20
            if value >= 50 and value < 80:
                traits["angler"] -= 20
                traits["artistic"] -= 20
                traits["avant garde"] -= 20
                traits["born salesman"] -= 20
                traits["brave"] -= 20
                traits["cat person"] -= 20
                traits["clumsy"] += 20
                traits["commitment issues"] += 20
                traits["daredevil"] += 20
                traits["disciplined"] -= 20
                traits["diva"] -= 20
                traits["dog person"] += 20
                traits["dramatic"] += 20
                traits["eccentric"] -= 20
                traits["eco-friendly"] -= 20
                traits["family-oriented"] += 20
                traits["frugal"] -= 20
                traits["gatherer"] += 20
                traits["green thumb"] -= 20
                traits["hates the outdoors"] += 20
                traits["hot-headed"] -= 20
                traits["inappropriate"] += 20
                traits["insane"] += 20
                traits["irresistible"] += 20
                traits["kleptomaniac"] += 20
                traits["loner"] -= 20
                traits["loves the cold"] += 20
                traits["loves the heat"] -= 20
                traits["loves the outdoors"] -= 20
                traits["mean-spirited"] -= 20
                traits["mooch"] += 20
                traits["natural cook"] -= 20
                traits["neat"] -= 20
                traits["neurotic"] += 20
                traits["never nude"] -= 20
                traits["nurturing"] += 20
                traits["party animal"] += 20
                traits["perceptive"] += 20
                traits["photographer's eye"] -= 20
                traits["rebellious"] += 20
                traits["sailor"] += 20
                traits["savvy sculptor"] -= 20
                traits["shy"] -= 20
                traits["snob"] -= 20
                traits["supernatural fan"] += 20
                traits["supernatural sceptic"] -= 20
                traits["unstable"] += 20
                traits["vegetarian"] -= 20
                traits["virtuoso"] -= 20
            if value >= 30 and value < 50:
                traits["angler"] += 20
                traits["artistic"] += 20
                traits["avant garde"] += 20
                traits["born salesman"] += 20
                traits["brave"] += 20
                traits["cat person"] += 20
                traits["clumsy"] -= 20
                traits["commitment issues"] -= 20
                traits["daredevil"] -= 20
                traits["disciplined"] += 20
                traits["diva"] += 20
                traits["dog person"] -= 20
                traits["dramatic"] -= 20
                traits["eccentric"] += 20
                traits["eco-friendly"] += 20
                traits["family-oriented"] -= 20
                traits["frugal"] += 20
                traits["gatherer"] -= 20
                traits["green thumb"] += 20
                traits["hates the outdoors"] -= 20
                traits["hot-headed"] += 20
                traits["inappropriate"] -= 20
                traits["insane"] -= 20
                traits["irresistible"] -= 20
                traits["kleptomaniac"] -= 20
                traits["loner"] += 20
                traits["loves the cold"] -= 20
                traits["loves the heat"] += 20
                traits["loves the outdoors"] += 20
                traits["mean-spirited"] += 20
                traits["mooch"] -= 20
                traits["natural cook"] += 20
                traits["neat"] += 20
                traits["neurotic"] -= 20
                traits["never nude"] += 20
                traits["nurturing"] -= 20
                traits["party animal"] -= 20
                traits["perceptive"] -= 20
                traits["photographer's eye"] += 20
                traits["rebellious"] -= 20
                traits["sailor"] -= 20
                traits["savvy sculptor"] += 20
                traits["shy"] += 20
                traits["snob"] += 20
                traits["supernatural fan"] -= 20
                traits["supernatural sceptic"] += 20
                traits["unstable"] -= 20
                traits["vegetarian"] += 20
                traits["virtuoso"] += 20
            if value <= 0:
                traits["absent-minded"] -= 20
                traits["adventurous"] -= 20
                traits["ambitious"] += 20
                traits["animal lover"] -= 20
                traits["bookworm"] += 20
                traits["bot fan"] += 20
                traits["brooding"] += 20
                traits["can't stand art"] += 20
                traits["charismatic"] -= 20
                traits["childish"] -= 20
                traits["computer whiz"] -= 20
                traits["couch potato"] -= 20
                traits["coward"] -= 20
                traits["dislikes children"] += 20
                traits["easily impressed"] -= 20
                traits["equestrian"] -= 20
                traits["evil"] += 20
                traits["excitable"] -= 20
                traits["flirty"] -= 20
                traits["friendly"] -= 20
                traits["genius"] += 20
                traits["good"] -= 20
                traits["good sense of humour"] -= 20
                traits["great kisser"] -= 20
                traits["grumpy"] += 20
                traits["handy"] -= 20
                traits["heavy sleeper"] -= 20
                traits["hopeless romantic"] -= 20
                traits["hydrophobic"] += 20
                traits["light sleeper"] += 20
                traits["loser"] -= 20
                traits["lucky"] += 20
                traits["natural born performer"] -= 20
                traits["night owl"] -= 20
                traits["no sense of humour"] += 20
                traits["over-emotional"] -= 20
                traits["perfectionist"] += 20
                traits["proper"] += 20
                traits["schmoozer"] -= 20
                traits["slob"] -= 20
                traits["social butterfly"] -= 20
                traits["socially awkward"] += 20
                traits["star quality"] -= 20
                traits["technophobe"] += 20
                traits["unflirty"] += 20
                traits["unlucky"] -= 20
                traits["vehicle enthusiast"] -= 20
                traits["workaholic"] += 20
        if key == "Popularity":
            if value >= 80:
                traits["absent-minded"] += 20
                traits["angler"] -= 20
                traits["animal lover"] += 20
                traits["artistic"] += 20
                traits["athletic"] += 20
                traits["brave"] += 20
                traits["brooding"] -= 20
                traits["can't stand art"] -= 20
                traits["charismatic"] += 20
                traits["couch potato"] += 20
                traits["coward"] -= 20
                traits["daredevil"] += 20
                traits["diva"] += 20
                traits["dog person"] += 20
                traits["dramatic"] += 20
                traits["easily impressed"] += 20
                traits["eccentric"] -= 20
                traits["equestrian"] += 20
                traits["evil"] -= 20
                traits["excitable"] += 20
                traits["friendly"] += 20
                traits["good"] += 20
                traits["good sense of humour"] += 20
                traits["grumpy"] -= 20
                traits["handy"] -= 20
                traits["hates the outdoors"] -= 20
                traits["heavy sleeper"] += 20
                traits["kleptomaniac"] -= 20
                traits["light sleeper"] -= 20
                traits["loner"] -= 20
                traits["loves the cold"] -= 20
                traits["loves the heat"] += 20
                traits["loves the outdoors"] += 20
                traits["mean-spirited"] -= 20
                traits["mooch"] += 20
                traits["natural born performer"] += 20
                traits["natural cook"] += 20
                traits["no sense of humour"] -= 20
                traits["over-emotional"] += 20
                traits["party animal"] += 20
                traits["photographer's eye"] += 20
                traits["rebellious"] += 20
                traits["sailor"] += 20
                traits["savvy sculptor"] += 20
                traits["schmoozer"] += 20
                traits["shy"] -= 20
                traits["snob"] -= 20
                traits["social butterfly"] += 20
                traits["socially awkward"] -= 20
                traits["star quality"] += 20
                traits["vehicle enthusiast"] += 20
                traits["virtuoso"] += 20
            if value >= 50 and value < 80:
                traits["ambitious"] += 20
                traits["avant garde"] += 20
                traits["bookworm"] += 20
                traits["born salesman"] += 20
                traits["bot fan"] += 20
                traits["cat person"] -= 20
                traits["childish"] += 20
                traits["clumsy"] += 20
                traits["commitment issues"] += 20
                traits["computer whiz"] += 20
                traits["disciplined"] -= 20
                traits["dislikes children"] -= 20
                traits["eco-friendly"] -= 20
                traits["family-oriented"] += 20
                traits["flirty"] += 20
                traits["frugal"] += 20
                traits["gatherer"] -= 20
                traits["genius"] -= 20
                traits["great kisser"] += 20
                traits["green thumb"] += 20
                traits["hopeless romantic"] -= 20
                traits["hot-headed"] -= 20
                traits["hydrophobic"] -= 20
                traits["inappropriate"] -= 20
                traits["insane"] -= 20
                traits["irresistible"] += 20
                traits["loser"] -= 20
                traits["lucky"] += 20
                traits["neat"] -= 20
                traits["neurotic"] += 20
                traits["never nude"] -= 20
                traits["night owl"] += 20
                traits["nurturing"] += 20
                traits["perceptive"] -= 20
                traits["perfectionist"] += 20
                traits["proper"] += 20
                traits["slob"] += 20
                traits["supernatural fan"] += 20
                traits["supernatural sceptic"] -= 20
                traits["technophobe"] -= 20
                traits["unflirty"] += 20
                traits["unlucky"] -= 20
                traits["unstable"] -= 20
                traits["vegetarian"] += 20
                traits["workaholic"] += 20
            if value >= 30 and value < 50:
                traits["ambitious"] -= 20
                traits["avant garde"] -= 20
                traits["bookworm"] -= 20
                traits["born salesman"] -= 20
                traits["bot fan"] -= 20
                traits["cat person"] += 20
                traits["childish"] -= 20
                traits["clumsy"] -= 20
                traits["commitment issues"] -= 20
                traits["computer whiz"] -= 20
                traits["disciplined"] += 20
                traits["dislikes children"] += 20
                traits["eco-friendly"] += 20
                traits["family-oriented"] -= 20
                traits["flirty"] -= 20
                traits["frugal"] -= 20
                traits["gatherer"] += 20
                traits["genius"] += 20
                traits["great kisser"] -= 20
                traits["green thumb"] -= 20
                traits["hopeless romantic"] += 20
                traits["hot-headed"] += 20
                traits["hydrophobic"] += 20
                traits["inappropriate"] += 20
                traits["insane"] += 20
                traits["irresistible"] -= 20
                traits["loser"] += 20
                traits["lucky"] -= 20
                traits["neat"] += 20
                traits["neurotic"] -= 20
                traits["never nude"] += 20
                traits["night owl"] -= 20
                traits["nurturing"] -= 20
                traits["perceptive"] += 20
                traits["perfectionist"] -= 20
                traits["proper"] -= 20
                traits["slob"] -= 20
                traits["supernatural fan"] -= 20
                traits["supernatural sceptic"] += 20
                traits["technophobe"] += 20
                traits["unflirty"] -= 20
                traits["unlucky"] += 20
                traits["unstable"] += 20
                traits["vegetarian"] -= 20
                traits["workaholic"] -= 20
            if value <= 0:
                traits["absent-minded"] -= 20
                traits["angler"] += 20
                traits["animal lover"] -= 20
                traits["artistic"] -= 20
                traits["athletic"] -= 20
                traits["brave"] -= 20
                traits["brooding"] += 20
                traits["can't stand art"] += 20
                traits["charismatic"] -= 20
                traits["couch potato"] -= 20
                traits["coward"] += 20
                traits["daredevil"] -= 20
                traits["diva"] -= 20
                traits["dog person"] -= 20
                traits["dramatic"] -= 20
                traits["easily impressed"] -= 20
                traits["eccentric"] += 20
                traits["equestrian"] -= 20
                traits["evil"] += 20
                traits["excitable"] -= 20
                traits["friendly"] -= 20
                traits["good"] -= 20
                traits["good sense of humour"] -= 20
                traits["grumpy"] += 20
                traits["handy"] += 20
                traits["hates the outdoors"] += 20
                traits["heavy sleeper"] -= 20
                traits["kleptomaniac"] += 20
                traits["light sleeper"] += 20
                traits["loner"] += 20
                traits["loves the cold"] += 20
                traits["loves the heat"] -= 20
                traits["loves the outdoors"] -= 20
                traits["mean-spirited"] += 20
                traits["mooch"] -= 20
                traits["natural born performer"] -= 20
                traits["natural cook"] -= 20
                traits["no sense of humour"] += 20
                traits["over-emotional"] -= 20
                traits["party animal"] -= 20
                traits["photographer's eye"] -= 20
                traits["rebellious"] -= 20
                traits["sailor"] -= 20
                traits["savvy sculptor"] -= 20
                traits["schmoozer"] -= 20
                traits["shy"] += 20
                traits["snob"] += 20
                traits["social butterfly"] -= 20
                traits["socially awkward"] += 20
                traits["star quality"] -= 20
                traits["vehicle enthusiast"] -= 20
                traits["virtuoso"] -= 20
        if key == "Romance":
            if value >= 80:
                traits["adventurous"] += 20
                traits["ambitious"] -= 20
                traits["artistic"] += 20
                traits["athletic"] += 20
                traits["bot fan"] -= 20
                traits["can't stand art"] -= 20
                traits["cat person"] -= 20
                traits["charismatic"] += 20
                traits["childish"] -= 20
                traits["commitment issues"] += 20
                traits["couch potato"] -= 20
                traits["daredevil"] += 20
                traits["dislikes children"] += 20
                traits["diva"] += 20
                traits["eco-friendly"] -= 20
                traits["family-oriented"] -= 20
                traits["flirty"] += 20
                traits["genius"] -= 20
                traits["great kisser"] += 20
                traits["green thumb"] -= 20
                traits["handy"] -= 20
                traits["hates the outdoors"] -= 20
                traits["heavy sleeper"] -= 20
                traits["hopeless romantic"] -= 20
                traits["hot-headed"] += 20
                traits["hydrophobic"] -= 20
                traits["irresistible"] += 20
                traits["light sleeper"] += 20
                traits["loner"] -= 20
                traits["loves the cold"] -= 20
                traits["loves the heat"] += 20
                traits["loves the outdoors"] += 20
                traits["mooch"] += 20
                traits["natural born performer"] += 20
                traits["natural cook"] -= 20
                traits["neat"] -= 20
                traits["neurotic"] -= 20
                traits["never nude"] -= 20
                traits["nurturing"] -= 20
                traits["over-emotional"] -= 20
                traits["party animal"] += 20
                traits["perceptive"] -= 20
                traits["photographer's eye"] += 20
                traits["proper"] -= 20
                traits["rebellious"] += 20
                traits["sailor"] += 20
                traits["savvy sculptor"] += 20
                traits["shy"] -= 20
                traits["slob"] += 20
                traits["star quality"] += 20
                traits["supernatural fan"] -= 20
                traits["supernatural sceptic"] += 20
                traits["technophobe"] += 20
                traits["unflirty"] -= 20
                traits["vegetarian"] -= 20
                traits["virtuoso"] += 20
                traits["workaholic"] += 20
            if value >= 50 and value < 80:
                traits["absent-minded"] -= 20
                traits["angler"] -= 20
                traits["animal lover"] -= 20
                traits["avant garde"] += 20
                traits["bookworm"] -= 20
                traits["born salesman"] -= 20
                traits["brave"] += 20
                traits["brooding"] += 20
                traits["clumsy"] -= 20
                traits["computer whiz"] -= 20
                traits["coward"] -= 20
                traits["disciplined"] -= 20
                traits["dog person"] += 20
                traits["dramatic"] += 20
                traits["easily impressed"] -= 20
                traits["eccentric"] -= 20
                traits["equestrian"] += 20
                traits["evil"] += 20
                traits["excitable"] -= 20
                traits["friendly"] -= 20
                traits["frugal"] -= 20
                traits["gatherer"] -= 20
                traits["good"] -= 20
                traits["good sense of humour"] += 20
                traits["grumpy"] += 20
                traits["inappropriate"] += 20
                traits["insane"] += 20
                traits["kleptomaniac"] += 20
                traits["loser"] -= 20
                traits["lucky"] += 20
                traits["mean-spirited"] += 20
                traits["night owl"] += 20
                traits["no sense of humour"] -= 20
                traits["perfectionist"] -= 20
                traits["schmoozer"] += 20
                traits["snob"] += 20
                traits["social butterfly"] += 20
                traits["socially awkward"] -= 20
                traits["unlucky"] -= 20
                traits["unstable"] += 20
                traits["vehicle enthusiast"] += 20
            if value >= 30 and value < 50:
                traits["absent-minded"] += 20
                traits["angler"] += 20
                traits["animal lover"] += 20
                traits["avant garde"] -= 20
                traits["bookworm"] += 20
                traits["born salesman"] += 20
                traits["brave"] -= 20
                traits["brooding"] -= 20
                traits["clumsy"] += 20
                traits["computer whiz"] += 20
                traits["coward"] += 20
                traits["disciplined"] += 20
                traits["dog person"] -= 20
                traits["dramatic"] -= 20
                traits["easily impressed"] += 20
                traits["eccentric"] += 20
                traits["equestrian"] -= 20
                traits["evil"] -= 20
                traits["excitable"] += 20
                traits["friendly"] += 20
                traits["frugal"] += 20
                traits["gatherer"] += 20
                traits["good"] += 20
                traits["good sense of humour"] -= 20
                traits["grumpy"] -= 20
                traits["inappropriate"] -= 20
                traits["insane"] -= 20
                traits["kleptomaniac"] -= 20
                traits["loser"] += 20
                traits["lucky"] -= 20
                traits["mean-spirited"] -= 20
                traits["night owl"] -= 20
                traits["no sense of humour"] += 20
                traits["perfectionist"] += 20
                traits["schmoozer"] -= 20
                traits["snob"] -= 20
                traits["social butterfly"] -= 20
                traits["socially awkward"] += 20
                traits["unlucky"] += 20
                traits["unstable"] -= 20
                traits["vehicle enthusiast"] -= 20
            if value <= 0:
                traits["adventurous"] -= 20
                traits["ambitious"] += 20
                traits["artistic"] -= 20
                traits["athletic"] -= 20
                traits["bot fan"] += 20
                traits["can't stand art"] += 20
                traits["cat person"] += 20
                traits["charismatic"] -= 20
                traits["childish"] += 20
                traits["commitment issues"] -= 20
                traits["couch potato"] += 20
                traits["daredevil"] -= 20
                traits["dislikes children"] -= 20
                traits["diva"] -= 20
                traits["eco-friendly"] += 20
                traits["family-oriented"] += 20
                traits["flirty"] -= 20
                traits["genius"] += 20
                traits["great kisser"] -= 20
                traits["green thumb"] += 20
                traits["handy"] += 20
                traits["hates the outdoors"] += 20
                traits["heavy sleeper"] += 20
                traits["hopeless romantic"] += 20
                traits["hot-headed"] -= 20
                traits["hydrophobic"] += 20
                traits["irresistible"] -= 20
                traits["light sleeper"] -= 20
                traits["loner"] += 20
                traits["loves the cold"] += 20
                traits["loves the heat"] -= 20
                traits["loves the outdoors"] -= 20
                traits["mooch"] -= 20
                traits["natural born performer"] -= 20
                traits["natural cook"] += 20
                traits["neat"] += 20
                traits["neurotic"] += 20
                traits["never nude"] += 20
                traits["nurturing"] += 20
                traits["over-emotional"] += 20
                traits["party animal"] -= 20
                traits["perceptive"] += 20
                traits["photographer's eye"] -= 20
                traits["proper"] += 20
                traits["rebellious"] -= 20
                traits["sailor"] -= 20
                traits["savvy sculptor"] -= 20
                traits["shy"] += 20
                traits["slob"] -= 20
                traits["star quality"] -= 20
                traits["supernatural fan"] += 20
                traits["supernatural sceptic"] -= 20
                traits["technophobe"] -= 20
                traits["unflirty"] += 20
                traits["vegetarian"] += 20
                traits["virtuoso"] -= 20
                traits["workaholic"] -= 20
