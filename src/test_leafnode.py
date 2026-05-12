import unittest

from htmlnode import HTMLNode, LeafNode


class TestLeafNode(unittest.TestCase):
    def get_sample_test_leaf_node_no_props(self) -> LeafNode:
        leaf_node = LeafNode(tag='<p>',
                             value='Some random paragraph!')
        return leaf_node
    
    def test_instantiate_works_no_children_allowed(self):
        list_item1 = HTMLNode(tag='li',
                              value='First item')
        list_item2 = HTMLNode(tag='li',
                              value='Second item')
        
        self.assertRaises(Exception, LeafNode(tag='<p>',
                                              value='Some random paragraph!',
                                              children=[list_item1, list_item2]))
      
    
    def test_instantiate_works_value_and_tag_required(self):
        leaf_node = LeafNode(tag='<p>',
                             value='Some random paragraph!',
                             props={'class': 'container'})
        
        self.assertEqual(leaf_node.tag, '<p>')
        self.assertEqual(leaf_node.value, 'Some random paragraph!')
    
    def test_instantiate_works_value_and_tag_required_tag_none(self):
        leaf_node = LeafNode(tag=None,
                             value='Some random paragraph!')
        
        self.assertEqual(leaf_node.tag, None)
        self.assertEqual(leaf_node.value, 'Some random paragraph!')

    def test_to_html_tag_none(self):
        leaf_node = self.get_sample_test_leaf_node_no_props()
        leaf_node.tag = None

        self.assertEqual('<p><p>', 
                         leaf_node.props_to_html())
        
    def test_to_html_no_props(self):
        leaf_node = self.get_sample_test_leaf_node_no_props()

        self.assertEqual('<p>Some random paragraph!</p>', 
                         leaf_node.props_to_html())

    def test_to_html_props(self):
        leaf_node = LeafNode(tag="a", 
                             value="Click me!", 
                             props={"href": "https://www.google.com"})

        self.assertEqual('<a href="https://www.google.com">Click me!</a>', 
                         leaf_node.props_to_html())

    def test___str__(self):
        leaf_node = LeafNode(tag="a", 
                             value="Click me!", 
                             props={"href": "https://www.google.com"})
        
        self.assertEqual('LeafNode(a, Click me!, "{"href": "https://www.google.com"}"', 
                         leaf_node.__str__())
        
    def test___repr__(self):
        leaf_node = LeafNode(tag="a", 
                             value="Click me!", 
                             props={"href": "https://www.google.com"})

        self.assertEqual('LeafNode(a, Click me!, "{"href": "https://www.google.com"}"', 
                         leaf_node.__repr__())


if __name__ == '__main__':
    unittest.main()