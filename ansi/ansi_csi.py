import sys
from ansi import ANSI

class ANSI_CSI():
  code = {
    'cuu': 'A',
    'cud': 'B',
    'cuf': 'C',
    'cub': 'D',
    'cnl': 'E',
    'cpl': 'F',
    'cha': 'G',
    'cup': 'H',
    'ed': 'J',
    'el': 'K',
    'su': 'S',
    'sd': 'T',
    'hvp': 'f',
    'sgr': 'm'
    '5i': '5i',
    '4i': '4i',
    'dsr': '6n',
  }

  def write(name, *args):
    if name not in ANSI_CSI.code.keys():
      raise Exception("UNKNOW CODE")

    sys.stdout.write(ANSI_CSI.code[name])