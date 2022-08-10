import re

from get_article import Article


FormattedArticle = str


class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def format_article(article: Article) -> FormattedArticle:
    """Get Article object that contains raw text parts of wikipedia's
    article. Formats them and returns printable version.
    """
    formatted_title = _format_title(article.title)
    formatted_paragraph = _format_paragraph(article.paragraph)
    formatted_contents = _format_contents(article.contents)
    formatted_url = _format_url(article.url)
    formatted_article = '\n\n'.join((
            formatted_title,
            formatted_paragraph,
            formatted_contents,
            formatted_url))
    return formatted_article


def _format_title(title: str) -> str:
    formatted_title = Color.RED + Color.BOLD + title.strip() + Color.END
    return formatted_title


def _format_paragraph(paragraph: str) -> str:
    pattern = r'\[\d+\]'
    formatted_paragraph = re.sub(pattern, '', paragraph)
    return formatted_paragraph.strip()


def _format_contents(contents: list[str]) -> str:
    if len(contents) < 5:
        return 'No content'
    # Remove "Content" label.
    contents.pop(0)
    # Remove "Exteranl links" label.
    contents.pop(-1)
    pattern = r'\[\w+\]'
    head = Color.BOLD + 'Contents\n' + Color.END
    formatted_contents = head + '\n'.join(
            [re.sub(pattern, '', c) for c in contents])
    return formatted_contents



def _format_url(url: str) -> str:
    formatted_url = Color.UNDERLINE + url.strip() + Color.END
    return formatted_url


if __name__ == '__main__':
    pass

