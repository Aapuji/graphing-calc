from enum import Enum

class TokenType(Enum):
  # 1-Char Token
  LParen  = 1, 
  RParen  = 2,
  Comma   = 3,
  Equal   = 4,
  Plus    = 5,
  Minus   = 6,
  Star    = 7,
  Slash   = 8,
  Carat   = 9,
  Hashtag = 10,
  
  # Literals
  Number  = 11,
  Ident   = 12,

  # Keywords
  Help    = 13,
  Quit    = 14

  EOF     = 0
  pass

class Token:
  type: TokenType
  

class Lexer:
  start: int
  current: int
  line: int
  had_err: bool

  def __init__(self) -> None:
    self.start = 0
    self.current = 0
    self.line = 1
    self.had_err = False

  def lex_token(self) -> Token:
    pass
