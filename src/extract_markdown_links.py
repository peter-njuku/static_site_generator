import re

from textnode import TextNode, TextType


def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(((?:[^()]|\([^()]*\))*)\)", text)
    return tuple(links)

def split_node_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        matches = list(re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text))
        if not matches:
            new_nodes.append(node)
            continue

        current_pos = 0
        for match in matches:
            start, end = match.span()
            link_text, url = match.groups()

            if current_pos < start:
                new_nodes.append(TextNode(text[current_pos:start], TextType.PLAIN_TEXT))
            
            new_nodes.append(TextNode(link_text, TextType.LINKS, url))
            current_pos = end

        if current_pos < len(text):
            new_nodes.append(TextNode(text[current_pos:], TextType.PLAIN_TEXT))

    return new_nodes