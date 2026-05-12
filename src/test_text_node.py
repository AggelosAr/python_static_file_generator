import unittest

from nodes.text_node import TextNode, TextType
from nodes.html_node import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(text='This is a text node', text_type=TextType.BOLD_TEXT)
        node2 = TextNode(text='This is a text node', text_type=TextType.BOLD_TEXT)

        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode(text='This is a text node', text_type=TextType.BOLD_TEXT)
        node2 = TextNode(text='This is a text node', text_type=TextType.ITALIC_TEXT)

        self.assertNotEqual(node, node2)

    def test_instantiate_works(self):
        text_node = TextNode(text='This is some anchor text',
                             text_type='link',
                             url='https://www.boot.dev')
        
        self.assertEqual(text_node.text, 'This is some anchor text')
        self.assertEqual(text_node.text_type, 'link')
        self.assertEqual(text_node.url, 'https://www.boot.dev')
    
    def test_instantiate_works_with_none_url(self):
        text_node = TextNode(text='This is some anchor text', text_type='link')
        self.assertEqual(text_node.text, 'This is some anchor text')
        self.assertEqual(text_node.text_type, 'link')
        self.assertEqual(text_node.url, None)

    def test_text_node_to_html_node_bold(self):
        node = TextNode('Hello', TextType.BOLD_TEXT)
        html_node = node.text_node_to_html_node(node)

        self.assertEqual('b', html_node.tag)
        self.assertEqual('Hello', html_node.value)

    def test_text_node_to_html_node_italic(self):
        node = TextNode('Hello', TextType.ITALIC_TEXT)
        html_node = node.text_node_to_html_node(node)

        self.assertEqual('i', html_node.tag)
        self.assertEqual('Hello', html_node.value)

    def test_text_node_to_html_node_code(self):
        node = TextNode("print('hi')", TextType.CODE_TEXT)
        html_node = node.text_node_to_html_node(node)

        self.assertEqual('code', html_node.tag)
        self.assertEqual("print('hi')", html_node.value)

    def test_text_node_to_html_node_link(self):
        node = TextNode(text='Boot.dev',
                        text_type=TextType.LINK,
                        url='https://boot.dev')

        html_node = node.text_node_to_html_node(node)

        self.assertEqual('a', html_node.tag)
        self.assertEqual('Boot.dev', html_node.value)
        self.assertEqual({'href': 'https://boot.dev'}, html_node.props)

    def test_text_node_to_html_node_image(self):
        node = TextNode(text='image alt',
                        text_type=TextType.IMAGE,
                        url='https://example.com/image.png')

        html_node = node.text_node_to_html_node(node)

        self.assertEqual('img', html_node.tag)
        self.assertEqual({'src': 'https://example.com/image.png',
                          'alt': 'image alt'}, 
                          html_node.props)

    def test_text_node_to_html_node_invalid_type(self):
        node = TextNode('Hello', 'invalid_type')

        with self.assertRaises(Exception) as context:
            node.text_node_to_html_node(node)

        self.assertEqual('Invalid text type: invalid_type', str(context.exception))

    def test___str__(self):
        node = TextNode(text='This is a text node', text_type=TextType.BOLD_TEXT)
        
        self.assertEqual('TextNode(This is a text node, bold_text, None)', 
                         node.__str__())
    
    def test___str___with_url(self):
        node = TextNode(text='This is a text node', 
                        text_type=TextType.BOLD_TEXT, 
                        url='https://www.boot.dev')
        
        self.assertEqual('TextNode(This is a text node, bold_text, https://www.boot.dev)', 
                         node.__str__())
        
    def test___repr__(self):
        node = TextNode(text='This is a text node', text_type=TextType.BOLD_TEXT)
        
        self.assertEqual('TextNode(This is a text node, bold_text, None)', 
                         node.__str__())


if __name__ == '__main__':
    unittest.main()