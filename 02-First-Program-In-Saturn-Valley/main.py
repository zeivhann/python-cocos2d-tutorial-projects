# Game development with Python and Cocos2d
# Part 2: First program in Saturn Valley

# Alex Silcott (alexsilcott@gmail.com)


# Imports

import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director
from cocos.layer import Layer # new import statement so we can create an object of the Layer class

# New import statement so we can create a label
from cocos.text import Label


# Player class

class Player(actions.Move):
		
	def step(self, dt):
		super(Player, self).step(dt)
		velocity_x = 140 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
		velocity_y = 140 * (keyboard[key.UP] - keyboard[key.DOWN])
		self.target.velocity = (velocity_x, velocity_y)
		

# Big Text Class inherits from Layer
		
class BigText(Layer):
	
		# We have to initialize this class with this function:
		def __init__(self):
			# Here, we initialize the parent class by calling the super function
			super(BigText, self).__init__()
			# We then create the label itself
			big_text_label = Label(
				"Hello World, ZOOM!", # This argument holds the string to display
				font_name = "Arial", # Assigns font face
				font_size = 18, # Assigns font size
				anchor_x = 'left', # anchors text to left side of x-axis
				anchor_y = 'center' # anchors text to middle of y-axis
			)
			
			# Set position of text
			big_text_label.position= 5, 285
			
			# Add label to the layer using the self identifier
			self.add(big_text_label)
		
# Main Function
		
def main():
	global keyboard 
	
	director.init(width=500, height=300, caption="In the beginning everything was Kay-O", autoscale=True, resizable=True)
	
	# Here we initialize the scene for cleaner code later
	main_scene = cocos.scene.Scene()
	
	# Create player layer and add player onto it
	player_layer = layer.Layer()
	player = sprite.Sprite('images/mr-saturn.png')
	player_layer.add(player)


	# Sets initial position and velocity of player
	player.position = (250, 150)
	player.velocity = (0, 0)

	# Set the sprite's movement class
	player.do(Player())
	
	# Add layers to main_scene that we initialized earlier
	# We have also added a second argument to the main_scene.add() call
	# This is the z-index, which explicity determines the order of layers.
	# Here, the player has a z-index of 1 and the text has an index of 2 so it will overlay the player.
	# We are assuming that a background would be z = 0
	main_scene.add(scene.Scene(player_layer), z = 1) 
	main_scene.add(scene.Scene(BigText()), z = 2) # This time we've added the BigText() object to the scene

	keyboard = key.KeyStateHandler()
	director.window.push_handlers(keyboard)
	
	# Run the scene we've built in the window
	director.run(main_scene)
	
# This is a neato python trick so that modules can remain...modular
# (http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm)
if __name__ == '__main__':
	main()
