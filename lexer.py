import sys

class Lexer:

    NUMBER, ID, WHILE, DO, IF, ELSE, FOR, LB, RB, LBR, RBR, PLUSik, MINUSik, LESS, MORE, EQUAL, SCOL, EOF = range (18)

    SMB = {'{': LB, 
           '}': RB, 
           '=': EQUAL,
           ';': SCOL,
           '(': LBR,
           ')': RBR,
           '+': PLUSik,
           '-': MINUSik,
           '<': LESS,
           '>': MORE
          }
    WRD = {'if': IF,
           'else': ELSE,
           'do': DO,
           'while': WHILE,
           'for': FOR
        }
    ch = ' '

    def error(self, msg):
        print ('Lexer error: ', msg)
        sys.exit(1)

    def getc(self):
        self.ch = sys.stdin.read(1)
    
    def next_token(self):
        self.value = None
        self.symbol = None
        while self.symbol == None:
            if len(self.ch) == 0:
                self.symbol = Lexer.EOF
            elif self.ch.isspace():
                self.getc()
            elif self.ch in Lexer.SMB:
                self.symbol = Lexer.SMB[self.ch]
                self.getc()
            elif self.ch.isdigit():
                intval = 0
                while self.ch.isdigit():
                    intval = intval * 10 + int(self.ch)
                    self.getc()
                self.value = intval
                self.symbol = Lexer.NUMBER
            elif self.ch.isalpha():
                ident = ''
                while self.ch.isalpha():
                    ident = ident + self.ch.lower()
                    self.getc()
                if ident in Lexer.WRD:
                    self.symbol = Lexer.WRD[ident]
                elif len(ident) == 1:
                    self.symbol = Lexer.ID
                    self.value = ord(ident) - ord('a')
                else:
                    self.error('Unknown identifier: ' + ident)
            else:
                self.error('Unexpected symbol: ' + self.ch)