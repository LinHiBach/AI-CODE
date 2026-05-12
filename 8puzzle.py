import random
import time

numbers = list(range(9))
# Xáo trộn ngẫu nhiên vị trí các số
random.shuffle(numbers)
#Cắt danh sách 1 chiều thành ma trận 3x3
board = [
    numbers[0:3],
    numbers[3:6],
    numbers[6:9]
]
# trạng thái hoàn thành
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
def print_board(board):
    for row in board:
        print(*row)
# Tập luật
def get_actions(x, y):
    # Góc trên trái
    if x == 0 and y == 0:
        return ["RIGHT", "DOWN"]
    # Góc trên phải
    elif x == 0 and y == 2:
        return ["LEFT", "DOWN"]
    # Góc dưới trái
    elif x == 2 and y == 0:
        return ["UP", "RIGHT"]
    # Góc dưới phải
    elif x == 2 and y == 2:
        return ["UP", "LEFT"]
    # Cạnh trên
    elif x == 0:
        return ["LEFT", "RIGHT", "DOWN"]
    # Cạnh dưới
    elif x == 2:
        return ["LEFT", "RIGHT", "UP"]
    # Cạnh trái
    elif y == 0:
        return ["UP", "DOWN", "RIGHT"]
    # Cạnh phải
    elif y == 2:
        return ["UP", "DOWN", "LEFT"]
    # Ở giữa
    else:
        return ["UP", "DOWN", "LEFT", "RIGHT"]
def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                return i,j
    #không có ô trống
    return -1,-1
max_steps=31

print_board(board)

for step in range(1,max_steps+1):
    if board==goal_state:
        print(f"Thắng ở bước {step-1} rồi hố hố!!!!")
        break
    x,y=find_blank(board)
    if 0<=x<=2 and 0<=y<=2:
        actions=get_actions(x,y)
        valid_action=[]
        action=random.choice(actions)
        print(f"Bước {step}, blank ở [{x},{y}] ->:{action}")
    new_x,new_y=x,y
    if action=="UP": new_x-=1
    elif action=="DOWN": new_x+=1
    elif action=="RIGHT": new_y+=1
    else: new_y-=1
    # 4. SWAP: Đổi chỗ ô trống và ô số để cập nhật trạng thái mới
    board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]
    
        # 5. In trạng thái mới ra màn hình
    print_board(board)
        
        # Dừng 1 giây để bạn kịp xem nó di chuyển
    time.sleep(1)
   

print(f"ĐÃ DỪNG SAU 31 BƯỚC.")
        
        
  
    

    