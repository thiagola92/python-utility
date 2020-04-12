class ANSI_CURSOR():
  move = {
    'up': '{0}',
    'down': '{0}',
    'forward': '{0}',
    'back': '{0}',
    'next line': '{0}',
    'previous line': '{0}',
    'horizontal absolute': '{0}',
    'position': '{0};{1}',
  }

  def get(name, *args):
    if name not in ANSI_CURSOR.move.keys():
      raise Exception('UNKNOW MOVE')
    
    return ANSI_CURSOR.move[name].format(*args)