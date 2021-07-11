# KarginProject

This project helps to find phrases in `kargin`.

## Environment

Run the following command to create a virtual environment

```
python -m venv .venv  # Create the environment
source .venv/bin/actvate  # Activate the environment
pip install -r requirements.txt  # Install requirements
```

Activate the virtual environment each time you open a new terminal.

## Testing

Run the following command to run tests

```
PYTHONPATH=src python -m pytest tests
```

## Usage

```
from search_engine.typo_fixer_engine import TypoFixerEngine
from yaml_parser.reader import read_yaml

engine = TypoFixerEngine()

for path in yaml_paths:
    engine.feed_data(read_yaml(path))

engine.search(phrase)
```

## Running the flask app

```
export FLASK_APP=flask/flask_app.py
flask run
```

Then enter "http://localhost:5000/TBpD6dgtVXM" from browser.

On each pause the "end time" field will be updated automatically. On each submit the part of the YAML will be generated and appended to editable text field. Hope this eases your work :)
