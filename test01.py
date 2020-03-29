import tkinter as tk
from tkinter import *
from tkinter import messagebox


def write_file(data):
    with open('customer.txt', 'a', encoding='utf8') as f:
        f.write(data + '\n')


def submitButton():
    messagebox.showinfo(title='แสดงข้อความ', message='เพิ่มข้อมูลเรียบร้อย')
    list_data = ','.join([name_title_text.get(), first_name_text.get(), surname_text.get()
                             , gender_text.get(), age_text.get(), tel_text.get()])
    write_file(list_data)
    name_title_text.set('')
    first_name_text.set('')
    surname_text.set('')
    gender_text.set('')
    age_text.set('')
    tel_text.set('')


window = tk.Tk()
window.title('Customer Personal Information')

name_title_text = StringVar()
first_name_text = StringVar()
surname_text = StringVar()
gender_text = StringVar()
age_text = StringVar()
tel_text = StringVar()

name_title_label = tk.Label(text="คำนำหน้าชื่อ").grid(row=0, sticky=E, padx=5, pady=5)
name_title_entry = tk.Entry(textvariable=name_title_text).grid(row=0, column=1, padx=10)

first_name_label = tk.Label(text="ชื่อ").grid(row=1, sticky=E, padx=5, pady=5)
first_name_entry = tk.Entry(textvariable=first_name_text).grid(row=1, column=1, padx=10)

surname_label = tk.Label(text="นามสกุล").grid(row=2, sticky=E, padx=5, pady=5)
surname_entry = tk.Entry(textvariable=surname_text).grid(row=2, column=1, padx=10)

gender_label = tk.Label(text="เพศ").grid(row=3, sticky=E, padx=5, pady=5)
gender_entry = tk.Entry(textvariable=gender_text).grid(row=3, column=1, padx=10)
# r1 = tk.Radiobutton(text="ชาย",value="1").grid(row=3,column=1)
# r2 = tk.Radiobutton(text="หญิง",value="2").grid(row=4,column=1)

age_label = tk.Label(text="อายุ").grid(row=5, sticky=E, padx=5, pady=5)
age_entry = tk.Entry(textvariable=age_text).grid(row=5, column=1)

tel_label = tk.Label(text="เบอร์โทรศัพท์").grid(row=6, sticky=E, padx=5, pady=5)
tel_entry = tk.Entry(textvariable=tel_text).grid(row=6, column=1)

submit = tk.Button(
    text="Submit",
    width=7,
    height=1,
    bg="white",
    bd=4,
    command=submitButton,
)
submit.grid(row=10, columnspan=2, pady=10)

window.mainloop()
