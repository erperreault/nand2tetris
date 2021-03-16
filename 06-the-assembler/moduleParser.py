import re

class Parser:
	# Parser loads a text file, moves around within it, and returns mnemonics.

	def __init__(self):
		self.lineNumber = 0

	def constructor(self, file):
		# opens input file
		self.file = []
		with open(file, 'r') as f:
			for line in f:
				if line.startswith('//') or line.startswith('\n'):
					pass
				else:
					line = line.split('//')[0]
					self.file.append(line.strip())
		self.currentCommand = self.file[self.lineNumber]

	def hasMoreCommands(self):
		# Are we at end of file?
		return self.lineNumber != len(self.file)

	def advance(self):
		# Read next command
		self.lineNumber += 1
		try:
			self.currentCommand = self.file[self.lineNumber]
		except:
			print('EOF')

	def commandType(self):
		# Return type of current command.
		if self.currentCommand.startswith('@'):
			return 'A_COMMAND'
		elif self.currentCommand.startswith('('):
			return 'L_COMMAND'
		else:
			return 'C_COMMAND'

	def symbol(self):
		# Return binary value of symbol (only for A or L commands).
		if self.commandType() == 'A_COMMAND':
			command = self.currentCommand[1:]
			return command
		else:
			command = self.currentCommand[1:-1]
			return command

	def dest(self):
		# Return dest mnemonic for current C-command.
		if self.commandType() == 'C_COMMAND':
			command = self.currentCommand
			if '=' in command:
				return re.split('=', command)[0]
			else:
				return 'null'
		else:
			return 'Not a C-command.'

	def comp(self):
		# Return comp mnemonic for current C-command.
		if self.commandType() != 'C_COMMAND':
			return 'Not a C-command.'
		else:
			command = self.currentCommand
			if '=' in command:
				command = re.split('=', command)[1]
			if ';' in command:
				return re.split(';', command)[0]
			else:
				return command

	def jump(self):
		# Return jump mnemonic for current C-command.
		if self.commandType() != 'C_COMMAND':
			return 'Not a C-command.'
		else:
			command = self.currentCommand
			if ';' in command:
				return re.split(';', self.currentCommand)[1]
			else:
				return 'null'