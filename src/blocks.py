from enum import Enum
import re

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "quote"
	UNORDERED_LIST = "unordered_list"
	ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str):
	return list(filter(lambda x: x != '', list(map(str.strip,markdown.split("\n\n")))))

def block_to_blocktype(text: str):
	if re.fullmatch(r'^#{1,6}\s\w+', text):
		return BlockType.HEADING
	if text.startswith('```') and text.endswith('```'):
		return BlockType.CODE
	if text.startswith('>'):
		return BlockType.QUOTE
	if text.startswith('- '):
		return BlockType.UNORDERED_LIST
	lines = text.splitlines()
	isOrderedList = True
	for i in range(len(lines)):
		if not lines[i].startswith(f'{i + 1}. '):
			isOrderedList = False
			break
	if isOrderedList:
		return BlockType.ORDERED_LIST
	return BlockType.PARAGRAPH


