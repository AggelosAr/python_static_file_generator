
# Todo for tag assert it doesnt conttain < and > or maybe a enum of tags
# Todo maybe add comparison method.
# todo add an enum of tags or smth. And validate against them. is this None?
class HTMLNode:

    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children: list['HTMLNode'] = None, 
                 props: dict | None = None):
        
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('Only children of this class should implement this method!')

    def props_to_html(self) -> str:
        return ''.join([f' {k}="{v}"' for k, v in self.props.items()])

    def __str__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    
    def __repr__(self):
        return self.__str__()
