import sys

# pytest, hypothesis

ROMAN_MAPPING = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

ARABIC_MAPPING = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

def roman_to_arabic(roman: str):
    """Converts any Roman number to a numeric value

    Args:
        roman (str): The input Roman number
    """
    prev_result = 0
    result = 0
    reps = 0

    # evaluating Roman number
    if all([i in ROMAN_MAPPING for i in roman]):
        for r in roman[::-1]: 
            current_result = ROMAN_MAPPING.get(r)
            reps = reps + 1 if current_result == prev_result else 0
            if reps > 3:
                print(f"Invalid Roman number. Your input: {roman}")
                sys.exit()

            if current_result >= prev_result:
                result += current_result
            
            else:
                result -= current_result

            prev_result = current_result
        
        print(result)
    
    else:
        print(f"Invalid Roman number: {roman}")
        sys.exit()
    return result
    


def arabic_to_roman(arabic: int):
    """Converts any Roman number to a numeric value

    Args:
        arabic (str): The input Arabic number
    """
    if not all([arabic > 0,  arabic < 3999]):
        print(f"Input should be between zero and 3999. Your input: {arabic}")
        sys.exit()

    result = ''
    for value, numeral in ARABIC_MAPPING.items():
        while arabic >= value:
            result += numeral
            arabic -= value


    print(result)
    return result

