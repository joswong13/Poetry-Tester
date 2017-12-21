"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""


def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """
    # This part skips the header
    reading = pronunciation_file.readline()
    while ';;;' in reading:
        reading = pronunciation_file.readline()
        
    # Once the header is skipped, create dictionary by splitting the word
    # and the pronunciation by the space between them.
    pronunciation_dict = {}
    while reading != '':
        space = reading.find('  ')        
        word = reading[:space]
        pronunciation = reading[space + 2:].rstrip()
        lst_pronunciation = pronunciation.split()
        pronunciation_dict[word] = (lst_pronunciation)        
        reading = pronunciation_file.readline()
    return pronunciation_dict    

def read_poetry_form_description(poetry_forms_file):
    """ (file open for reading) -> poetry pattern

    Precondition: we have just read a poetry form name from poetry_forms_file.

    Return the next poetry pattern from poetry_forms_file.
    """
    reading = poetry_forms_file.readline()
 
    rhymes_per_line = []
    syllables_per_line = []
    poetry_forms = (syllables_per_line, rhymes_per_line)
    
    # #########################################################################
    # While reading doesn't equal new line character and if reading doesn't 
    # equal empty string, will split the syllables and rhyme pattern and
    # append each to a list. Returns tuple of two lists.# #########################################################################

    while reading != '\n':

        if reading != '':
            space = reading.find(' ')         
            syllables = int(reading[:space])
            rhyme = reading[space + 1:].rstrip()
            syllables_per_line.append(syllables)            
            rhymes_per_line.append(rhyme)
            reading = poetry_forms_file.readline() 
        else:
            return poetry_forms
    return poetry_forms    

def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """
    # #########################################################################
    # Reads first line and strips the right side if reading doesn't equal 
    # empty string. Adds the words and the tuple from read_poetry_description
    # to new dictionary.
    # #########################################################################
    
    reading = poetry_forms_file.readline()
    dictionary_of_poetry = {}
    while reading != '':
        poetry_name = reading.rstrip()
        poetry_forms = read_poetry_form_description(poetry_forms_file)
        dictionary_of_poetry[poetry_name] = (poetry_forms)
        reading = poetry_forms_file.readline()
    return dictionary_of_poetry       