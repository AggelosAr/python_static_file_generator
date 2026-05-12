from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEX = "code_text"
    LINK = "link"
    IMAGE = "image" 


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        # assert text_type in TextType # Todo finish the validation and add test for it 
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: 'TextNode'):
        return all(
            [
                self.text == other.text,
                self.text_type == other.text_type,
                self.url == other.url
            ]
        )
    
    def __str__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
    def __repr__(self):
        return self.__str__()
