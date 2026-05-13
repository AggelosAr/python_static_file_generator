from enum import Enum
from typing import Literal

from .leaf_node import LeafNode


# TODO maybe add a connector here for the text_node_to_html_node match logic and text_type?
class TextType(Enum):
    TEXT = 'text'
    BOLD_TEXT = 'bold_text'
    ITALIC_TEXT = 'italic_text'
    CODE_TEXT = 'code_text'
    LINK = 'link'
    IMAGE = 'image'

    # TODO add test
    @classmethod
    def get_enum_type_from_symbol(cls, 
                                  symbol: Literal['**', '_', '`', '![', '[']
                                  ) -> 'TextType':
        match symbol:
            case '**':
                return TextType.BOLD_TEXT
            case '_':
                return TextType.ITALIC_TEXT
            case '`':
                return TextType.CODE_TEXT
            case '[':
                return TextType.LINK
            case '![':
                return TextType.IMAGE
            case _:
                return TextType.TEXT


class TextNode:

    def __init__(self, 
                 text: str, 
                 text_type: TextType, 
                 url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def text_node_to_html_node(self) -> LeafNode:
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(value=self.text)
            case TextType.BOLD_TEXT:
                return LeafNode(tag='b', value=self.text)
            case TextType.ITALIC_TEXT:
                return LeafNode(tag='i', value=self.text)
            case TextType.CODE_TEXT:
                return LeafNode(tag='code', value=self.text)
            case TextType.LINK:
                return LeafNode(tag='a', 
                                value=self.text, 
                                props={'href': self.url})
            case TextType.IMAGE:
                return LeafNode(tag='img', 
                                props={'src': self.url,
                                       'alt': self.text})

    def __eq__(self, other: 'TextNode') -> bool:
        return all(
            [
                self.text == other.text,
                self.text_type == other.text_type,
                self.url == other.url
            ]
        )

    def __str__(self) -> str:
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
    
    def __repr__(self) -> str:
        return self.__str__()
