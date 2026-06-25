import customtkinter as ctk

# Настройка внешнего вида
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Создание окна
app = ctk.CTk()
app.title("JSON2Mieru")
app.geometry("700x500")

# Заголовок
title = ctk.CTkLabel(
    app,
    text="JSON2Mieru",
    font=("Segoe UI", 28, "bold")
)
title.pack(pady=30)

# Запуск программы
app.mainloop()