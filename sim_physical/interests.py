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
            traits["evil"] += 1
        if crime >= 9:
            traits["brave"] += 1
            traits["perceptive"] += 1
        if crime == 0:
            traits["good"] += 1

        # Culture
        if culture >= 8:
            traits["virtuoso"] += 1
        if culture >= 7:
            traits["artistic"] += 1
        if culture == 6:
            traits["easily impressed"] += 1

        # Entertainment
        if entertainment >= 8:
            traits["couch potato"] += 1
            traits["virtuoso"] += 1

        # Environment
        if environment >= 8:
            traits["loves the outdoors"] += 1
        if environment <= 5:
            traits["neurotic"] += 1
        if environment <= 3:
            traits["absent-minded"] += 1
            traits["clumsy"] += 1
            traits["grumpy"] += 1
        if environment <= 2:
            traits["hates the outdoors"] += 1

        # Food
        if food >= 8:
            traits["slob"] += 1

        # Health
        if health >= 9:
            traits["brave"] += 1
            traits["neurotic"] += 1
        if health >= 8:
            traits["disciplined"] += 1
        if health <= 3:
            traits["couch potato"] += 1
            traits["slob"]
        if health <= 2:
            traits["absent-minded"] += 1
            traits["hates the outdoors"] += 1
            traits["insane"] += 1

        # Money
        if money >= 8:
            traits["evil"] += 1

        # Politics
        if politics == 10:
            traits["evil"] += 1
        if politics >= 9:
            traits["grumpy"] += 1
        if politics <= 4:
            traits["good"] += 1

        # School
        if school >= 8:
            traits["genius"] += 1
        if school <= 3:
            traits["heavy sleeper"] += 1

        # SciFi
        if sciFi >= 7:
            traits["eccentric"] += 1

        # Sports
        if sports == 5:
            traits["excitable"] += 1

        # Travel
        if travel >= 8:
            traits["loves the outdoors"] += 1
        if travel <= 2:
            traits["hates the outdoors"] += 1

        # Weather
        if weather >= 9:
            traits["loves the outdoors"] += 1

        # Work
        if work >= 9:
            traits["light sleeper"] += 1
            traits["perceptive"] += 1
        if work <= 3:
            traits["heavy sleeper"] += 1

    elif age == "child":
        # Crime
        if crime == 10:
            traits["evil"] += 1
        if crime >= 9:
            traits["brave"] += 1
            traits["perceptive"] += 1
        if crime >= 8:
            traits["kleptomaniac"] += 1
        if crime >= 6:
            traits["frugal"] += 1
        if crime <= 3:
            traits["coward"] += 1
        if crime <= 2:
            traits["shy"] += 1
        if crime == 0:
            traits["good"] += 1

        # Culture
        if culture == 10:
            traits["star quality"] += 1
        if culture >= 8:
            traits["over-emotional"] += 1
            traits["photographer's eye"] += 1
            traits["virtuoso"] += 1
        if culture >= 7:
            traits["artistic"] += 1
        if culture == 6:
            traits["easily impressed"] += 1
        if culture <= 2:
            traits["can't stand art"] += 1

        # Entertainment
        if entertainment == 10:
            traits["star quality"] += 1
        if entertainment >= 8:
            traits["couch potato"] += 1
            traits["good sense of humour"] += 1
            traits["over-emotional"] += 1
            traits["virtuoso"] += 1
        if entertainment <= 2:
            traits["no sense of humour"] += 1
            traits["technophobe"] += 1

        # Environment
        if environment >= 9:
            traits["eco-friendly"] += 1
        if environment >= 8:
            traits["loves the outdoors"] += 1
        if environment >= 7:
            traits["angler"] += 1
        if environment <= 5:
            traits["neurotic"] += 1
        if environment <= 3:
            traits["absent-minded"] += 1
            traits["clumsy"] += 1
            traits["grumpy"] += 1
        if environment <= 2:
            traits["hates the outdoors"] += 1

        # Fashion
        if fashion >= 9:
            traits["snob"] += 1
        if fashion <= 2:
            traits["can't stand art"] += 1
            traits["never nude"] += 1

        # Food
        if food >= 8:
            traits["slob"] += 1
            traits["vegetarian"] += 1

        # Health
        if health >= 9:
            traits["brave"] += 1
            traits["neurotic"] += 1
        if health >= 8:
            traits["disciplined"] += 1
            traits["neat"] += 1
            traits["vegetarian"] += 1
        if health <= 4:
            traits["technophobe"] += 1
        if health <= 3:
            traits["couch potato"] += 1
            traits["slob"] += 1
        if health <= 2:
            traits["absent-minded"] += 1
            traits["hates the outdoors"] += 1
            traits["hydrophobic"] += 1
            traits["inappropriate"] += 1
            traits["insane"] += 1

        # Money
        if money >= 9:
            traits["frugal"] += 1
            traits["mooch"] += 1
            traits["snob"] += 1
        if money >= 8:
            traits["evil"] += 1
        if money == 0:
            traits["loser"] += 1

        # Paranormal
        if paranormal <= 3:
            traits["coward"] += 1

        # Politics
        if politics == 10:
            traits["evil"] += 1
        if politics >= 9:
            traits["grumpy"] += 1
        if politics >= 8:
            traits["hot-headed"] += 1
        if politics >= 7:
            traits["ambitious"] += 1
        if politics <= 4:
            traits["good"] += 1
        if politics <= 2:
            traits["rebellious"] += 1
            traits["shy"] += 1

        # School
        if school >= 9:
            traits["light sleeper"] += 1
            traits["workaholic"] += 1
        if school >= 8:
            traits["bookworm"] += 1
            traits["family-oriented"] += 1
            traits["genius"] += 1
        if school <= 3:
            traits["heavy sleeper"] += 1
        if school <= 2:
            traits["rebellious"] += 1

        # SciFi
        if sciFi >= 7:
            traits["computer whiz"] += 1
            traits["eccentric"] += 1
        if sciFi <= 3:
            traits["coward"] += 1
        if sciFi <= 2:
            traits["technophobe"] += 1

        # Sports
        if sports >= 8:
            traits["daredevil"] += 1
        if sports == 5:
            traits["excitable"] += 1

        # Toys
        if toys >= 8:
            traits["family-oriented"] += 1

        # Travel
        if travel >= 8:
            traits["adventurous"] += 1
            traits["loves the outdoors"] += 1
            traits["photographer's eye"] += 1
        if travel <= 2:
            traits["hates the outdoors"] += 1

        # Weather
        if weather >= 9:
            traits["eco-friendly"] += 1
            traits["loves the outdoors"] += 1
        if weather >= 8:
            traits["angler"] += 1
        if weather <= 2:
            traits["hydrophobic"] += 1

        # Work
        if work == 10:
            traits["perfectionist"] += 1
        if work >= 9:
            traits["light sleeper"] += 1
            traits["perceptive"] += 1
            traits["workaholic"] += 1
        if work >= 8:
            traits["ambitious"] += 1
        if work <= 3:
            traits["heavy sleeper"] += 1
            traits["hot-headed"] += 1
        if work <= 2:
            traits["rebellious"] += 1
        if work == 0:
            traits["loser"] += 1

    elif age == "teen":
        # Crime
        if crime == 10:
            traits["evil"] += 1
        if crime >= 9:
            traits["brave"] += 1
            traits["perceptive"] += 1
        if crime >= 8:
            traits["kleptomaniac"] += 1
        if crime >= 6:
            traits["frugal"] += 1
        if crime <= 3:
            traits["coward"] += 1
        if crime <= 2:
            traits["shy"] += 1
        if crime == 0:
            traits["good"] += 1

        # Culture
        if culture == 10:
            traits["star quality"] += 1
        if culture >= 8:
            traits["over-emotional"] += 1
            traits["photographer's eye"] += 1
            traits["savvy sculptor"] += 1
            traits["virtuoso"] += 1
        if culture >= 7:
            traits["artistic"] += 1
        if culture == 6:
            traits["easily impressed"] += 1
        if culture <= 2:
            traits["can't stand art"] += 1

        # Entertainment
        if entertainment == 10:
            traits["star quality"] += 1
        if entertainment >= 8:
            traits["couch potato"] += 1
            traits["dramatic"] += 1
            traits["good sense of humour"] += 1
            traits["over-emotional"] += 1
            traits["virtuoso"] += 1
        if entertainment <= 2:
            traits["no sense of humour"] += 1
            traits["technophobe"] += 1

        # Environment
        if environment >= 9:
            traits["eco-friendly"] += 1
        if environment >= 8:
            traits["green thumb"] += 1
            traits["loves the outdoors"] += 1
        if environment >= 7:
            traits["angler"] += 1
        if environment <= 5:
            traits["neurotic"] += 1
        if environment <= 3:
            traits["absent-minded"] += 1
            traits["clumsy"] += 1
            traits["grumpy"] += 1
        if environment <= 2:
            traits["hates the outdoors"] += 1

        # Fashion
        if fashion >= 9:
            traits["snob"] += 1
        if fashion >= 8:
            traits["dramatic"] += 1
        if fashion <= 2:
            traits["can't stand art"] += 1
            traits["never nude"] += 1

        # Food
        if food >= 8:
            traits["natural cook"] += 1
            traits["slob"] += 1
            traits["vegetarian"] += 1

        # Health
        if health >= 9:
            traits["brave"] += 1
            traits["neurotic"] += 1
        if health >= 8:
            traits["disciplined"] += 1
            traits["neat"] += 1
            traits["vegetarian"] += 1
        if health <= 4:
            traits["technophobe"] += 1
        if health <= 3:
            traits["couch potato"] += 1
            traits["slob"] += 1
        if health <= 2:
            traits["absent-minded"] += 1
            traits["hates the outdoors"] += 1
            traits["hydrophobic"] += 1
            traits["inappropriate"] += 1
            traits["insane"] += 1

        # Money
        if money >= 9:
            traits["frugal"] += 1
            traits["mooch"] += 1
            traits["snob"] += 1
        if money >= 8:
            traits["born salesman"] += 1
            traits["evil"] += 1
        if money <= 5:
            traits["handy"] += 1
        if money == 0:
            traits["loser"] += 1

        # Paranormal
        if paranormal <= 3:
            traits["coward"] += 1

        # Politics
        if politics == 10:
            traits["evil"] += 1
        if politics >= 9:
            traits["grumpy"] += 1
        if politics >= 8:
            traits["charismatic"] += 1
            traits["hot-headed"] += 1
            traits["schmoozer"] += 1
        if politics >= 7:
            traits["ambitious"] += 1
        if politics <= 4:
            traits["good"] += 1
        if politics <= 2:
            traits["rebellious"] += 1
            traits["shy"] += 1

        # School
        if school >= 9:
            traits["light sleeper"] += 1
            traits["workaholic"] += 1
        if school >= 8:
            traits["bookworm"] += 1
            traits["family-oriented"] += 1
            traits["genius"] += 1
            traits["nurturing"] += 1
        if school <= 3:
            traits["heavy sleeper"] += 1
        if school <= 2:
            traits["rebellious"] += 1

        # SciFi
        if sciFi >= 7:
            traits["computer whiz"] += 1
            traits["eccentric"] += 1
        if sciFi <= 3:
            traits["coward"] += 1
        if sciFi <= 2:
            traits["technophobe"] += 1

        # Sports
        if sports >= 8:
            traits["daredevil"] += 1
        if sports == 5:
            traits["excitable"] += 1

        # Toys
        if toys >= 8:
            traits["childish"] += 1
            traits["family-oriented"] += 1
        if toys >= 6:
            traits["nurturing"] += 1
        if toys <= 2:
            traits["dislikes children"] += 1

        # Travel
        if travel >= 8:
            traits["adventurous"] += 1
            traits["loves the outdoors"] += 1
            traits["photographer's eye"] += 1
        if travel <= 2:
            traits["hates the outdoors"] += 1

        # Weather
        if weather >= 9:
            traits["eco-friendly"] += 1
            traits["loves the outdoors"] += 1
        if weather >= 8:
            traits["angler"] += 1
        if weather <= 2:
            traits["hydrophobic"] += 1

        # Work
        if work == 10:
            traits["perfectionist"] += 1
        if work >= 9:
            traits["light sleeper"] += 1
            traits["perceptive"] += 1
            traits["workaholic"] += 1
        if work >= 8:
            traits["ambitious"] += 1
            traits["born salesman"] += 1
            traits["schmoozer"] += 1
        if work <= 5:
            traits["handy"] += 1
        if work <= 3:
            traits["heavy sleeper"] += 1
            traits["hot-headed"] += 1
        if work <= 2:
            traits["rebellious"] += 1
        if work == 0:
            traits["loser"] += 1

    else:
        # Animals
        if animals >= 8:
            traits["animal lover"] += 1
        if animals >= 7:
            traits["equestrian"] += 1
        if animals >= 5:
            traits["cat person"] += 1
            traits["dog person"] += 1

        # Crime
        if crime == 10:
            traits["evil"] += 1
        if crime >= 9:
            traits["brave"] += 1
            traits["perceptive"] += 1
        if crime >= 8:
            traits["kleptomaniac"] += 1
        if crime >= 6:
            traits["frugal"] += 1
        if crime <= 3:
            traits["coward"] += 1
        if crime <= 2:
            traits["shy"] += 1
        if crime == 0:
            traits["good"] += 1

        # Culture
        if culture == 10:
            traits["star quality"] += 1
        if culture >= 9:
            traits["brooding"] += 1
        if culture >= 8:
            traits["avant garde"] += 1
            traits["natural born performer"] += 1
            traits["over-emotional"] += 1
            traits["photographer's eye"] += 1
            traits["proper"] += 1
            traits["savvy sculptor"] += 1
            traits["virtuoso"] += 1
        if culture >= 7:
            traits["artistic"] += 1
        if culture == 6:
            traits["easily impressed"] += 1
        if culture <= 2:
            traits["can't stand art"] += 1

        # Entertainment
        if entertainment == 10:
            traits["star quality"] += 1
        if entertainment >= 9:
            traits["diva"]
            traits["natural born performer"] += 1
        if entertainment >= 8:
            traits["couch potato"] += 1
            traits["dramatic"] += 1
            traits["good sense of humour"] += 1
            traits["over-emotional"] += 1
            traits["virtuoso"] += 1
        if entertainment <= 2:
            traits["no sense of humour"] += 1
            traits["technophobe"] += 1

        # Environment
        if environment >= 9:
            traits["eco-friendly"] += 1
        if environment >= 8:
            traits["green thumb"] += 1
            traits["loves the outdoors"] += 1
            traits["sailor"] += 1
        if environment >= 7:
            traits["angler"] += 1
        if environment >= 6:
            traits["loves the cold"] += 1
        if environment == 5:
            traits["gatherer"] += 1
        if environment <= 5:
            traits["neurotic"] += 1
        if environment <= 3:
            traits["absent-minded"] += 1
            traits["clumsy"] += 1
            traits["grumpy"] += 1
            traits["loves the heat"] += 1
        if environment <= 2:
            traits["hates the outdoors"] += 1

        # Fashion
        if fashion >= 9:
            traits["diva"] += 1
            traits["snob"] += 1
        if fashion >= 8:
            traits["dramatic"] += 1
            traits["proper"] += 1
        if fashion <= 2:
            traits["can't stand art"] += 1
            traits["never nude"] += 1

        # Food
        if food >= 8:
            traits["natural cook"] += 1
            traits["slob"] += 1
            traits["vegetarian"] += 1

        # Health
        if health >= 9:
            traits["brave"] += 1
            traits["neurotic"] += 1
        if health >= 8:
            traits["disciplined"] += 1
            traits["loves to swim"] += 1
            traits["neat"] += 1
            traits["vegetarian"] += 1
        if health <= 4:
            traits["technophobe"] += 1
        if health == 3:
            traits["unstable"] += 1
        if health <= 3:
            traits["couch potato"] += 1
            traits["night owl"] += 1
            traits["slob"] += 1
        if health <= 2:
            traits["absent-minded"] += 1
            traits["hates the outdoors"] += 1
            traits["hydrophobic"] += 1
            traits["inappropriate"] += 1
            traits["insane"] += 1

        # Money
        if money >= 9:
            traits["frugal"] += 1
            traits["mooch"] += 1
            traits["snob"] += 1
        if money >= 8:
            traits["born salesman"] += 1
            traits["evil"] += 1
        if money <= 5:
            traits["handy"] += 1
        if money == 0:
            traits["loser"] += 1

        # Paranormal
        if paranormal >= 9:
            traits["supernatural fan"] += 1
        if paranormal <= 3:
            traits["coward"] += 1
        if paranormal <= 2:
            traits["supernatural sceptic"] += 1

        # Politics
        if politics == 10:
            traits["evil"] += 1
        if politics >= 9:
            traits["grumpy"] += 1
        if politics >= 8:
            traits["charismatic"] += 1
            traits["hot-headed"] += 1
            traits["schmoozer"] += 1
        if politics >= 7:
            traits["ambitious"] += 1
        if politics <= 4:
            traits["good"] += 1
        if politics <= 2:
            traits["rebellious"] += 1
            traits["shy"] += 1

        # School
        if school >= 9:
            traits["light sleeper"] += 1
            traits["workaholic"] += 1
        if school >= 8:
            traits["bookworm"] += 1
            traits["family-oriented"] += 1
            traits["genius"] += 1
            traits["nurturing"] += 1
        if school <= 3:
            traits["heavy sleeper"] += 1
        if school <= 2:
            traits["rebellious"] += 1

        # SciFi
        if sciFi >= 9:
            traits["supernatural fan"] += 1
        if sciFi >= 7:
            traits["bot fan"] += 1
            traits["computer whiz"] += 1
            traits["eccentric"] += 1
        if sciFi <= 3:
            traits["coward"] += 1
        if sciFi <= 2:
            traits["supernatural sceptic"] += 1
            traits["technophobe"] += 1

        # Sports
        if sports >= 8:
            traits["daredevil"] += 1
            traits["social butterfly"] += 1
        if sports == 5:
            traits["excitable"] += 1

        # Toys
        if toys >= 8:
            traits["childish"] += 1
            traits["family-oriented"] += 1
        if toys >= 6:
            traits["nurturing"] += 1
        if toys <= 2:
            traits["dislikes children"] += 1

        # Travel
        if travel >= 8:
            traits["adventurous"] += 1
            traits["loves the outdoors"] += 1
            traits["photographer's eye"] += 1
            traits["sailor"] += 1
        if travel >= 7:
            traits["loves the heat"] += 1
        if travel <= 3:
            traits["loves the cold"] += 1
        if travel <= 2:
            traits["hates the outdoors"] += 1

        # Weather
        if weather >= 9:
            traits["eco-friendly"] += 1
            traits["loves the outdoors"] += 1
        if weather >= 8:
            traits["angler"] += 1
            traits["loves to swim"] += 1
            traits["sailor"] += 1
        if weather >= 7:
            traits["loves the heat"] += 1
        if weather <= 3:
            traits["loves the cold"] += 1
        if weather <= 2:
            traits["hydrophobic"] += 1

        # Work
        if work == 10:
            traits["perfectionist"] += 1
        if work >= 9:
            traits["light sleeper"] += 1
            traits["perceptive"] += 1
            traits["workaholic"] += 1
        if work >= 8:
            traits["ambitious"] += 1
            traits["born salesman"] += 1
            traits["schmoozer"] += 1
        if work <= 5:
            traits["handy"] += 1
        if work <= 3:
            traits["heavy sleeper"] += 1
            traits["hot-headed"] += 1
        if work <= 2:
            traits["rebellious"] += 1
        if work == 0:
            traits["loser"] += 1
