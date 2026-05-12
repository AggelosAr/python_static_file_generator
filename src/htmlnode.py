

class HTMLNode:

    def __init__(self, 
                 tag: str, # todo add an enum of tags or smth. And validate against them. is this None?
                 value: str | None = None, 
                 children: list['HTMLNode'] = None, 
                 props: dict | None = None):
        
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props

    # Todo add tests for this method.
    def to_html(self):
        raise NotImplementedError
    
    # Todo maybe add comparison method.

    def props_to_html(self) -> str:
        return ''.join([f' {k}="{v}"' for k, v in self.props.items()])

    def __str__(self):
        ...
    
    def __repr__(self):
        return self.__str__()


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
        
        props = ' '.join([f'{k}="{v}"' for k, v in self.props.items()])
        tag_start, tag_close, html_tag_close = '<', '>', '/'

        start = f'{tag_start}{self.tag} {props}{tag_close}'
        middle = f'{self.value}'
        end = f'{tag_start}{html_tag_close}{self.tag}{tag_close}'

        return f'{start}{middle}{end}'
    
    def __str__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
    def __repr__(self):
        return self.__str__()
