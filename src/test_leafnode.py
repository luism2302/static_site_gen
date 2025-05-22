import unittest
from htmlnode import HTMLNode, LeafNode
class TestTextNode(unittest.TestCase):
	def test_to_html_no_props(self):
		node = LeafNode("p", "This is a paragraph of text.")
		result = "<p>This is a paragraph of text.</p>"
		self.assertEqual(node.to_html(), result)
	
	def test_to_html_props(self):
		node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		result = '<a href="https://www.google.com">Click me!</a>'
		self.assertEqual(node.to_html(), result)

	def test_no_tag(self):
		node = LeafNode(None, "No tag test", None)
		result = "No tag test"
		self.assertEqual(node.to_html(), result)
		
	

if __name__ == "__main__":
	unittest.main()
	