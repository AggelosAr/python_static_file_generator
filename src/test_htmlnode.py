import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def get_sample_test_html_node_no_props(self) -> HTMLNode:
        html_node = HTMLNode(tag='<p>',
                             value='I went to school today!')
        return html_node
    
    def test_instantiate_works_no_children(self):
        html_node = HTMLNode(tag='<p>',
                             value='I went to school today!',
                             props={'class': 'container'})
        
        self.assertEqual(html_node.tag, '<p>')
        self.assertEqual(html_node.value, 'I went to school today!')
        self.assertEqual(html_node.props, {'class': 'container'})

    def test_instantiate_works_with_nested_list_children(self):

        list_item1 = HTMLNode(tag='li',
                              value='First item')

        list_item2 = HTMLNode(tag='li',
                              value='Second item')

        ordered_list = HTMLNode(tag='ol',
                                children=[list_item1, list_item2])

        html_node = HTMLNode(tag='div',
                             children=[ordered_list],
                             props={'class': 'container'})

        self.assertEqual(html_node.tag, 'div')
        self.assertEqual(html_node.props, {'class': 'container'})

        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, 'ol')

        self.assertEqual(html_node.children[0].children,
                         [list_item1, list_item2])

        self.assertEqual(html_node.children[0].children[0].value,
                         'First item')

        self.assertEqual(html_node.children[0].children[1].value,
                         'Second item')
    
    def test_props_to_html_none(self):
        props = {}
        html_node = self.get_sample_test_html_node_no_props()
        html_node.props = props

        self.assertEqual('', 
                         html_node.props_to_html())

    def test_props_to_html_single(self):
        props = {'class': 'container'}
        html_node = self.get_sample_test_html_node_no_props()
        html_node.props = props

        self.assertEqual(' class="container"', 
                         html_node.props_to_html())
        
    def test_props_to_html_double(self):
        props = {
            'href': 'https://www.google.com',
            'target': '_blank'
        }
        html_node = self.get_sample_test_html_node_no_props()
        html_node.props = props

        self.assertEqual(' href="https://www.google.com" target="_blank"', 
                         html_node.props_to_html())



if __name__ == '__main__':
    unittest.main()
