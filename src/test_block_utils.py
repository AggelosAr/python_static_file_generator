import unittest

from blocks.block_utils import MarkDownBlock, BlockType, markdown_to_html_node


class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks_normal(self):
        md = MarkDownBlock(value='''
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
''')
        blocks = md.markdown_to_blocks()
        self.assertEqual(
            [
                'This is **bolded** paragraph',
                'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line',
                '- This is a list\n- with items',
            ],
            blocks
        )

    def test_markdown_to_blocks_more_new_lines(self):
        md = MarkDownBlock(value='''
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
''')
        blocks = md.markdown_to_blocks()
        self.assertEqual(
            [
                'This is **bolded** paragraph',
                'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line',
                '- This is a list\n- with items',
            ],
            blocks
        )

    def test_markdown_to_blocks_most_new_lines(self):
        md = MarkDownBlock(value='''
This is **bolded** paragraph







This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
''')
        blocks = md.markdown_to_blocks()
        self.assertEqual( 
            [
                'This is **bolded** paragraph',
                'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line',
                '- This is a list\n- with items',
            ],
            blocks
        )
    
    def test_markdown_to_blocks_empty(self):
        md = MarkDownBlock(value='''

''')
        blocks = md.markdown_to_blocks()

        self.assertEqual([], blocks)

    def test_block_to_block_type_paragraph(self):
        md = MarkDownBlock(value='''
This is a normal paragraph.
''')
        self.assertEqual(BlockType.PARAGRAPH, BlockType.block_to_block_type(markdown_block=md))
    
    def test_block_to_block_type_heading_one(self):
        md = MarkDownBlock(value='''
# This is a heading
''')
        self.assertEqual(BlockType.HEADING, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_heading_two(self):
        md = MarkDownBlock(value='''
## This is a heading
''')
        self.assertEqual(BlockType.HEADING, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_heading_three(self):
        md = MarkDownBlock(value='''
### This is a heading
''')
        self.assertEqual(BlockType.HEADING, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_heading_four(self):
        md = MarkDownBlock(value='''
#### This is a heading
''')
        self.assertEqual(BlockType.HEADING, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_heading_five(self):
        md = MarkDownBlock(value='''
##### This is a heading
''')
        self.assertEqual(BlockType.HEADING, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_heading_six(self):
        md = MarkDownBlock(value='''
###### This is a heading
''')
        self.assertEqual(BlockType.HEADING, BlockType.block_to_block_type(markdown_block=md))
    
    def test_block_to_block_type_heading_seven(self):
        md = MarkDownBlock(value='''
####### This is a heading
''')
        self.assertEqual(BlockType.PARAGRAPH, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_code(self):
        md = MarkDownBlock(value='''
```
python
print('Hello, world!')
```
''')
        self.assertEqual(BlockType.CODE, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_quote_single(self):
        md = MarkDownBlock(value='''
> Quote Text
''')
        self.assertEqual(BlockType.QUOTE, BlockType.block_to_block_type(markdown_block=md))
    
    def test_block_to_block_type_quote_double(self):
        md = MarkDownBlock(value='''
> Quote Text
>Quote Text2
''')
        self.assertEqual(BlockType.QUOTE, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_quote_triple(self):
        md = MarkDownBlock(value='''
>Quote Text
> Quote Text2
>Quote Text3
''')
        self.assertEqual(BlockType.QUOTE, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_ul(self):
        md = MarkDownBlock(value='''
- l1
- l2
''')
        self.assertEqual(BlockType.UNORDERED_LIST, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_ul_trailing_space_and_new_line(self):
        md = MarkDownBlock(value='''
- l1
- l2
                           
''')
        self.assertEqual(BlockType.UNORDERED_LIST, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_ol_single(self):
        md = MarkDownBlock(value='''
1. l
''')
        self.assertEqual(BlockType.ORDERED_LIST, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_ol_single_fails(self):
            md = MarkDownBlock(value='''
1.
''')
            self.assertEqual(BlockType.PARAGRAPH, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_ol_single_wins(self):
                md = MarkDownBlock(value='''
1. 
''')
                self.assertEqual(BlockType.ORDERED_LIST, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_ol(self):
        md = MarkDownBlock(value='''
1. l
2.  l
3.   l
''')
        self.assertEqual(BlockType.ORDERED_LIST, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_ol_fails(self):
        md = MarkDownBlock(value='''
1 l
2. l
3.  l
''')
        self.assertEqual(BlockType.PARAGRAPH, BlockType.block_to_block_type(markdown_block=md))

    def test_block_to_block_type_ol_fails_another_case(self):
        md = MarkDownBlock(value='''
1. l
.   l
3.   l
''')
        self.assertEqual(BlockType.PARAGRAPH, BlockType.block_to_block_type(markdown_block=md))

    def test_markdown_to_html_paragraph(self):
        md = MarkDownBlock(value='''
This is **bolded** paragraph
text in a p
tag here



''')
        node = markdown_to_html_node(markdown=md)
        html = node.to_html()

        self.assertEqual(
            '<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>',
            html
        )
    
    def test_markdown_to_html_paragraphs(self):
        md = MarkDownBlock(value='''
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

''')
        node = markdown_to_html_node(markdown=md)
        html = node.to_html()

        self.assertEqual(
            '<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>',
            html
        )

    def test_markdown_to_html_codeblock(self):
        md = MarkDownBlock(value='''
```
This is text that _should_ remain
the **same** even with inline stuff
```
''')
        node = markdown_to_html_node(markdown=md)
        html = node.to_html()

        self.assertEqual(
            '<div><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></div>',
            html
        )
# TODO add test for empty code block or broken code block ? 

    def test_markdown_to_html_lists(self):
        md = '''
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

'''
        node = markdown_to_html_node(md)
        html = node.to_html()
        print('-----------------------')
        print(html)

        print(            '<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>',
)
        print('-----------------------')
        self.assertEqual(
            '<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>',
            html
        )

    def test_markdown_to_html_headings(self):
        md = '''
# this is an h1

this is paragraph text

## this is an h2

### this is an h3

#### this is an h4

##### this is an h5

###### this is an h6

####### this is a parapgraph

######## this is a parapgraph
'''
        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            '<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2><h3>this is an h3</h3><h4>this is an h4</h4><h5>this is an h5</h5><h6>this is an h6</h6><p>####### this is a parapgraph</p><p>######## this is a parapgraph</p></div>',
            html
        )

    def test_markdown_to_html_blockquote(self):
        md = '''
> This is a
> blockquote block

this is paragraph text

'''
        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            '<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>',
            html
        )


if __name__ == '__main__':
    unittest.main()
