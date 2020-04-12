class ANSI_COLOR():
  color = {
    'black': '0',
    'red': '1',
    'green': '2',
    'yellow': '3',
    'blue': '4',
    'magenta': '5',
    'cyan': '6',
    'white': '7',
    '8bit': '8;5;{0}',
    'rgb': '8;2;{0};{1};{2}',
    'default': '9',
  }

  def get(name, *args):
    if name not in ANSI_COLOR.color.keys():
      raise Exception('UNKNOW COLOR')

    return ANSI_COLOR.color[name].format(*args)

