import unittest
import poetry_functions

class TestCountLines(unittest.TestCase):
    ''' Example unittest test method for count_lines'''
    
    def test_check_syllables_1(self):
        ''' Test check_syllables with all strings having correct number of 
        syllables.'''
        word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                            'GAP': ['G', 'AE1', 'P'],
                            'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'LEADS': ['L', 'IY1', 'D', 'Z'],
                            'WITH': ['W', 'IH1', 'DH'],
                            'LINE': ['L', 'AY1', 'N'],
                            'THEN': ['DH', 'EH1', 'N'],
                            'THE': ['DH', 'AH0'], 
                            'A': ['AH0'], 
                            'FIRST': ['F', 'ER1', 'S', 'T'], 
                            'ENDS': ['EH1', 'N', 'D', 'Z'],
                            'POEM': ['P', 'OW1', 'AH0', 'M'],
                            'OFF': ['AO1', 'F']}  
        poem_lines = ['The first line leads off,', 
                      'With a gap before the next.', 'Then the poem ends.']
        pattern = ([5, 7, 5], ['*', '*', '*'])
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)    
    
    def test_check_syllables_2(self):
        ''' Test check_syllables with no syllable requirement per line.''' 
        word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                            'GAP': ['G', 'AE1', 'P'],
                            'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'LEADS': ['L', 'IY1', 'D', 'Z'],
                            'WITH': ['W', 'IH1', 'DH'],
                            'LINE': ['L', 'AY1', 'N'],
                            'THEN': ['DH', 'EH1', 'N'],
                            'THE': ['DH', 'AH0'], 
                            'A': ['AH0'], 
                            'FIRST': ['F', 'ER1', 'S', 'T'], 
                            'ENDS': ['EH1', 'N', 'D', 'Z'],
                            'POEM': ['P', 'OW1', 'AH0', 'M'],
                            'OFF': ['AO1', 'F']}  
        pattern = ([0, 0, 0], ['*', '*', '*'])        
        poem_lines = ['First line,\n', 'Before line,\n', 'Ends line\n']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)
    
    def test_check_syllables_3(self):
        ''' Test check_syllables with one no syllable requirement and 
        two lines that have syllable requirements.''' 
        word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                            'GAP': ['G', 'AE1', 'P'],
                            'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'LEADS': ['L', 'IY1', 'D', 'Z'],
                            'WITH': ['W', 'IH1', 'DH'],
                            'LINE': ['L', 'AY1', 'N'],
                            'THEN': ['DH', 'EH1', 'N'],
                            'THE': ['DH', 'AH0'], 
                            'A': ['AH0'], 
                            'FIRST': ['F', 'ER1', 'S', 'T'], 
                            'ENDS': ['EH1', 'N', 'D', 'Z'],
                            'POEM': ['P', 'OW1', 'AH0', 'M'],
                            'OFF': ['AO1', 'F']}  
        pattern = ([2, 0, 2], ['*', '*', '*'])        
        poem_lines = ['First line,\n', 'Before line,\n', 'Ends line\n']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)
       
        
    
    def test_check_syllables_4(self):
        ''' Test check_syllables with one string that doesn't match the syllable
        pattern.'''
        word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                            'GAP': ['G', 'AE1', 'P'],
                            'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'LEADS': ['L', 'IY1', 'D', 'Z'],
                            'WITH': ['W', 'IH1', 'DH'],
                            'LINE': ['L', 'AY1', 'N'],
                            'THEN': ['DH', 'EH1', 'N'],
                            'THE': ['DH', 'AH0'], 
                            'A': ['AH0'], 
                            'FIRST': ['F', 'ER1', 'S', 'T'], 
                            'ENDS': ['EH1', 'N', 'D', 'Z'],
                            'POEM': ['P', 'OW1', 'AH0', 'M'],
                            'OFF': ['AO1', 'F']}  
        poem_lines = ['The first line leads off,', 
                      'With a gap before the next.', 'Then the poem ends.']
        pattern = ([5, 3, 5], ['*', '*', '*'])        
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = ['With a gap before the next.']
        self.assertEqual(actual, expected) 
        
    def test_check_syllables_5(self):
        ''' Test check_syllables with three string that doesn't match the syllable
        pattern.'''
        word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                            'GAP': ['G', 'AE1', 'P'],
                            'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'LEADS': ['L', 'IY1', 'D', 'Z'],
                            'WITH': ['W', 'IH1', 'DH'],
                            'LINE': ['L', 'AY1', 'N'],
                            'THEN': ['DH', 'EH1', 'N'],
                            'THE': ['DH', 'AH0'], 
                            'A': ['AH0'], 
                            'FIRST': ['F', 'ER1', 'S', 'T'], 
                            'ENDS': ['EH1', 'N', 'D', 'Z'],
                            'POEM': ['P', 'OW1', 'AH0', 'M'],
                            'OFF': ['AO1', 'F']}  
        poem_lines = ['The first line leads off,', 
                      'With a gap before the next.', 'Then the poem ends.']
        pattern = ([3, 3, 3], ['*', '*', '*'])        
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = ['The first line leads off,', 
                      'With a gap before the next.', 'Then the poem ends.']
        self.assertEqual(actual, expected)  
    
    def test_check_syllables_6(self):
        ''' Test check_syllables with five string that doesn't match the 
        syllable pattern.'''
        word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                            'GAP': ['G', 'AE1', 'P'],
                            'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'LEADS': ['L', 'IY1', 'D', 'Z'],
                            'WITH': ['W', 'IH1', 'DH'],
                            'LINE': ['L', 'AY1', 'N'],
                            'THEN': ['DH', 'EH1', 'N'],
                            'THE': ['DH', 'AH0'], 
                            'A': ['AH0'], 
                            'FIRST': ['F', 'ER1', 'S', 'T'], 
                            'ENDS': ['EH1', 'N', 'D', 'Z'],
                            'POEM': ['P', 'OW1', 'AH0', 'M'],
                            'OFF': ['AO1', 'F']}  
        poem_lines = ['The first line leads off,', 
                      'With a gap before the next.', 'Then the poem ends.',
                      'With a gap before the next.', 'Then the poem ends.']
        pattern = ([3, 3, 3, 3, 3], ['*', '*', '*'])        
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = ['The first line leads off,', 
                      'With a gap before the next.', 'Then the poem ends.',
                      'With a gap before the next.', 'Then the poem ends.']
        self.assertEqual(actual, expected)         
    

if __name__ == '__main__':
    unittest.main(exit=False)