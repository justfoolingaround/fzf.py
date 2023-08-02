"""
This example showcases a processed prompt selection.

Equivalence not applicable.
"""


import enum

import fzf


class RPS(enum.Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    @classmethod
    def get_winner(cls, choice):
        return {
            cls.ROCK: cls.SCISSORS,
            cls.PAPER: cls.ROCK,
            cls.SCISSORS: cls.PAPER,
        }[choice]


choice = fzf.fzf_prompt(
    RPS.__iter__(),
    processor=lambda x: x.value,
)

if choice is not None:
    print(
        f"You chose: {choice.value}, I chose: {RPS.get_winner(RPS(choice)).value}, I win!"
    )
else:
    print("You didn't choose anything!")
