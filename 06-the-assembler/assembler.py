#!python3
# Assembler for Hack assembly language, implemented in Python.

from moduleParser import Parser
from moduleCode import Code
from moduleSymbolTable import SymbolTable
from data import FILENAME

def firstPass(parser: object, symboltable: object):
	# Builds the symbol table without other effects.
	command_address = 0
	while parser.hasMoreCommands():
		if parser.commandType() == 'L_COMMAND':
			symboltable.addEntry(parser.symbol(), command_address)
		else:
			command_address += 1
		parser.advance()

def secondPass(parser: object, symboltable: object):
	# Showtime!
	ram_slot = 16 # This is our first open RAM slot for @xxx declarations.
	with open('output.hack', 'w') as output:
		while parser.hasMoreCommands():
			if parser.commandType() == 'C_COMMAND':
				binComp = Code.comp(parser.comp())
				binDest = Code.dest(parser.dest())
				binJump = Code.jump(parser.jump())
				binary = f'111{binComp}{binDest}{binJump}'
				output.write(binary + '\n')
			elif parser.commandType() == 'A_COMMAND':
				symbol = parser.symbol()
				if symboltable.contains(symbol):
					address = symboltable.getAddress(symbol)
					binAddress = bin(int(address))[2:]
					binary = f'{"0"*(16-len(binAddress))}{binAddress}'
				elif symbol.isnumeric():
					binAddress = bin(int(symbol))[2:]
					binary = f'{"0"*(16-len(str(binAddress)))}{binAddress}'
				else:
					symboltable.addEntry(symbol, ram_slot)
					ram_slot += 1
					address = symboltable.getAddress(symbol)
					binAddress = bin(int(address))[2:]
					binary = f'{"0"*(16-len(str(binAddress)))}{binAddress}'
				output.write(binary + '\n')

			parser.advance()


### Main ###

if __name__ == '__main__':
	parser = Parser()
	parser.constructor(FILENAME)

	symboltable = SymbolTable()
	symboltable.constructor()

	firstPass(parser, symboltable)

	parser = Parser()
	parser.constructor(FILENAME)

	secondPass(parser, symboltable)

### Tests Below ###

	assert Code.dest('D') == '010'