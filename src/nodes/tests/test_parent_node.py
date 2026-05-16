import unittest

from nodes.leaf_node import LeafNode
from nodes.parent_node import ParentNode


# TODO add tests for __str__ and __repr__.
class TestParentNode(unittest.TestCase):

    def get_sample_test_parent_node_no_props(self) -> ParentNode:
        children = [LeafNode(tag="b", value="Bold text"),
                    LeafNode(tag=None, value="Normal text"),
                    LeafNode(tag="i", value="italic text"),
                    LeafNode(tag=None, value="Normal text")]
        parent_node = ParentNode(tag='p', children=children)
        return parent_node
    
    def test_instantiate_works_tag_children_required(self):
        parent_node = self.get_sample_test_parent_node_no_props()
        
        self.assertEqual('p', parent_node.tag)
        self.assertEqual('LeafNode(b, Bold text, {})', parent_node.children[0].__str__())
        self.assertEqual('LeafNode(None, Normal text, {})', parent_node.children[1].__str__())
        self.assertEqual('LeafNode(i, italic text, {})', parent_node.children[2].__str__())
        self.assertEqual('LeafNode(None, Normal text, {})', parent_node.children[3].__str__())
        
    def test_to_html_tag_missing(self):
        parent_node = self.get_sample_test_parent_node_no_props()
        parent_node.tag = None

        with self.assertRaises(ValueError) as context:
            _ = parent_node.to_html()
        
        self.assertEqual('Tag missing from ParentNode.', str(context.exception))
    
    def test_to_html_children_missing(self):
        parent_node = self.get_sample_test_parent_node_no_props()
        parent_node.children = None

        with self.assertRaises(ValueError) as context:
            _ = parent_node.to_html()
        
        self.assertEqual('Children missing from ParentNode.', str(context.exception))
    
    def test_to_html_many_children_one_level_deep(self):
        parent_node = self.get_sample_test_parent_node_no_props()

        self.assertEqual('<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>', 
                         parent_node.to_html())

    def test_to_html_many_children_two_level_deep_same_level_nest(self):
        nested_children = [
            ParentNode(tag="b", children=[LeafNode(tag=None, value="Bold text")]),
            ParentNode(tag="i", children=[LeafNode(tag=None, value="italic text")]),
        ]
        parent_node = ParentNode(tag="p", children=nested_children)

        self.assertEqual('<p><b>Bold text</b><i>italic text</i></p>', parent_node.to_html())

def test_to_html_many_children_two_level_deep_different_level_nest(self):
    parent_node = ParentNode(
        tag="div",
        children=[
            ParentNode(tag="p",
                       children=[
                           LeafNode(tag=None, value="Normal text "),
                           ParentNode(
                               tag="b",
                               children=[
                                   LeafNode(tag=None, value="Bold and "),
                                   ParentNode(tag="i", children=[LeafNode(tag=None, value="italic")])
                               ]
                           )
                      ]
            )
        ]
    )

    self.assertEqual('<div><p>Normal text <b>Bold and <i>italic</i></b></p></div>', 
                     parent_node.to_html())
        

if __name__ == '__main__':
    unittest.main()
