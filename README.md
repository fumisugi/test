# Word Frequency Counter

This project provides a simple word frequency counter that can be used as a module or via the command line.

## Project Structure
- `test/`: Python package containing the implementation.
  - `__init__.py`: Package initializer exporting helper functions.
  - `__main__.py`: Entry point enabling `python -m test ...` execution.
  - `count.py`: Core logic for normalizing text, tokenizing, and counting word frequency.
- `tests/`: Pytest-based unit tests.
- `requirements.txt`: Python dependencies for development and testing.

## Installation
Install dependencies in a virtual environment:

```bash
pip install -r requirements.txt
```

## Usage
You can run the word counter against a text file or a raw string.

### Analyze a file
```bash
python -m test count --file sample.txt
```

### Analyze inline text
```bash
python -m test count --text "Hello, world! Hello?"
```

### Specify number of results
```bash
python -m test count --text "a b c a b c d" --top 2
```

## Testing
Run the unit tests with pytest:

```bash
pytest
```

## Sample Output
Using the inline text example:
```
hello: 2
world: 1
```
