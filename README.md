# Converter CLI

This app converts a user input from Roman to Arabic numbers and vice versa.

## Setup

```
python3 -m venv env
source env/bin/activate
pip3 install .
```

## Packaging 

Package instructions can be found in the pyproject.toml file.

## Usage

To convert Roman numbers into Arabic numbers, type for example: 

```
converter XV
```

Output:

```
Running Roman numeral converter...
Input was Roman.
15
```

To convert an Arabic number into a Roman number, type for example: 

```
converter 15
```

Output:

```
Running Roman numeral converter...
Input was Arabic.
XV
```

