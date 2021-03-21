# numToEng
A toy package for converting numbers to written out English.


## Getting Started
In this directory:
```bash
pip install .
python3 numToEng/main.py 1234
```

## Constraints
- The number must be an integer (negative values are supported)
- The absolute value of the number must have a max value of 10^66-1.

## Running tests
In this directory:
```bash
pip install pytest
pytest
```

## Other notes
There may be ambiguity on how to properly write out certain number.  Sample examples and 
num2words were used as reference points.  I am willing to discuss some of these decisions further.