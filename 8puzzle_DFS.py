import customtkinter as ctk
from tkinter import messagebox
from collections import deque
import random

GOAL = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)

# Tập luật
MOVES = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

def get_blankcanmoves(state):
    state_move = []
    x, y = find_blank(state)
    
    for move_name, (dx, dy) in MOVES.items():
        new_x = x + dx
        new_y = y + dy
        
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            matrix = []
            for row in state:
                matrix.append(list(row))
                
            temp = matrix[x][y]
            matrix[x][y] = matrix[new_x][new_y]
            matrix[new_x][new_y] = temp
            state_move.append(tuple(tuple(row) for row in matrix))
            
    return state_move

def DFS(state):
    if state == GOAL:
        return [state]
        
    frontier = deque()
    first_path = []
    first_path.append(state)
    
    frontier.append((state, first_path))
    
    reached = set()
    reached.add(state)
    
    while len(frontier) > 0:
        current_state, path = frontier.pop()
        state_move = get_blankcanmoves(current_state)
        
        for next_step in state_move:
            if next_step not in reached:
                if next_step == GOAL:
                    correct_path = list(path)
                    correct_path.append(next_step)
                    return correct_path
            
                # Nếu chưa phải đích
                reached.add(next_step)
                
                next_path = list(path)
                next_path.append(next_step)
                frontier.append((next_step, next_path))
    return None
class PuzzleApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("8-Puzzle AI Solver")
        self.geometry("380x520")
        self.resizable(False, False)
        
        self.current_state = [list(row) for row in GOAL]
        self.grid_buttons = []
        
        self.create_widgets()
        self.shuffle_board()

    def create_widgets(self):
       
        self.title_label = ctk.CTkLabel(self, text="8-PUZZLE DFS SOLVER", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=15)
        
        self.board_frame = ctk.CTkFrame(self, width=260, height=260)
        self.board_frame.pack(pady=10)
        
        for i in range(3):
            button_row = []
            for j in range(3):
                btn = ctk.CTkButton(
                    self.board_frame, 
                    text="", 
                    font=("Helvetica", 24, "bold"),
                    width=75, 
                    height=75,
                    corner_radius=8,
                    command=lambda r=i, c=j: self.player_click(r, c)
                )
                btn.grid(row=i, column=j, padx=4, pady=4)
                button_row.append(btn)
            self.grid_buttons.append(button_row)
            
        self.status_label = ctk.CTkLabel(self, text="Trạng thái: Sẵn sàng!", font=("Helvetica", 13))
        self.status_label.pack(pady=10)
        
        # Khung chứa các nút chức năng điều khiển
        self.control_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.control_frame.pack(pady=10)
        
        self.shuffle_btn = ctk.CTkButton(self.control_frame, text="Xáo Trộn", width=110, command=self.shuffle_board)
        self.shuffle_btn.grid(row=0, column=0, padx=10)
        
        self.solve_btn = ctk.CTkButton(self.control_frame, text="AI Giải (DFS)", width=110, fg_color="green", hover_color="darkgreen", command=self.click_solve_bfs)
        self.solve_btn.grid(row=0, column=1, padx=10)

        self.update_buttons_display()

    def update_buttons_display(self):
        for i in range(3):
            for j in range(3):
                value = self.current_state[i][j]
                if value == 0:
                    self.grid_buttons[i][j].configure(text="", fg_color="#333333", hover_color="#333333")
                else:
                    self.grid_buttons[i][j].configure(text=str(value), fg_color="#1f538d", hover_color="#2a72bd")

    def player_click(self, r, c):
       
        x_blank, y_blank = find_blank(tuple(tuple(row) for row in self.current_state))
        
        if abs(r - x_blank) + abs(c - y_blank) == 1:
            matrix = [list(row) for row in self.current_state]
            matrix[x_blank][y_blank], matrix[r][c] = matrix[r][c], matrix[x_blank][y_blank]
            self.current_state = matrix
            self.update_buttons_display()
            
            if tuple(tuple(row) for row in self.current_state) == GOAL:
                messagebox.showinfo("Chúc mừng", "Bạn đã tự giải thành công!")

    def shuffle_board(self):
        current = GOAL
        for _ in range(15): # Trượt ngẫu nhiên 15 lần
            neighbors = get_blankcanmoves(current)
            current = random.choice(neighbors)
            
        self.current_state = [list(row) for row in current]
        self.update_buttons_display()
        self.status_label.configure(text="Trạng thái: Đã xáo trộn đề bài mới!")

    def click_solve_bfs(self):
     
        self.status_label.configure(text="Trạng thái: AI đang tính toán...")
        self.update() # Ép giao diện hiển thị chữ ngay lập tức
        
        start_tuple = tuple(tuple(row) for row in self.current_state)
        path_solution = DFS(start_tuple)
        
        if path_solution is not None:
            steps = len(path_solution) - 1
            self.status_label.configure(text=f"Trạng thái: Đang trình diễn lời giải ({steps} bước)...")
            
            self.shuffle_btn.configure(state="disabled")
            self.solve_btn.configure(state="disabled")
            
            self.animate_solution(path_solution)
        else:
            self.status_label.configure(text="Trạng thái: Không tìm thấy lời giải!")

    def animate_solution(self, path):
        """Hàm chạy hoạt ảnh dịch chuyển tự động mượt mà sau mỗi 0.5 giây"""
        if len(path) == 0:
            self.status_label.configure(text="Trạng thái: Hoàn thành! AI giải xong.")
            self.shuffle_btn.configure(state="normal")
            self.solve_btn.configure(state="normal")
            return
            
        next_step = path.pop(0)
        self.current_state = [list(row) for row in next_step]
        self.update_buttons_display()
        
        self.after(500, lambda: self.animate_solution(path))

if __name__ == "__main__":
    app = PuzzleApp()
    app.mainloop()