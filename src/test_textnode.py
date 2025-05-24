import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq_no_url(self):
		node1 = TextNode("this is a test", TextType.CODE)
		node2 = TextNode("this is a test", TextType.CODE)
		self.assertEqual(node1, node2)

	def test_eq_url(self):
		node1 = TextNode("this is a test", TextType.IMAGE, "url.gog")
		node2 = TextNode("this is a test", TextType.IMAGE, "url.gog")
		self.assertEqual(node1, node2)

	def test_ineq_no_text(self):
		node1 = TextNode("", TextType.TEXT, "url.gog")
		node2 = TextNode("this is a test", TextType.BOLD)
		self.assertNotEqual(node1, node2)

	def test_ineq_no_url(self):
		node1 = TextNode("", TextType.ITALIC, "url.gog")
		node2 = TextNode("", TextType.ITALIC)
		self.assertNotEqual(node1, node2)
	

if __name__ == "__main__":
	unittest.main()
	