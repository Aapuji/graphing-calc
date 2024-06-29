import graphics as gfx
from lexer import Lexer

def main():
  window = gfx.init()
  gfx.run(window)

  lexer = Lexer()

  print('Type in a mathematical expression, and it will be evaluated or displayed.\nEnter \x1b[0;31;35mQuit\x1b[0m or \x1b[0;31;35mCtrl+Z\x1b[0m to end the REPL!\n')
  try:
    while True:
      line = input('> ')

      





      if line.lower() == 'quit':
        raise KeyboardInterrupt 
  except KeyboardInterrupt:
    pass
  except EOFError:
    pass

  print('See you later :)')
  pass

if __name__ == '__main__':
  main()