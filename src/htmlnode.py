class HTMLNode:
	def __init__(self, tag = None, value = None, children = None, props = None):
		self.tag = tag
		self.value =  value
		self.children = children
		self.props = props
	
	def to_html(self):
		raise NotImplementedError
	
	def props_to_html(self):
		if self.props is None:
			return None
		html = ""
		for k, v in self.props.items():
			fProps = f'{k}="{v}"'
			html = html + " " + fProps
		return html
	
	def __repr__(self):
		return f'HTMLNode(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}'

	def __eq__(self, other):
		if self.tag != other.tag:
			return False
		if self.value != other.value:
			return False
		if self.children != other.children:
			return False
		if self.props != other.props:
			return False
		return True

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props = None):
		super().__init__(tag, value, None, props)
		if value is None:
			raise ValueError("value is required")

	def to_html(self):
		if self.tag is None:
			return self.value
		if self.props is None:
			return f"<{self.tag}>{self.value}</{self.tag}>"
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props = None):
		super().__init__(tag, None, children, props)
		if tag is None:
			raise ValueError("tag is required")
		if children is None:
			raise ValueError("children is required")
		
	def to_html(self):
		if self.props is None:
			html_props = ""
		else:
			html_props = self.props_to_html()

		html = f"<{self.tag}{html_props}>"
		for child in self.children:
			child_html = child.to_html()
			html += child_html
		html += f"</{self.tag}>"
		return html
