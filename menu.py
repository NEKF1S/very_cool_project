from customtkinter import *
from PIL import Image, ImageDraw, ImageTk   # Pillow — обов'язково встанови: pip install pillow
from tkinter import filedialog
main_window = CTk()
messages = CTkScrollableFrame(main_window, height = 180)
bottom_frame=CTkFrame(main_window)
message = CTkEntry(bottom_frame, placeholder_text="введіть повідомлення")
send_btn = CTkButton(bottom_frame, text = '➧')
messages.pack(side ='top', fill = 'both')
bottom_frame.pack(side='bottom', fill='both')
button.pack(pady=40)
make_name.pack(pady=20)
window.mainloop()
messages = CTkScrollableFrame(main_window, height = 180)
bottom_frame=CTkFrame(main_window)
message = CTkEntry(bottom_frame, placeholder_text="введіть повідомлення")
send_btn = CTkButton(bottom_frame, text = '➧')
messages.pack(side ='top', fill = 'both')
bottom_frame.pack(side='bottom', fill='both')
window = CTk()
window.geometry("400x400")
window.title("Реєстрація")
button = CTkButton(window, text="Обрати зображення", width = 200)
make_name = CTkEntry(master=window, placeholder_text="Введіть своє ім'я", width = 200, )
def get_name():
    global name
    name = make_name.get()
    main_window.mainloop()



