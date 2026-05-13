from nodes.text_node import TextType, TextNode
from .link_extractor import extract_markdown_images, extract_markdown_links


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

            #TODO (FIX) this only works for delimiters of [**, *, _]e.tc.
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


# TODO remove code duplication. Only differences are [extract_markdown_images, formatting]
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(text=node.text)
        if not images:
            new_nodes.append(node)
            continue

        image_selector = 0

        while node.text and image_selector < len(images):
            
            image = images[image_selector]

            formated_image = f'![{image[0]}]({image[1]})'
            parts = node.text.partition(formated_image)

            if parts[0]:
                new_nodes.append(TextNode(text=parts[0], 
                                          text_type=TextType.TEXT))
            new_nodes.append(TextNode(text=image.text, 
                                      url=image.url,
                                      text_type=TextType.IMAGE))

            node.text = parts[2]
            image_selector += 1

        if node.text:
            new_nodes.append(TextNode(text=node.text, 
                                      text_type=TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(text=node.text)
        if not links:
            new_nodes.append(node)
            continue

        link_selector = 0

        while node.text and link_selector < len(links):
            
            link = links[link_selector]
            formated_link = f'[{link[0]}]({link[1]})'
            parts = node.text.partition(formated_link)

            if parts[0]:
                new_nodes.append(TextNode(text=parts[0], 
                                          text_type=TextType.TEXT))
            new_nodes.append(TextNode(text=link.text, 
                                      url=link.url, 
                                      text_type=TextType.LINK))

            node.text = parts[2]
            link_selector += 1

        if node.text:
            new_nodes.append(TextNode(text=node.text, 
                                      text_type=TextType.TEXT))
      
    return new_nodes
