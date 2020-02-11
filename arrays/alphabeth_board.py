class Solution:
	def alphabetBoardPath(self, target: str) -> str:

		# make diction of board for easy access
		board = dict()
		for i, s in enumerate("abcdefghijklmnopqrstuvwxyz"):
			board[s] = divmod(i, 5)

		# loop
		res = [self.char2char(board, 'a', target[0])]
		for idx in range(1, len(target)):
			res = res + [self.char2char(board, target[idx-1], target[idx])]
		return ''.join(res)

	def char2char(self, board, ch1, ch2):
		LR = 'L' * (board[ch1][1] - board[ch2][1]) + \
                    'R' * (board[ch2][1] - board[ch1][1])
		UD = 'U' * (board[ch1][0] - board[ch2][0]) + \
                    'D' * (board[ch2][0] - board[ch1][0])
		if ch1 == 'z':
			return UD + LR + '!'
		else:
			return LR + UD + '!'
