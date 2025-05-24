import unittest
from textnode import split_nodes_image, split_nodes_link, TextType, TextNode, LeafNode

class TestTextNode(unittest.TestCase):

	def test_extract_one_image(self):
		node = TextNode("![image](linktoimage.com) this has an image at the beginning",TextType.TEXT)
		result = [TextNode("image", TextType.IMAGE, "linktoimage.com"), TextNode(" this has an image at the beginning", TextType.TEXT)]
		self.assertEqual(split_nodes_image([node]), result)

	def test_extract_multiple_nodes(self):
		node = TextNode("![image](linktoimage.com) this has an image at the beginning",TextType.TEXT)
		node2 = TextNode("this has an image ![image2](image2/com) in the middle",TextType.TEXT)
		node3 = TextNode("this has an image at the end ![image3](image3.com)",TextType.TEXT)

		result = [TextNode("image", TextType.IMAGE, "linktoimage.com"), TextNode(" this has an image at the beginning", TextType.TEXT),
			TextNode("this has an image ", TextType.TEXT),TextNode("image2", TextType.IMAGE, "image2/com"), TextNode(" in the middle", TextType.TEXT),
			TextNode("this has an image at the end ", TextType.TEXT),TextNode("image3", TextType.IMAGE, "image3.com")]
		self.assertEqual(split_nodes_image([node, node2, node3]), result)

	def test_extract_one_link(self):
		node = TextNode("[link](link.com) this has a link at the beginning",TextType.TEXT)
		result = [TextNode("link", TextType.LINK, "link.com"), TextNode(" this has a link at the beginning", TextType.TEXT)]
		self.assertEqual(split_nodes_link([node]), result)

	def test_extract_multiple_links(self):
		node = TextNode("[link](link.com) this has a link at the beginning",TextType.TEXT)
		node2 = TextNode("this has a link [link2](link2.gov) in the middle",TextType.TEXT)
		node3 = TextNode("this has a link at the end [link3](www.link3.web)",TextType.TEXT)

		result = [TextNode("link", TextType.LINK, "link.com"), TextNode(" this has a link at the beginning", TextType.TEXT),
			TextNode("this has a link ", TextType.TEXT),TextNode("link2", TextType.LINK, "link2.gov"), TextNode(" in the middle", TextType.TEXT),
			TextNode("this has a link at the end ", TextType.TEXT),TextNode("link3", TextType.LINK, "www.link3.web")]
		self.assertEqual(split_nodes_link([node, node2, node3]), result)


if __name__ == "__main__":
	unittest.main()