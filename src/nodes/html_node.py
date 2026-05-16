# Todo for tag assert it doesnt conttain < and > or maybe a enum of tags
# Todo maybe add comparison method.
# todo add an enum of tags or smth. And validate against them. is this None?
from typing import Sequence


class HTMLNode:

    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children: Sequence['HTMLNode'] | None = None, 
                 props: dict | None = None):
        
        self.tag = tag 
        self.value = value
        if not children:
            self.children: list['HTMLNode'] = []
        else:
            self.children = list(children)
        if not props:
            self.props = {}
        else:
            self.props = props
    
    def add_children(self, _from: 'HTMLNode' | Sequence['HTMLNode']):
        # TODO add test
        assert isinstance(_from, HTMLNode) or isinstance(_from, list)

        if isinstance(_from, list):
            self.children.extend(_from)
            return
        elif isinstance(_from, HTMLNode):
            self.children.extend([_from])
            return
        raise Exception('Can only add children as list of HTMLNode or single HTMLNode.')

    def to_html(self):
        raise NotImplementedError('Only children of this class should implement this method!')

    def get_props_formated(self) -> str:
        props = ''
        if self.props:
            props = ' ' + ' '.join([f'{k}="{v}"' for k, v in self.props.items()])
        return props

    # get_props_formated and props_to_html are kinda the same maybe refactor 
    def props_to_html(self) -> str:
        return ''.join([f' {k}="{v}"' for k, v in self.props.items()])

    def __str__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    
    def __repr__(self):
        return self.__str__()
