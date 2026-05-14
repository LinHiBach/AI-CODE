import random
import time

numbers = list(range(9))
random.shuffle(numbers)

board = [
    numbers[0:3],
    numbers[3:6],
    numbers[6:9]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def print_board(board):
    for row in board:
        print(*row)
    print("-" * 15)

# TẬP LUẬT CƠ BẢN (Quy tắc di chuyển)
def get_actions(x, y):
    moves = []
    if x > 0: moves.append("UP")
    if x < 2: moves.append("DOWN")
    if y > 0: moves.append("LEFT")
    if y < 2: moves.append("RIGHT")
    return moves


def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return -1, -1

# TRÍ NHỚ (Internal State)
visited = set()
visited.add(str(board)) 

print("BÀN CỜ BAN ĐẦU:")
print_board(board)
step = 1

while True:
    if board == goal_state:
        print(f"Thắng ở bước {step-1} rồi hố hố!!!!")
        break
        
    x, y = find_blank(board)
    
    if 0 <= x <= 2 and 0 <= y <= 2:
        actions = get_actions(x, y)
        random.shuffle(actions)
        moved_successfully = False
        
        for action in actions:
            new_x, new_y = x, y
            if action == "UP": new_x -= 1
            elif action == "DOWN": new_x += 1
            elif action == "RIGHT": new_y += 1
            else: new_y -= 1
            
           
            board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]
            
            
            if str(board) not in visited:
               
                visited.add(str(board))
                print(f"Bước {step}, blank ở [{x},{y}] -> Chọn đi: {action}")
                moved_successfully = True
                break
            else:
                # Nếu đã từng xảy ra -> Rút lui (Hoàn tác mô hình)
                board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]
        
        # Cập nhật trạng thái và hiển thị
        if not moved_successfully:
            print(f" Bước {step}: Bí đường rồi, đi đâu cũng dính quá khứ!")
            break
            
        step += 1
        print_board(board)
        # time.sleep(0.5)
        
    else:
        print("Lỗi: Không tìm thấy ô trống!")
        break