from enum import Enum
from functools import reduce
from nodes.html_node import HTMLNode
from inline.splits import text_to_textnodes

Block = str

MAX_HEADING_LEVEL = 6
HEADING_CHAR = '#'
CODE_S = '```'
UNORDERED_S = '- '
SINGLE_O_L = '1. '


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

    @classmethod
    def block_to_block_type(cls, markdown_block: str) -> 'BlockType':
        # TODO(***) add function to sanitize new lines and spaces 
        # TODO maybe r/l crop whitespaces?
        # remove leading new lines
        markdown_block = markdown_block.lstrip('\n')

        lines = markdown_block.split('\n')
        # remove traling empty
        if lines[-1] == '':
            lines.pop()

        line = lines[0]
        
        match len(lines):
            
            case 0:
                return BlockType.PARAGRAPH
            case 1:
                first_character = line[0]
                match first_character == '>':
                    # check quote
                    case True:
                        return BlockType.QUOTE
                    # check heading and check ordered_list or unordered_list of single element
                    case False:
                        match first_character == HEADING_CHAR:
                            case True:
                                match line[:MAX_HEADING_LEVEL-1].count(HEADING_CHAR) < MAX_HEADING_LEVEL:
                                    case True:
                                        match MAX_HEADING_LEVEL < len(line):
                                            case True:
                                                next_char = line[MAX_HEADING_LEVEL]
                                                match next_char == HEADING_CHAR:
                                                    case True:
                                                        return BlockType.PARAGRAPH
                                                    case _:
                                                        return BlockType.HEADING
                                            case False:
                                                return BlockType.PARAGRAPH
                                    case False:
                                        return BlockType.PARAGRAPH
                            case False:
                                # check ordered_list
                                # check unordered_list
                                match line[:len(UNORDERED_S)] == UNORDERED_S:
                                    case True:
                                        return BlockType.UNORDERED_LIST
                                    case False:
                                        match line[:len(SINGLE_O_L)] == SINGLE_O_L:
                                            case True:
                                                return BlockType.ORDERED_LIST
                                            case _:
                                                return BlockType.PARAGRAPH
            case _:
                # check code
                match CODE_S == line and lines[-1][-len(CODE_S):] == CODE_S:
                    case True:
                        return BlockType.CODE
                    case _:
                        # check unordered_list
                        # check ordered_list
                        # check paragraph
                        three_first_chars = [l[:len(SINGLE_O_L)] for l in lines]
                        two_first_chars = [l[:len(UNORDERED_S)] for l in lines]
                        match two_first_chars[0] == UNORDERED_S and reduce(lambda x, y: x==y, two_first_chars) == True:
                            case True:
                                return BlockType.UNORDERED_LIST
                            case _:
                                # check ordered_list
                                # check paragraph
                                match three_first_chars == [f'{i}. ' for i in range(1, len(lines)+1)]:
                                    case True:
                                        return BlockType.ORDERED_LIST
                                    case _:
                                        return BlockType.PARAGRAPH
                

def markdown_to_blocks(markdown: str) -> list[Block]:
    return list(filter(lambda l: l != '', map(lambda l: l.lstrip('\n').strip(), markdown.split('\n\n'))))


def markdown_to_html_node(markdown: str) -> HTMLNode:
    
    root = HTMLNode(tag='div', children=[])

    for block in markdown_to_blocks(markdown=markdown):

        # TODO this var is useless ?!
        block_root = HTMLNode(tag='div', children=[])
        # TODO(***) add function to sanitize new lines and spaces 
        lines = block .split('\n')
        match BlockType.block_to_block_type(markdown_block=block):
            case BlockType.PARAGRAPH:
                for line in lines:
                    block_root.children.extend(text_to_textnodes(text=line))
            case BlockType.HEADING:
                # This should assert len of lines is 1.
                # I assume there is no point of more lines in this context.
                for line in lines:
                    block_root.children.extend(text_to_textnodes(text=line))
            case BlockType.CODE:
                block_root.children.extend()
            case BlockType.QUOTE:
                # This should assert len of lines is 1.
                # I assume there is no point of more lines in this context.
                for line in lines:
                    block_root.children.extend(text_to_textnodes(text=line))
            case BlockType.UNORDERED_LIST:
                block_root.children.extend()
            case BlockType.ORDERED_LIST:
                block_root.children.extend()

        root.children.extend(block_root.children)

    return root
