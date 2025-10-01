from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list, props:dict=None):
        if children is None or len(children) == 0:
            raise ValueError("Children missing")
        super().__init__(tag=tag,
                          value=None, 
                          children=children, 
                          props=props if props is not None else {},
                          )
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("No Tags")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Children missing")
        
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        