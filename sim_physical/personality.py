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
            traits["brave"] += 5
        if active >= 8:
            traits["athletic"] += 5
            traits["excitable"] += 5
            traits["light sleeper"] += 5
            traits["loves the outdoors"] += 5
            traits["perceptive"] += 5
            traits["couch potato"] -= 5
            traits["grumpy"] -= 5
        if active <= 7:
            traits["disciplined"] += 5
        if active <= 2:
            traits["couch potato"] += 5
            traits["hates the outdoors"] += 5
            traits["heavy sleeper"] += 5
            traits["grumpy"] += 5
            traits["athletic"] -= 5
            traits["light sleeper"] -= 5
            traits["disciplined"] -= 5

        # Neat
        if neat >= 8:
            traits["slob"] -= 5
        if neat <= 5:
            traits["clumsy"] += 5
        if neat <= 2:
            traits["slob"] += 5

        # Nice
        if nice == 10:
            traits["good"] += 5
            traits["evil"] -= 5
        if nice >= 9:
            traits["easily impressed"] += 5
            traits["grumpy"] -= 5
        if nice >= 8:
            traits["excitable"] += 5
            traits["friendly"] += 5
        if nice >= 7:
            traits["virtuoso"] += 5
        if nice >= 6:
            traits["brave"] += 5
        if nice <= 2:
            traits["grumpy"] += 5
            traits["hates the outdoors"] += 5
            traits["easily impressed"] -= 5
            traits["friendly"] -= 5
        if nice == 0:
            traits["evil"] += 5
            traits["good"] -= 5

        # Outgoing
        if outgoing >= 9:
            traits["insane"] += 5
            traits["loner"] -= 5
            traits["artistic"] -= 5
        if outgoing >= 8:
            traits["eccentric"] += 5
        if outgoing <= 8:
            traits["artistic"] += 5
        if outgoing >= 7:
            traits["brave"] += 5
            traits["virtuoso"] += 5
        if outgoing >= 6:
            traits["friendly"] += 5
        if outgoing <= 4:
            traits["clumsy"] += 5
        if outgoing <= 2:
            traits["loner"] += 5
            traits["insane"] -= 5
            traits["eccentric"] -= 5
            traits["brave"] -= 5

        # Playful
        if playful == 10:
            traits["excitable"] += 5
            traits["insane"] += 5
        if playful >= 8:
            traits["absent-minded"] += 5
            traits["clumsy"] += 5
            traits["disciplined"] -= 5
            traits["genius"] -= 5
            traits["neurotic"] -= 5
            traits["grumpy"] -= 5
            traits["light sleeper"] -= 5
        if playful >= 6:
            traits["eccentric"] += 5
        if playful >= 5:
            traits["easily impressed"] += 5
        if playful <= 3:
            traits["disciplined"] += 5
            traits["genius"] += 5
            traits["neurotic"] += 5
        if playful <= 2:
            traits["grumpy"] += 5
            traits["light sleeper"] += 5
            traits["excitable"] -= 5
            traits["insane"] -= 5
            traits["eccentric"] -= 5

    elif age == "child":

        # Active
        if active == 10:
            traits["brave"] += 5
        if active >= 9:
            traits["party animal"] += 5
        if active >= 8:
            traits["adventurous"] += 5
            traits["athletic"] += 5
            traits["excitable"] += 5
            traits["hydrophobic"] += 5
            traits["light sleeper"] += 5
            traits["loves the outdoors"] += 5
            traits["perceptive"] += 5
            traits["couch potato"] -= 5
            traits["grumpy"] -= 5
        if active >= 6:
            traits["vehicle enthusiast"] += 5
        if active <= 7:
            traits["disciplined"] += 5
        if active <= 3:
            traits["computer whiz"] += 5
        if active <= 2:
            traits["couch potato"] += 5
            traits["hates the outdoors"] += 5
            traits["heavy sleeper"] += 5
            traits["grumpy"] += 5
            traits["athletic"] -= 5
            traits["light sleeper"] -= 5
            traits["disciplined"] -= 5
        if active == 0:
            traits["loser"] += 5

        # Neat
        if neat == 10:
            traits["perfectionist"] += 5
        if neat >= 8:
            traits["neat"] += 5
            traits["slob"] -= 5
        if neat >= 7:
            traits["eco-friendly"] += 5
        if neat >= 6:
            traits["vehicle enthusiast"] += 5
        if neat <= 5:
            traits["clumsy"] += 5
        if neat <= 2:
            traits["party animal"] += 5
            traits["slob"] += 5

        # Nice
        if nice == 10:
            traits["good"] += 5
            traits["lucky"] += 5
            traits["over-emotional"] += 5
            traits["evil"] -= 5
        if nice >= 9:
            traits["easily impressed"] += 5
            traits["grumpy"] -= 5
        if nice >= 8:
            traits["excitable"] += 5
            traits["family-oriented"] += 5
            traits["friendly"] += 5
            traits["good sense of humour"] += 5
            traits["unlucky"] += 5
        if nice >= 7:
            traits["virtuoso"] += 5
        if nice >= 6:
            traits["brave"] += 5
        if nice <= 3:
            traits["hot-headed"] += 5
            traits["perfectionist"] += 5
            traits["snob"] += 5
        if nice <= 2:
            traits["can't stand art"] += 5
            traits["grumpy"] += 5
            traits["hates the outdoors"] += 5
            traits["mean-spirited"] += 5
            traits["easily impressed"] -= 5
            traits["friendly"] -= 5
        if nice == 0:
            traits["evil"] += 5
            traits["good"] -= 5

        # Outgoing
        if outgoing == 10:
            traits["lucky"] += 5
            traits["party animal"] += 5
        if outgoing >= 9:
            traits["inappropriate"] += 5
            traits["insane"] += 5
            traits["mooch"] += 5
            traits["over-emotional"] += 5
            traits["star quality"] += 5
            traits["loner"] -= 5
            traits["artistic"] -= 5
        if outgoing >= 8:
            traits["ambitious"] += 5
            traits["daredevil"] += 5
            traits["eccentric"] += 5
        if outgoing <= 8:
            traits["artistic"] += 5
        if outgoing >= 7:
            traits["brave"] += 5
            traits["eco-friendly"] += 5
            traits["virtuoso"] += 5
        if outgoing >= 6:
            traits["friendly"] += 5
        if outgoing <= 6:
            traits["photographer's eye"] += 5
            traits["vehicle enthusiast"] += 5
        if outgoing <= 4:
            traits["angler"] += 5
            traits["clumsy"] += 5
            traits["computer whiz"] += 5
        if outgoing <= 3:
            traits["bookworm"] += 5
            traits["coward"] += 5
            traits["never nude"] += 5
            traits["unlucky"] += 5
        if outgoing <= 2:
            traits["loner"] += 5
            traits["shy"] += 5
            traits["insane"] -= 5
            traits["eccentric"] -= 5
            traits["brave"] -= 5

        # Playful
        if playful == 10:
            traits["excitable"] += 5
            traits["insane"] += 5
            traits["unlucky"] += 5
        if playful >= 9:
            traits["good sense of humour"] += 5
            traits["inappropriate"] += 5
        if playful >= 8:
            traits["absent-minded"] += 5
            traits["clumsy"] += 5
            traits["daredevil"] += 5
            traits["disciplined"] -= 5
            traits["genius"] -= 5
            traits["neurotic"] -= 5
            traits["grumpy"] -= 5
            traits["light sleeper"] -= 5
        if playful >= 7:
            traits["coward"] += 5
        if playful >= 6:
            traits["eccentric"] += 5
        if playful >= 5:
            traits["easily impressed"] += 5
        if playful <= 6:
            traits["photographer's eye"] += 5
        if playful <= 4:
            traits["bookworm"] += 5
            traits["eco-friendly"] += 5
            traits["hot-headed"] += 5
            traits["neat"] += 5
        if playful <= 3:
            traits["angler"] += 5
            traits["can't stand art"] += 5
            traits["disciplined"] += 5
            traits["genius"] += 5
            traits["mean-spirited"] += 5
            traits["neurotic"] += 5
            traits["never nude"] += 5
            traits["snob"] += 5
        if playful <= 2:
            traits["frugal"] += 5
            traits["grumpy"] += 5
            traits["light sleeper"] += 5
            traits["no sense of humour"] += 5
            traits["workaholic"] += 5
            traits["excitable"] -= 5
            traits["insane"] -= 5
            traits["eccentric"] -= 5
        if playful == 0:
            traits["perfectionist"] += 5

    elif age == "teen":

        # Active
        if active == 10:
            traits["brave"] += 5
        if active >= 9:
            traits["party animal"] += 5
        if active >= 8:
            traits["adventurous"] += 5
            traits["athletic"] += 5
            traits["excitable"] += 5
            traits["hydrophobic"] += 5
            traits["light sleeper"] += 5
            traits["loves the outdoors"] += 5
            traits["perceptive"] += 5
            traits["couch potato"] -= 5
            traits["grumpy"] -= 5
        if active >= 6:
            traits["green thumb"] += 5
            traits["vehicle enthusiast"] += 5
        if active <= 7:
            traits["disciplined"] += 5
        if active <= 3:
            traits["computer whiz"] += 5
        if active <= 2:
            traits["couch potato"] += 5
            traits["hates the outdoors"] += 5
            traits["heavy sleeper"] += 5
            traits["grumpy"] += 5
            traits["athletic"] -= 5
            traits["light sleeper"] -= 5
            traits["disciplined"] -= 5
        if active == 0:
            traits["loser"] += 5

        # Neat
        if neat == 10:
            traits["perfectionist"] += 5
        if neat >= 8:
            traits["neat"] += 5
            traits["slob"] -= 5
        if neat >= 7:
            traits["eco-friendly"] += 5
        if neat >= 6:
            traits["vehicle enthusiast"] += 5
        if neat <= 5:
            traits["clumsy"] += 5
        if neat <= 3:
            traits["green thumb"] += 5
        if neat <= 2:
            traits["party animal"] += 5
            traits["slob"] += 5

        # Nice
        if nice == 10:
            traits["good"] += 5
            traits["lucky"] += 5
            traits["over-emotional"] += 5
            traits["evil"] -= 5
        if nice >= 9:
            traits["easily impressed"] += 5
            traits["hopeless romantic"] += 5
            traits["grumpy"] -= 5
        if nice >= 8:
            traits["excitable"] += 5
            traits["family-oriented"] += 5
            traits["friendly"] += 5
            traits["good sense of humour"] += 5
            traits["nurturing"] += 5
            traits["unlucky"] += 5
        if nice >= 7:
            traits["charismatic"] += 5
            traits["childish"] += 5
            traits["virtuoso"] += 5
        if nice >= 6:
            traits["brave"] += 5
        if nice >= 5:
            traits["flirty"] += 5
        if nice <= 6:
            traits["born salesman"] += 5
        if nice <= 4:
            traits["commitment issues"] += 5
        if nice <= 3:
            traits["dislikes children"] += 5
            traits["hot-headed"] += 5
            traits["perfectionist"] += 5
            traits["snob"] += 5
        if nice <= 2:
            traits["can't stand art"] += 5
            traits["dramatic"] += 5
            traits["grumpy"] += 5
            traits["hates the outdoors"] += 5
            traits["mean-spirited"] += 5
            traits["easily impressed"] -= 5
            traits["friendly"] -= 5
        if nice == 0:
            traits["evil"] += 5
            traits["good"] -= 5

        # Outgoing
        if outgoing == 10:
            traits["lucky"] += 5
            traits["party animal"] += 5
        if outgoing >= 9:
            traits["dramatic"] += 5
            traits["inappropriate"] += 5
            traits["insane"] += 5
            traits["mooch"] += 5
            traits["over-emotional"] += 5
            traits["schmoozer"] += 5
            traits["star quality"] += 5
            traits["loner"] -= 5
            traits["artistic"] -= 5
        if outgoing >= 8:
            traits["ambitious"] += 5
            traits["born salesman"] += 5
            traits["charismatic"] += 5
            traits["commitment issues"] += 5
            traits["daredevil"] += 5
            traits["eccentric"] += 5
            traits["flirty"] += 5
            traits["great kisser"] += 5
        if outgoing <= 8:
            traits["artistic"] += 5
        if outgoing >= 7:
            traits["brave"] += 5
            traits["eco-friendly"] += 5
            traits["hopeless romantic"] += 5
            traits["virtuoso"] += 5
        if outgoing >= 6:
            traits["friendly"] += 5
        if outgoing <= 6:
            traits["photographer's eye"] += 5
            traits["vehicle enthusiast"] += 5
        if outgoing <= 4:
            traits["angler"] += 5
            traits["clumsy"] += 5
            traits["computer whiz"] += 5
        if outgoing <= 3:
            traits["bookworm"] += 5
            traits["coward"] += 5
            traits["never nude"] += 5
            traits["savvy sculptor"] += 5
            traits["unflirty"] += 5
            traits["unlucky"] += 5
        if outgoing <= 2:
            traits["loner"] += 5
            traits["shy"] += 5
            traits["insane"] -= 5
            traits["eccentric"] -= 5
            traits["brave"] -= 5

        # Playful
        if playful == 10:
            traits["excitable"] += 5
            traits["insane"] += 5
            traits["unlucky"] += 5
        if playful >= 9:
            traits["good sense of humour"] += 5
            traits["inappropriate"] += 5
        if playful >= 8:
            traits["absent-minded"] += 5
            traits["childish"] += 5
            traits["clumsy"] += 5
            traits["daredevil"] += 5
            traits["disciplined"] -= 5
            traits["genius"] -= 5
            traits["neurotic"] -= 5
            traits["grumpy"] -= 5
            traits["light sleeper"] -= 5
        if playful >= 7:
            traits["coward"] += 5
            traits["flirty"] += 5
            traits["great kisser"] += 5
        if playful >= 6:
            traits["eccentric"] += 5
        if playful >= 5:
            traits["easily impressed"] += 5
        if playful <= 6:
            traits["photographer's eye"] += 5
        if playful <= 5:
            traits["handy"] += 5
        if playful <= 4:
            traits["bookworm"] += 5
            traits["eco-friendly"] += 5
            traits["hot-headed"] += 5
            traits["neat"] += 5
        if playful <= 3:
            traits["angler"] += 5
            traits["can't stand art"] += 5
            traits["disciplined"] += 5
            traits["dislikes children"] += 5
            traits["genius"] += 5
            traits["mean-spirited"] += 5
            traits["neurotic"] += 5
            traits["never nude"] += 5
            traits["snob"] += 5
        if playful <= 2:
            traits["frugal"] += 5
            traits["grumpy"] += 5
            traits["light sleeper"] += 5
            traits["no sense of humour"] += 5
            traits["unflirty"] += 5
            traits["workaholic"] += 5
            traits["excitable"] -= 5
            traits["insane"] -= 5
            traits["eccentric"] -= 5
        if playful == 0:
            traits["perfectionist"] += 5

    else:

        # Active
        if active == 10:
            traits["brave"] += 5
        if active >= 9:
            traits["party animal"] += 5
        if active >= 8:
            traits["adventurous"] += 5
            traits["athletic"] += 5
            traits["equestrian"] += 5
            traits["excitable"] += 5
            traits["hydrophobic"] += 5
            traits["light sleeper"] += 5
            traits["loves the outdoors"] += 5
            traits["loves to swim"] += 5
            traits["perceptive"] += 5
            traits["sailor"] += 5
            traits["couch potato"] -= 5
            traits["grumpy"] -= 5
        if active >= 6:
            traits["green thumb"] += 5
            traits["vehicle enthusiast"] += 5
        if active <= 7:
            traits["disciplined"] += 5
        if active <= 4:
            traits["socially awkward"] += 5
        if active <= 3:
            traits["computer whiz"] += 5
        if active <= 2:
            traits["couch potato"] += 5
            traits["hates the outdoors"] += 5
            traits["heavy sleeper"] += 5
            traits["grumpy"] += 5
            traits["athletic"] -= 5
            traits["light sleeper"] -= 5
            traits["disciplined"] -= 5
        if active == 0:
            traits["loser"] += 5

        # Neat
        if neat == 10:
            traits["irresistible"] += 5
            traits["perfectionist"] += 5
        if neat >= 9:
            traits["proper"] += 5
        if neat >= 8:
            traits["neat"] += 5
            traits["slob"] -= 5
        if neat >= 7:
            traits["eco-friendly"] += 5
        if neat >= 6:
            traits["vehicle enthusiast"] += 5
        if neat <= 5:
            traits["clumsy"] += 5
        if neat <= 3:
            traits["green thumb"] += 5
        if neat <= 2:
            traits["party animal"] += 5
            traits["slob"] += 5

        # Nice
        if nice == 10:
            traits["good"] += 5
            traits["lucky"] += 5
            traits["over-emotional"] += 5
            traits["evil"] -= 5
        if nice >= 9:
            traits["easily impressed"] += 5
            traits["equestrian"] += 5
            traits["hopeless romantic"] += 5
            traits["grumpy"] -= 5
        if nice >= 8:
            traits["animal lover"] += 5
            traits["excitable"] += 5
            traits["family-oriented"] += 5
            traits["friendly"] += 5
            traits["good sense of humour"] += 5
            traits["nurturing"] += 5
            traits["unlucky"] += 5
        if nice >= 7:
            traits["charismatic"] += 5
            traits["childish"] += 5
            traits["dog person"] += 5
            traits["virtuoso"] += 5
        if nice >= 6:
            traits["brave"] += 5
        if nice >= 5:
            traits["cat person"] += 5
            traits["flirty"] += 5
        if nice <= 6:
            traits["born salesman"] += 5
        if nice <= 4:
            traits["commitment issues"] += 5
            traits["diva"] += 5
        if nice <= 3:
            traits["dislikes children"] += 5
            traits["hot-headed"] += 5
            traits["perfectionist"] += 5
            traits["snob"] += 5
            traits["socially awkward"] += 5
        if nice <= 2:
            traits["brooding"] += 5
            traits["can't stand art"] += 5
            traits["dramatic"] += 5
            traits["grumpy"] += 5
            traits["hates the outdoors"] += 5
            traits["mean-spirited"] += 5
            traits["supernatural sceptic"] += 5
            traits["easily impressed"] -= 5
            traits["friendly"] -= 5
        if nice == 0:
            traits["evil"] += 5
            traits["good"] -= 5

        # Outgoing
        if outgoing == 10:
            traits["irresistible"] += 5
            traits["lucky"] += 5
            traits["party animal"] += 5
        if outgoing >= 9:
            traits["dramatic"] += 5
            traits["inappropriate"] += 5
            traits["insane"] += 5
            traits["mooch"] += 5
            traits["natural born performer"] += 5
            traits["over-emotional"] += 5
            traits["schmoozer"] += 5
            traits["social butterfly"] += 5
            traits["star quality"] += 5
            traits["unstable"] += 5
            traits["loner"] -= 5
            traits["artistic"] -= 5
        if outgoing >= 8:
            traits["ambitious"] += 5
            traits["animal lover"] += 5
            traits["born salesman"] += 5
            traits["charismatic"] += 5
            traits["commitment issues"] += 5
            traits["daredevil"] += 5
            traits["diva"] += 5
            traits["eccentric"] += 5
            traits["flirty"] += 5
            traits["great kisser"] += 5
        if outgoing <= 8:
            traits["artistic"] += 5
        if outgoing >= 7:
            traits["brave"] += 5
            traits["eco-friendly"] += 5
            traits["hopeless romantic"] += 5
            traits["socially awkward"] += 5
            traits["virtuoso"] += 5
        if outgoing >= 6:
            traits["dog person"] += 5
            traits["friendly"] += 5
        if outgoing <= 6:
            traits["photographer's eye"] += 5
            traits["vehicle enthusiast"] += 5
        if outgoing <= 4:
            traits["angler"] += 5
            traits["clumsy"] += 5
            traits["computer whiz"] += 5
        if outgoing <= 3:
            traits["bookworm"] += 5
            traits["bot fan"] += 5
            traits["coward"] += 5
            traits["never nude"] += 5
            traits["night owl"] += 5
            traits["savvy sculptor"] += 5
            traits["unflirty"] += 5
            traits["unlucky"] += 5
        if outgoing <= 2:
            traits["cat person"] += 5
            traits["loner"] += 5
            traits["shy"] += 5
            traits["insane"] -= 5
            traits["eccentric"] -= 5
            traits["brave"] -= 5
        if outgoing == 0:
            traits["brooding"] += 5

        # Playful
        if playful == 10:
            traits["excitable"] += 5
            traits["insane"] += 5
            traits["unlucky"] += 5
        if playful >= 9:
            traits["good sense of humour"] += 5
            traits["inappropriate"] += 5
        if playful >= 8:
            traits["absent-minded"] += 5
            traits["animal lover"] += 5
            traits["childish"] += 5
            traits["clumsy"] += 5
            traits["daredevil"] += 5
            traits["disciplined"] -= 5
            traits["genius"] -= 5
            traits["neurotic"] -= 5
            traits["grumpy"] -= 5
            traits["light sleeper"] -= 5
        if playful >= 7:
            traits["coward"] += 5
            traits["equestrian"] += 5
            traits["flirty"] += 5
            traits["great kisser"] += 5
        if playful >= 6:
            traits["eccentric"] += 5
        if playful >= 5:
            traits["cat person"] += 5
            traits["dog person"] += 5
            traits["easily impressed"] += 5
        if playful <= 6:
            traits["photographer's eye"] += 5
        if playful <= 5:
            traits["handy"] += 5
        if playful <= 4:
            traits["avant garde"] += 5
            traits["bookworm"] += 5
            traits["bot fan"] += 5
            traits["eco-friendly"] += 5
            traits["hot-headed"] += 5
            traits["neat"] += 5
        if playful <= 3:
            traits["angler"] += 5
            traits["can't stand art"] += 5
            traits["disciplined"] += 5
            traits["dislikes children"] += 5
            traits["gatherer"] += 5
            traits["genius"] += 5
            traits["mean-spirited"] += 5
            traits["neurotic"] += 5
            traits["never nude"] += 5
            traits["snob"] += 5
        if playful <= 2:
            traits["brooding"] += 5
            traits["frugal"] += 5
            traits["grumpy"] += 5
            traits["light sleeper"] += 5
            traits["no sense of humour"] += 5
            traits["supernatural sceptic"] += 5
            traits["unflirty"] += 5
            traits["workaholic"] += 5
            traits["excitable"] -= 5
            traits["insane"] -= 5
            traits["eccentric"] -= 5
        if playful == 0:
            traits["perfectionist"] += 5
