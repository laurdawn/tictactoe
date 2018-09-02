#coding=utf8

import random, os, copy
class board:

	def __init__(self):
		self.ai = 1
		self.player = -1
		self.win_arr = [
            [0, 1, 2],
            [0, 3, 6],
            [0, 4, 8],
            [1, 4, 7],
            [2, 5, 8],
            [3, 4, 5],
            [6, 7, 8],
            [2, 4, 6]
        ]
		self.board_arr = [
        	[ 0, 0, 0],
        	[ 0, 0, 0],
        	[ 0, 0, 0],
        	0
        ]
		self.side = 3 #边长

	#获得棋盘格子的状态，"0"为空子，"1"为ai棋子，"-1"为玩家棋子
	def box(self, index):
		return index

	def judgePiece(self):
		for i in range(self.side):
			for j in range(self.side):
				if self.board_arr[i][j] == 0:
					return True
		return False

	#将二维数组变成一维数组
	def toOne(self):
		arr = copy.copy(self.board_arr)
		arr.pop()
		one = []
		for i in range(len(arr)):
			for j in range(len(arr[i])):
				one.append(arr[i][j])
		return one

	#ai随机下子
	def randomPlay(self):
		arr = []
		for i in range(self.side):
			for j in range(self.side):
				if 0 == self.board_arr[i][j]:
					arr.append([i, j])
		index = random.randint(0, len(arr)-1)
		return arr[index]

	def checkSituation(self):
		one = self.toOne()
		win_arr = self.win_arr
		for i in range(len(win_arr)):
			if one[win_arr[i][0]] != 0 and one[win_arr[i][0]] == one[win_arr[i][1]] == one[win_arr[i][2]]:
				if self.ai == one[win_arr[i][0]]:
					#你输了
					return 1
				else:
					#你赢了
					return -1
		if not self.judgePiece():
			#平局
			return 0
		return None

	def prepare(self):
		print("-1：玩家先，1：电脑先")
		order = input("请输入先手顺序:")
		if order == '1' or order == '-1':
			self.board_arr[3] = int(order)
			print('\n', self.board_arr[0], '\n', self.board_arr[1], '\n', self.board_arr[2])
			self.game()
		else:
			print("command error.Please try again.")
			self.prepare()
			
	def player_play(self, pos):
		self.board_arr[3] = self.ai
		player_x, player_y = pos
		self.board_arr[player_x][player_y] = self.player
		# print('\n', self.board_arr[0], '\n', self.board_arr[1], '\n', self.board_arr[2])

	def ai_play(self):
		self.board_arr[3] = self.player
		ai_x, ai_y = self.randomPlay()
		self.board_arr[ai_x][ai_y] = self.ai
		# print('\n', self.board_arr[0], '\n', self.board_arr[1], '\n', self.board_arr[2])
		return [ai_x, ai_y]

if __name__ == '__main__':
	b = board()
	b.prepare()