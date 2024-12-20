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

        self.countdown_label = tk.Label(self.root, text="", font=("Helvetica", 10), fg="gray")
        self.countdown_label.pack(pady=5)

    def start_game(self):
        difficulty = self.selected_level.get()
        count = self.levels[difficulty]
        self.numbers_to_memorize = [random.randint(0, 99) for _ in range(count)]

        self.show_numbers()

    def show_numbers(self):
        self.result_label.config(text=" ".join(map(str, self.numbers_to_memorize)), fg="blue")
        self.countdown(3)

    def countdown(self, seconds):
        if seconds > 0:
            self.countdown_label.config(text=f"Числа исчезнут через: {seconds} сек")
            self.root.update()
            self.root.after(1000, self.countdown, seconds - 1)
        else:
            self.countdown_label.config(text="")
            self.result_label.config(text="")
            self.ask_for_numbers()

    def ask_for_numbers(self):
        user_input = []
        for i in range(len(self.numbers_to_memorize)):
            input_window = tk.Toplevel(self.root)
            input_window.title("Ввод числа")

            prompt_label = tk.Label(input_window, text=f"Введите число {i + 1}:", font=("Helvetica", 14))
            prompt_label.pack(pady=10)

            input_entry = tk.Entry(input_window, font=("Helvetica", 14))
            input_entry.pack(pady=10)
            input_entry.focus_set()

            submit_button = tk.Button(input_window, text="ОК", font=("Helvetica", 12), command=lambda: self.get_user_input(input_entry, input_window, user_input))
            submit_button.pack(pady=10)

            self.root.wait_window(input_window)

        self.check_results(user_input)

    def get_user_input(self, input_entry, input_window, user_input):
        try:
            number = int(input_entry.get())
            user_input.append(number)
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число.")
            return
        input_window.destroy()

    def check_results(self, user_input):
        if user_input == self.numbers_to_memorize:
            self.result_label.config(text="Верно! Вы запомнили все числа!", fg="green")
        else:
            self.result_label.config(text=f"Неверно! Правильные числа были: {', '.join(map(str, self.numbers_to_memorize))}", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
