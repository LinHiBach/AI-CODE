import random
import time

# 1. Khởi tạo mảng 3x3 random với rác (1) và sạch (0) 
board = [
    [random.choice([0, 1]) for _ in range(3)],
    [random.choice([0, 1]) for _ in range(3)],
    [random.choice([0, 1]) for _ in range(3)]
]


rx = random.randint(0, 2)
ry = random.randint(0, 2)
def print_env(board, rx, ry):
    for i in range(3):
        for j in range(3):
            if i == rx and j == ry:
                print(f"[{board[i][j]}]", end=" ") # Robot đang ở đây
            else:
                print(f" {board[i][j]} ", end=" ") # Các ô bình thường
        print() # Xuống dòng khi hết 1 hàng
    print("-" * 15)
def get_actions(x, y):
    action = []
    if x > 0: action.append("UP")
    if x < 2: action.append("DOWN")
    if y > 0: action.append("LEFT")
    if y < 2: action.append("RIGHT")
    return action
def is_clean(board):
    tong_rac = sum(sum(row) for row in board)
    return tong_rac == 0

print_env(board, rx, ry)
step=1
while True:
    # Kiểm tra điều kiện dừng
    if is_clean(board):
        print(f"DONE Nhà sạch ở bước {step - 1}.")
        break

    
    current_status = board[rx][ry]
    
    

    #Thực thi hành động
    if action == "HÚT":
        board[rx][ry] = 0 # Làm sạch ô hiện tại
    elif action == "UP": rx -= 1
    elif action == "DOWN": rx += 1
    elif action == "LEFT": ry -= 1
    elif action == "RIGHT": ry += 1

    # In ra trạng thái mới
    print_env(board, rx, ry)
    step+=1
    time.sleep(1)

else:
    print(f" DỪNG SAU {max_steps} BƯỚC")