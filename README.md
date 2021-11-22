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

### Troubleshooting

#### Fix Pytube
Change in pytube/parser.py

```
    func_regex = re.compile(r"function\([^)]+\)")
```

to

```
    func_regex = re.compile(r"function\([^)]?\)")
```
