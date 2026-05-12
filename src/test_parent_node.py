import unittest

from nodes.leaf_node import LeafNode
from nodes.parent_node import ParentNode


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
        self.assertEqual('LeafNode(Bold text, b, None)', parent_node.children[0].__str__())
        self.assertEqual('LeafNode(Normal text, None, None)', parent_node.children[1].__str__())
        self.assertEqual('LeafNode(italic text, i, None)', parent_node.children[2].__str__())
        self.assertEqual('LeafNode(Normal text, None, None)', parent_node.children[3].__str__())
        
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

    # def test_to_html_many_children_two_level_deep_same_level_nest(self):
    #     parent_node = self.get_sample_test_parent_node_no_props()
    #     parent_node.children = 

    #     self.assertEqual('', 
    #                      parent_node.to_html())
        
    # def test_to_html_many_children_two_level_deep_different_level_nest(self):
    #     parent_node = self.get_sample_test_parent_node_no_props()
    #     parent_node.children = 

    #     self.assertEqual('', 
    #                      parent_node.to_html())

        
if __name__ == '__main__':
    unittest.main()
