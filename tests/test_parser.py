import unittest
from src.parser import parse_data

class TestParser(unittest.TestCase):
    def test_parse_data(self):
        sample_text = """
        This is a sample text about pride and prejudice. 
        Elizabeth loves Darcy, but Darcy is proud and prejudiced.
        Love wins in the end.
        """
        result = parse_data(sample_text)

        expected = [
            'pride', 'prejudice', 'elizabeth', 'loves', 'darcy',
            'darcy', 'proud', 'prejudiced', 'love', 'wins'
        ]

        self.assertEqual(sorted(result), sorted(expected))

    def test_parse_data_empty(self):
        result = parse_data("12345 !@#$%")
        self.assertEqual(result, [])

    def test_parse_data_case_insensitive(self):
        result = parse_data("Love LOVE love")
        self.assertEqual(sorted(result), ['love', 'love', 'love'])

if __name__ == "__main__":
    unittest.main()