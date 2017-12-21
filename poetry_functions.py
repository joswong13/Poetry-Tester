"""
A poetry pattern:  tuple of (list of int, list of str)
  - first item is a list of the number of syllables required in each line
  - second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""

# ===================== Helper Functions =====================

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result

def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', 'Finally', "we're done."]
    
    >>> split_on_separators("Row, Row, Row your boat", ".!,")
    ['Row', 'Row', 'Row your boat']
    """
    
    result = [original]
    
    # Cycles through the set of separators individually    
    for separator in separators:
        split_words = []
        
    # #########################################################################
    # Cycle through the strings in the list of strings from result. Extends the 
    # list split_words with the strings split at separator. result is now 
    # the list of strings split with separator.
    # #########################################################################    
        
        for string in result:
            words = string.split(separator)
            for strings in words:
                if strings != '' and strings != ' ':
                    split_words.append(strings.strip())    
        result = split_words
    return result

def pattern_dict(pattern):
    ''' (list of int, list of str) -> dict
    Return a dictionary where keys are the poetry pattern and the value is the 
    index of occurrence.
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> poetry_dict = pattern_dict(pattern)
    >>> poetry_dict == {'B': [1], 'A': [0, 2]}
    True
    
    >>> pattern = ([5, 7, 5, 4, 3], ['A', 'B', 'A', 'C', 'A', 'C', 'A'])
    >>> poetry_dict = pattern_dict(pattern)
    >>> poetry_dict == {'B': [1], 'C': [3, 5], 'A': [0, 2, 4, 6]}
    True
    '''
    pattern_dict = {}
    
    # Looks at the second element in the pattern tuple
    lst = pattern[1]
    
    # #########################################################################
    # For the number of values in the second element of tuple, create dictionary
    # key and append the index (i) of occurrence. If value in dictionary, 
    # append the index (i) to the key.
    # #########################################################################
    for i in range(len(lst)):
        if lst[i] not in pattern_dict:
            pattern_dict[lst[i]] = [i]
        else:
            pattern_dict[lst[i]].append(i)
    return pattern_dict

def lst_of_lst_of_strings(rhyme_pattern):
    ''' (dict) -> list of list of str
    
    Return a list of list of string based on the sorted dictionary key.
    
    >>> rhyme_pattern = {'B': [1], 'A': [0, 2]}
    >>> lst_of_lst_of_strings(rhyme_pattern)
    [[0, 2], [1]]
    
    >>> rhyme_pattern = {'B': [1], 'A': [0, 2], 'C': []}
    >>> lst_of_lst_of_strings(rhyme_pattern)
    [[0, 2], [1]]
    '''
    # For the sorted keys in the dictionary, append the values to a new list 
    lst_of_values = []
    lst_return = []
    for keys in sorted(rhyme_pattern):
        lst_of_values.append(rhyme_pattern[keys])
    # If the value is not an empty list, append value to new list .    
    for lst_of_lsts in lst_of_values:
        if not len(lst_of_lsts) == 0:
            lst_return.append(lst_of_lsts)
    return lst_return
                

# ===================== Required Functions =====================

def count_lines(lst):
    r""" (list of str) -> int

    Precondition: each str in lst[:-1] ends in \n.

    Return the number of non-blank, non-empty strings in lst.

    >>> count_lines(['The first line leads off,\n', '\n', '  \n',
    ... 'With a gap before the next.\n', 'Then the poem ends.\n'])
    3
    >>> count_lines(['First line,\n', 'Second line,\n', '  \n',
    ... 'Third line after gap,\n', 'Fourth line,\n', 
    ... 'Fifth line,\n', 'Ending line.\n']) 
    6
    """
    # For each string in list, performs clean_up and if line is not empty string
    # will add 1 to num_lines.
    num_lines = 0
    for lines in lst:
        clean_lines = clean_up(lines)
        if clean_lines.strip() != '':            
            num_lines += 1
    return num_lines
    

def get_poem_lines(poem):
    r""" (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed 
    from the beginning and end of each line.

    >>> get_poem_lines('The first line leads off,\n\n\n'
    ... + 'With a gap before the next.\nThen the poem ends.\n')
    ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    
    >>> get_poem_lines('   First line,\n\n\nPoems are fun!\n\n \n'
    ... + 'Second line.\nThird line.\n') 
    ['First line,', 'Poems are fun!', 'Second line.', 'Third line.']
    """
    result = split_on_separators(poem, '\n')

    return result


def check_syllables(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    syllables for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of syllables, return the empty list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 5, 4], ['*', '*', '*'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_syllables(poem_lines, pattern, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> check_syllables(poem_lines, ([0], ['*']), word_to_phonemes)
    []
    
    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> check_syllables(poem_lines, ([5, 0, 4], ['*', '*', '*']), word_to_phonemes)
    ['Then the poem ends.']
    """
    rhy_position = 0
    poem = []
    # If the poem is only one line and the syllable pattern is 0, return empty list.
    if len(pattern[0]) == 1 and pattern[0][0] == 0:
        return poem
    # #########################################################################
    # For each strings in the poem, split the string into list of strings 
    # (splitting). For each word in splitting, perform clean_up and obtain
    # phonemes. For each phonemes, if the last character is digit, syllable
    # counter will plus one.
    # #########################################################################
    for strings in poem_lines:
        syllables = 0
        splitting = strings.split()
        for i in range(len(splitting)): 
            word = clean_up(splitting[i])
            phonemes = word_to_phonemes[word]
            for segments in phonemes:
                if segments[-1].isdigit() == True: 
                    syllables += 1
            
    # If the syllable pattern at position rhy_position is 0, rhy_pattern counter
    # will add one.
        if pattern[0][rhy_position] == 0:
            rhy_position += 1
    # If the syllable counter does not equal the syllable pattern at rhy_position
    # append the string.
        elif syllables != pattern[0][rhy_position]:
            poem.append(strings)
            rhy_position += 1 
    # If syllable counter equals the syllable pattern, rhy_position will add one.
        else:
            rhy_position += 1
    return poem    

def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) 
                                                        -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with 
    each other but don't. If all lines rhyme as they should, return the empty 
    list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['The first line leads off,', 'Then the poem ends.']]
    
    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem off.']
    >>> pattern = ([5, 7, 5], ['*', '*', '*'])
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    []
    """
    final_result = []
    
    # Create dictionary for poetry pattern
    rhyme_pattern = pattern_dict(pattern)
    
    # Cycle though each key in dictionary and create empty list for each key
    for keys in rhyme_pattern:
        rhyme = []
        list_of_strings = []
    # Cycle through each value in keys
        for position in rhyme_pattern[keys]:
    # #########################################################################
    # Split string and get last word from string and perform clean_up to 
    # reference the key in word_to_phonemes dictionary. Create variables to 
    # stop for loop.
    # #########################################################################
            string = poem_lines[position]
            stopper = 0
            rhyme_counter = 0
            splitting = string.split()               
            last_word = splitting[-1]
            word = clean_up(last_word)
            pronunciation = word_to_phonemes[word]
    # #########################################################################
    # Find the syllable in the list of pronunciation starting from the back. 
    # Append the syllable to the end of the list to a new list, rhyme.
    # #########################################################################
            for i in range(len(pronunciation)-1, -1, -1):
                if stopper < 1:
                    if pronunciation[i][-1].isdigit() == True:
                        rhyme.append(pronunciation[i:])
                        stopper += 1
    # #########################################################################
    # If rhyme only contains one list, will not compare phonemes. For rhymes 
    # more than one list, will compare the phonemes and count if the list 
    # are the same. If the rhymes are not the same, list_of_strings will
    # append the lines of the poem that don't rhyme and assign to rhyme_pattern
    # dictionary. If the rhymes are the same, then blank list will be assigned
    # to rhyme_pattern dictionary.
    # #########################################################################
        if len(rhyme) == 1 or keys == '*':
            list_of_strings = []
            rhyme_pattern[keys] = list_of_strings
        else:
            for i in range(len(rhyme)-1): 
                if not rhyme[i] == rhyme[i+1]:                    
                    rhyme_counter +=1
            if rhyme_counter > 0:
                for position in rhyme_pattern[keys]:
                    list_of_strings.append(poem_lines[position])
                rhyme_pattern[keys] = list_of_strings
            else:
                list_of_strings = []
                rhyme_pattern[keys] = list_of_strings 
    # #########################################################################
    # Sorts the rhyme_pattern dictionary bye key and appends the new values
    # to a new list. Creates list of list of strings.
    # #########################################################################
    final_result = lst_of_lst_of_strings(rhyme_pattern)
    return final_result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
