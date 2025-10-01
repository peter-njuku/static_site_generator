class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Not implemented")
        
    def props_to_html(self):
        if not self.props:
            return ""
        
        return " " + " ".join(f'{key} = "{value}"' for key, value in self.props.items())
        
    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'


