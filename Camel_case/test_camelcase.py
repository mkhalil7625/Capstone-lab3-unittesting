import unittest
from unittest import TestCase
import Camel_case.camel as camel

class TestCamelCase(TestCase):
    def test_capitalize(self):

        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        capitalized = 'Abc'

        for word in input_words:
            self.assertEqual(capitalized, camel.capitalize(word))


    def test_lower(self):
        # this isn't really needed, since we can assume that Python's library functions work correctly :)
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        lower = 'abc'

        for word in input_words:
            self.assertEqual(lower, camel.lowercase(word))

    def test_camelCase_sentence(self):
        self.assertEqual('helloWorld',camel.camel_case('Hello World'))
        self.assertEqual('helloWorld', camel.camel_case('hELLO wORLD'))
        self.assertEqual('helloWorld', camel.camel_case('HELLO WORLD'))
        self.assertEqual('spacesBefore', camel.camel_case('  Spaces Before'))
        self.assertEqual('spacesAfter', camel.camel_case('Spaces after   '))
        self.assertEqual('👽🌎🌺', camel.camel_case('👽🌎🌺'))

    # def test_camelCase_empty_string(self):
    #     self.assertEqual(' ', camel.camel_case(' '))


if __name__ == '__main__':
    unittest.main()