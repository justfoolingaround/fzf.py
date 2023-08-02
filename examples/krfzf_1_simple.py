"""
This example showcases a processed prompt selection.

Equivalence:

```sh
printf "rock\npaper\nscissors" | fzf
```

"""


import fzf

choice = fzf.fzf_prompt(
    ["rock", "paper", "scissors"],
    prompt_string="Select a choice: ",
)

if choice is not None:
    print(
        f"You chose: {choice}, I chose: { {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}[choice] }, I win!"
    )
else:
    print("You didn't choose anything!")
