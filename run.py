import logging
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.scraper import scrape_website
from src.parser import parse_data
from src.analyzer import analyze_data, generate_report
from src.utils import setup_logging
from config.settings import TARGET_URL

setup_logging()

def main():
    logging.info(f"Scraping {TARGET_URL}")
    html = scrape_website(TARGET_URL)
    
    if not html:
        logging.error("Failed to retrieve HTML")
        return
    
    logging.info("Parsing data")
    data = parse_data(html)
    
    logging.info("Analyzing data")
    word_counts = analyze_data(data)
    
    logging.info("Generating report")
    generate_report(word_counts)

if __name__ == "__main__":
    main()