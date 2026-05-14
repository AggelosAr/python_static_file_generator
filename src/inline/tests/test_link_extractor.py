import unittest

from inline.link_extractor import extract_markdown_images, extract_markdown_links


class TestParentNode(unittest.TestCase):

    def test_extract_markdown_images_zero_image(self):
        text = ''
        self.assertEqual([], 
                         extract_markdown_images(text))
    
    def test_extract_markdown_images_one_image(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)'
        self.assertEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif')], 
                         extract_markdown_images(text))

    def test_extract_markdown_images_two_images(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        
        self.assertEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), 
                          ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], 
                         extract_markdown_images(text))
        
    def test_extract_markdown_links_zero_links(self):
        text = ''
        self.assertEqual([], 
                         extract_markdown_links(text))
    
    def test_extract_markdown_links_one_link(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)'
        self.assertEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif')], 
                         extract_markdown_links(text))

    def test_extract_markdown_links_two_links(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        self.assertEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), 
                          ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], 
                         extract_markdown_images(text))
        

if __name__ == '__main__':
    unittest.main()
