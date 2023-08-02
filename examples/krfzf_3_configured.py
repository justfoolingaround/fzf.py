"""
This example showcases a configured+simple prompt selection.

Equivalence:

```sh
printf "rock\npaper\nscissors" | fzf --height="50%" --color="fg:#d60a79" --cycle --no-mouse --reverse
```

"""

import fzf

choice = fzf.fzf_prompt(
    ["rock", "paper", "scissors"],
    prompt_string="Select a choice: ",
    height="50%",
    color="fg:#d60a79",
    cycle=True,
    mouse=False,
    reversed_layout=True,
)

# Get configuration from fzf/options.py


if choice is not None:
    print(
        f"You chose: {choice}, I chose: { {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}[choice] }, I win!"
    )
else:
    print("You didn't choose anything!")
