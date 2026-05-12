import unittest

from nodes.text_node import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', TextType.BOLD_TEXT)
        node2 = TextNode('This is a text node', TextType.BOLD_TEXT)

        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode('This is a text node', TextType.BOLD_TEXT)
        node2 = TextNode('This is a text node', TextType.ITALIC_TEXT)

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