# K.R.E Rev-Engineered
import pyxel

import constants
import input
import game

class App:
    def __init__(self):
        pyxel.init(
            constants.GAME_WIDTH, 
            constants.GAME_HEIGHT, 
            caption=constants.GAME_TITLE, 
            fps=constants.GAME_FPS, 
            scale=constants.GAME_SCALE
        )
        
        pyxel.load(constants.RESOURCE_FILE)
        pyxel.image(0).load(0, 0, constants.IMAGE_BANK_0_FILE)

        self.input = input.Input()
        self.game = game.Game()
        pyxel.mouse(False)
        #pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.input.get()
        self.game.update(self.input)
        
    def draw(self):
        self.game.draw()

App()
  
