import unittest

from nodes.text_node import TextType, TextNode
from inline.splits import split_nodes_delimiter, split_node_with_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes


# TODO add tests for LINK and IMAGE TextTypes
class TestTextNode(unittest.TestCase):

    def test_split_node_with_delimiter(self):
        node = TextNode(text='This is text with a `code block` word', text_type=TextType.TEXT)
        new_nodes = split_node_with_delimiter(old_node=node, delimiter='`', text_type=TextType.CODE_TEXT)

        expected = [
            TextNode(text='This is text with a ', text_type=TextType.TEXT),
            TextNode(text='code block', text_type=TextType.CODE_TEXT),
            TextNode(text=' word', text_type=TextType.TEXT)
        ]
        self.assertEqual(expected, new_nodes)

    def test_split_node_with_bold_delimiter(self):
        node = TextNode(text='This has **bold text** inside', text_type=TextType.TEXT)
        new_nodes = split_node_with_delimiter(old_node=node, 
                                              delimiter='**', 
                                              text_type=TextType.BOLD_TEXT)

        expected = [
            TextNode(text='This has ', text_type=TextType.TEXT),
            TextNode(text='bold text', text_type=TextType.BOLD_TEXT),
            TextNode(text=' inside', text_type=TextType.TEXT)
        ]

        self.assertEqual(expected, new_nodes)

    def test_split_node_with_italic_delimiter(self):
        node = TextNode(text='This has _italic text_ inside', text_type=TextType.TEXT)
        new_nodes = split_node_with_delimiter(old_node=node, 
                                              delimiter='_',
                                                text_type=TextType.ITALIC_TEXT)

        expected = [
            TextNode(text='This has ', text_type=TextType.TEXT),
            TextNode(text='italic text', text_type=TextType.ITALIC_TEXT),
            TextNode(text=' inside', text_type=TextType.TEXT)
        ]
        self.assertEqual(expected, new_nodes)

    def test_split_node_multiple_code_blocks(self):
        node = TextNode('Use `code1` and `code2` here', TextType.TEXT)
        new_nodes = split_node_with_delimiter(old_node=node, 
                                              delimiter='`', 
                                              text_type=TextType.CODE_TEXT)

        expected = [
            TextNode(text='Use ', text_type=TextType.TEXT),
            TextNode(text='code1', text_type=TextType.CODE_TEXT),
            TextNode(text=' and ', text_type=TextType.TEXT),
            TextNode(text='code2', text_type=TextType.CODE_TEXT),
            TextNode(text=' here', text_type=TextType.TEXT)
        ]
        self.assertEqual(expected, new_nodes)

    def test_split_node_without_delimiter(self):
        node = TextNode(text='Plain text only', text_type=TextType.TEXT)
       
        new_nodes = split_node_with_delimiter(old_node=node, 
                                              delimiter='`', 
                                              text_type=TextType.CODE_TEXT)
        
        self.assertEqual([TextNode(text='Plain text only', text_type=TextType.TEXT)], new_nodes)

    def test_split_node_empty_string(self):
        node = TextNode(text='', text_type=TextType.TEXT)
        
        new_nodes = split_node_with_delimiter(old_node=node, 
                                              delimiter='`', 
                                              text_type=TextType.CODE_TEXT)
        
        self.assertEqual([TextNode(text='', text_type=TextType.TEXT)], new_nodes)

    def test_split_node_unmatched_delimiter(self):
        node = TextNode(text='This has a `broken code block', text_type=TextType.TEXT)

        with self.assertRaises(Exception) as context:
            _ = split_node_with_delimiter(old_node=node, 
                                          delimiter='`', 
                                          text_type=TextType.CODE_TEXT)

        self.assertEqual('Invalid Markdown syntax.', str(context.exception))

    def test_split_nodes_delimiter_list_with_one_element(self):
        node = TextNode(text='This is text with a `code block` word', text_type=TextType.TEXT)
        new_nodes = split_nodes_delimiter(old_nodes=[node], 
                                          delimiter='`', 
                                          text_type=TextType.CODE_TEXT)

        expected = [
            TextNode(text='This is text with a ', text_type=TextType.TEXT),
            TextNode(text='code block', text_type=TextType.CODE_TEXT),
            TextNode(text=' word', text_type=TextType.TEXT)
        ]
        self.assertEqual(expected, new_nodes)
    
    def test_split_nodes_delimiter_list_with_double_element(self):
        node = TextNode(text='This is text with a `code block` word `code block`', text_type=TextType.TEXT)
        new_nodes = split_nodes_delimiter(old_nodes=[node], 
                                          delimiter='`', 
                                          text_type=TextType.CODE_TEXT)

        expected = [
            TextNode(text='This is text with a ', text_type=TextType.TEXT),
            TextNode(text='code block', text_type=TextType.CODE_TEXT),
            TextNode(text=' word ', text_type=TextType.TEXT),
            TextNode(text='code block', text_type=TextType.CODE_TEXT)
        ]
        self.assertEqual(expected, new_nodes)

    def test_split_nodes_delimiter_list_with_two_elements(self):
        node = TextNode(text='This is text with a `code block` word', text_type=TextType.TEXT)
        node_2 = TextNode(text='This has **bold text** inside', text_type=TextType.TEXT)
        new_nodes = split_nodes_delimiter(old_nodes=[node, node_2], 
                                          delimiter='`', 
                                          text_type=TextType.CODE_TEXT)

        expected = [
            TextNode(text='This is text with a ', text_type=TextType.TEXT),
            TextNode(text='code block', text_type=TextType.CODE_TEXT),
            TextNode(text=' word', text_type=TextType.TEXT),
            TextNode(text='This has **bold text** inside', text_type=TextType.TEXT)
        ]

        self.assertEqual(expected, new_nodes)

    def test_split_nodes_image(self):
        node = TextNode(text='This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)',
                        text_type=TextType.TEXT)
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode(text='This is text with an ', text_type=TextType.TEXT),
                TextNode(text='image', text_type=TextType.IMAGE, url='https://i.imgur.com/zjjcJKZ.png'),
                TextNode(text=' and another ', text_type=TextType.TEXT),
                TextNode(text='second image', text_type=TextType.IMAGE, url='https://i.imgur.com/3elNhQu.png'),
            ],
            new_nodes
        )
    
    def test_split_image(self):
        node = TextNode(text='This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)',
                        text_type=TextType.TEXT)
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode(text='This is text with an ', text_type=TextType.TEXT),
                TextNode(text='image', text_type=TextType.IMAGE, url='https://i.imgur.com/zjjcJKZ.png'),
            ],
            new_nodes
        )

    def test_split_image_single(self):
        node = TextNode(text='![image](https://www.example.COM/IMAGE.PNG)',
                        text_type=TextType.TEXT)
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode(text='image', text_type=TextType.IMAGE, url='https://www.example.COM/IMAGE.PNG'),
            ],
            new_nodes
        )
    
    def test_split_links(self):
        node = TextNode(
            text='This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows',
            text_type=TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode(text='This is text with a ', text_type=TextType.TEXT),
                TextNode(text='link', text_type=TextType.LINK, url='https://boot.dev'),
                TextNode(text=' and ', text_type=TextType.TEXT),
                TextNode(text='another link', text_type=TextType.LINK, url='https://wikipedia.org'),
                TextNode(text=' with text that follows', text_type=TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_text_to_textnodes(self):
        text = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        nodes = text_to_textnodes(text=text)

        self.assertListEqual(
            [
                TextNode(text='This is ', text_type=TextType.TEXT),
                TextNode(text='text', text_type=TextType.BOLD_TEXT),
                TextNode(text=' with an ', text_type=TextType.TEXT),
                TextNode(text='italic', text_type=TextType.ITALIC_TEXT),
                TextNode(text=' word and a ', text_type=TextType.TEXT),
                TextNode(text='code block', text_type=TextType.CODE_TEXT),
                TextNode(text=' and an ', text_type=TextType.TEXT),
                TextNode(text='obi wan image', text_type=TextType.IMAGE, url='https://i.imgur.com/fJRm4Vk.jpeg'),
                TextNode(text=' and a ', text_type=TextType.TEXT),
                TextNode(text='link', text_type=TextType.LINK, url='https://boot.dev'),
            ],
            nodes
        )

if __name__ == '__main__':
    unittest.main()
