import unittest

from nodes.html_node import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def get_sample_test_html_node_no_props(self) -> HTMLNode:
        html_node = HTMLNode(tag='p', value='Some random paragraph!')
        return html_node

    def get_sample_test_html_node_with_children(self) -> HTMLNode:
        list_item1 = HTMLNode(tag='li', value='First item')
        list_item2 = HTMLNode(tag='li', value='Second item')
        ordered_list = HTMLNode(tag='ol', children=[list_item1, list_item2])

        html_node = HTMLNode(tag='div',
                             children=[ordered_list],
                             props={'class': 'container'})
        return html_node
    
    def test_instantiate_works_no_children(self):
        props = {}
        html_node = self.get_sample_test_html_node_no_props()
        html_node.props = props
        
        self.assertEqual('p', html_node.tag)
        self.assertEqual('Some random paragraph!', html_node.value)
        self.assertEqual({}, html_node.props)

    def test_instantiate_works_with_nested_list_children(self):
        html_node = self.get_sample_test_html_node_with_children()

        self.assertEqual('div', html_node.tag)
        self.assertEqual({'class': 'container'}, html_node.props)

        self.assertEqual(1, len(html_node.children))
        self.assertEqual('ol', html_node.children[0].tag)

        self.assertEqual(2, len(html_node.children[0].children))
        self.assertEqual('li', html_node.children[0].children[1].tag)
        self.assertEqual('First item', html_node.children[0].children[0].value)
        self.assertEqual('li', html_node.children[0].children[1].tag)
        self.assertEqual('Second item', html_node.children[0].children[1].value)
    
    def test_to_html_raises_exc(self):
        html_node = self.get_sample_test_html_node_no_props()

        with self.assertRaises(NotImplementedError) as context:
            _ = html_node.to_html()
        
        self.assertEqual('Only children of this class should implement this method!', 
                         str(context.exception))

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

    def test___str__with_no_children_no_props(self):
        html_node = self.get_sample_test_html_node_no_props()
        expected = 'HTMLNode(p, Some random paragraph!, children: None, None)'

        self.assertEqual(expected, html_node.__str__())
    
    def test___str__with_nested_children_and_props(self):
        props = {'class': 'container'}
        html_node = self.get_sample_test_html_node_with_children()
        html_node.props = props

        expected = "HTMLNode(div, None, children: [HTMLNode(ol, None, " \
        "children: [HTMLNode(li, First item, children: None, None), " \
        "HTMLNode(li, Second item, children: None, None)], None)], {'class': 'container'})"

        self.assertEqual(expected, html_node.__str__())
    
    def test___str___with_no_children_and_props(self):
        props = {'class': 'container'}
        html_node = self.get_sample_test_html_node_no_props()
        html_node.props = props

        expected = "HTMLNode(p, Some random paragraph!, children: None, {'class': 'container'})"

        self.assertEqual(expected, html_node.__str__())
     
    def test___repr__(self):
        html_node = self.get_sample_test_html_node_no_props()
        expected = 'HTMLNode(p, Some random paragraph!, children: None, None)'

        self.assertEqual(expected, html_node.__str__())


if __name__ == '__main__':
    unittest.main()
