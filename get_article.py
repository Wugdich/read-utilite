from typing import NamedTuple

import requests
from bs4 import BeautifulSoup

from exceptions import CantFindTitle, CantFindFirstParagraph, CantFindContents
import config


class Article(NamedTuple):
    title: str
    paragraph: str
    contents: list[str]
    url: str


def get_random_article() -> Article:
    """Returns random head of article from wikipedia.org."""
    url = config.RANDOM_ARTICLE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = _get_title(soup)
    first_paragraph = _get_first_paragraph(soup)
    contents = _get_contents(soup)
    url = response.url
    return Article(title, first_paragraph, contents, url)


def _get_title(soup: BeautifulSoup) -> str:
    try:
        title = soup.find(id='firstHeading').get_text()
    except AttributeError:
        raise CantFindTitle
    return title


def _get_first_paragraph(soup: BeautifulSoup) -> str:
    try:
        body = soup.find('div', class_='mw-parser-output')
        # Lambda function avoid empty <p> tag if there is. 
        first_paragraph = body.find('p',
                class_=lambda c: c != 'mw-empty-elt').get_text()
    except AttributeError:
        raise CantFindFirstParagraph
    return first_paragraph


def _get_contents(soup: BeautifulSoup) -> list[str]:
    try:
        all_headings = soup.find_all('h2')
    except AttributeError:
        raise CantFindContents
    contents = [heading.text for heading in all_headings]
    return contents


if __name__ == '__main__':
    print(get_random_article())

