import sys
from ansi import ANSI
from ansi_sgr import ANSI_SGR
from ansi_color import ANSI_COLOR
from ansi_csi import ANSI_CSI

class TerminalColor():
  def set_font(name, *args):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_SGR.get('foreground color') + 
      ANSI_COLOR.get(name, *args) +
      ANSI_CSI.get('select graphic rendition')
    )

  def set_bg(name, *args):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_SGR.get('background color') + 
      ANSI_COLOR.get(name, *args) +
      ANSI_CSI.get('select graphic rendition')
    )
  
  def set_bright_font(name):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_SGR.get('bright foreground color') + 
      ANSI_COLOR.get(name) +
      ANSI_CSI.get('select graphic rendition')
    )

  def set_bright_bg(name):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_SGR.get('bright background color') + 
      ANSI_COLOR.get(name) +
      ANSI_CSI.get('select graphic rendition')
    )