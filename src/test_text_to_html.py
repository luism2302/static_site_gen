import unittest
from textnode import text_node_to_html_node, TextType, TextNode, LeafNode

class TestTextNode(unittest.TestCase):
	def test_text(self):
		value = "This is a text node"
		textNode = TextNode(value, TextType.TEXT)
		htmlNode = LeafNode(None, value)
		self.assertEqual(text_node_to_html_node(textNode), htmlNode)

	def test_bold(self):
		value = "This is a bold node"
		textNode = TextNode(value, TextType.BOLD)
		htmlNode = LeafNode("b", value)
		self.assertEqual(text_node_to_html_node(textNode), htmlNode)

	def test_italic(self):
		value = "This is a italic node"
		textNode = TextNode(value, TextType.ITALIC)
		htmlNode = LeafNode("i", value)
		self.assertEqual(text_node_to_html_node(textNode), htmlNode)

	def test_code(self):
		value = "This is a code node"
		textNode = TextNode(value, TextType.CODE)
		htmlNode = LeafNode("code", value)
		self.assertEqual(text_node_to_html_node(textNode), htmlNode)

	def test_link(self):
		value = "anchor text"
		url = "google.com"
		textNode = TextNode(value, TextType.LINK, url)
		htmlNode = LeafNode("a", value, {"href":url})
		self.assertEqual(text_node_to_html_node(textNode), htmlNode)

	def test_image(self):
		value = "anchor text"
		url = "google.com"
		textNode = TextNode(value, TextType.IMAGE, url)
		htmlNode = LeafNode("img", "", {"src":url, "alt":value})
		self.assertEqual(text_node_to_html_node(textNode), htmlNode)

if __name__ == "__main__":
	unittest.main()
	