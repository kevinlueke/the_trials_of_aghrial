# Run Game

import engine
import map

area = map.Map('intro')
game = engine.Engine(area)
game.play()
