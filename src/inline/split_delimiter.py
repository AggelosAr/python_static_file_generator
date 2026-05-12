from nodes.text_node import TextType, TextNode
from itertools import repeat


# todo We Don't Care About Nested Inline Elements
def split_nodes_delimiter(old_nodes: list[TextNode], 
                          delimiter: str, 
                          text_type: TextType) -> list[TextNode]:
    
    results = []
    for node in old_nodes:
        results.extend(split_node_with_delimiter(old_node=node,
                                                 delimiter=delimiter,
                                                 text_type=text_type))
    return results

def split_node_with_delimiter(old_node: TextNode, 
                              delimiter: str, 
                              text_type: TextType) -> list[TextNode]:
    
    if old_node.text == '':
        return [old_node]
    
    if old_node.text_type != TextType.TEXT:
        return [old_node]

    if old_node.text.count(delimiter)%2 == 1:
        raise Exception('Invalid Markdown syntax.')

    new_nodes = []
    idx = 0
    current_split = []

    while idx < len(old_node.text):

        if old_node.text[idx] == delimiter[0]:

            new_node = TextNode(text=''.join(current_split), 
                                text_type=TextType.TEXT)
            new_nodes.append(new_node)
            current_split = []

            # this only works for delimiters of [**, *, _]e.tc.
            while old_node.text[idx] == delimiter[0]:
                idx += 1
            while old_node.text[idx] != delimiter[0]:
                current_split.append(old_node.text[idx])
                idx += 1
            while old_node.text[idx] == delimiter[0]:
                idx += 1

            new_node = TextNode(text=''.join(current_split), 
                                text_type=TextType.get_enum_type_from_symbol(symbol=delimiter))
            new_nodes.append(new_node)
            current_split = []
        
        current_split.append(old_node.text[idx])
        idx += 1

    if current_split:
        new_node = TextNode(text=''.join(current_split), 
                                text_type=TextType.TEXT)
        new_nodes.append(new_node)

    return new_nodes
