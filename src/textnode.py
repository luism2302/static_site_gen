from enum import Enum
from htmlnode import HTMLNode, LeafNode
import re

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text: str, text_type: TextType, url = None):
		self.text =  text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		if self.text != other.text:
			return False
		if self.text_type != other.text_type:
			return False
		if self.url != other.url:
			return False
		return True
	
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode):
	match text_node.text_type:
		case TextType.TEXT:
			return LeafNode(None, text_node.text)
		case TextType.BOLD:
			return LeafNode("b",text_node.text)
		case TextType.ITALIC:
			return LeafNode("i", text_node.text)
		case TextType.CODE:
			return LeafNode("code", text_node.text)
		case TextType.LINK:
			return LeafNode("a", text_node.text, {"href":text_node.url})
		case TextType.IMAGE:
			return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
		case _:
			raise ValueError("unknown text type")

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
	if old_nodes is None:
		return None
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		separated = node.text.split(delimiter)
		if len(separated) % 2 == 0:
			raise Exception("couldnt find a matching separator")
		for i in range(len(separated)):
			if separated[i] == "" or separated[i] == " ":
				continue
			if i % 2 != 0:
				new_nodes.append(TextNode(separated[i], text_type))
			else:
				new_nodes.append(TextNode(separated[i], TextType.TEXT))
	return new_nodes

def extract_markdown_images(text):
	return re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)',text)
	
def extract_markdown_links(text):
	return re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)',text)

def split_nodes_image(old_nodes: list[TextNode]):
	if old_nodes is None:
		return None
	
	new_nodes = []

	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue

		extracted = extract_markdown_images(node.text)
		if len(extracted) == 0:
			new_nodes.append(node)
			continue

		text_to_split = node.text

		for i in range(len(extracted)):
			image = extracted[i]
			splitted = text_to_split.split(f'![{image[0]}]({image[1]})', 1)
			if splitted[0] != '':
				new_nodes.append(TextNode(splitted[0], TextType.TEXT))
			new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
			text_to_split = splitted[1]
			
			if i + 1 == len(extracted) and text_to_split != '':
				new_nodes.append(TextNode(text_to_split, TextType.TEXT))
	
	return new_nodes

def split_nodes_link(old_nodes: list[TextNode]):
	if old_nodes is None:
		return None
	
	new_nodes = []

	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue

		extracted = extract_markdown_links(node.text)
		if len(extracted) == 0:
			new_nodes.append(node)
			continue

		text_to_split = node.text

		for i in range(len(extracted)):
			link = extracted[i]
			splitted = text_to_split.split(f'[{link[0]}]({link[1]})', 1)
			if splitted[0] != '':
				new_nodes.append(TextNode(splitted[0], TextType.TEXT))
			new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
			text_to_split = splitted[1]
			
			if i + 1 == len(extracted) and text_to_split != '':
				new_nodes.append(TextNode(text_to_split, TextType.TEXT))
	
	return new_nodes

def text_to_textnodes(text):
	initial = TextNode(text, TextType.TEXT)	
	bold = split_nodes_delimiter([initial], "**", TextType.BOLD)
	italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
	code = split_nodes_delimiter(italic, "`", TextType.CODE)
	links = split_nodes_link(code)
	image = split_nodes_image(links)

	return image
	

		

