import re


def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"[!]{1,}[[]{1,}(image)[]]{1,}[(]{1,}(.*[^)])[)]{1,}", text)


def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"[[]{1,}(link)[]]{1,}[(]{1,}(.*[^)])[)]{1,}", text)
