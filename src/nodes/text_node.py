from enum import Enum
from typing import Literal

from .html_node import HTMLNode


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
    
    @staticmethod
    def text_node_to_html_node(text_node: 'TextNode') -> HTMLNode:
        match text_node.text_type:
            case TextType.TEXT:
                return HTMLNode(value=text_node.text)
            case TextType.BOLD_TEXT:
                return HTMLNode(tag='b', value=text_node.text)
            case TextType.ITALIC_TEXT:
                return HTMLNode(tag='i', value=text_node.text)
            case TextType.CODE_TEXT:
                return HTMLNode(tag='code', value=text_node.text)
            case TextType.LINK:
                return HTMLNode(tag='a', 
                                value=text_node.text, 
                                props={'href': text_node.url})
            case TextType.IMAGE:
                return HTMLNode(tag='img', 
                                props={'src': text_node.url,
                                       'alt': text_node.text})
            case _:
                # TODO maybe add validation elsewhere for the text_type
                raise Exception(f'Invalid text type: {text_node.text_type}')

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
