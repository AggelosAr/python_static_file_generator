from enum import Enum

class Bender(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEX = "code_text"
    LINK = "link"
    IMAGE = "image" 

    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: 'Bender'):
        return all(
            self.text == other.text,
            self.text_type == other.text_type,
            self.url == other.url,
        )
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
