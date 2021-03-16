from data import DEST_DICT, JUMP_DICT, COMP_DICT

class Code:
	# Code takes mnemonics and returns the binary equivalents.
	# These are hard-coded references to data.py dictionaries.
	
	def dest(mnemonic):
		# Return binary of dest mnemonic.
		return DEST_DICT[mnemonic]

	def comp(mnemonic):
		# Return binary of comp mnemonic.
		return COMP_DICT[mnemonic]

	def jump(mnemonic):
		# Return binary of jump mnemonic.
		return JUMP_DICT[mnemonic]