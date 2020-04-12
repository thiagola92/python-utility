import sys
from ansi import ANSI
from ansi_cursor import ANSI_CURSOR
from ansi_csi import ANSI_CSI

class TerminalCursor():
  def up(moves):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_CURSOR.get('up', moves) +
      ANSI_CSI.get('cursor up')
    )