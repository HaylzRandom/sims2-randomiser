# Get personality - Neat, Outgoing, Active, Playful, Nice
def get_personality():
    personality = {"Neat": 0, "Outgoing": 0, "Active": 0, "Playful": 0, "Nice": 0}

    print("\nPersonality Values\n")
    for value in personality:
        personality[value] = int(input(f"Please enter value for {value}: "))

    return personality.values()


def personality_traits(neat, outgoing, active, playful, nice, age, traits):
    # Personality

    if age == "toddler":
        # Active
        if active == 10:
            traits["brave"] += 1
        if active >= 8:
            traits["athletic"] += 1
            traits["excitable"] += 1
            traits["light sleeper"] += 1
            traits["loves the outdoors"] += 1
            traits["perceptive"] += 1
        if active <= 7:
            traits["disciplined"] += 1
        if active <= 2:
            traits["couch potato"] += 1
            traits["hates the outdoors"] += 1
            traits["heavy sleeper"] += 1

        # Neat
        if neat <= 5:
            traits["clumsy"] += 1
        if neat <= 2:
            traits["slob"] += 1

        # Nice
        if nice == 10:
            traits["good"] += 1
        if nice >= 9:
            traits["easily impressed"] += 1
        if nice >= 8:
            traits["excitable"] += 1
            traits["friendly"] += 1
        if nice >= 7:
            traits["virtuoso"] += 1
        if nice >= 6:
            traits["brave"] += 1
        if nice <= 2:
            traits["grumpy"] += 1
            traits["hates the outdoors"] += 1
        if nice == 0:
            traits["evil"] += 1

        # Outgoing
        if outgoing >= 9:
            traits["insane"] += 1
        if outgoing >= 8:
            traits["eccentric"] += 1
        if outgoing <= 8:
            traits["artistic"] += 1
        if outgoing >= 7:
            traits["brave"] += 1
            traits["virtuoso"] += 1
        if outgoing >= 6:
            traits["friendly"] += 1
        if outgoing <= 4:
            traits["clumsy"] += 1
        if outgoing <= 2:
            traits["loner"] += 1

        # Playful
        if playful == 10:
            traits["excitable"] += 1
            traits["insane"] += 1
        if playful >= 8:
            traits["absent-minded"] += 1
            traits["clumsy"] += 1
        if playful >= 6:
            traits["eccentric"] += 1
        if playful >= 5:
            traits["easily impressed"] += 1
        if playful <= 3:
            traits["disciplined"] += 1
            traits["genius"] += 1
            traits["neurotic"] += 1
        if playful <= 2:
            traits["grumpy"] += 1
            traits["light sleeper"] += 1

    elif age == "child":

        # Active
        if active == 10:
            traits["brave"] += 1
        if active >= 9:
            traits["party animal"] += 1
        if active >= 8:
            traits["adventurous"] += 1
            traits["athletic"] += 1
            traits["excitable"] += 1
            traits["hydrophobic"] += 1
            traits["light sleeper"] += 1
            traits["loves the outdoors"] += 1
            traits["perceptive"] += 1
        if active >= 6:
            traits["vehicle enthusiast"] += 1
        if active <= 7:
            traits["disciplined"] += 1
        if active <= 3:
            traits["computer whiz"] += 1
        if active <= 2:
            traits["couch potato"] += 1
            traits["hates the outdoors"] += 1
            traits["heavy sleeper"] += 1
        if active == 0:
            traits["loser"] += 1

        # Neat
        if neat == 10:
            traits["perfectionist"] += 1
        if neat >= 8:
            traits["neat"] += 1
        if neat >= 7:
            traits["eco-friendly"] += 1
        if neat >= 6:
            traits["vehicle enthusiast"] += 1
        if neat <= 5:
            traits["clumsy"] += 1
        if neat <= 2:
            traits["party animal"] += 1
            traits["slob"] += 1

        # Nice
        if nice == 10:
            traits["good"] += 1
            traits["lucky"] += 1
            traits["over-emotional"] += 1
        if nice >= 9:
            traits["easily impressed"] += 1
        if nice >= 8:
            traits["excitable"] += 1
            traits["family-oriented"] += 1
            traits["friendly"] += 1
            traits["good sense of humour"] += 1
            traits["unlucky"] += 1
        if nice >= 7:
            traits["virtuoso"] += 1
        if nice >= 6:
            traits["brave"] += 1
        if nice <= 3:
            traits["hot-headed"] += 1
            traits["perfectionist"] += 1
            traits["snob"] += 1
        if nice <= 2:
            traits["can't stand art"] += 1
            traits["grumpy"] += 1
            traits["hates the outdoors"] += 1
            traits["mean-spirited"] += 1
        if nice == 0:
            traits["evil"] += 1

        # Outgoing
        if outgoing == 10:
            traits["lucky"] += 1
            traits["party animal"] += 1
        if outgoing >= 9:
            traits["inappropriate"] += 1
            traits["insane"] += 1
            traits["mooch"] += 1
            traits["over-emotional"] += 1
            traits["star quality"] += 1
        if outgoing >= 8:
            traits["ambitious"] += 1
            traits["daredevil"] += 1
            traits["eccentric"] += 1
        if outgoing <= 8:
            traits["artistic"] += 1
        if outgoing >= 7:
            traits["brave"] += 1
            traits["eco-friendly"] += 1
            traits["virtuoso"] += 1
        if outgoing >= 6:
            traits["friendly"] += 1
        if outgoing <= 6:
            traits["photographer's eye"] += 1
            traits["vehicle enthusiast"] += 1
        if outgoing <= 4:
            traits["angler"] += 1
            traits["clumsy"] += 1
            traits["computer whiz"] += 1
        if outgoing <= 3:
            traits["bookworm"] += 1
            traits["coward"] += 1
            traits["never nude"] += 1
            traits["unlucky"] += 1
        if outgoing <= 2:
            traits["loner"] += 1
            traits["shy"] += 1

        # Playful
        if playful == 10:
            traits["excitable"] += 1
            traits["insane"] += 1
            traits["unlucky"] += 1
        if playful >= 9:
            traits["good sense of humour"] += 1
            traits["inappropriate"] += 1
        if playful >= 8:
            traits["absent-minded"] += 1
            traits["clumsy"] += 1
            traits["daredevil"] += 1
        if playful >= 7:
            traits["coward"] += 1
        if playful >= 6:
            traits["eccentric"] += 1
        if playful >= 5:
            traits["easily impressed"] += 1
        if playful <= 6:
            traits["photographer's eye"] += 1
        if playful <= 4:
            traits["bookworm"] += 1
            traits["eco-friendly"] += 1
            traits["hot-headed"] += 1
            traits["neat"] += 1
        if playful <= 3:
            traits["angler"] += 1
            traits["can't stand art"] += 1
            traits["disciplined"] += 1
            traits["genius"] += 1
            traits["mean-spirited"] += 1
            traits["neurotic"] += 1
            traits["never nude"] += 1
            traits["snob"] += 1
        if playful <= 2:
            traits["frugal"] += 1
            traits["grumpy"] += 1
            traits["light sleeper"] += 1
            traits["no sense of humour"] += 1
            traits["workaholic"] += 1
        if playful == 0:
            traits["perfectionist"] += 1

    elif age == "teen":

        # Active
        if active == 10:
            traits["brave"] += 1
        if active >= 9:
            traits["party animal"] += 1
        if active >= 8:
            traits["adventurous"] += 1
            traits["athletic"] += 1
            traits["excitable"] += 1
            traits["hydrophobic"] += 1
            traits["light sleeper"] += 1
            traits["loves the outdoors"] += 1
            traits["perceptive"] += 1
        if active >= 6:
            traits["green thumb"] += 1
            traits["vehicle enthusiast"] += 1
        if active <= 7:
            traits["disciplined"] += 1
        if active <= 3:
            traits["computer whiz"] += 1
        if active <= 2:
            traits["couch potato"] += 1
            traits["hates the outdoors"] += 1
            traits["heavy sleeper"] += 1
        if active == 0:
            traits["loser"] += 1

        # Neat
        if neat == 10:
            traits["perfectionist"] += 1
        if neat >= 8:
            traits["neat"] += 1
        if neat >= 7:
            traits["eco-friendly"] += 1
        if neat >= 6:
            traits["vehicle enthusiast"] += 1
        if neat <= 5:
            traits["clumsy"] += 1
        if neat <= 3:
            traits["green thumb"] += 1
        if neat <= 2:
            traits["party animal"] += 1
            traits["slob"] += 1

        # Nice
        if nice == 10:
            traits["good"] += 1
            traits["lucky"] += 1
            traits["over-emotional"] += 1
        if nice >= 9:
            traits["easily impressed"] += 1
            traits["hopeless romantic"] += 1
        if nice >= 8:
            traits["excitable"] += 1
            traits["family-oriented"] += 1
            traits["friendly"] += 1
            traits["good sense of humour"] += 1
            traits["nurturing"] += 1
            traits["unlucky"] += 1
        if nice >= 7:
            traits["charismatic"] += 1
            traits["childish"] += 1
            traits["virtuoso"] += 1
        if nice >= 6:
            traits["brave"] += 1
        if nice >= 5:
            traits["flirty"] += 1
        if nice <= 6:
            traits["born salesman"] += 1
        if nice <= 4:
            traits["commitment issues"] += 1
        if nice <= 3:
            traits["dislikes children"] += 1
            traits["hot-headed"] += 1
            traits["perfectionist"] += 1
            traits["snob"] += 1
        if nice <= 2:
            traits["can't stand art"] += 1
            traits["dramatic"] += 1
            traits["grumpy"] += 1
            traits["hates the outdoors"] += 1
            traits["mean-spirited"] += 1
        if nice == 0:
            traits["evil"] += 1

        # Outgoing
        if outgoing == 10:
            traits["lucky"] += 1
            traits["party animal"] += 1
        if outgoing >= 9:
            traits["dramatic"] += 1
            traits["inappropriate"] += 1
            traits["insane"] += 1
            traits["mooch"] += 1
            traits["over-emotional"] += 1
            traits["schmoozer"] += 1
            traits["star quality"] += 1
        if outgoing >= 8:
            traits["ambitious"] += 1
            traits["born salesman"] += 1
            traits["charismatic"] += 1
            traits["commitment issues"] += 1
            traits["daredevil"] += 1
            traits["eccentric"] += 1
            traits["flirty"] += 1
            traits["great kisser"] += 1
        if outgoing <= 8:
            traits["artistic"] += 1
        if outgoing >= 7:
            traits["brave"] += 1
            traits["eco-friendly"] += 1
            traits["hopeless romantic"] += 1
            traits["virtuoso"] += 1
        if outgoing >= 6:
            traits["friendly"] += 1
        if outgoing <= 6:
            traits["photographer's eye"] += 1
            traits["vehicle enthusiast"] += 1
        if outgoing <= 4:
            traits["angler"] += 1
            traits["clumsy"] += 1
            traits["computer whiz"] += 1
        if outgoing <= 3:
            traits["bookworm"] += 1
            traits["coward"] += 1
            traits["never nude"] += 1
            traits["savvy sculptor"] += 1
            traits["unflirty"] += 1
            traits["unlucky"] += 1
        if outgoing <= 2:
            traits["loner"] += 1
            traits["shy"] += 1

        # Playful
        if playful == 10:
            traits["excitable"] += 1
            traits["insane"] += 1
            traits["unlucky"] += 1
        if playful >= 9:
            traits["good sense of humour"] += 1
            traits["inappropriate"] += 1
        if playful >= 8:
            traits["absent-minded"] += 1
            traits["childish"] += 1
            traits["clumsy"] += 1
            traits["daredevil"] += 1
        if playful >= 7:
            traits["coward"] += 1
            traits["flirty"] += 1
            traits["great kisser"] += 1
        if playful >= 6:
            traits["eccentric"] += 1
        if playful >= 5:
            traits["easily impressed"] += 1
        if playful <= 6:
            traits["photographer's eye"] += 1
        if playful <= 5:
            traits["handy"] += 1
        if playful <= 4:
            traits["bookworm"] += 1
            traits["eco-friendly"] += 1
            traits["hot-headed"] += 1
            traits["neat"] += 1
        if playful <= 3:
            traits["angler"] += 1
            traits["can't stand art"] += 1
            traits["disciplined"] += 1
            traits["dislikes children"] += 1
            traits["genius"] += 1
            traits["mean-spirited"] += 1
            traits["neurotic"] += 1
            traits["never nude"] += 1
            traits["snob"] += 1
        if playful <= 2:
            traits["frugal"] += 1
            traits["grumpy"] += 1
            traits["light sleeper"] += 1
            traits["no sense of humour"] += 1
            traits["unflirty"] += 1
            traits["workaholic"] += 1
        if playful == 0:
            traits["perfectionist"] += 1

    else:

        # Active
        if active == 10:
            traits["brave"] += 1
        if active >= 9:
            traits["party animal"] += 1
        if active >= 8:
            traits["adventurous"] += 1
            traits["athletic"] += 1
            traits["equestrian"] += 1
            traits["excitable"] += 1
            traits["hydrophobic"] += 1
            traits["light sleeper"] += 1
            traits["loves the outdoors"] += 1
            traits["loves to swim"] += 1
            traits["perceptive"] += 1
            traits["sailor"] += 1
        if active >= 6:
            traits["green thumb"] += 1
            traits["vehicle enthusiast"] += 1
        if active <= 7:
            traits["disciplined"] += 1
        if active <= 4:
            traits["socially awkward"] += 1
        if active <= 3:
            traits["computer whiz"] += 1
        if active <= 2:
            traits["couch potato"] += 1
            traits["hates the outdoors"] += 1
            traits["heavy sleeper"] += 1
        if active == 0:
            traits["loser"] += 1

        # Neat
        if neat == 10:
            traits["irresistible"] += 1
            traits["perfectionist"] += 1
        if neat >= 9:
            traits["proper"] += 1
        if neat >= 8:
            traits["neat"] += 1
        if neat >= 7:
            traits["eco-friendly"] += 1
        if neat >= 6:
            traits["vehicle enthusiast"] += 1
        if neat <= 5:
            traits["clumsy"] += 1
        if neat <= 3:
            traits["green thumb"] += 1
        if neat <= 2:
            traits["party animal"] += 1
            traits["slob"] += 1

        # Nice
        if nice == 10:
            traits["good"] += 1
            traits["lucky"] += 1
            traits["over-emotional"] += 1
        if nice >= 9:
            traits["easily impressed"] += 1
            traits["equestrian"] += 1
            traits["hopeless romantic"] += 1
        if nice >= 8:
            traits["animal lover"] += 1
            traits["excitable"] += 1
            traits["family-oriented"] += 1
            traits["friendly"] += 1
            traits["good sense of humour"] += 1
            traits["nurturing"] += 1
            traits["unlucky"] += 1
        if nice >= 7:
            traits["charismatic"] += 1
            traits["childish"] += 1
            traits["dog person"] += 1
            traits["virtuoso"] += 1
        if nice >= 6:
            traits["brave"] += 1
        if nice >= 5:
            traits["cat person"] += 1
            traits["flirty"] += 1
        if nice <= 6:
            traits["born salesman"] += 1
        if nice <= 4:
            traits["commitment issues"] += 1
            traits["diva"] += 1
        if nice <= 3:
            traits["dislikes children"] += 1
            traits["hot-headed"] += 1
            traits["perfectionist"] += 1
            traits["snob"] += 1
            traits["socially awkward"] += 1
        if nice <= 2:
            traits["brooding"] += 1
            traits["can't stand art"] += 1
            traits["dramatic"] += 1
            traits["grumpy"] += 1
            traits["hates the outdoors"] += 1
            traits["mean-spirited"] += 1
            traits["supernatural sceptic"] += 1
        if nice == 0:
            traits["evil"] += 1

        # Outgoing
        if outgoing == 10:
            traits["irresistible"] += 1
            traits["lucky"] += 1
            traits["party animal"] += 1
        if outgoing >= 9:
            traits["dramatic"] += 1
            traits["inappropriate"] += 1
            traits["insane"] += 1
            traits["mooch"] += 1
            traits["natural born performer"] += 1
            traits["over-emotional"] += 1
            traits["schmoozer"] += 1
            traits["social butterfly"] += 1
            traits["star quality"] += 1
            traits["unstable"] += 1
        if outgoing >= 8:
            traits["ambitious"] += 1
            traits["animal lover"] += 1
            traits["born salesman"] += 1
            traits["charismatic"] += 1
            traits["commitment issues"] += 1
            traits["daredevil"] += 1
            traits["diva"] += 1
            traits["eccentric"] += 1
            traits["flirty"] += 1
            traits["great kisser"] += 1
        if outgoing <= 8:
            traits["artistic"] += 1
        if outgoing >= 7:
            traits["brave"] += 1
            traits["eco-friendly"] += 1
            traits["hopeless romantic"] += 1
            traits["socially awkward"] += 1
            traits["virtuoso"] += 1
        if outgoing >= 6:
            traits["dog person"] += 1
            traits["friendly"] += 1
        if outgoing <= 6:
            traits["photographer's eye"] += 1
            traits["vehicle enthusiast"] += 1
        if outgoing <= 4:
            traits["angler"] += 1
            traits["clumsy"] += 1
            traits["computer whiz"] += 1
        if outgoing <= 3:
            traits["bookworm"] += 1
            traits["bot fan"] += 1
            traits["coward"] += 1
            traits["never nude"] += 1
            traits["night owl"] += 1
            traits["savvy sculptor"] += 1
            traits["unflirty"] += 1
            traits["unlucky"] += 1
        if outgoing <= 2:
            traits["cat person"] += 1
            traits["loner"] += 1
            traits["shy"] += 1
        if outgoing == 0:
            traits["brooding"] += 1

        # Playful
        if playful == 10:
            traits["excitable"] += 1
            traits["insane"] += 1
            traits["unlucky"] += 1
        if playful >= 9:
            traits["good sense of humour"] += 1
            traits["inappropriate"] += 1
        if playful >= 8:
            traits["absent-minded"] += 1
            traits["animal lover"] += 1
            traits["childish"] += 1
            traits["clumsy"] += 1
            traits["daredevil"] += 1
        if playful >= 7:
            traits["coward"] += 1
            traits["equestrian"] += 1
            traits["flirty"] += 1
            traits["great kisser"] += 1
        if playful >= 6:
            traits["eccentric"] += 1
        if playful >= 5:
            traits["cat person"] += 1
            traits["dog person"] += 1
            traits["easily impressed"] += 1
        if playful <= 6:
            traits["photographer's eye"] += 1
        if playful <= 5:
            traits["handy"] += 1
        if playful <= 4:
            traits["avant garde"] += 1
            traits["bookworm"] += 1
            traits["bot fan"] += 1
            traits["eco-friendly"] += 1
            traits["hot-headed"] += 1
            traits["neat"] += 1
        if playful <= 3:
            traits["angler"] += 1
            traits["can't stand art"] += 1
            traits["disciplined"] += 1
            traits["dislikes children"] += 1
            traits["gatherer"] += 1
            traits["genius"] += 1
            traits["mean-spirited"] += 1
            traits["neurotic"] += 1
            traits["never nude"] += 1
            traits["snob"] += 1
        if playful <= 2:
            traits["brooding"] += 1
            traits["frugal"] += 1
            traits["grumpy"] += 1
            traits["light sleeper"] += 1
            traits["no sense of humour"] += 1
            traits["supernatural sceptic"] += 1
            traits["unflirty"] += 1
            traits["workaholic"] += 1
        if playful == 0:
            traits["perfectionist"] += 1
