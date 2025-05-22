from textnode import TextNode, TextType

def main():
	myNode = TextNode("this is a test", TextType.LINK,  "www.link.gov")
	print(myNode)

if __name__ == "__main__":
	main()