import unittest
import poetry_functions

class TestCountLines(unittest.TestCase):
    ''' Example unittest test method for count_lines'''
    
    def test_count_lines_1(self):
        ''' Test count_lines with only new line characters only and no 
        strings in list.'''
        lst = ['\n', '  \n']
        actual = poetry_functions.count_lines(lst)
        expected = 0
        self.assertEqual(actual, expected)    
    
    def test_count_lines_2(self):
        ''' Test count_lines with three strings in list.'''        
        lst = ['First line,\n', 'Second line,\n', 'Last line\n']
        actual = poetry_functions.count_lines(lst)
        expected = 3
        self.assertEqual(actual, expected)
    
    def test_count_lines_3(self):
        ''' Test count_lines with five strings in list combined with strings
        only containing new line characters.'''  
        lst = ['The first line leads off,\n', '\n', '  \n', 
               'With a gap before the next.\n', 'Then the poem doesn\'t ends.\n'
               , 'The poem continues with the next line,\n', 'Then ends here.\n']
        actual = poetry_functions.count_lines(lst)
        expected = 5
        self.assertEqual(actual, expected)        

if __name__ == '__main__':
    unittest.main(exit=False)