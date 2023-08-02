<h1 align="center">Fzf.py - A Pythonic Fzf Wrapper</h1>

<p align="center">Fully covers the fzf command line arguments, alongside Pythonic generators and context managers.</p>

This project uses `subprocess.PIPE` at a non-blocking interface with the fzf `stdin`. This allows the project to:

*   Write continuously to the fzf `stdin`,
*   Stop when the fzf `stdin` is closed,
*   Not write **any** files and use the unsafe shell interface. [Ahem.](https://github.com/nk412/pyfzf/blob/master/pyfzf/pyfzf.py#L57)

## Installation

This project can be installed on to your device via different mechanisms, these mechanisms are listed below in the order of ease.

<ol>

<li id="pip-installation"> PIP Installs Packages <strong>aka</strong> PIP Installation 

    $ pip install git+https://www.github.com/justfoolingaround/fzf.py

</li>
<li id="source-code-download"> Source Code Download

    $ git clone https://www.github.com/justfoolingaround/fzf.py

Given that you have [`git`](https://git-scm.com/) installed, you can clone the repository from GitHub. If you do not have or want to deal with installation of [`git`](https://git-scm.com/), you can simply download the repository using [this link.](https://github.com/justfoolingaround/gitcord/archive/refs/heads/master.zip)

After the repository is downloaded and placed in an appropriate directory, you can use the following command:

    $ pip install .

</li>

</ol>
This command is to be executed from the directory where the repository is located.

## Usage

Please see [the examples present in the codebase](./examples) to get a gist of how the codebase is supposed to be used in various different contexts.

## `class Fzf` vs. `function fzf_prompt`

In the above examples, two very different classes and functions are being used.

The class `Fzf` is a raw interface to `fzf`. It is mainly suited for instances where you would want to get total control over the fzf process, i.e. adding more results and such.

During raw declaraction, it will take cli directly from you. To get automatic parsing, you may use the `.load_with_options` class method. This will automatically handle keyword arguments and translate them to fzf arguments.

The function `fzf_prompt` is a helper function built over the class. It will handle processing and stdout prompts automatically so that you don't need to mess around much with how data is passed to `fzf`.

The class may also be used as a context manager for that syntactic sugar.

## In a nutshell,

Compared to whatever Python support is available at the moment, this project reigns supreme.
