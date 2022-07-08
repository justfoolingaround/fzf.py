from setuptools import find_packages, setup

from fzf import __version__

setup(
    name="fzf.py",
    version=__version__,
    author="kr@justfoolingaround",
    author_email="kr.justfoolingaround@gmail.com",
    description="Fzf.py - A Pythonic Fzf Wrapper",
    packages=find_packages(),
    url="https://github.com/justfoolingaround/fzf.py",
)
