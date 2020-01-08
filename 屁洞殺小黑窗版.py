import time
setup_list = [[0,0,0],	#遊戲人數對應職業的設置[狼人數,先知人數,村民人數]
			  [0,1,0],
			  [1,1,0],
			  [1,1,1],
			  [1,1,2],
			  [1,1,3],
			  [2,2,2],
			  [2,2,3],
			  [2,2,4],
			  [3,2,4],
			  [3,2,5],
			  [3,3,5],
			  [3,3,6],
			  [4,3,6],
			  [4,3,7],
			  [4,4,7],
			  [4,4,8],
			  [4,4,9],
			  [4,4,10]]

class_list = ["狼人","先知","村民"]
character_list = [[666,1]]		#[職業,死了沒] 0=狼人,1=先知,2=村民,666=上帝; 0=活著,1=死了

def setup_game():
	player_num = int(input("玩家人數: "))
	for i in range(player_num):
		character_list.append(["",0])
		
	input_str = input("狼人玩家的號碼({}個)".format(setup_list[player_num][0]))
	for i in input_str.split(','):
		character_list[int(i)][0] = 0
		
	input_str = input("先知玩家的號碼({}個)".format(setup_list[player_num][1]))
	for i in input_str.split(','):
		character_list[int(i)][0] = 1

	for i in range(player_num):
		if(character_list[i+1][0]==""):
			character_list[i+1][0] = 2

def night():
	print("天黑請閉眼")
	time.sleep(.5)
	print("先知請張眼")
	time.sleep(.5)
	print("先知請選擇要調查的玩家號碼")
	chosed_guy = int(input(">>>"))
	print("{}號玩家的身分是---{}!".format(chosed_guy,class_list[int(character_list[chosed_guy][0])]))
	time.sleep(.5)
	print("先知請閉眼")
	time.sleep(.5)
	print("狼人請張眼")
	time.sleep(.5)
	print("狼人請選擇要殺死的人")
	poor_guy = int(input(">>>"))
	print("選擇殺死{}號玩家.".format(poor_guy))
	time.sleep(.5)
	print("狼人請閉眼")
	time.sleep(.5)
	print("天亮了，所有人睜開眼睛")
	time.sleep(.5)
	print("無辜的{}號被狼人無情殺害了，他的身分是---{}!".format(poor_guy,class_list[int(character_list[poor_guy][0])]))
	character_list[poor_guy][1] = 1
	
def day():
	print("請開始討論誰是狼人")
	time.sleep(.5)
	print("開始投票")
	time.sleep(.5)
	print("輸入被表決殺死的玩家")
	poor_guy = int(input(">>>"))
	print("{}號玩家被處以絞刑，他的身分是---{}!".format(poor_guy,class_list[int(character_list[poor_guy][0])]))
	character_list[poor_guy][1] = 1
	
def verify():
	werewolf_num = 0
	player_num = 0
	for i in character_list:
		if (i[1] == 0):
			player_num += 1
			if(i[0] == 0):
				werewolf_num += 1

	if(werewolf_num == 0):
		return(1)
	
	if(werewolf_num*2+1 >= player_num):
		return(2)
	else:
		return(0)

def gameover(victory):
	print("遊戲結束!")
	if(victory == 1):
		print("人類方獲得勝利!")
	
	elif(victory == 2):
		print("狼人方獲得勝利!")
		
def main():
	setup_game()
	victory = 0
	while(victory == 0):
		night()
		day()
		victory = verify()

	gameover(victory)
	
if __name__ == '__main__':
	main()