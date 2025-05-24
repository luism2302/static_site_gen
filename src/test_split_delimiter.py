import unittest
from textnode import split_nodes_delimiter, TextType, TextNode, LeafNode

class TestTextNode(unittest.TestCase):
	def test_delimiter_bold(self):
		value = "This is a text node with **lots of** bold words **inside this** block of **text**"
		textNode = TextNode(value, TextType.TEXT)
		result = [TextNode("This is a text node with ", TextType.TEXT), TextNode("lots of", TextType.BOLD), TextNode(" bold words ", TextType.TEXT), TextNode("inside this", TextType.BOLD), TextNode(" block of ", TextType.TEXT), TextNode("text", TextType.BOLD)]
		self.assertEqual(split_nodes_delimiter([textNode], "**", TextType.BOLD), result)

	def test_delimiter_italic(self):
		value = "This is a text node with _lots of_ bold words _inside this_ block of _text_"
		textNode = TextNode(value, TextType.TEXT)
		result = [TextNode("This is a text node with ", TextType.TEXT), TextNode("lots of", TextType.ITALIC), TextNode(" bold words ", TextType.TEXT), TextNode("inside this", TextType.ITALIC), TextNode(" block of ", TextType.TEXT), TextNode("text", TextType.ITALIC)]
		self.assertEqual(split_nodes_delimiter([textNode], "_", TextType.ITALIC), result)

	def test_delimiter_code(self):
		value = "This `is a code block` made for `testing`"
		textNode = TextNode(value, TextType.TEXT)
		result = [TextNode("This ", TextType.TEXT), TextNode("is a code block", TextType.CODE), TextNode(" made for ", TextType.TEXT), TextNode("testing", TextType.CODE)]
		self.assertEqual(split_nodes_delimiter([textNode], "`", TextType.CODE), result)


if __name__ == "__main__":
	unittest.main()