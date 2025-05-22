import unittest
from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
	def test_props(self):
		node1 = HTMLNode("a", "this is a htmlnode text", None, {"href":"https://www.google.com", "target": "_blank"})
		result = ' href="https://www.google.com" target="_blank"'
		self.assertEqual(node1.props_to_html(), result)

	def test_lots_of_props(self):
		node1 = HTMLNode("b", "another test", None, {"href":"https://www.google.com", "target": "_blank", "object": "1", "attribute": "gold", "color": "blue"})
		result = ' href="https://www.google.com" target="_blank" object="1" attribute="gold" color="blue"'
		self.assertEqual(node1.props_to_html(), result)

	def test_no_props(self):
		node1 = HTMLNode()
		self.assertEqual(node1.props_to_html(), None)

	

if __name__ == "__main__":
	unittest.main()
	