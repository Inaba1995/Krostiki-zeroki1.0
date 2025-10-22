import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики‑нолики")
        self.window.geometry("400x450")
        self.window.resizable(False, False)

        self.current_player = "X"
        self.buttons = []
        self.moves_count = 0

        # Заголовок
        self.title_label = tk.Label(
            self.window,
            text="Крестики‑нолики",
            font=("Arial", 18, "bold"),
            pady=10
        )
        self.title_label.pack()

        # Информация о текущем игроке
        self.status_label = tk.Label(
            self.window,
            text=f"Ход игрока: {self.current_player}",
            font=("Arial", 12),
            pady=5
        )
        self.status_label.pack()

        # Игровое поле
        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=10)

        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.frame,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=4,
                    height=2,
                    bg="#f0f0f0",
                    activebackground="#e0e0e0",
                    command=lambda r=i, c=j: self.on_click(r, c)
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)

        # Кнопка рестарта
        self.restart_button = tk.Button(
            self.window,
            text="Начать заново",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            command=self.restart_game
        )
        self.restart_button.pack(pady=10, ipadx=10, ipady=5)

    def check_winner(self):
        # Проверка горизонтальных линий
        for i in range(3):
            if (self.buttons[i][0]["text"] ==
                    self.buttons[i][1]["text"] ==
                    self.buttons[i][2]["text"] != ""):
                return self.buttons[i][0]["text"]

        # Проверка вертикальных линий
        for i in range(3):
            if (self.buttons[0][i]["text"] ==
                    self.buttons[1][i]["text"] ==
                    self.buttons[2][i]["text"] != ""):
                return self.buttons[0][i]["text"]

        # Проверка диагоналей
        if (self.buttons[0][0]["text"] ==
                self.buttons[1][1]["text"] ==
                self.buttons[2][2]["text"] != ""):
            return self.buttons[0][0]["text"]

        if (self.buttons[0][2]["text"] ==
                self.buttons[1][1]["text"] ==
                self.buttons[2][0]["text"] != ""):
            return self.buttons[0][2]["text"]

        return None

    def is_board_full(self):
        return self.moves_count == 9

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] != "":
            return

        # Делаем ход
        self.buttons[row][col]["text"] = self.current_player
        self.moves_count += 1

        # Проверяем победителя
        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Игра окончена", f"Игрок {winner} победил!")
            self.disable_buttons()
            return

        # Проверяем ничью
        if self.is_board_full():
            messagebox.showinfo("Игра окончена", "Ничья!")
            self.disable_buttons()
            return

        # Переключаем игрока
        self.current_player = "0" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Ход игрока: {self.current_player}")

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def restart_game(self):
        # Очищаем все кнопки
        for row in self.buttons:
            for button in row:
                button.config(text="", state="normal")

        # Сбрасываем переменные
        self.current_player = "X"
        self.moves_count = 0
        self.status_label.config(text=f"Ход игрока: {self.current_player}")

    def run(self):
        self.window.mainloop()


# Запуск игры
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
