import pyxel
from Classes.board import Board
import constants

# Initializes the board object
board = Board()

# Initializes pyxel
pyxel.init(board.width, board.height, "1942", fps=constants.FRAME_RATE)  # type: ignore
# Loads the resource file
pyxel.load("pyxel_resource_file.pyxres")
# Runs the game
pyxel.run(board.update, board.draw)
