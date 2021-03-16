from moduleCode import Code

def firstPass(parser: object, symboltable: object):
	# Builds the symbol table without other effects.
	command_address = 0
	while parser.hasMoreCommands():
		if parser.commandType() == 'L_COMMAND':
			# Don't increment! L-commands are just labels
			symboltable.addEntry(parser.symbol(), command_address) 
		else:
			# The actual line number in output.hack
			command_address += 1
		parser.advance()

def secondPass(parser: object, symboltable: object):
	# Actual parsing takes place here. Each command is either C-, A-, or L-type.
	ram_slot = 16
	with open('output.hack', 'w') as output:
		while parser.hasMoreCommands():
			if parser.commandType() == 'C_COMMAND':
				# C-commands are handled by our Code module.
				binComp = Code.comp(parser.comp())
				binDest = Code.dest(parser.dest())
				binJump = Code.jump(parser.jump())
				binary = f'111{binComp}{binDest}{binJump}'
				output.write(binary + '\n')
			elif parser.commandType() == 'A_COMMAND':
				symbol = parser.symbol()
				if symboltable.contains(symbol):
					# If the A-command is referencing an L-command label from firstPass.
					# In this case the symbol is a command address in the program.
					address = symboltable.getAddress(symbol)
					binAddress = bin(int(address))[2:]
					binary = f'{"0"*(16-len(binAddress))}{binAddress}'
				elif symbol.isnumeric():
					# If the A-command is a number, we use that value directly.
					binAddress = bin(int(symbol))[2:]
					binary = f'{"0"*(16-len(str(binAddress)))}{binAddress}'
				else:
					# Else A-command is a variable declaration; assign it a new RAM address.
					symboltable.addEntry(symbol, ram_slot)
					ram_slot += 1
					address = symboltable.getAddress(symbol)
					binAddress = bin(int(address))[2:]
					binary = f'{"0"*(16-len(str(binAddress)))}{binAddress}'
				output.write(binary + '\n')

			parser.advance()