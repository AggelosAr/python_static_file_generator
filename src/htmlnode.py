

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

    def props_to_html(self):
        return ''.join([f' {k}="{v}"' for k, v in self.props.items()])

    def __str__(self):
        ...
    
    def __repr__(self):
        return self.__str__()
