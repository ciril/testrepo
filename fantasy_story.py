"""Generate a short, randomized fantasy story."""

import argparse
import random


HEROES = ["Mira the apprentice mage", "Thorn the wandering knight", "Pip the fearless fox"]
PLACES = ["the Moonlit Forest", "the ruins of Emberfall", "a village above the clouds"]
COMPANIONS = ["a talkative raven", "a tiny dragon with hiccups", "an old map that gave advice"]
ADVENTURES = [
    (
        "the moon had vanished from the sky",
        "a silver bell",
        "rang it once, and the moon returned to its place",
    ),
    (
        "a sleeping giant blocked the only bridge",
        "a lantern full of blue fire",
        "held it high, revealing a hidden path around the giant",
    ),
    (
        "the village well had turned into starlight",
        "a seed that glowed like sunrise",
        "planted it beside the well, and a moonflower restored the water",
    ),
]
ENDINGS = [
    "From then on, they kept a place at the table for unexpected magic.",
    "The kingdom celebrated, though the raven took credit for everything.",
    "And whenever the stars shimmered, they remembered their strange adventure.",
]


def generate_story(rng=None):
    """Return a randomly assembled fantasy story."""
    chooser = rng or random
    hero = chooser.choice(HEROES)
    place = chooser.choice(PLACES)
    companion = chooser.choice(COMPANIONS)
    trouble, magic, solution = chooser.choice(ADVENTURES)
    ending = chooser.choice(ENDINGS)

    return (
        f"{hero} traveled to {place} with {companion}. There, they discovered that {trouble}. "
        f"Luckily, they carried {magic}. With a little courage, they {solution}. "
        f"{ending}"
    )


def main():
    parser = argparse.ArgumentParser(description="Generate a random fantasy short story.")
    parser.add_argument("--seed", type=int, help="use a seed to reproduce a story")
    args = parser.parse_args()
    print(generate_story(random.Random(args.seed)))


if __name__ == "__main__":
    main()
