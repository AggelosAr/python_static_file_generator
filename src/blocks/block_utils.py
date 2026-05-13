from enum import Enum
from functools import reduce
from nodes.html_node import HTMLNode
from inline.splits import text_to_textnodes
from nodes.text_node import TextNode
from nodes.parent_node import ParentNode
from nodes.leaf_node import LeafNode


class MarkDownBlock(str):

    def __new__(cls, value: str): 
        return super().__new__(cls, cls.sanitize(value))

    def get_lines(self) -> list[str]:
        return self.split('\n')
    
    def markdown_to_blocks(self) -> list['MarkDownBlock']:
        return list(map(MarkDownBlock, filter(lambda l: l != '', self.split('\n\n'))))
    
    @staticmethod
    def sanitize(value: str) -> str:
        value = value.lstrip('\n')

        lines = value.split('\n')
        # remove leading empty
        if lines[0] == '':
            lines = lines[1:]
        # remove traling empty
        if lines and lines[-1] == '':
            lines.pop()

        return '\n'.join(lines)


_MAX_HEADING_LEVEL = 6
_HEADING_CHAR = '#'
_CODE_S = '```'
_UNORDERED_S = '- '
_SINGLE_O_L = '1. '

class BlockType(Enum):

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

    @classmethod
    def block_to_block_type(cls, markdown_block: MarkDownBlock) -> 'BlockType':
        
        lines = markdown_block.get_lines()
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
                        match first_character == _HEADING_CHAR:
                            case True:
                                match line[:_MAX_HEADING_LEVEL-1].count(_HEADING_CHAR) < _MAX_HEADING_LEVEL:
                                    case True:
                                        match _MAX_HEADING_LEVEL < len(line):
                                            case True:
                                                next_char = line[_MAX_HEADING_LEVEL]
                                                match next_char == _HEADING_CHAR:
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
                                match line[:len(_UNORDERED_S)] == _UNORDERED_S:
                                    case True:
                                        return BlockType.UNORDERED_LIST
                                    case False:
                                        match line[:len(_SINGLE_O_L)] == _SINGLE_O_L:
                                            case True:
                                                return BlockType.ORDERED_LIST
                                            case _:
                                                return BlockType.PARAGRAPH
            case _:
                # check code
                match _CODE_S == line and lines[-1][-len(_CODE_S):] == _CODE_S:
                    case True:
                        return BlockType.CODE
                    case _:
                        # check unordered_list
                        # check ordered_list
                        # check paragraph
                        thre_frst_chrs = [l[:len(_SINGLE_O_L)] for l in lines]
                        two_frst_chrs = [l[:len(_UNORDERED_S)] for l in lines]
                        match two_frst_chrs[0] == _UNORDERED_S and reduce(lambda x, y: x==y, two_frst_chrs) == True:
                            case True:
                                return BlockType.UNORDERED_LIST
                            case _:
                                # check ordered_list
                                # check paragraph
                                match thre_frst_chrs == [f'{i}. ' for i in range(1, len(lines)+1)]:
                                    case True:
                                        return BlockType.ORDERED_LIST
                                    case _:
                                        return BlockType.PARAGRAPH



# Todo add test for this
def single_line_text_to_html_nodes(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text=text)
    html_nodes = [text_node.text_node_to_html_node() for text_node in text_nodes]
    return html_nodes
    

def markdown_to_html_node(markdown: str) -> HTMLNode:
    
    root = ParentNode(tag='div', children=[])

    for block in MarkDownBlock(value=markdown).markdown_to_blocks():

        lines = block.get_lines()

        block_node = ParentNode(tag=None, children=[])

        match BlockType.block_to_block_type(markdown_block=block):

            case BlockType.PARAGRAPH:
                
                block_node.tag = 'p'

                for line in lines:
                    nodes = single_line_text_to_html_nodes(text=line)
                    block_node.add_children(nodes)
                    # seperate each line by a space (except the last one)
                    block_node.add_children(LeafNode(value=' ', tag=None))
                block_node.children.pop()
                
            case BlockType.HEADING:
                # This should assert len of lines is 1.
                # I assume there is no point of more lines in this context.
                block_node.tag = 'p'

            case BlockType.CODE:
                block_node.tag = 'p'

            case BlockType.QUOTE:
                block_node.tag = 'p'

            case BlockType.UNORDERED_LIST:
                block_node.tag = 'p'

            case BlockType.ORDERED_LIST:
                block_node.tag = 'p'

        root.add_children(_from=block_node)

    return root
