from bs4 import BeautifulSoup
from unicodedata import normalize

def parse_npr_references(response):
    """Given a typical article on Fox Newws, parse any anchor tags to retrieve
    their links, text, and (if the anchor tag is in a paragraph tag) the
    surrounding content.

    Args:
        response: a scrapy response object

    Returns:
        list(dict) of references and their respective contexts
    """
    # Create a list to store the references
    references = []

    # Parse out all the anchor tags contained (i.e. <a>) tags in the article
    # body
    article_anchor_tags = response.xpath('//div[@class="article-body"]/p/a')

    # Retrieve the hrefs from the anchor tags
    anchor_hrefs = article_anchor_tags.xpath('@href').extract()

    # Retrieve the text from the anchor tags
    anchor_texts = article_anchor_tags.xpath('text()').extract()

    # Retrieve the context from the anchor tags
    #anchor_contexts = 
