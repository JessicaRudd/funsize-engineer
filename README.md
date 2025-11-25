# funsize-engineer

A personal calling card for Jessica Rudd, Staff Data Engineer at FanDuel.

## Quick Start

Run this single command in your terminal (requires Python installed):

```bash
python -m pip install funsize-engineer && python -m funsize_engineer
```

## Installation

### From PyPI (Production)

```bash
pip install funsize-engineer
```

### From TestPyPI (Testing)

If you want to test the latest development version from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ funsize-engineer
```

> **Note:** The `--extra-index-url` flag is required to ensure dependencies (like `rich`) are installed from the main PyPI, as they may not be available on TestPyPI.

## Usage

Run the command:

```bash
funsize-engineer
```

Or import it in Python:

```python
import funsize_engineer
funsize_engineer.card()
```

## "npx-style" Usage

To run the card without installing it globally (similar to `npx`), you can use `pipx`:

```bash
pipx run funsize-engineer
```
