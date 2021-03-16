# Assembler for Hack assembly language, implemented in Python.

from moduleParser import Parser
from moduleCode import Code
from moduleSymbolTable import SymbolTable
from procedures import firstPass, secondPass
from data import FILENAME

### Tests ###

# Code module #
assert type(Code.dest('null')) == str
assert Code.dest('D') == '010'
assert Code.dest('AMD') == '111'
assert Code.dest('null') == '000'

# Parser module #
parser = Parser()

# SymbolTable module #
symboltable = SymbolTable()
symboltable.constructor()
table = symboltable.table

assert type(table) == dict
assert type(table['SP']) == int
assert table['SP'] == 0

### Main ###

if __name__ == '__main__':
	# Throwaway parser to guide us through first pass.
	parser = Parser()
	parser.constructor(FILENAME)

	symboltable = SymbolTable()
	symboltable.constructor()

	firstPass(parser, symboltable)

	# Start over but use the symboltable object from first pass.
	parser = Parser()
	parser.constructor(FILENAME)

	secondPass(parser, symboltable)