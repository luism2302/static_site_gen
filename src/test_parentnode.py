import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
class TestTextNode(unittest.TestCase):
	def test_parent_html(self):
		node = ParentNode("p", [LeafNode("b","Bold Text"),LeafNode(None, "Normal text"), LeafNode("i", "italic text"),  LeafNode(None, "Normal text")])
		result = "<p><b>Bold Text</b>Normal text<i>italic text</i>Normal text</p>"
		self.assertEqual(node.to_html(), result)

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_with_grandchildren_props(self):
		grandchild_node = LeafNode("b", "grandchild", {"href":"google.com"})
		grandchild_node2 = LeafNode("b", "grandchild2")
		child_node = ParentNode("span", [grandchild_node, grandchild_node2], {"atts":"attribute 1"})
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			'<div><span atts="attribute 1"><b href="google.com">grandchild</b><b>grandchild2</b></span></div>',
		)


if __name__ == "__main__":
	unittest.main()