import re
from typing import NamedTuple


class MarkdownURI(NamedTuple):
    text: str
    url: str


def extract_markdown_images(text: str) -> list[MarkdownURI]:
    return [MarkdownURI(*el) for el in re.findall(r'!\[([^]]*)\]\(([^)]*)\)', text)]


def extract_markdown_links(text: str) -> list[MarkdownURI]:
    return [MarkdownURI(*el) for el in re.findall(r'\[([^]]*)\]\(([^)]*)\)', text)]
