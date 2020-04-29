# Bash In Jupyter

Bash scripts are the best ! But sometimes it is quite hard to iterate on them as
fast as with python scripts. This small repository aims to demonstrate how we
can leverage existing tooling to develop bash scripts.

- [Bootstrap project](#bootstrap-project)
- [Install dependencies](#install-dependencies)
- [Jupyter Notebooks](#jupyter-notebooks)
- [Inline Code Cells](#inline-code-cells)
- [Documentation](#documentation)

## Bootstrap project

Skip this section, it is only useful to me to remember how to bootstrap this
repository

```bash
PIPENV_VENV_IN_PROJECT=enabled pipenv install --dev jupyter
```

## Install dependencies

```bash
PIPENV_VENV_IN_PROJECT=enabled pipenv sync --dev
```

## Jupyter Notebooks

<https://code.visualstudio.com/docs/python/jupyter-support>

See how we can leverage _notebooks_ to build an interactive bash script in
[bash.ipynb](bash.ipynb)

![bash.ipynb screenshot](https://user-images.githubusercontent.com/19719047/80550720-46ef4200-89c1-11ea-8a18-19c68d6aa8ef.png)

## Inline Code Cells

<https://code.visualstudio.com/docs/python/jupyter-support-py>

See how we can leverage _inline code cells_ to build an interactive bash script
in [bash.py](bash.py)

![bash.py screenshot](https://user-images.githubusercontent.com/19719047/80550657-0d1e3b80-89c1-11ea-91fc-75d23343d0e7.png)

## Documentation

- <https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe>
- <https://github.com/pypa/pipenv>
- <https://github.com/pypa/pipenv/issues/3123>
- <https://docs.pipenv.org/en/latest/basics/>
- <https://stackoverflow.com/questions/52540121/make-pipenv-create-the-virtualenv-in-the-same-folder>
- <https://code.visualstudio.com/docs/python/jupyter-support>
