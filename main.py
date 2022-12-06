import pyxel
from Classes.board import Board
import constants

# Initializes the board object
board = Board()

# Initializes and runs pyxel and loads the resources
pyxel.init(board.width, board.height, "1942", fps=constants.FRAME_RATE)  # type: ignore
pyxel.load("pyxel_resource_file.pyxres")
pyxel.run(board.update, board.draw)
