import unittest
from textnode import extract_markdown_images, extract_markdown_links, TextType, TextNode, LeafNode

class TestTextNode(unittest.TestCase):
	def test_one_image(self):
		text = "This is a test for ![extracting](www.this_is_image.gif.com.web.jpeg) for my function"
		result = [("extracting","www.this_is_image.gif.com.web.jpeg")]
		self.assertEqual(extract_markdown_images(text), result)
	def test_two_images(self):
		text = "This ![image1](www.image1.jpeg) contains ![image2](www.gov.gif)"
		result = [("image1", "www.image1.jpeg"),("image2", "www.gov.gif")]
		self.assertEqual(extract_markdown_images(text), result)
	def test_one_link(self):
		text = "This is a test for [extracting](www.this_is_image.gif.com.web.jpeg) for my function"
		result = [("extracting","www.this_is_image.gif.com.web.jpeg")]
		self.assertEqual(extract_markdown_links(text), result)
	def test_two_links(self):
		text = "This [image1](www.image1.jpeg) contains [image2](www.gov.gif)"
		result = [("image1", "www.image1.jpeg"),("image2", "www.gov.gif")]
		self.assertEqual(extract_markdown_links(text), result)


if __name__ == "__main__":
	unittest.main()