"""
This example showcases a live configured prompt selection.

Live could be supported by fzf.fzf_prompt if the function
is ran in a separate thread.

Partial equivalence:

```sh
seq 1 inf | fzf --height="50%" --color="fg:#d60a79" --cycle --no-mouse --reverse
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
    i = 1

    while instance.is_alive:
        instance.add_lines((str(i),))
        i += 1

choice = instance.get_output()


if choice is not None:
    print(f"Range: {', '.join(map(str, range(1, int(choice) + 1)))}")
