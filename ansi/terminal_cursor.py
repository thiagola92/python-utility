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

  def down(moves=1):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_CURSOR.get('down', moves) +
      ANSI_CSI.get('cursor down')
    )

  def forward(moves=1):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_CURSOR.get('forward', moves) +
      ANSI_CSI.get('cursor forward')
    )

  def back(moves=1):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_CURSOR.get('back', moves) +
      ANSI_CSI.get('cursor back')
    )

  def next_line(moves=1):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_CURSOR.get('next line', moves) +
      ANSI_CSI.get('cursor next line')
    )

  def previous_line(moves=1):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_CURSOR.get('previous line', moves) +
      ANSI_CSI.get('cursor previous line')
    )

  def column(column=1):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_CURSOR.get('horizontal absolute', column) +
      ANSI_CSI.get('cursor horizontal absolute')
    )

  def position(row=1, column=1):
    sys.stdout.write(
      ANSI.get('csi') +
      ANSI_CURSOR.get('position', row, column) +
      ANSI_CSI.get('cursor position')
    )