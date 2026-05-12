from .html_node import HTMLNode
from .leaf_node import LeafNode


class ParentNode(HTMLNode):

    def __init__(self,
                 tag: str | None,
                 children: list['ParentNode', LeafNode],
                 props: dict | None = None):
        
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError('Tag missing from ParentNode.')
        if self.children is None:
            raise ValueError('Children missing from ParentNode.') 
        
        html = []
        tag_start, tag_close, html_tag_close = '<', '>', '/'

        start = f'{tag_start}{self.tag}{self.get_props_formated()}{tag_close}'
        end = f'{tag_start}{html_tag_close}{self.tag}{tag_close}'

        for child in self.children:
            html.append(child.to_html())

        return f'{start}{"".join(html)}{end}'

    def __str__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'
    
    def __repr__(self):
        return self.__str__()
