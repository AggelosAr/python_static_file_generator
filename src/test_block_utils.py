import unittest

from blocks.block_utils import markdown_to_blocks


class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks_normal(self):
        md = '''
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
'''
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                'This is **bolded** paragraph',
                'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line',
                '- This is a list\n- with items',
            ],
            blocks
        )

    def test_markdown_to_blocks_more_new_lines(self):
        md = '''
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
'''
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                'This is **bolded** paragraph',
                'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line',
                '- This is a list\n- with items',
            ],
            blocks
        )

    def test_markdown_to_blocks_most_new_lines(self):
        md = '''
This is **bolded** paragraph







This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
'''
        blocks = markdown_to_blocks(md)
        self.assertEqual( 
            [
                'This is **bolded** paragraph',
                'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line',
                '- This is a list\n- with items',
            ],
            blocks
        )
    
    def test_markdown_to_blocks_empty(self):
        md = '''

'''
        blocks = markdown_to_blocks(md)

        self.assertEqual([], blocks)


if __name__ == '__main__':
    unittest.main()
