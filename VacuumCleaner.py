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
print(f"Vị trí ngẫu nhiên {rx},{ry}")
# Hàm in ma trận
def print_env(board, rx, ry):
    for i in range(3):
        for j in range(3):
            if i == rx and j == ry:
                print(f"[{board[i][j]}]", end=" ") # Robot đang ở đây
            else:
                print(f" {board[i][j]} ", end=" ") # Các ô bình thường
        print() # Xuống dòng khi hết 1 hàng
    print("-" * 15)

# Tập luật
def get_actions(x, y):
    moves = []
    if x > 0: moves.append("UP")
    if x < 2: moves.append("DOWN")
    if y > 0: moves.append("LEFT")
    if y < 2: moves.append("RIGHT")
    return moves

# Kiểm tra xem nhà đã sạch hết chưa
def is_clean(board):
    tong_rac = sum(sum(row) for row in board)
    return tong_rac == 0

max_steps = 30


print_env(board, rx, ry)

for step in range(1, max_steps + 1):
    # 1. Kiểm tra điều kiện dừng
    if is_clean(board):
        print(f"🎉 DONE Nhà sạch ở bước {step - 1}.")
        break

    
    current_status = board[rx][ry]
    
    
    if current_status == 1:
        action = "HÚT"
    else:
        action = random.choice(get_actions(rx, ry))

    trang_thai_chu = "Dơ" if current_status == 1 else "Sạch"
    print(f"Bước {step}: Robot ở [{rx},{ry}] (Đang {trang_thai_chu}) -> Hành động: {action}")

    #Thực thi hành động
    if action == "HÚT":
        board[rx][ry] = 0 # Làm sạch ô hiện tại
    elif action == "UP": rx -= 1
    elif action == "DOWN": rx += 1
    elif action == "LEFT": ry -= 1
    elif action == "RIGHT": ry += 1

    # In ra trạng thái mới
    print_env(board, rx, ry)
    time.sleep(1)

else:
    print(f" DỪNG SAU {max_steps} BƯỚC")