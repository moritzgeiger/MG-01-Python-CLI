"""Module handling the entry converter function."""

import sys
import typer

from roman_converter import utils

def main():
    """
    Identifies if input is Roman or Arabic and executes conversion functions for either of them.
    """

    # instanciating user input
    args = sys.argv

    if len(args) < 2:
        print("Please provide valid integer or string.")
        sys.exit()

    m = args[1]
    print('Running Roman numeral converter...')

    if m.isnumeric():
        print('Input was Arabic.')
        _ = utils.arabic_to_roman(int(m))
        sys.exit()

    if isinstance(m, str):
        print('Input was Roman.')
        _ = utils.roman_to_arabic(m)
        sys.exit()

if __name__ == "__main__":
    typer.run(main)
