import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from serv_to_base import add_serv_to_base

root = tk.Tk()
root.title("ServerControl")
root.geometry("1200x700")
root.resizable(True, True)
root.iconbitmap("Client/icon/server.ico")


#Кнопка настроек
button_width_set = 40
button_height_set = 40

icon_set = Image.open("Client/icon/filer.png")
resized_icon_set = icon_set.copy()
resized_icon_set.thumbnail((button_width_set, button_height_set))
photo_icon_set = ImageTk.PhotoImage(resized_icon_set)

button_settings = tk.Button(root, image=photo_icon_set, command=lambda: settings(), width=button_width_set, height=button_height_set, bg="#FFF", relief="flat", bd=0, highlightthickness=0, highlightcolor="white", highlightbackground="white", activebackground="white", activeforeground="white")
button_settings.place(relx=0.98, rely=0.025, anchor="ne")


#Кнопка добавления сервера
button_width_add = 40
button_height_add = 40

icon_add = Image.open("Client/icon/add.png")
resized_icon_add = icon_add.copy()
resized_icon_add.thumbnail((button_width_add, button_height_add))
photo_icon_add = ImageTk.PhotoImage(resized_icon_add)

button_add_serv = tk.Button(root, image=photo_icon_add, command=lambda: add_serv(), width=button_width_add, height=button_height_add, bg="#FFF", relief="flat", bd=0, highlightthickness=0, highlightcolor="white", highlightbackground="white", activebackground="white", activeforeground="white")
button_add_serv.place(relx=0.93, rely=0.025, anchor="ne")

#Меню добавления сервера
def settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("800x700")
    settings_window.iconbitmap("Client/icon/server.ico")


def add_serv():
    add_serv_window = tk.Toplevel(root)
    add_serv_window.title("Add Server")
    add_serv_window.geometry("400x400")
    add_serv_window.iconbitmap("Client/icon/server.ico")

    name_serv = Entry(add_serv_window, width=35)
    name_serv.place(relx=0.5, rely=0.1, anchor=CENTER)

    ip_serv = Entry(add_serv_window, width=35)
    ip_serv.place(relx=0.5, rely=0.3, anchor=CENTER)

    port_serv = Entry(add_serv_window, width=35)
    port_serv.place(relx=0.5, rely=0.5, anchor=CENTER)

    login_serv = Entry(add_serv_window, width=35)
    login_serv.place(relx=0.5, rely=0.7, anchor=CENTER)

    pass_serv = Entry(add_serv_window, width=35)
    pass_serv.place(relx=0.5, rely=0.9, anchor=CENTER)

    name_serv.insert(0,"Название сервера:")
    ip_serv.insert(0,"IP сервера:")
    port_serv.insert(0,"Порт:")
    login_serv.insert(0,"Логин:")
    pass_serv.insert(0,"Пароль:")

    name_serv.pack(padx=20, pady=20)
    ip_serv.pack(padx=20, pady=20)
    port_serv.pack(padx=20, pady=20)
    login_serv.pack(padx=20, pady=20)
    pass_serv.pack(padx=20, pady=20)

    def on_name_serv_click(event):
        if name_serv.get() == "Название сервера:":
            name_serv.delete(0, END)
    def on_ip_serv_click(event):
        if ip_serv.get() == "IP сервера:":
           ip_serv.delete(0, END)
    def on_port_serv_click(event):
        if port_serv.get() == "Порт:":
          port_serv.delete(0, END)
    def on_login_serv_click(event):
        if login_serv.get() == "Логин:":
           login_serv.delete(0, END)
    def on_pass_serv_click(event):
        if pass_serv.get() == "Пароль:":
           pass_serv.delete(0, END)

    name_serv.bind("<FocusIn>", on_name_serv_click)
    ip_serv.bind("<FocusIn>", on_ip_serv_click)
    port_serv.bind("<FocusIn>", on_port_serv_click)
    login_serv.bind("<FocusIn>", on_login_serv_click)
    pass_serv.bind("<FocusIn>", on_pass_serv_click)

    def on_name_serv_lost_focus(event):
        if not name_serv.get():
            name_serv.insert(0, "Название сервера:")
    def on_ip_serv_lost_focus(event):
        if not ip_serv.get():
            ip_serv.insert(0, "IP сервера:")
    def on_port_serv_lost_focus(event):
        if not port_serv.get():
            port_serv.insert(0, "Порт:")
    def on_login_serv_lost_focus(event):
        if not login_serv.get():
            login_serv.insert(0, "Логин:")
    def on_pass_serv_lost_focus(event):
        if not pass_serv.get():
            pass_serv.insert(0, "Пароль:")

    name_serv.bind("<FocusOut>", on_name_serv_lost_focus)
    ip_serv.bind("<FocusOut>", on_ip_serv_lost_focus)
    port_serv.bind("<FocusOut>", on_port_serv_lost_focus)
    login_serv.bind("<FocusOut>", on_login_serv_lost_focus)
    pass_serv.bind("<FocusOut>", on_pass_serv_lost_focus)

    button_add = tk.Button(add_serv_window, text="Добавить", command=lambda: add_serv_to_base(),)
    button_add.pack()
    button_add.place(relx=0.5, rely=0.9, anchor="s")
root.mainloop()