```bash
mkdir hypermodern-python && cd hypermodern-python   #NOTE dash !!!
pyenv install --list        # show available versions
pyenv install 3.11.2
pyenv versions              # show installed versions
pyenv local 3.11.2          # creates .python-version file

poetry init --no-interaction # creates pyproject.toml

mkdir src
mkdir src/hypermodern_python && cd src/hypermodern_python #NOTE underscore !!!
touch __init__.py           # edit to contain __version__ = "0.1.0"
cd ../..

poetry config virtualenvs.in-project true # for vscode pylance support - didnt work ...
poetry install # creates venv, poetry.lock
poetry env list
poetry show -v
poetry run python
>>> import hypermodern_python
>>> hypermodern_python.__version__
>>> ctrl-D

poetry add click
poetry add requests
poetry install

poetry run hypermodern-python # from pyproject.toml [tool.poetry.scripts]


```