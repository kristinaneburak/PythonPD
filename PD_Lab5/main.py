import tkinter as tk
from string import StringModule 

def display_documentation(func_doc):
    label.config(text=func_doc)

def on_count_letters():
    display_documentation(StringModule.count_letters.__doc__)

def on_count_words():
    display_documentation(StringModule.count_words.__doc__)

def on_count_vowels():
    display_documentation(StringModule.count_vowels.__doc__)

def on_concatenate_strings():
    display_documentation(StringModule.concatenate_strings.__doc__)

def on_multiply_string():
    display_documentation(StringModule.multiply_string.__doc__)

# Создаем основное окно
window = tk.Tk()
window.title("Function Documentation")

# Создаем кнопки для каждой функции
btn_count_letters = tk.Button(window, text="Count Letters", command=on_count_letters,padx=10, pady=10, font=("Helvetica", 12), foreground='#FFB6C1', background='#98FB98')
btn_count_words = tk.Button(window, text="Count Words", command=on_count_words,padx=10, pady=10, font=("Helvetica", 12), foreground='#FFB6C1', background='#98FB98')
btn_count_vowels = tk.Button(window, text="Count Vowels", command=on_count_vowels,padx=10, pady=10, font=("Helvetica", 12), foreground='#FFB6C1', background='#98FB98')
btn_concatenate_strings = tk.Button(window, text="Concatenate Strings", command=on_concatenate_strings,padx=10, pady=10, font=("Helvetica", 12), foreground='#FFB6C1', background='#98FB98')
btn_multiply_string = tk.Button(window, text="Multiply String", command=on_multiply_string,padx=10, pady=10, font=("Helvetica", 12), foreground='#FFB6C1', background='#98FB98')

# Создаем метку для вывода документации
label = tk.Label(window, text="Select a function to view documentation.")

# Размещаем элементы в окне
btn_count_letters.pack()
btn_count_words.pack()
btn_count_vowels.pack()
btn_concatenate_strings.pack()
btn_multiply_string.pack()
label.pack()

# Запускаем цикл событий
window.mainloop()
