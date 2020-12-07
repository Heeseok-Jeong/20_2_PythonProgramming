from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import *
from tkinter.filedialog import *
from datetime import datetime
import random

age_group_list = ["0-2 years", "3-10 years", "11-65 years", "> 65 years"]
msmt_site_list = ["Oral", "Ear", "Rectal", "Acillary"]
temperature_range_table = {}
temperature_range_table[age_group_list[0]] = {msmt_site_list[0] : (-1, -1), msmt_site_list[1] : (36.4, 38.0), msmt_site_list[2] : (36.6, 38.0), msmt_site_list[3] : (34.7, 37.3)} 
temperature_range_table[age_group_list[1]] = {msmt_site_list[0] : (35.5, 37.5), msmt_site_list[1] : (36.1, 37.8), msmt_site_list[2] : (36.6, 38.0), msmt_site_list[3] : (35.9, 36.7)} 
temperature_range_table[age_group_list[2]] = {msmt_site_list[0] : (36.4, 37.6), msmt_site_list[1] : (35.9, 37.6), msmt_site_list[2] : (37.0, 38.1), msmt_site_list[3] : (35.2, 36.9)} 
temperature_range_table[age_group_list[3]] = {msmt_site_list[0] : (35.8, 36.9), msmt_site_list[1] : (35.8, 37.5), msmt_site_list[2] : (36.2, 37.3), msmt_site_list[3] : (35.6, 36.3)} 

root = Tk()
root.geometry('600x620')
root.title("Body Temperatur Program")

frame1 = Frame(root, bd = 1)
frame1.pack()

def age_sel():
    label['text'] = 'Age radio button ' + str(age_option.get()) + ' clicked.'

age_label = Label(frame1, text = "Age Groups", font = 'bold')
age_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
age_frame = Frame(frame1)
age_frame.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)
age_option = StringVar(value = -1)
age_r0 = Radiobutton(age_frame, text = age_group_list[0], variable = age_option, value = 0, command = age_sel)
age_r0.grid(row = 0, column = 0)
age_r1 = Radiobutton(age_frame, text = age_group_list[1], variable = age_option, value = 1, command = age_sel)
age_r1.grid(row = 0, column = 1)
age_r2 = Radiobutton(age_frame, text = age_group_list[2], variable = age_option, value = 2, command = age_sel)
age_r2.grid(row = 0, column = 2)
age_r3 = Radiobutton(age_frame, text = age_group_list[3], variable = age_option, value = 3, command = age_sel)
age_r3.grid(row = 0, column = 3)

def site_sel():
    label['text'] = 'Site radio button ' + str(site_option.get()) + ' clicked.'

site_label = Label(frame1, text = "Measurement Site", font = 'bold')
site_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = W)
site_frame = Frame(frame1)
site_frame.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)
site_option = StringVar(value = -1)
site_r0 = Radiobutton(site_frame, text = msmt_site_list[0], variable = site_option, value = 0, command = site_sel)
site_r0.grid(row = 0, column = 0)
site_r1 = Radiobutton(site_frame, text = msmt_site_list[1], variable = site_option, value = 1, command = site_sel)
site_r1.grid(row = 0, column = 1)
site_r2 = Radiobutton(site_frame, text = msmt_site_list[2], variable = site_option, value = 2, command = site_sel)
site_r2.grid(row = 0, column = 2)
site_r3 = Radiobutton(site_frame, text = msmt_site_list[3], variable = site_option, value = 3, command = site_sel)
site_r3.grid(row = 0, column = 3)

body_label = Label(frame1, text = "Body Temperature", font = 'bold')
body_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = W)
body_entry = Entry(frame1, bd = 5)
body_entry.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

frame2 = Frame(root, bd = 1)
frame2.pack()

def random_click():
    global age_option
    global site_option
    age_option.set(random.randrange(0, 4))
    if age_option.get() == "0":
        age_r0.select()
    elif age_option.get() == "1":
        age_r1.select()
    elif age_option.get() == "2":
        age_r2.select()
    else:
        age_r3.select()
    
    site_option.set(random.randrange(0, 4))
    if site_option.get() == "0":
        site_r0.select()
    elif site_option.get() == "1":
        site_r1.select()
    elif site_option.get() == "2":
        site_r2.select()
    else:
        site_r3.select()

    body_entry.delete(0, 'end')
    body_entry.insert(0, round(random.uniform(35, 40), 2))

random_button = Button(frame2, text = "Button to generate random input", command = random_click, width = 50, height = 2)
random_button.pack()

def test_click():
    is_valid_input = False
    global age_option
    global site_option
    body_temp = 0
    if not 0 <= int(age_option.get()) <= 3:
        messagebox.showinfo("Invalid Input", "No age group")
    elif not 0 <= int(site_option.get()) <= 3:
        messagebox.showinfo("Invalid Input", "No measurement site")
    elif not body_entry.get():
        messagebox.showinfo("Invalid Input", "No body temperature")
    else:
        try:
            body_temp = float(body_entry.get())
            is_valid_input = True
        except: #Q4-d
            messagebox.showinfo("Invalid Input", "Non-numeric value body temperature")
        if body_temp < 0: #Q4-d
            messagebox.showinfo("Invalid Input", "Negative value body temperature")
            is_valid_input = False

    if is_valid_input:
        age_group = age_group_list[int(age_option.get())]
        msmt_site = msmt_site_list[int(site_option.get())]
        
        for i in range(4): 
            for j in range(4):
                if age_group_list[i] == age_group and msmt_site_list[j] == msmt_site: 
                    result = ""
                    if temperature_range_table[age_group][msmt_site][0] == -1:
                        result = "Error Combination"
                    elif body_temp < temperature_range_table[age_group][msmt_site][0]:
                        result = "Low"
                    elif temperature_range_table[age_group][msmt_site][0] <= body_temp < temperature_range_table[age_group][msmt_site][1]: 
                        result = "Normal"
                    elif temperature_range_table[age_group][msmt_site][1] <= body_temp:
                        result = "Fever"
                    else: 
                        result = "Error Combination"
                    messagebox.showerror("Result", result)

                    global results_st
                    now = datetime.now()
                    content = str(now) + ", " + age_group + ", " + msmt_site + ", " + str(body_entry.get()) + ", " + result + "\n"
                    results_st.insert('end', content)

                    age_option.set(-1)
                    age_r0.deselect()
                    age_r1.deselect()
                    age_r2.deselect()
                    age_r3.deselect()
                    site_option.set(-1)
                    site_r0.deselect()
                    site_r1.deselect()
                    site_r2.deselect()
                    site_r3.deselect()
                    body_entry.delete(0, 'end')
        

test_button = Button(frame2, text = "Button to test the temperrature", command = test_click, width = 50, height = 2)
test_button.pack()

frame3 = Frame(root, bd = 1)
frame3.pack()

result_label = Label(frame3, text = "Temperature Test Results (Accumulated)")
result_label.pack(anchor = W)
results_st = ScrolledText(frame3)
results_st.pack()

frame4 = Frame(root, bd = 1)
frame4.pack()

def save_click():
    name = asksaveasfilename()
    messagebox.showinfo("Save Result", "Save to : " + name + "\nResults count : " + str(results_st.get(1.0, END).count('\n')-1))
    results_st.delete(1.0, END)
    
errmsg = 'Error!'
save_button = Button(frame4, text = "Button to save the results in a file", command = save_click, width = 50, height = 2)
save_button.pack(fill=X)


label = Label()
label.pack(side = BOTTOM)

root.mainloop()