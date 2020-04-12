import sys

class ANSI_SGR():
  sgr = {
    'reset': '0',
    'normal': '0',
    
    'bold': '1',
    'increased intensity': '1',

    'faint': '2',
    'decreased intensity': '2',
    'dim': '2',

    'italic': '3',

    'underline': '4',

    'slow blink': '5',

    'rapid blink': '6',

    'reverse': '7',
    'reverse video': '7',
    'invert': '7',

    'conceal': '8',
    'hide': '8',

    'crossed-out': '9',
    'strike': '9',
    'strikethrough': '9',

    'font': '1', # 10-19

    'fraktur': '20',

    'doubly underline': '21',
    'bold off': '21',

    'normal color': '22',
    'normal intensity': '22',

    'not italic': '23',
    'not fraktur': '23',

    'underline off': '24',

    'blink off': '25',

    'reverse off': '27',
    'invert off': '27',

    'reveal': '28',
    'conceal off': '28',

    'not crossed out': '29',

    'foreground color': '3', # 30-39
    'background color': '4', # 40-49

    'framed': '51',

    'encircled': '52',

    'overlined': '53',

    'not framed': '54',
    'not encircled': '54',

    'not overlined': '55',

    'ideogram underline': '60',
    'right side line': '60',

    'ideogram double underline': '61',
    'double line on the right side': '61',

    'ideogram overlined': '62',
    'left side line': '62',

    'ideogram double overlined': '63',
    'double line on the left side': '63',

    'ideogram stress marking': '64',

    'ideogram attributes off': '65',

    'bright foreground color': '9', # 90-97
    'bright background color': '10', # 100-107
  }

  def write(name):
    if name not int ANSI_SGR.sgr.keys():
      raise Exception('UNKNOW SGR')

    sys.stdout.write(ANSI_SGR.sgr[name])