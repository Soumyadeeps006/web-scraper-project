import unittest
from src.analyzer import analyze_data

class TestAnalyzer(unittest.TestCase):
    def test_analyze_data(self):
        sample_words = ['love'] * 5 + ['pride'] * 3 + ['darcy'] * 2 + ['elizabeth'] * 1
        result = analyze_data(sample_words)
        
        expected = [('love', 5), ('pride', 3), ('darcy', 2), ('elizabeth', 1)]
        self.assertEqual(list(result.items()), expected)

    def test_analyze_data_limit_to_10(self):
        words = ['a'] * 10 + ['b'] * 9 + ['c'] * 8
        for i in range(8):
            words += [f'word{i}'] * (7 - i)
        result = analyze_data(words)
        self.assertEqual(len(result), 10)

if __name__ == "__main__":
    unittest.main()