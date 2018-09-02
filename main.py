#coding=utf-8
import kivy, Board
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse
from kivy.uix.label import Label

# kivy.resources.resource_add_path("./")
# font_heiti = kivy.resources.resource_find("font.TTF")

class JingGame(Widget):

	grid_side = 86
	piece_redius = 25
	chess = Board.board()
	allow_draw = True
	win_label = ''

	def game(self):
		# print(self.chess.win_arr)
		self.chess.board_arr[3] = self.chess.player

	def on_touch_up(self, touch):
		#通行证
		if not self.allow_draw:
			return

		try:
			player_x, player_y = self.limit(touch.x, touch.y)
		except:
			return
		value = self.chess.board_arr[player_x][player_y]
		if value != 0:
			return
		self.chess.player_play([player_x, player_y])
		self.draw_circle(player_x, player_y)
		boolean = self.chess.checkSituation()
		if boolean == None:
			ai_x, ai_y = self.chess.ai_play()
			self.draw_cha(ai_x, ai_y)
			boolean = self.chess.checkSituation()
			if boolean == None:
				return
		if boolean == -1:
			self.add_widget(Label(text="You win",font_size= 100, center_x = self.center_x, top = self.top-50))
		elif boolean == 1 :
			self.add_widget(Label(text="Computer win",font_size= 100, center_x = self.center_x, top = self.top-50))
		elif boolean == 0:
			self.add_widget(Label(text="Dogfall",font_size= 100, center_x = self.center_x, top = self.top-50))
		self.allow_draw = False

	#-1为玩家，画圆
	def draw_circle(self, x, y):
		circle_x, circle_y = self.get_draw_coor(x, y)
		self.canvas.add(Ellipse(source='./yuan.png', size=(50, 50), pos=(circle_x, circle_y)))

	#1为ai，画叉
	def draw_cha(self, x, y):
		cha_x, cha_y = self.get_draw_coor(x, y)
		self.canvas.add(Ellipse(source='./cha.png', size=(50, 50), pos=(cha_x, cha_y)))

	def get_draw_coor(self, x, y):
		if (x, y) == (0, 0):
			return self.center_x - self.grid_side - self.piece_redius, self.center_y + self.grid_side - self.piece_redius
		elif (x, y) == (0, 1):
			return self.center_x - self.piece_redius, self.center_y + self.grid_side - self.piece_redius
		elif (x, y) == (0, 2):	
			return self.center_x + self.grid_side - self.piece_redius, self.center_y + self.grid_side - self.piece_redius
		elif (x, y) == (1, 0):	
			return self.center_x - self.grid_side - self.piece_redius, self.center_y - self.piece_redius
		elif (x, y) == (1, 1):	
			return self.center_x - self.piece_redius, self.center_y - self.piece_redius
		elif (x, y) == (1, 2):	
			return self.center_x + self.grid_side - self.piece_redius, self.center_y - self.piece_redius
		elif (x, y) == (2, 0):	
			return self.center_x - self.grid_side - self.piece_redius, self.center_y - self.grid_side - self.piece_redius
		elif (x, y) == (2, 1):	
			return self.center_x - self.piece_redius, self.center_y - self.grid_side - self.piece_redius
		elif (x, y) == (2, 2):	
			return self.center_x + self.grid_side - self.piece_redius, self.center_y - self.grid_side - self.piece_redius

	def limit(self, x, y):
		#从上至下
		#1-3
		if self.center_x - self.grid_side*1.5 < x < self.center_x - self.grid_side/2 and \
		self.center_y + self.grid_side/2 < y < self.center_y + self.grid_side*1.5:
			# self.draw_cha(self.center_x - self.grid_side - self.piece_redius, self.center_y + self.grid_side - self.piece_redius)
			return (0, 0)
		elif self.center_x - self.grid_side/2 < x < self.center_x + self.grid_side/2 and \
		self.center_y + self.grid_side/2 < y < self.center_y + self.grid_side*1.5:
			# self.draw_circle(self.center_x - self.piece_redius, self.center_y + self.grid_side - self.piece_redius)
			return (0, 1)
		elif self.center_x + self.grid_side/2 < x < self.center_x + self.grid_side*1.5 and \
		self.center_y + self.grid_side/2 < y < self.center_y + self.grid_side*1.5:
			# self.draw_cha(self.center_x + self.grid_side - self.piece_redius, self.center_y + self.grid_side - self.piece_redius)
			return (0, 2)
		#4-6
		elif self.center_x - self.grid_side*1.5 < x < self.center_x - self.grid_side/2 and \
		self.center_y - self.grid_side/2 < y < self.center_y + self.grid_side/2:
			# self.draw_circle(self.center_x - self.grid_side - self.piece_redius, self.center_y - self.piece_redius)
			return (1, 0)
		elif self.center_x - self.grid_side/2 < x < self.center_x + self.grid_side/2 and \
		self.center_y - self.grid_side/2 < y < self.center_y + self.grid_side/2:
			# self.draw_cha(self.center_x - self.piece_redius, self.center_y - self.piece_redius)
			return (1, 1)
		elif self.center_x + self.grid_side/2 < x < self.center_x + self.grid_side*1.5 and \
		self.center_y - self.grid_side/2 < y < self.center_y + self.grid_side/2:
			# self.draw_circle(self.center_x + self.grid_side - self.piece_redius, self.center_y - self.piece_redius)
			return (1, 2)
		#7-9
		elif self.center_x - self.grid_side*1.5 < x < self.center_x - self.grid_side/2 and \
		self.center_y - self.grid_side*1.5 < y < self.center_y - self.grid_side/2:
			# self.draw_cha(self.center_x - self.grid_side - self.piece_redius, self.center_y - self.grid_side - self.piece_redius)
			return (2, 0)
		elif self.center_x - self.grid_side/2 < x < self.center_x + self.grid_side/2 and \
		self.center_y - self.grid_side*1.5 < y < self.center_y - self.grid_side/2:
			# self.draw_circle(self.center_x - self.piece_redius, self.center_y - self.grid_side - self.piece_redius)
			return (2, 1)
		elif self.center_x + self.grid_side/2 < x < self.center_x + self.grid_side*1.5 and \
		self.center_y - self.grid_side*1.5 < y < self.center_y - self.grid_side/2:
			# self.draw_cha(self.center_x + self.grid_side - self.piece_redius, self.center_y - self.grid_side - self.piece_redius)
			return (2, 2)
		else:
			return None


class JingApp(App):
	title = "井字棋"
	def build(self):
		j = JingGame()
		j.game()
		return j
 
if __name__ == '__main__':
	JingApp().run()