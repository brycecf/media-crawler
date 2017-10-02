from bs4 import BeautifulSoup
from unicodedata import normalize

def parse_npr_references(response):
    """Given a typical article on NPR, parse any anchor tags to retrieve their
    links, text, and (if the anchor tag is in a paragraph tag) the surrounding
    content.

    Args:
        response: a scrapy response object

    Returns:
        list(dict) of references and their respective contexts
    """
    # Create a list to store the references
    references = []

    # Parse out all the paragraph (i.e. <p>) tags in the article body
    
