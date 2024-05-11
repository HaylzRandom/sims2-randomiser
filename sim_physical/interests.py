# Get Interests - Politics, Crime, Food, Sports, Work, School, Money, Entertainment, Health, Paranormal, Weather, Toys, Environment, Culture, Fashion, Travel, Animals and SciFi
def get_interests():
    interests = {
        "Politics": 0,
        "Crime": 0,
        "Food": 0,
        "Sports": 0,
        "Work": 0,
        "School": 0,
        "Money": 0,
        "Entertainment": 0,
        "Health": 0,
        "Paranormal": 0,
        "Weather": 0,
        "Toys": 0,
        "Environment": 0,
        "Culture": 0,
        "Fashion": 0,
        "Travel": 0,
        "Animals": 0,
        "SciFi": 0,
    }

    print("\nInterest Values\n")

    for interest in interests:
        interests[interest] = int(input(f"Please enter value for {interest}: "))

    return interests.values()


def interests_aspiration(
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
    # aspiration_choice["Family"] += school + toys + animals + food
    # aspiration_choice["Fortune"] += crime + money + work + politics
    # aspiration_choice["Knowledge"] += weather + paranormal + environment + sciFi
    # aspiration_choice["Pleasure"] += food + entertainment + culture + travel
    # aspiration_choice["Popularity"] += politics + sports + fashion + entertainment
    # aspiration_choice["Romance"] += fashion + travel + health + culture

    # Politics
    if politics >= 6:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] -= 5

    # Crime
    if crime >= 6:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] -= 5

    # Food
    if food >= 6:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] -= 5

    # Sports
    if sports >= 6:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] -= 5

    # Work
    if work >= 6:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] -= 5
    else:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] += 5

    # School
    if school >= 6:
        aspirations["Family"] += 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] -= 5
    else:
        aspirations["Family"] -= 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] += 5

    # Money
    if money >= 6:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] -= 5

    # Entertainment
    if entertainment >= 6:
        aspirations["Family"] -= 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] += 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] -= 5

    # Health
    if health >= 6:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] -= 5

    # Paranormal
    if paranormal >= 6:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] -= 5
    else:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] += 5

    # Weather
    if weather >= 6:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] -= 5
    else:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] += 5

    # Toys
    if toys >= 6:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] -= 5
    else:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] += 5

    # Environment
    if environment >= 6:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] -= 5
    else:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] += 5

    # Culture
    if culture >= 6:
        aspirations["Family"] -= 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] += 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] -= 5

    # Fashion
    if fashion >= 6:
        aspirations["Family"] -= 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] += 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] -= 5

    # Travel
    if travel >= 6:
        aspirations["Family"] -= 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] += 5
    else:
        aspirations["Family"] += 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] -= 5

    # Animals
    if animals >= 6:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] -= 5
    else:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] += 5

    # SciFi
    if sciFi >= 6:
        aspirations["Family"] += 5
        aspirations["Fortune"] -= 5
        aspirations["Knowledge"] += 5
        aspirations["Pleasure"] += 5
        aspirations["Popularity"] -= 5
        aspirations["Romance"] -= 5
    else:
        aspirations["Family"] -= 5
        aspirations["Fortune"] += 5
        aspirations["Knowledge"] -= 5
        aspirations["Pleasure"] -= 5
        aspirations["Popularity"] += 5
        aspirations["Romance"] += 5

    return aspirations


def interests_traits(
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
):

    if age == "toddler":

        # Crime
        if crime == 10:
            traits["evil"] += 5
            traits["good"] -= 5
        if crime >= 9:
            traits["brave"] += 5
            traits["perceptive"] += 5
            traits["insane"] += 5
        if crime >= 8:
            traits["excitable"] -= 5
        if crime <= 2:
            traits["excitable"] += 5
            traits["brave"] -= 5
            traits["perceptive"] -= 5
            traits["insane"] -= 5
        if crime == 0:
            traits["good"] += 5
            traits["evil"] -= 5

        # Culture
        if culture >= 8:
            traits["virtuoso"] += 5
        if culture >= 7:
            traits["artistic"] += 5
        if culture == 6:
            traits["easily impressed"] += 5
        if culture <= 3:
            traits["virtuoso"] -= 5
            traits["artistic"] -= 5

        # Entertainment
        if entertainment >= 8:
            traits["couch potato"] += 5
            traits["virtuoso"] += 5
            traits["loner"] -= 5
        if entertainment <= 2:
            traits["loner"] += 5
            traits["couch potato"] -= 5
            traits["virtuoso"] -= 5

        # Environment
        if environment >= 9:
            traits["neurotic"] -= 5
        if environment >= 8:
            traits["loves the outdoors"] += 5
            traits["hates the outdoors"] -= 5
            traits["absent-minded"] -= 5
            traits["clumsy"] -= 5
            traits["grumpy"] -= 5
        if environment <= 5:
            traits["neurotic"] += 5
        if environment <= 3:
            traits["absent-minded"] += 5
            traits["clumsy"] += 5
            traits["grumpy"] += 5
        if environment <= 2:
            traits["hates the outdoors"] += 5
            traits["loves the outdoors"] -= 5

        # Food
        if food >= 8:
            traits["slob"] += 5
            traits["absent-minded"] -= 5
        if food <= 2:
            traits["absent-minded"] += 5
            traits["slob"] -= 5

        # Health
        if health >= 9:
            traits["brave"] += 5
            traits["neurotic"] += 5
            traits["absent-minded"] -= 5
            traits["hates the outdoors"] -= 5
            traits["insane"] -= 5
            traits["couch potato"] -= 5
            traits["slob"] -= 5
        if health >= 8:
            traits["disciplined"] += 5
        if health <= 3:
            traits["couch potato"] += 5
            traits["slob"] += 5
        if health <= 2:
            traits["absent-minded"] += 5
            traits["hates the outdoors"] += 5
            traits["insane"] += 5
            traits["brave"] -= 5
            traits["neurotic"] -= 5
            traits["disciplined"] -= 5

        # Money
        if money >= 8:
            traits["evil"] += 5
            traits["good"] -= 5
        if money <= 2:
            traits["evil"] -= 5
            traits["good"] += 5

        # Politics
        if politics == 10:
            traits["evil"] += 5
        if politics >= 9:
            traits["grumpy"] += 5
            traits["friendly"] -= 5
        if politics <= 4:
            traits["good"] += 5
        if politics <= 2:
            traits["friendly"] += 5
            traits["evil"] -= 5

        # School
        if school >= 9:
            traits["light sleeper"] += 5
            traits["heavy sleeper"] -= 5
        if school >= 8:
            traits["genius"] += 5
            traits["perceptive"] += 5
        if school <= 3:
            traits["heavy sleeper"] += 5
            traits["genius"] -= 5
            traits["perceptive"] -= 5
            traits["light sleeper"] -= 5

        # SciFi
        if sciFi >= 9:
            traits["loner"] += 5
            traits["neurotic"] += 5
            traits["absent-minded"] -= 5
            traits["artistic"] -= 5
            traits["virtuoso"] -= 5
        if sciFi >= 7:
            traits["eccentric"] += 5
            traits["easily impressed"] -= 5
        if sciFi <= 3:
            traits["loner"] -= 5
            traits["neurotic"] -= 5
        if sciFi <= 2:
            traits["absent-minded"] += 5
            traits["easily impressed"] += 5
            traits["artistic"] += 5
            traits["virtuoso"] += 5
            traits["eccentric"] -= 5

        # Sports
        if sports >= 8:
            traits["athletic"] += 5
            traits["couch potato"] += 5
            traits["disciplined"] -= 5
        if sports == 5:
            traits["excitable"] += 5
        if sports <= 2:
            traits["disciplined"] += 5
            traits["athletic"] -= 5
            traits["couch potato"] -= 5

        # Travel
        if travel >= 8:
            traits["brave"] += 5
            traits["loves the outdoors"] += 5
            traits["grumpy"] -= 5
        if travel <= 2:
            traits["grumpy"] += 5
            traits["hates the outdoors"] += 5
            traits["brave"] -= 5

        # Weather
        if weather >= 9:
            traits["loves the outdoors"] += 5
        if weather >= 8:
            traits["hates the outdoors"] -= 5
        if weather >= 7:
            traits["eccentric"] += 5
        if weather <= 2:
            traits["hates the outdoors"] += 5
            traits["loves the outdoors"] -= 5
            traits["eccentric"] -= 5

        # Work
        if work >= 9:
            traits["light sleeper"] += 5
            traits["perceptive"] += 5
            traits["hates the outdoors"] += 5
            traits["clumsy"] -= 5
            traits["heavy sleeper"] -= 5
        if work <= 3:
            traits["clumsy"] += 5
            traits["heavy sleeper"] += 5
            traits["hates the outdoors"] -= 5
            traits["light sleeper"] -= 5

    elif age == "child":
        # Crime
        if crime == 10:
            traits["evil"] += 5
            traits["good"] -= 5
        if crime >= 9:
            traits["brave"] += 5
            traits["perceptive"] += 5
            traits["insane"] += 5
        if crime >= 8:
            traits["kleptomaniac"] += 5
            traits["excitable"] -= 5
            traits["coward"] -= 5
        if crime >= 6:
            traits["frugal"] += 5
        if crime <= 3:
            traits["coward"] += 5
        if crime <= 2:
            traits["shy"] += 5
            traits["excitable"] += 5
            traits["brave"] -= 5
            traits["perceptive"] -= 5
            traits["insane"] -= 5
            traits["kleptomaniac"] -= 5
            traits["frugal"] -= 5
        if crime == 0:
            traits["good"] += 5
            traits["evil"] -= 5

        # Culture
        if culture == 10:
            traits["star quality"] += 5
        if culture >= 8:
            traits["over-emotional"] += 5
            traits["photographer's eye"] += 5
            traits["virtuoso"] += 5
            traits["can't stand art"] -= 5
        if culture >= 7:
            traits["artistic"] += 5
        if culture == 6:
            traits["easily impressed"] += 5
        if culture <= 3:
            traits["virtuoso"] -= 5
            traits["artistic"] -= 5
            traits["photographer's eye"] -= 5
        if culture <= 2:
            traits["can't stand art"] += 5
            traits["star quality"] -= 5
            traits["over-emotional"] -= 5

        # Entertainment
        if entertainment == 10:
            traits["star quality"] += 5
        if entertainment >= 8:
            traits["couch potato"] += 5
            traits["good sense of humour"] += 5
            traits["over-emotional"] += 5
            traits["virtuoso"] += 5
            traits["loner"] -= 5
            traits["no sense of humour"] -= 5
        if entertainment <= 2:
            traits["no sense of humour"] += 5
            traits["technophobe"] += 5
            traits["loner"] += 5
            traits["couch potato"] -= 5
            traits["virtuoso"] -= 5
            traits["star quality"] -= 5
            traits["good sense of humour"] -= 5

        # Environment
        if environment >= 9:
            traits["eco-friendly"] += 5
            traits["neurotic"] -= 5
        if environment >= 8:
            traits["loves the outdoors"] += 5
            traits["hates the outdoors"] -= 5
            traits["absent-minded"] -= 5
            traits["clumsy"] -= 5
            traits["grumpy"] -= 5
        if environment >= 7:
            traits["angler"] += 5
        if environment <= 5:
            traits["neurotic"] += 5
        if environment <= 3:
            traits["absent-minded"] += 5
            traits["clumsy"] += 5
            traits["grumpy"] += 5
        if environment <= 2:
            traits["hates the outdoors"] += 5
            traits["loves the outdoors"] -= 5
            traits["eco-friendly"] -= 5

        # Fashion
        if fashion >= 9:
            traits["snob"] += 5
            traits["can't stand art"] -= 5
            traits["never nude"] -= 5
        if fashion <= 2:
            traits["can't stand art"] += 5
            traits["never nude"] += 5
            traits["snob"] -= 5

        # Food
        if food >= 8:
            traits["slob"] += 5
            traits["vegetarian"] += 5
            traits["absent-minded"] -= 5
        if food <= 2:
            traits["absent-minded"] += 5
            traits["slob"] -= 5
            traits["vegetarian"] -= 5

        # Health
        if health >= 9:
            traits["brave"] += 5
            traits["neurotic"] += 5
            traits["absent-minded"] -= 5
            traits["hates the outdoors"] -= 5
            traits["insane"] -= 5
            traits["couch potato"] -= 5
            traits["slob"] -= 5
        if health >= 8:
            traits["disciplined"] += 5
            traits["neat"] += 5
            traits["vegetarian"] += 5
        if health <= 4:
            traits["technophobe"] += 5
        if health <= 3:
            traits["couch potato"] += 5
            traits["slob"] += 5
        if health <= 2:
            traits["absent-minded"] += 5
            traits["hates the outdoors"] += 5
            traits["hydrophobic"] += 5
            traits["inappropriate"] += 5
            traits["insane"] += 5
            traits["brave"] -= 5
            traits["neurotic"] -= 5
            traits["disciplined"] -= 5
            traits["neat"] -= 5
            traits["vegetarian"] -= 5

        # Money
        if money >= 9:
            traits["frugal"] += 5
            traits["mooch"] += 5
            traits["snob"] += 5
            traits["loser"] -= 5
        if money >= 8:
            traits["evil"] += 5
            traits["good"] -= 5
        if money <= 2:
            traits["evil"] -= 5
            traits["good"] += 5
            traits["frugal"] -= 5
            traits["mooch"] -= 5
            traits["snob"] -= 5
        if money == 0:
            traits["loser"] += 5

        # Paranormal
        if paranormal >= 8:
            traits["coward"] -= 5
        if paranormal <= 3:
            traits["coward"] += 5

        # Politics
        if politics == 10:
            traits["evil"] += 5
        if politics >= 9:
            traits["grumpy"] += 5
            traits["friendly"] -= 5
            traits["good"] -= 5
        if politics >= 8:
            traits["hot-headed"] += 5
            traits["rebellious"] -= 5
            traits["shy"] -= 5
        if politics >= 7:
            traits["ambitious"] += 5
        if politics <= 4:
            traits["good"] += 5
        if politics <= 2:
            traits["rebellious"] += 5
            traits["shy"] += 5
            traits["friendly"] += 5
            traits["evil"] -= 5
            traits["ambitious"] -= 5
            traits["grumpy"] -= 5
            traits["hot-headed"] -= 5

        # School
        if school >= 9:
            traits["light sleeper"] += 5
            traits["workaholic"] += 5
            traits["heavy sleeper"] -= 5
        if school >= 8:
            traits["bookworm"] += 5
            traits["family-oriented"] += 5
            traits["genius"] += 5
            traits["perceptive"] += 5
        if school <= 3:
            traits["heavy sleeper"] += 5
            traits["genius"] -= 5
            traits["perceptive"] -= 5
            traits["light sleeper"] -= 5
            traits["workaholic"] -= 5
        if school <= 2:
            traits["rebellious"] += 5
            traits["genius"] -= 5
            traits["family-oriented"] -= 5
            traits["bookworm"] -= 5

        # SciFi
        if sciFi >= 9:
            traits["loner"] += 5
            traits["neurotic"] += 5
            traits["absent-minded"] -= 5
            traits["artistic"] -= 5
            traits["virtuoso"] -= 5
            traits["coward"] -= 5
        if sciFi >= 7:
            traits["computer whiz"] += 5
            traits["eccentric"] += 5
            traits["easily impressed"] -= 5
        if sciFi <= 3:
            traits["coward"] += 5
            traits["loner"] -= 5
            traits["neurotic"] -= 5
        if sciFi <= 2:
            traits["technophobe"] += 5
            traits["absent-minded"] += 5
            traits["easily impressed"] += 5
            traits["artistic"] += 5
            traits["virtuoso"] += 5
            traits["eccentric"] -= 5

        # Sports
        if sports >= 8:
            traits["daredevil"] += 5
            traits["athletic"] += 5
            traits["couch potato"] += 5
            traits["disciplined"] -= 5
        if sports == 5:
            traits["excitable"] += 5
        if sports <= 2:
            traits["disciplined"] += 5
            traits["athletic"] -= 5
            traits["couch potato"] -= 5
            traits["daredevil"] -= 5

        # Toys
        if toys >= 8:
            traits["family-oriented"] += 5
        if toys <= 2:
            traits["family-oriented"] -= 5

        # Travel
        if travel >= 8:
            traits["adventurous"] += 5
            traits["loves the outdoors"] += 5
            traits["photographer's eye"] += 5
            traits["brave"] += 5
            traits["grumpy"] -= 5
            traits["hates the outdoors"] -= 5
        if travel <= 2:
            traits["grumpy"] += 5
            traits["hates the outdoors"] += 5
            traits["brave"] -= 5
            traits["adventurous"] -= 5
            traits["loves the outdoors"] -= 5
            traits["photographer's eye"] -= 5

        # Weather
        if weather >= 9:
            traits["eco-friendly"] += 5
            traits["loves the outdoors"] += 5
        if weather >= 8:
            traits["angler"] += 5
            traits["hates the outdoors"] -= 5
        if weather >= 7:
            traits["eccentric"] += 5
        if weather <= 3:
            traits["angler"] -= 5
        if weather <= 2:
            traits["hydrophobic"] += 5
            traits["hates the outdoors"] += 5
            traits["loves the outdoors"] -= 5
            traits["eccentric"] -= 5
            traits["eco-friendly"] -= 5

        # Work
        if work == 10:
            traits["perfectionist"] += 5
        if work >= 9:
            traits["light sleeper"] += 5
            traits["perceptive"] += 5
            traits["workaholic"] += 5
            traits["hates the outdoors"] += 5
            traits["clumsy"] -= 5
            traits["heavy sleeper"] -= 5
        if work >= 8:
            traits["ambitious"] += 5
            traits["clumsy"] -= 5
            traits["rebellious"] -= 5
        if work <= 3:
            traits["clumsy"] += 5
            traits["heavy sleeper"] += 5
            traits["hates the outdoors"] -= 5
            traits["hot-headed"] += 5
            traits["light sleeper"] -= 5
        if work <= 2:
            traits["rebellious"] += 5
            traits["perfectionist"] -= 5
            traits["perceptive"] -= 5
            traits["workaholic"] -= 5
        if work == 0:
            traits["loser"] += 5

    elif age == "teen":
        # Crime
        if crime == 10:
            traits["evil"] += 5
            traits["good"] -= 5
        if crime >= 9:
            traits["brave"] += 5
            traits["perceptive"] += 5
            traits["insane"] += 5
        if crime >= 8:
            traits["kleptomaniac"] += 5
            traits["excitable"] -= 5
            traits["coward"] -= 5
        if crime >= 6:
            traits["frugal"] += 5
        if crime <= 3:
            traits["coward"] += 5
        if crime <= 2:
            traits["shy"] += 5
            traits["excitable"] += 5
            traits["brave"] -= 5
            traits["perceptive"] -= 5
            traits["insane"] -= 5
            traits["kleptomaniac"] -= 5
            traits["frugal"] -= 5
        if crime == 0:
            traits["good"] += 5
            traits["evil"] -= 5

        # Culture
        if culture == 10:
            traits["star quality"] += 5
        if culture >= 8:
            traits["over-emotional"] += 5
            traits["photographer's eye"] += 5
            traits["savvy sculptor"] += 5
            traits["virtuoso"] += 5
            traits["can't stand art"] -= 5
            traits["hopeless romantic"] += 5
        if culture >= 7:
            traits["artistic"] += 5
            traits["great kisser"] += 5
        if culture == 6:
            traits["easily impressed"] += 5
        if culture <= 3:
            traits["virtuoso"] -= 5
            traits["artistic"] -= 5
            traits["savvy sculptor"] -= 5
            traits["photographer's eye"] -= 5
        if culture <= 2:
            traits["can't stand art"] += 5
            traits["star quality"] -= 5
            traits["over-emotional"] -= 5
            traits["great kisser"] -= 5
            traits["hopeless romantic"] -= 5

        # Entertainment
        if entertainment == 10:
            traits["star quality"] += 5
        if entertainment >= 9:
            traits["hopeless romantic"] += 5
        if entertainment >= 8:
            traits["couch potato"] += 5
            traits["dramatic"] += 5
            traits["good sense of humour"] += 5
            traits["over-emotional"] += 5
            traits["virtuoso"] += 5
            traits["party animal"] += 5
            traits["loner"] -= 5
            traits["no sense of humour"] -= 5
        if entertainment >= 7:
            traits["great kisser"] += 5
            traits["flirty"] += 5
        if entertainment <= 3:
            traits["party animal"] -= 5
        if entertainment <= 2:
            traits["no sense of humour"] += 5
            traits["technophobe"] += 5
            traits["loner"] += 5
            traits["couch potato"] -= 5
            traits["virtuoso"] -= 5
            traits["star quality"] -= 5
            traits["good sense of humour"] -= 5
            traits["dramatic"] -= 5
            traits["great kisser"] -= 5
            traits["flirty"] -= 5
            traits["hopeless romantic"] -= 5

        # Environment
        if environment >= 9:
            traits["eco-friendly"] += 5
            traits["neurotic"] -= 5
        if environment >= 8:
            traits["green thumb"] += 5
            traits["loves the outdoors"] += 5
            traits["hates the outdoors"] -= 5
            traits["absent-minded"] -= 5
            traits["clumsy"] -= 5
            traits["grumpy"] -= 5
        if environment >= 7:
            traits["angler"] += 5
        if environment <= 5:
            traits["neurotic"] += 5
        if environment <= 3:
            traits["absent-minded"] += 5
            traits["clumsy"] += 5
            traits["grumpy"] += 5
        if environment <= 2:
            traits["hates the outdoors"] += 5
            traits["loves the outdoors"] -= 5
            traits["eco-friendly"] -= 5
            traits["green thumb"] -= 5
            traits["angler"] -= 5

        # Fashion
        if fashion >= 9:
            traits["snob"] += 5
            traits["can't stand art"] -= 5
            traits["never nude"] -= 5
            traits["hopeless romantic"] += 5
        if fashion >= 8:
            traits["dramatic"] += 5
            traits["great kisser"] += 5
        if fashion <= 3:
            traits["great kisser"] -= 5
        if fashion <= 2:
            traits["can't stand art"] += 5
            traits["never nude"] += 5
            traits["dramatic"] -= 5
            traits["snob"] -= 5
            traits["hopeless romantic"] -= 5

        # Food
        if food >= 8:
            traits["natural cook"] += 5
            traits["slob"] += 5
            traits["vegetarian"] += 5
            traits["absent-minded"] -= 5
        if food <= 2:
            traits["absent-minded"] += 5
            traits["slob"] -= 5
            traits["vegetarian"] -= 5
            traits["natural cook"] -= 5

        # Health
        if health >= 9:
            traits["brave"] += 5
            traits["neurotic"] += 5
            traits["absent-minded"] -= 5
            traits["hates the outdoors"] -= 5
            traits["insane"] -= 5
            traits["couch potato"] -= 5
            traits["slob"] -= 5
        if health >= 8:
            traits["disciplined"] += 5
            traits["neat"] += 5
            traits["vegetarian"] += 5
            traits["nurturing"] += 5
        if health <= 4:
            traits["technophobe"] += 5
        if health <= 3:
            traits["couch potato"] += 5
            traits["slob"] += 5
        if health <= 2:
            traits["absent-minded"] += 5
            traits["hates the outdoors"] += 5
            traits["hydrophobic"] += 5
            traits["inappropriate"] += 5
            traits["insane"] += 5
            traits["brave"] -= 5
            traits["neurotic"] -= 5
            traits["disciplined"] -= 5
            traits["neat"] -= 5
            traits["vegetarian"] -= 5
            traits["nurturing"] -= 5

        # Money
        if money >= 9:
            traits["frugal"] += 5
            traits["mooch"] += 5
            traits["snob"] += 5
            traits["loser"] -= 5
            traits["handy"] -= 5
        if money >= 8:
            traits["born salesman"] += 5
            traits["evil"] += 5
            traits["good"] -= 5
        if money <= 5:
            traits["handy"] += 5
        if money <= 2:
            traits["evil"] -= 5
            traits["good"] += 5
            traits["frugal"] -= 5
            traits["mooch"] -= 5
            traits["snob"] -= 5
            traits["born salesman"] -= 5
        if money == 0:
            traits["loser"] += 5

        # Paranormal
        if paranormal >= 8:
            traits["coward"] -= 5
        if paranormal <= 3:
            traits["coward"] += 5

        # Politics
        if politics == 10:
            traits["evil"] += 5
        if politics >= 9:
            traits["grumpy"] += 5
            traits["friendly"] -= 5
            traits["good"] -= 5
        if politics >= 8:
            traits["charismatic"] += 5
            traits["hot-headed"] += 5
            traits["schmoozer"] += 5
            traits["rebellious"] -= 5
            traits["shy"] -= 5
        if politics >= 7:
            traits["ambitious"] += 5
        if politics <= 4:
            traits["good"] += 5
            traits["schmoozer"] -= 5
        if politics <= 2:
            traits["rebellious"] += 5
            traits["shy"] += 5
            traits["friendly"] += 5
            traits["evil"] -= 5
            traits["ambitious"] -= 5
            traits["grumpy"] -= 5
            traits["hot-headed"] -= 5
            traits["charismatic"] -= 5

        # School
        if school >= 9:
            traits["light sleeper"] += 5
            traits["workaholic"] += 5
            traits["heavy sleeper"] -= 5
        if school >= 8:
            traits["bookworm"] += 5
            traits["family-oriented"] += 5
            traits["genius"] += 5
            traits["nurturing"] += 5
        if school <= 3:
            traits["heavy sleeper"] += 5
            traits["genius"] -= 5
            traits["perceptive"] -= 5
            traits["light sleeper"] -= 5
            traits["workaholic"] -= 5
        if school <= 2:
            traits["rebellious"] += 5
            traits["genius"] -= 5
            traits["family-oriented"] -= 5
            traits["bookworm"] -= 5
            traits["nurturing"] -= 5

        # SciFi
        if sciFi >= 9:
            traits["loner"] += 5
            traits["neurotic"] += 5
            traits["absent-minded"] -= 5
            traits["artistic"] -= 5
            traits["virtuoso"] -= 5
            traits["coward"] -= 5
        if sciFi >= 7:
            traits["computer whiz"] += 5
            traits["eccentric"] += 5
            traits["easily impressed"] -= 5
        if sciFi <= 3:
            traits["coward"] += 5
            traits["loner"] -= 5
            traits["neurotic"] -= 5
        if sciFi <= 2:
            traits["technophobe"] += 5
            traits["absent-minded"] += 5
            traits["easily impressed"] += 5
            traits["artistic"] += 5
            traits["virtuoso"] += 5
            traits["eccentric"] -= 5

        # Sports
        if sports >= 8:
            traits["daredevil"] += 5
            traits["athletic"] += 5
            traits["couch potato"] += 5
            traits["disciplined"] -= 5
        if sports == 5:
            traits["excitable"] += 5
        if sports <= 2:
            traits["disciplined"] += 5
            traits["athletic"] -= 5
            traits["couch potato"] -= 5
            traits["daredevil"] -= 5

        # Toys
        if toys >= 8:
            traits["childish"] += 5
            traits["family-oriented"] += 5
        if toys >= 6:
            traits["nurturing"] += 5
        if toys <= 2:
            traits["dislikes children"] += 5
            traits["family-oriented"] -= 5
            traits["nurturing"] -= 5

        # Travel
        if travel >= 8:
            traits["adventurous"] += 5
            traits["loves the outdoors"] += 5
            traits["photographer's eye"] += 5
            traits["brave"] += 5
            traits["grumpy"] -= 5
            traits["hates the outdoors"] -= 5
        if travel <= 2:
            traits["grumpy"] += 5
            traits["hates the outdoors"] += 5
            traits["brave"] -= 5
            traits["adventurous"] -= 5
            traits["loves the outdoors"] -= 5
            traits["photographer's eye"] -= 5

        # Weather
        if weather >= 9:
            traits["eco-friendly"] += 5
            traits["loves the outdoors"] += 5
        if weather >= 8:
            traits["angler"] += 5
            traits["hates the outdoors"] -= 5
        if weather >= 7:
            traits["eccentric"] += 5
        if weather <= 3:
            traits["angler"] -= 5
        if weather <= 2:
            traits["hydrophobic"] += 5
            traits["hates the outdoors"] += 5
            traits["loves the outdoors"] -= 5
            traits["eccentric"] -= 5
            traits["eco-friendly"] -= 5

        # Work
        if work == 10:
            traits["perfectionist"] += 5
        if work >= 9:
            traits["light sleeper"] += 5
            traits["perceptive"] += 5
            traits["workaholic"] += 5
            traits["hates the outdoors"] += 5
            traits["clumsy"] -= 5
            traits["heavy sleeper"] -= 5
        if work >= 8:
            traits["ambitious"] += 5
            traits["born salesman"] += 5
            traits["schmoozer"] += 5
            traits["clumsy"] -= 5
            traits["rebellious"] -= 5
        if work <= 5:
            traits["handy"] += 5
        if work <= 3:
            traits["heavy sleeper"] += 5
            traits["hot-headed"] += 5
            traits["clumsy"] += 5
            traits["hates the outdoors"] -= 5
            traits["light sleeper"] -= 5
        if work <= 2:
            traits["rebellious"] += 5
            traits["perfectionist"] -= 5
            traits["perceptive"] -= 5
            traits["workaholic"] -= 5
            traits["born salesman"] -= 5
            traits["schmoozer"] -= 5
        if work == 0:
            traits["loser"] += 5

    else:
        # Animals
        if animals >= 9:
            traits["animal lover"] += 5
            traits["cat person"] -= 5
            traits["dog person"] -= 5
        if animals >= 7:
            traits["equestrian"] += 5
        if animals >= 5:
            traits["cat person"] += 5
            traits["dog person"] += 5
        if animals <= 2:
            traits["animal lover"] -= 5
            traits["equestrian"] -= 5
            traits["cat person"] -= 5
            traits["dog person"] -= 5

        # Crime
        if crime == 10:
            traits["evil"] += 5
        if crime >= 9:
            traits["brave"] += 5
            traits["perceptive"] += 5
            traits["insane"] += 5
        if crime >= 8:
            traits["kleptomaniac"] += 5
            traits["excitable"] -= 5
            traits["coward"] -= 5
        if crime >= 6:
            traits["frugal"] += 5
        if crime <= 3:
            traits["coward"] += 5
        if crime <= 2:
            traits["shy"] += 5
            traits["excitable"] += 5
            traits["brave"] -= 5
            traits["perceptive"] -= 5
            traits["insane"] -= 5
            traits["kleptomaniac"] -= 5
            traits["frugal"] -= 5
        if crime == 0:
            traits["good"] += 5
            traits["evil"] -= 5

        # Culture
        if culture == 10:
            traits["star quality"] += 5
        if culture >= 9:
            traits["brooding"] += 5
        if culture >= 8:
            traits["avant garde"] += 5
            traits["natural born performer"] += 5
            traits["over-emotional"] += 5
            traits["photographer's eye"] += 5
            traits["proper"] += 5
            traits["savvy sculptor"] += 5
            traits["virtuoso"] += 5
            traits["can't stand art"] -= 5
            traits["hopeless romantic"] += 5
        if culture >= 7:
            traits["artistic"] += 5
            traits["great kisser"] += 5
        if culture == 6:
            traits["easily impressed"] += 5
        if culture <= 3:
            traits["virtuoso"] -= 5
            traits["artistic"] -= 5
            traits["savvy sculptor"] -= 5
            traits["photographer's eye"] -= 5
        if culture <= 2:
            traits["can't stand art"] += 5
            traits["proper"] += 5
            traits["star quality"] -= 5
            traits["over-emotional"] -= 5
            traits["great kisser"] -= 5
            traits["hopeless romantic"] -= 5

        # Entertainment
        if entertainment == 10:
            traits["star quality"] += 5
        if entertainment >= 9:
            traits["diva"] += 5
            traits["natural born performer"] += 5
            traits["hopeless romantic"] += 5
        if entertainment >= 8:
            traits["couch potato"] += 5
            traits["dramatic"] += 5
            traits["good sense of humour"] += 5
            traits["over-emotional"] += 5
            traits["virtuoso"] += 5
            traits["party animal"] += 5
            traits["loner"] -= 5
            traits["no sense of humour"] -= 5
        if entertainment >= 7:
            traits["great kisser"] += 5
            traits["flirty"] += 5
        if entertainment <= 3:
            traits["party animal"] -= 5
        if entertainment <= 2:
            traits["no sense of humour"] += 5
            traits["technophobe"] += 5
            traits["loner"] += 5
            traits["couch potato"] -= 5
            traits["virtuoso"] -= 5
            traits["star quality"] -= 5
            traits["good sense of humour"] -= 5
            traits["dramatic"] -= 5
            traits["great kisser"] -= 5
            traits["flirty"] -= 5
            traits["natural born performer"] -= 5
            traits["hopeless romantic"] -= 5

        # Environment
        if environment >= 9:
            traits["eco-friendly"] += 5
            traits["neurotic"] -= 5
            traits["loves the heat"] -= 5
        if environment >= 8:
            traits["green thumb"] += 5
            traits["loves the outdoors"] += 5
            traits["sailor"] += 5
            traits["hates the outdoors"] -= 5
            traits["absent-minded"] -= 5
            traits["clumsy"] -= 5
            traits["grumpy"] -= 5
        if environment >= 7:
            traits["angler"] += 5
        if environment >= 6:
            traits["loves the cold"] += 5
        if environment == 5:
            traits["gatherer"] += 5
        if environment <= 5:
            traits["neurotic"] += 5
        if environment <= 3:
            traits["absent-minded"] += 5
            traits["clumsy"] += 5
            traits["grumpy"] += 5
            traits["loves the heat"] += 5
        if environment <= 2:
            traits["hates the outdoors"] += 5
            traits["loves the outdoors"] -= 5
            traits["eco-friendly"] -= 5
            traits["green thumb"] -= 5
            traits["angler"] -= 5
            traits["loves the cold"] -= 5
            traits["sailor"] -= 5

        # Fashion
        if fashion >= 9:
            traits["diva"] += 5
            traits["snob"] += 5
            traits["can't stand art"] -= 5
            traits["never nude"] -= 5
            traits["hopeless romantic"] += 5
        if fashion >= 8:
            traits["dramatic"] += 5
            traits["proper"] += 5
            traits["great kisser"] += 5
        if fashion <= 3:
            traits["great kisser"] -= 5
        if fashion <= 2:
            traits["can't stand art"] += 5
            traits["never nude"] += 5
            traits["dramatic"] -= 5
            traits["snob"] -= 5
            traits["hopeless romantic"] -= 5
            traits["diva"] -= 5
            traits["proper"] -= 5

        # Food
        if food >= 8:
            traits["natural cook"] += 5
            traits["slob"] += 5
            traits["vegetarian"] += 5
            traits["absent-minded"] -= 5
        if food <= 2:
            traits["absent-minded"] += 5
            traits["slob"] -= 5
            traits["vegetarian"] -= 5
            traits["natural cook"] -= 5

        # Health
        if health >= 9:
            traits["brave"] += 5
            traits["neurotic"] += 5
            traits["absent-minded"] -= 5
            traits["hates the outdoors"] -= 5
            traits["insane"] -= 5
            traits["couch potato"] -= 5
            traits["slob"] -= 5
            traits["night owl"] -= 5
        if health >= 8:
            traits["disciplined"] += 5
            traits["loves to swim"] += 5
            traits["neat"] += 5
            traits["vegetarian"] += 5
            traits["nurturing"] += 5
        if health <= 4:
            traits["technophobe"] += 5
        if health == 3:
            traits["unstable"] += 5
        if health <= 3:
            traits["couch potato"] += 5
            traits["night owl"] += 5
            traits["slob"] += 5
        if health <= 2:
            traits["absent-minded"] += 5
            traits["hates the outdoors"] += 5
            traits["hydrophobic"] += 5
            traits["inappropriate"] += 5
            traits["insane"] += 5
            traits["brave"] -= 5
            traits["neurotic"] -= 5
            traits["disciplined"] -= 5
            traits["neat"] -= 5
            traits["vegetarian"] -= 5
            traits["nurturing"] -= 5
            traits["loves to swim"] -= 5

        # Money
        if money >= 9:
            traits["frugal"] += 5
            traits["mooch"] += 5
            traits["snob"] += 5
            traits["loser"] -= 5
            traits["handy"] -= 5
        if money >= 8:
            traits["born salesman"] += 5
            traits["evil"] += 5
            traits["good"] -= 5
        if money <= 5:
            traits["handy"] += 5
        if money <= 2:
            traits["evil"] -= 5
            traits["good"] += 5
            traits["frugal"] -= 5
            traits["mooch"] -= 5
            traits["snob"] -= 5
            traits["born salesman"] -= 5
        if money == 0:
            traits["loser"] += 5

        # Paranormal
        if paranormal >= 9:
            traits["supernatural fan"] += 5
        if paranormal >= 8:
            traits["coward"] -= 5
        if paranormal <= 3:
            traits["coward"] += 5
        if paranormal <= 2:
            traits["supernatural sceptic"] += 5

        # Politics
        if politics == 10:
            traits["evil"] += 5
        if politics >= 9:
            traits["grumpy"] += 5
            traits["friendly"] -= 5
            traits["good"] -= 5
        if politics >= 8:
            traits["charismatic"] += 5
            traits["hot-headed"] += 5
            traits["schmoozer"] += 5
            traits["rebellious"] -= 5
            traits["shy"] -= 5
        if politics >= 7:
            traits["ambitious"] += 5
        if politics <= 4:
            traits["good"] += 5
            traits["schmoozer"] -= 5
        if politics <= 2:
            traits["rebellious"] += 5
            traits["shy"] += 5
            traits["friendly"] += 5
            traits["evil"] -= 5
            traits["ambitious"] -= 5
            traits["grumpy"] -= 5
            traits["hot-headed"] -= 5
            traits["charismatic"] -= 5

        # School
        if school >= 9:
            traits["light sleeper"] += 5
            traits["workaholic"] += 5
            traits["heavy sleeper"] -= 5
        if school >= 8:
            traits["bookworm"] += 5
            traits["family-oriented"] += 5
            traits["genius"] += 5
            traits["nurturing"] += 5
        if school <= 3:
            traits["heavy sleeper"] += 5
            traits["genius"] -= 5
            traits["perceptive"] -= 5
            traits["light sleeper"] -= 5
            traits["workaholic"] -= 5
        if school <= 2:
            traits["rebellious"] += 5
            traits["genius"] -= 5
            traits["family-oriented"] -= 5
            traits["bookworm"] -= 5
            traits["nurturing"] -= 5

        # SciFi
        if sciFi >= 9:
            traits["supernatural fan"] += 5
            traits["loner"] += 5
            traits["neurotic"] += 5
            traits["absent-minded"] -= 5
            traits["artistic"] -= 5
            traits["virtuoso"] -= 5
            traits["coward"] -= 5
        if sciFi >= 7:
            traits["bot fan"] += 5
            traits["computer whiz"] += 5
            traits["eccentric"] += 5
            traits["easily impressed"] -= 5
        if sciFi <= 3:
            traits["coward"] += 5
            traits["loner"] -= 5
            traits["neurotic"] -= 5
        if sciFi <= 2:
            traits["supernatural sceptic"] += 5
            traits["technophobe"] += 5
            traits["absent-minded"] += 5
            traits["easily impressed"] += 5
            traits["artistic"] += 5
            traits["virtuoso"] += 5
            traits["eccentric"] -= 5

        # Sports
        if sports >= 8:
            traits["daredevil"] += 5
            traits["social butterfly"] += 5
            traits["athletic"] += 5
            traits["couch potato"] += 5
            traits["disciplined"] -= 5
        if sports == 5:
            traits["excitable"] += 5
        if sports <= 2:
            traits["disciplined"] += 5
            traits["athletic"] -= 5
            traits["couch potato"] -= 5
            traits["daredevil"] -= 5
            traits["social butterfly"] -= 5

        # Toys
        if toys >= 8:
            traits["childish"] += 5
            traits["family-oriented"] += 5
        if toys >= 6:
            traits["nurturing"] += 5
        if toys <= 2:
            traits["dislikes children"] += 5
            traits["family-oriented"] -= 5
            traits["nurturing"] -= 5

        # Travel
        if travel >= 8:
            traits["adventurous"] += 5
            traits["loves the outdoors"] += 5
            traits["photographer's eye"] += 5
            traits["sailor"] += 5
            traits["brave"] += 5
            traits["grumpy"] -= 5
            traits["hates the outdoors"] -= 5
            traits["loves the cold"] -= 5
        if travel >= 7:
            traits["loves the heat"] += 5
        if travel <= 3:
            traits["loves the cold"] += 5
        if travel <= 2:
            traits["grumpy"] += 5
            traits["hates the outdoors"] += 5
            traits["brave"] -= 5
            traits["adventurous"] -= 5
            traits["loves the outdoors"] -= 5
            traits["photographer's eye"] -= 5
            traits["loves the heat"] -= 5
            traits["sailor"] -= 5

        # Weather
        if weather >= 9:
            traits["eco-friendly"] += 5
            traits["loves the outdoors"] += 5
        if weather >= 8:
            traits["angler"] += 5
            traits["loves to swim"] += 5
            traits["sailor"] += 5
            traits["hates the outdoors"] -= 5
            traits["loves the cold"] -= 5
        if weather >= 7:
            traits["loves the heat"] += 5
            traits["eccentric"] += 5
        if weather <= 3:
            traits["loves the cold"] += 5
            traits["angler"] -= 5
        if weather <= 2:
            traits["hydrophobic"] += 5
            traits["hates the outdoors"] += 5
            traits["loves the outdoors"] -= 5
            traits["eccentric"] -= 5
            traits["eco-friendly"] -= 5
            traits["loves the heat"] -= 5
            traits["sailor"] -= 5

        # Work
        if work == 10:
            traits["perfectionist"] += 5
        if work >= 9:
            traits["light sleeper"] += 5
            traits["perceptive"] += 5
            traits["workaholic"] += 5
            traits["hates the outdoors"] += 5
            traits["clumsy"] -= 5
            traits["heavy sleeper"] -= 5
        if work >= 8:
            traits["ambitious"] += 5
            traits["born salesman"] += 5
            traits["schmoozer"] += 5
            traits["clumsy"] -= 5
            traits["rebellious"] -= 5
        if work <= 5:
            traits["handy"] += 5
        if work <= 3:
            traits["heavy sleeper"] += 5
            traits["hot-headed"] += 5
            traits["clumsy"] += 5
            traits["hates the outdoors"] -= 5
            traits["light sleeper"] -= 5
        if work <= 2:
            traits["rebellious"] += 5
            traits["perfectionist"] -= 5
            traits["perceptive"] -= 5
            traits["workaholic"] -= 5
            traits["born salesman"] -= 5
            traits["schmoozer"] -= 5
        if work == 0:
            traits["loser"] += 5
