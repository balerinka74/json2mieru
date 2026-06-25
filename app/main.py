import json
import re
from urllib.parse import quote

from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk
import pyperclip

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("JSON2Mieru")
app.geometry("800x500")

selected_file = ctk.StringVar(value="Файл не выбран")
result_link = ctk.StringVar(value="")


def convert(data, filename):

    mieru = None

    for outbound in data.get("outbounds", []):

        if outbound.get("type") == "mieru":
            mieru = outbound
            break

    if mieru is None:
        messagebox.showerror(
            "Ошибка",
            "Mieru outbound не найден."
        )
        return

    server = mieru["server"]

    # если имя файла начинается с mieru-,
    # берем домен из имени файла
    name = Path(filename).stem

    m = re.match(r"^mieru-(?:[^-]+-)?(.+)$", name, re.IGNORECASE)

    if m:
        server = m.group(1)

    username = quote(
        str(mieru["username"]),
        safe=""
    )

    password = quote(
        str(mieru["password"]),
        safe=""
    )

    port = mieru["server_port"]

    protocol = mieru.get(
        "transport",
        "TCP"
    )

    multiplexing = mieru.get(
        "multiplexing",
        "MULTIPLEXING_HIGH"
    )

    uri = (
        f"mierus://"
        f"{username}:{password}"
        f"@{server}"
        f"?profile=default"
        f"&port={port}"
        f"&protocol={protocol}"
        f"&multiplexing={multiplexing}"
    )

    result_link.set(uri)


def choose_file():

    filename = filedialog.askopenfilename(
        filetypes=[("JSON", "*.json")]
    )

    if not filename:
        return

    selected_file.set(Path(filename).name)

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    convert(data, filename)


def copy_link():

    if not result_link.get():
        return

    pyperclip.copy(result_link.get())

    messagebox.showinfo(
        "Готово",
        "Ссылка скопирована в буфер обмена."
    )


title = ctk.CTkLabel(
    app,
    text="JSON2Mieru",
    font=("Segoe UI", 28, "bold")
)

title.pack(pady=20)

button = ctk.CTkButton(
    app,
    text="Выбрать JSON",
    command=choose_file
)

button.pack()

label = ctk.CTkLabel(
    app,
    textvariable=selected_file
)

label.pack(pady=10)

textbox = ctk.CTkTextbox(
    app,
    width=700,
    height=150
)

textbox.pack(pady=20)


def update_box(*args):

    textbox.delete("1.0", "end")
    textbox.insert("1.0", result_link.get())


result_link.trace_add("write", update_box)

copy_button = ctk.CTkButton(
    app,
    text="Копировать ссылку",
    command=copy_link
)

copy_button.pack()

app.mainloop()