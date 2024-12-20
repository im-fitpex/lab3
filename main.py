import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра на проверку памяти")

        self.levels = {
            "Легко": 1,
            "Средне": 3,
            "Сложно": 5
        }

        self.numbers_to_memorize = []
        self.selected_level = tk.StringVar(value="Легко")

        # Настройка интерфейса
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        settings_menu = tk.Menu(menu_bar, tearoff=0)
        for level in self.levels:
            settings_menu.add_radiobutton(label=level, variable=self.selected_level, value=level)

        menu_bar.add_cascade(label="Сложность", menu=settings_menu)

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Игра на проверку памяти", font=("Helvetica", 18))
        self.title_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Начать игру", font=("Helvetica", 14), command=self.start_game)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

    def start_game(self):
        difficulty = self.selected_level.get()
        count = self.levels[difficulty]
        self.numbers_to_memorize = [random.randint(0, 99) for _ in range(count)]

        self.show_numbers()

    def show_numbers(self):
        self.result_label.config(text=" ".join(map(str, self.numbers_to_memorize)), fg="blue")
        self.root.update()
        time.sleep(3)
        self.result_label.config(text="")
        self.ask_for_numbers()

    def ask_for_numbers(self):
        user_input = []
        for i in range(len(self.numbers_to_memorize)):
            number = simpledialog.askinteger("Вспомните", f"Введите число {i + 1}:")
            if number is None:
                messagebox.showwarning("Предупреждение", "Вы вышли из игры досрочно!")
                return
            user_input.append(number)

        self.check_results(user_input)

    def check_results(self, user_input):
        if user_input == self.numbers_to_memorize:
            self.result_label.config(text="Верно! Вы запомнили все числа!", fg="green")
        else:
            self.result_label.config(text=f"Неверно! Правильные числа были: {', '.join(map(str, self.numbers_to_memorize))}", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
