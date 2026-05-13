

def markdown_to_blocks(markdown: str) -> list[str]:
    return list(filter(lambda l: l != '', map(lambda l: l.lstrip('\n').strip(), markdown.split('\n\n'))))
