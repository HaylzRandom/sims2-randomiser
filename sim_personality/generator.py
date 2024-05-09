from globals import (
    MIN,
    MAX,
    SKIN,
    EYE_COLOURS,
    HAIR_COLOUR,
    EYEBROWS,
    TURN_ONS_OFFS,
    BOOL_ANSWER,
    FAVOURITE_COLOURS,
)
from random import randint, choice, sample
import inquirer


# Functions
def generate_personality():
    personality = [
        randint(0, 10) for _ in range(5)
    ]  # Generate random numbers for each variable
    total = sum(personality)  # Calculate the total sum

    # Check if total is not 25 and regenerate numbers if necessary
    while total != 25:
        personality = [randint(0, 10) for _ in range(5)]
        total = sum(personality)

    return personality


def generate_number(a, b):
    value = randint(a, b)

    if value == 0:
        return generate_number(a, b)
    else:
        return value


def generate_sim():

    print("Sim Randomiser Generator\n")

    gender = inquirer.list_input("Male or Female?", choices=["Female", "Male"]).lower()

    print("Sim Physical Traits\n")
    print(f"Skin: {choice(SKIN)}")
    print(f"Eyes: {choice(EYE_COLOURS)}")
    print(f"Hair Colour: {choice(HAIR_COLOUR)}")
    print(f"Eyebrows: {choice(EYEBROWS)}")
    print(f"Fatness?: {choice(BOOL_ANSWER)}")
    print(f"Wears Glasses?: {choice(BOOL_ANSWER)}")

    if gender == "male":
        print(f"Beard: {choice(BOOL_ANSWER)}")

    chosenValues = sample(TURN_ONS_OFFS, 3)

    turnOn1, turnOn2, turnOff = chosenValues

    print(f"\nTurn Ons & Offs: {turnOn1}, {turnOn2} & {turnOff}")
    print(f"Favourite Colour: {choice(FAVOURITE_COLOURS)}")

    sloppy, shy, lazy, serious, grouchy = generate_personality()

    print("\nPersonality")
    print(f"\nSloppy/Neat: {sloppy}")
    print(f"Shy/Outgoing: {shy}")
    print(f"Lazy/Active: {lazy}")
    print(f"Serious/Playful: {serious}")
    print(f"Grouchy/Nice: {grouchy}\n")

    face = inquirer.confirm(message="Roll Face?", default=True)

    if face:
        print(f"\nFace Outer Orbit Depth: {generate_number(MIN, MAX)}")
        print(f"Face Earshape: {generate_number(MIN, MAX)}")
        print(f"Face Ear Depth Difference: {generate_number(MIN, MAX)}")
        print(f"Face Upper Jowl Width: {generate_number(MIN, MAX)}")
        print(f"Face Cheek Raise: {generate_number(MIN, MAX)}")
        print(f"Face Ear Sticking-Out: {generate_number(MIN, MAX)}")
        print(f"Face Ear Rotation: {generate_number(MIN, MAX)}")
        print(f"Face Gaunt/Plump: {generate_number(MIN, MAX)}")
        print(f"Face Long/Short: {generate_number(MIN, MAX)}")
        print(f"Cheek Size: {generate_number(MIN, MAX)}")
        print(f"Lower Face Width: {generate_number(MIN, MAX)}")
        print(f"Upper Face Width: {generate_number(MIN, MAX)}")
        print(f"Underneck Up-Down: {generate_number(MIN, MAX)}")
        print(f"Cheekbone Fwd-Back: {generate_number(MIN, MAX)}")
        print(f"Cheekbone Size: {generate_number(MIN, MAX)}")
        print(f"Cheekbone Up-Down: {generate_number(MIN, MAX)}")
        print(f"Ear Size: {generate_number(MIN, MAX)}\n")

    brow = inquirer.confirm(message="Roll Brow?", default=True)

    if brow:
        print(f"\nBrow Eyebrow Center Shift: {generate_number(MIN, MAX)}")
        print(f"Brow Eyebrow Head Thickness: {generate_number(MIN, MAX)}")
        print(f"Brow Eyebrows Distance: {generate_number(MIN, MAX)}")
        print(f"Brow Thickness: {generate_number(MIN, MAX)}")
        print(f"Brow Up-Down: {generate_number(MIN, MAX)}")
        print(f"Brow Arch: {generate_number(MIN, MAX)}")
        print(f"Brow Rotate: {generate_number(MIN, MAX)}")
        print(f"Brow Orbit Shape: {generate_number(MIN, MAX)}")
        print(f"Forehead In-Out: {generate_number(MIN, MAX)}")
        print(f"Brow In-Out: {generate_number(MIN, MAX)}\n")

    eyes = inquirer.confirm(message="Roll Eyes?", default=True)

    if eyes:
        print(f"\nEye Lower Eyelid Width: {generate_number(MIN, MAX)}")
        print(f"Eye Lower Eyelid Height: {generate_number(MIN, MAX)}")
        print(f"Eye Eye Bag Lift: {generate_number(MIN, MAX)}")
        print(f"Eye Eye Bag Curve: {generate_number(MIN, MAX)}")
        print(f"Eye Lower Eyelid Shift: {generate_number(MIN, MAX)}")
        print(f"Eye Corners Height Difference: {generate_number(MIN, MAX)}")
        print(f"Eye Corners Distance: {generate_number(MIN, MAX)}")
        print(f"Eye Upper Eyelid Width: {generate_number(MIN, MAX)}")
        print(f"Eye Upper Eyelid Height: {generate_number(MIN, MAX)}")
        print(f"Eye Eyelid Crease Lift: {generate_number(MIN, MAX)}")
        print(f"Eye Eyelid Crease Curve: {generate_number(MIN, MAX)}")
        print(f"Eye Upper Eyelid Shift: {generate_number(MIN, MAX)}")
        print(f"Eye Lower Eyelid Curve: {generate_number(MIN, MAX)}")
        print(f"Eye Upper Eyelid Lift: {generate_number(MIN, MAX)}")
        print(f"Eye Upper Eyelid Curve: {generate_number(MIN, MAX)}")
        print(f"Eye Eye Squint: {generate_number(MIN, MAX)}")
        print(f"Eye Eyelash Curl: {generate_number(MIN, MAX)}")
        print(f"Eye Size: {generate_number(MIN, MAX)}")
        print(f"Eye Width: {generate_number(MIN, MAX)}")
        print(f"Outer Eye Down-Up: {generate_number(MIN, MAX)}")
        print(f"Eye Closeness: {generate_number(MIN, MAX)}")
        print(f"Eyes Up-Down: {generate_number(MIN, MAX)}")
        print(f"Orbit Up-Down: {generate_number(MIN, MAX)}")
        print(f"Eye Deepness: {generate_number(MIN, MAX)}")
        print(f"Eye Squint: {generate_number(MIN, MAX)}")
        print(f"Eyelash Size: {generate_number(MIN, MAX)}")
        print(f"Eyes Rotate: {generate_number(MIN, MAX)}\n")

    nose = inquirer.confirm(message="Roll Nose?", default=True)

    if nose:
        print(f"\nNose Nostril Rotation: {generate_number(MIN, MAX)}")
        print(f"Nose Nasal Tip Size: {generate_number(MIN, MAX)}")
        print(f"Nose Nose Definition: {generate_number(MIN, MAX)}")
        print(f"Nose Nose Root Depth: {generate_number(MIN, MAX)}")
        print(f"Nose Nostril Height: {generate_number(MIN, MAX)}")
        print(f"Nose Septum Width: {generate_number(MIN, MAX)}")
        print(f"Nose Size: {generate_number(MIN, MAX)}")
        print(f"Nose Width: {generate_number(MIN, MAX)}")
        print(f"Nostril Width: {generate_number(MIN, MAX)}")
        print(f"Nose Length: {generate_number(MIN, MAX)}")
        print(f"Nose Up-Down: {generate_number(MIN, MAX)}")
        print(f"Nose Turned Up-Down: {generate_number(MIN, MAX)}")
        print(f"Nose Tip Up-Down: {generate_number(MIN, MAX)}")
        print(f"Nose Tip Turn: {generate_number(MIN, MAX)}")
        print(f"Bridge Curve: {generate_number(MIN, MAX)}")
        print(f"Bridge In-Out: {generate_number(MIN, MAX)}")
        print(f"Bridge Width: {generate_number(MIN, MAX)}")
        print(f"Nose In-Out: {generate_number(MIN, MAX)}\n")

    mouth = inquirer.confirm(message="Roll Mouth?", default=True)

    if mouth:
        print(f"\nMouth Philtrum Depth: {generate_number(MIN, MAX)}")
        print(f"Mouth Lower Lip Center Height: {generate_number(MIN, MAX)}")
        print(f"Mouth Cupid's Bow Height: {generate_number(MIN, MAX)}")
        print(f"Mouth Cupid's Bow Width: {generate_number(MIN, MAX)}")
        print(f"Mouth Lips Depth Difference: {generate_number(MIN, MAX)}")
        print(f"Mouth Upper Lip Raise: {generate_number(MIN, MAX)}")
        print(f"Mouth Cupid's Bow Shape: {generate_number(MIN, MAX)}")
        print(f"Mouth Width: {generate_number(MIN, MAX)}")
        print(f"Mouth Up-Down: {generate_number(MIN, MAX)}")
        print(f"Mouth Corner Down-Up: {generate_number(MIN, MAX)}")
        print(f"Lips Thickness: {generate_number(MIN, MAX)}")
        print(f"Upper Lip Pinch: {generate_number(MIN, MAX)}")
        print(f"Lower Lip Pinch: {generate_number(MIN, MAX)}")
        print(f"Upper Lip Thickness: {generate_number(MIN, MAX)}")
        print(f"Lower Lip Thickness: {generate_number(MIN, MAX)}")
        print(f"Mouth Corner Fwd-Back: {generate_number(MIN, MAX)}")
        print(f"Mouth In-Out: {generate_number(MIN, MAX)}\n")

    jaw = inquirer.confirm(message="Roll Jaw?", default=True)

    if jaw:
        print(f"\nChin Jaw Definition: {generate_number(MIN, MAX)}")
        print(f"Chin Chin Definition: {generate_number(MIN, MAX)}")
        print(f"Chin Chin Cleft: {generate_number(MIN, MAX)}")
        print(f"Chin Chin Crease Depth: {generate_number(MIN, MAX)}")
        print(f"Chin Up-Down: {generate_number(MIN, MAX)}")
        print(f"Chin In-Out: {generate_number(MIN, MAX)}")
        print(f"Chin Point: {generate_number(MIN, MAX)}")
        print(f"Jaw In-Out: {generate_number(MIN, MAX)}")
        print(f"Jaw Square-Angled: {generate_number(MIN, MAX)}")
        print(f"Jaw Width: {generate_number(MIN, MAX)}")
        print(f"Jaw Taper: {generate_number(MIN, MAX)}\n")

    templates = inquirer.confirm(message="Roll Face Templates?", default=True)

    if templates:

        print("\nFace Templates")

        if gender == "male":
            maxFace = 106
        if gender == "female":
            maxFace = 105

        minFace = 1

        print(
            f"\nFace: {generate_number(minFace, maxFace)} + {generate_number(minFace, maxFace)}"
        )
        print(
            f"Brow: {generate_number(minFace, maxFace)} + {generate_number(minFace, maxFace)}"
        )
        print(
            f"Eyes: {generate_number(minFace, maxFace)} + {generate_number(minFace, maxFace)}"
        )
        print(
            f"Nose: {generate_number(minFace, maxFace)} + {generate_number(minFace, maxFace)}"
        )
        print(
            f"Mouth: {generate_number(minFace, maxFace)} + {generate_number(minFace, maxFace)}"
        )
        print(
            f"Jaw: {generate_number(minFace, maxFace)} + {generate_number(minFace, maxFace)}"
        )

        print("\nSim Creation Completed!")
