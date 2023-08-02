"""
This example showcases a preview.

Equivalence:

```sh
printf "https://github.com/justfoolingaround\nhttps://www.youtube.com/\nhttps://www.reddit.com/" | fzf --preview="curl -sLI {}"
```
"""

from fzf import fzf_prompt

print(
    "Saw the preview for:",
    fzf_prompt(
        [
            "https://github.com/justfoolingaround",
            "https://www.youtube.com/",
            "https://www.reddit.com/",
        ],
        preview="curl -sLI {}",
    ),
)
