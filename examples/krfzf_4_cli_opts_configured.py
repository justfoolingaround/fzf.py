"""
This example showcases a CLI configured prompt selection.

These options are secure and not prone to injection attacks.

Equivalence:

```sh
printf "rock\npaper\nscissors" | fzf --height="50%" --color="fg:#d60a79" --cycle --no-mouse --reverse
```
"""


import fzf

with fzf.Fzf(
    executable="fzf",
    opts=[
        "--height=50%",
        "--color=fg:#d60a79",
        "--cycle",
        "--no-mouse",
        "--reverse",
    ],
) as instance:
    instance.add_lines(
        ["rock", "paper", "scissors"],
    )

choice = instance.get_output()

if choice is not None:
    print(
        f"You chose: {choice}, I chose: { {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}[choice] }, I win!"
    )
else:
    print("You didn't choose anything!")
