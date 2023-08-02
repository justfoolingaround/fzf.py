"""
This example showcases a preview, except it uses a subprocess instead of a shell command.

Equivalence:

```sh
ls | fzf --preview="cat {}"
```
"""

import subprocess

from fzf import Fzf

with Fzf.load_with_options(preview="cat {}") as fzf:
    ls = subprocess.Popen(["ls"], stdout=subprocess.PIPE)

    fzf.pipe_from_stream(ls.stdout)

print(fzf.get_output())
