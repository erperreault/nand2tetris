from data import SYMBOL_TABLE

class SymbolTable:

    def constructor(self):
        # Create new empty symbol table.
        self.table = SYMBOL_TABLE

    def addEntry(self, symbol, address):
        # Add 'symbol':'address' pair to table.
        self.table[symbol] = address

    def contains(self, symbol: str) -> bool:
        # Does table contain symbol?
        return symbol in self.table.keys()

    def getAddress(self, symbol: str) -> int:
        # Return address for associated symbol.
        return self.table[symbol]