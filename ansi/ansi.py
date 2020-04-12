import sys

class ANSI():
  esc = '\x1b'
  sequence = {
    "ss2": 'N',
    "ss3": 'O',
    "dcs": 'P',
    "csi": '[',
    "st": '\\',
    "osc": ']',
    "sos": 'X',
    "pm": '^',
    "apc": '_',
    "ris": 'c',
  }

  def write(name):
    if name not in ANSI.sequence.keys():
      raise Exception("UNKNOW SEQUENCE")

    sys.stdout.write(ANSI.esc + ANSI.sequence[name])