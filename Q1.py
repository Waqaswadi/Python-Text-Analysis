# 22096309 -  Student ID

import numpy as np

# Solution for Question 1.a ;

def repetitionCounter(s, i):
    """
    Definition:
    Counts the number of consecutive repetitions of a character in a string, starting at a given index.

    Parameters:
    s (str): Input string.
    i (int): Starting index in the string.

    Returns:
    int: Number of consecutive repetitions of the character at index i.
    
    """
    # Initialize the counter to 1, since we are counting the character at index i
    count = 1
    # Iterate over the string starting at index i+1
    for j in range(i, len(s)-1):
        # Check if the current character is the same as the character at index i
        if(s[j].lower() == s[j+1].lower()):
            # If it is, increment the counter
            count += 1
        else:
            # Otherwise, return the count
            return count
    # Return the count if the loop completes without encountering a different character
    return count

def changeCase(letter, toUpper):
    """
    Definition:
    Changes the case of a letter to upper or lower case.

    Parameters:
    letter (str): Input letter.
    toUpper (bool): True if the letter should be converted to uppercase, False if it should be converted to lowercase.

    Returns:
    str: Input letter in the specified case.
    
    """
    # Check the value of toUpper
    if toUpper:
        # If it is True, return the letter in uppercase
        return letter.upper()
    # If toUpper is False, return the letter in lowercase
    return letter.lower()



def shift_vowels(s):
    """
    Definition:
    Shifts the vowels in a string to the next vowel in the alphabet.

    Parameters:
    s (str): Input string.

    Returns:
    str: String with shifted vowels.
    
    """
    # List of vowels in the alphabet
    vowels = ["a", "e", "i", "o", "u"]
    # Number of vowels in the alphabet
    SIZE = len(vowels)

    # Initialize an empty string to store the result
    newText = ""
    # Index of the current character in the input string
    j = 0

    # Loop through the input string
    while(j < len(s)):
        # Get the current character in lowercase
        letter = s[j].lower()
        # Check if the current character is uppercase
        isUpperCase = s[j].isupper()

        # Check if the current character is a vowel
        if letter not in vowels:
            # If it's not a vowel, add it to the result string as is
            newText += changeCase(letter, isUpperCase)
            # Move to the next character
            j += 1
        else:
            # If it's a vowel, get its index in the list of vowels
            i = vowels.index(letter)

            # Count the number of consecutive repetitions of the vowel
            steps = repetitionCounter(s, j)

            # Calculate the index of the new vowel in the list of vowels
            newVowelIndex = (steps+i+1) % SIZE
            # Get the new vowel from the list of vowels
            newVowel = vowels[newVowelIndex]

            # Loop through the consecutive repetitions of the vowel
            for step in range(0, steps):
                # Check if the current vowel is uppercase
                isUpperCase = s[j].isupper()
                # Add the new vowel to the result string in the same case as the original vowel
                newText += changeCase(newVowel, isUpperCase)
                # Move to the next vowel
                j += 1

    # Return the result string
    return newText



# Solution for Question 1.b ;

def sum_of_digits(s):
    """
    definition:
    Sums the digits in a string and returns the sum.

    Parameters:
    s (str): Input string.

    Returns:
    int: Sum of the digits in the input string.
    
    """
    # Initialize the sum to 0
    sum = 0
    # Check if the input string is empty
    if len(s) == 0:
        print("Empty string entered!")

    else:
        # Initialize an empty list to store the non-digit characters
        extractedString = []
        # Initialize an empty string to store the digits and their summation
        var = ""

        # Loop through the characters in the input string
        for i in s:
            # Check if the current character is a digit
            if i.isnumeric():
                # If the sum is not 0, add a "+" before the current digit
                if sum != 0:
                    var += "+"
                # Add the digit to the sum
                sum += int(i)
                # Add the digit to the string that stores the digits and their summation
                var += i
            else:
                # If the current character is not a digit, add it to the list of non-digit characters
                extractedString += i
        # If at least one digit was found, print the summation of the digits and the list of non-digit characters
        if sum != 0:
            print("The sum of digits operation performs ",var)
            print("The extracted non-digits are: ",extractedString)
        # If no digits were found, print an error message and the list of non-digit characters
        else:
            print("The sum of digits operation could not detect a digit!")
            print("The returned input letters are: ",extractedString)

        # Return the sum of the digits
        return sum

    










