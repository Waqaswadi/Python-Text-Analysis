# 22096309 -  Student ID


import re
import numpy as np

# Solution for Question 3.a ;


def gettagssequence(tags_file):
    """
    Definition:
    Reads in a file containing tag sequences, removes the <SEP> special character,
    lowercases all tags, and returns the resulting list of tag sequences.

    Parameters:
    tags_file (str): Path to the file containing tag sequences.

    Returns:
    list[str]: List of tag sequences.
    
    """
    # Initialize empty list to store the tag sequences
    tag_sequences = []

    # Open the file and read its contents line by line
    with open(tags_file, "r") as f:
        for line in f:
            # Remove the <SEP> special character from the line
            # using a regular expression
            pattern = r'<SEP>'
            regex = re.compile(pattern)
            line = regex.sub('',line)
            # Lower case the line and remove the newline character
            line = line.lower().rstrip()
            # Append the modified line to the list of tag sequences
            tag_sequences.append(line)

    return tag_sequences

def getwordssequence(words_file):
    """
    Definition:
    Reads in a file containing word sequences, splits the sequences by the <SEP> special token,
    lowercases all words, and returns the resulting list of word sequences.

    Parameters:
    words_file (str): Path to the file containing word sequences.

    Returns:
    list[list[str]]: List of word sequences.
    
    """
    # Initialize empty list to store the word sequences
    word_sequences = []

    # Open the file and read its contents line by line
    with open(words_file, "r") as f:
        for line in f:
            # Split the line by the special token <SEP>
            # and lower case all the tags
            words = [word.lower()
                     for word in line.strip().split("<SEP>")]
            word_sequences.append(words)

    return word_sequences


tags_sequences = gettagssequence("alice_tags.txt") #filename for the data with tags
word_sequences = getwordssequence("alice_words.txt")#filename for the data with words




# Solution for Question 3.b ;


def find_positions(tags_sequences):
    """
    Definition:
    Finds the positions of sequences of tags that match the regular expression (?:J*N+)+ in a list of tag sequences.
    The regular expression matches any sequence of tags that consists of one or more repetitions of any number of "J" tags
    followed by one or more "N" tags. 

    Parameters:
    tags_sequences (list[str]): List of tag sequences.

    Returns:
    list[list[tuple[int, int]]]: List of lists of start and end positions of matches in the tag sequences.
    
    """
    # Compile the regular expression
    pattern = re.compile(r'(?:J*N+)+', re.IGNORECASE)

    # Initialize an empty list to store the positions
    positions = []

    # Iterate over the tags sequences
    for tags in tags_sequences:
        # Find all the matches of the regular expression in the tags sequence
        matches = pattern.finditer(tags)
        # Extract the start and end positions of each match
        pos = [(m.start(), m.end()) for m in matches]
        # Append the positions to the list
        positions.append(pos)

    return positions

positions = find_positions(tags_sequences)



# Solution for Question 3.c ;

def find_noun_phrase(input_word, matches_list, words_sequences):
    """
    Definition:
    Finds the noun phrases in a list of word sequences that contain a given input word. 
    Prints the sentence id and noun phrase for each match.

    Parameters:
    input_word (str): Word to search for in the noun phrases.
    matches_list (list[list[tuple[int, int]]]): List of lists of start and end positions of noun phrases in the word sequences.
    words_sequences (list[list[str]]): List of word sequences.
    
    """
    # Iterate over the matches list
    for i, matches in enumerate(matches_list):
        # Iterate over the noun phrases in the current sentence
        for start, end in matches:
            # Extract the noun phrase from the words sequence
            noun_phrase = " ".join(words_sequences[i][start:end])
            # Check if the input word is in the noun phrase
            if input_word in noun_phrase:
                # Print the sentence id and noun phrase
                print(f"{i+1}: {noun_phrase}")

