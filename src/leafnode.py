from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag:str=None, value:str=None, props:dict=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Error:", "No value in tags")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"