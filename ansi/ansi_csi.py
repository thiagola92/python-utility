class ANSI_CSI():
  code = {
    'cuu': 'A',
    'cursor up': 'A',

    'cud': 'B',
    'cursor down': 'B',

    'cuf': 'C',
    'cursor forward': 'C',

    'cub': 'D',
    'cursor back': 'D',

    'cnl': 'E',
    'cursor next line': 'E',

    'cpl': 'F',
    'cursor previous line': 'F',

    'cha': 'G',
    'cursor horizontal absolute': 'G',
    
    'cup': 'H',
    'cursor position': 'H',

    'ed': 'J',
    'erase display': 'J',

    'el': 'K',
    'erase line': 'K',

    'su': 'S',
    'scroll up': 'S',

    'sd': 'T',
    'scroll down': 'T',

    'hvp': 'f',
    'horizontal vertical position': 'f',

    'sgr': 'm',
    'select graphic rendition': 'm',

    '5i': '5i',
    'aux port on': '5i',

    '4i': '4i',
    'aux port off': '4i',

    'dsr': '6n',
    'device status report': '6n',
  }

  def get(name, *args):
    if name not in ANSI_CSI.code.keys():
      raise Exception('UNKNOW CODE')

    return ANSI_CSI.code[name]