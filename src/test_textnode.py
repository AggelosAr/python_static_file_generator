import unittest

from nodes.textnode import TextNode, TextType


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
        text_node = TextNode(text='This is some anchor text',
                             text_type='link')
        self.assertEqual(text_node.text, 'This is some anchor text')
        self.assertEqual(text_node.text_type, 'link')
        self.assertEqual(text_node.url, None)




if __name__ == '__main__':
    unittest.main()