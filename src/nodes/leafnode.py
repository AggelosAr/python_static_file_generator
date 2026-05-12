from .htmlnode import HTMLNode


class LeafNode(HTMLNode):

    def __init__(self, 
                 value: str,
                 tag: str | None,
                 props: dict | None = None):
        
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError('All leaf nodes must have a value.')
        if self.tag is None:
            return str(self.value)
        
        props = ''
        if self.props:
            props = ' ' + ' '.join([f'{k}="{v}"' for k, v in self.props.items()])

        tag_start, tag_close, html_tag_close = '<', '>', '/'

        start = f'{tag_start}{self.tag}{props}{tag_close}'
        middle = f'{self.value}'
        end = f'{tag_start}{html_tag_close}{self.tag}{tag_close}'

        return f'{start}{middle}{end}'
    
    def __str__(self):
        # Todo maybe update this for the props attr to show better.
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
    def __repr__(self):
        return self.__str__()
