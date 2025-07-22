import unittest
import requests_mock
from src.scraper import scrape_website

class TestScraper(unittest.TestCase):
    @requests_mock.mock()
    def test_scrape_website(self, m):
        m.get("https://example.com", text="# Example Domain\nThis domain is for use...")
        html = scrape_website("https://example.com")
        self.assertIn("Example Domain", html)