from os import error
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv


GUI = Tk()
GUI.title('HW4-โปรแกรมบันทึกค่าใช้จ่าย By itspeem')
GUI.geometry('600x700+500+50')

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

icon_t1 = PhotoImage(file='T1-AddExpense.png')
icon_t2 = PhotoImage(file='T2-Expenselist.png')

Tab.add(T1, text='Add Expense',image=icon_t1,compound='left')
Tab.add(T2, text='Expense List',image=icon_t2,compound='left') 

F1 = Frame(T1)
F1.place(x=100,y=50)
F1.pack()

days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์'}

def Save(event=None):
	expense = v_expense.get()
	price = v_price.get()
	quantity = v_quantity.get()

	if expense  == '':
		print('No Data')
		messagebox.showerror('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
		return
	elif price == '':
		messagebox.showerror('Error','กรุณากรอกข้อมูลราคา')
		return
	elif quantity == '':
			quantity = 1
		
	total = int(price) * int(quantity)

	try:
		total = int(price) * int(quantity)
		print('รายการ：{} ราคา: {} บาท จำนวน: {} รวม: {} บาท'.format(expense,price,quantity,total))
		text = 'รายการ：{} ราคา: {} บาท จำนวน: {} รวม: {} บาท'.format(expense,price,quantity,total)
		v_result.set(text)
		#เครียร์ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')

		

		#บันทึกข้อมูลลง csv
		today = datetime.now().strftime('%a')
		print(today)
		dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		dt = days[today] + '-' + dt
		with open ('savedataHW2.csv','a',encoding='utf-8',newline='') as f:
			fw = csv.writer(f)
			data = [dt,expense,price,quantity]
			fw.writerow(data)
		E1.focus()
	except :
		print('ERROR')
		messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		#message.boxwarrning('Error','กรุณากรอกข้อมูลใหม่')
		#message.boxinfo('Error','กรุณากรอกข้อมูลใหม่')
		
		
	
#กด enter ได้
GUI.bind('<Return>',Save)

FONT1= (None,20)

#--------image-----
main_icon = PhotoImage(file='Monster-icon.png')

Main_icon = Label(F1,image=main_icon)
Main_icon.pack()

#text1
L = ttk.Label(F1,text='รายการ',font=FONT1).pack()
v_expense = StringVar()
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#------

#text2
L = ttk.Label(F1,text='จำนวน',font=FONT1).pack()
v_quantity = StringVar()
E2 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E2.pack()
#-----

#text3
L = ttk.Label(F1,text='ราคา',font=FONT1).pack()
v_price = StringVar()
E3 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E3.pack()
#----
icon_b1 = PhotoImage(file='saveicon.png')

B2 = ttk.Button(F1,text='บันทึก',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)

v_result = StringVar()
v_result.set('ผลลัพธ์')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='red')
result.pack(pady=20)

####################Tab2#################

def read_csv():
	with open('savedataHW2.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr)
	return data



L = ttk.Label(T2,text='ตารางแสดงข้อมูล',font=FONT1).pack(pady=20)

header = ['วัน-เวลา','รายการ','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=13)
resulttable.pack()

for h in header:
	resulttable.heading(h,text=h)

headerwidth = [150,150,80,80,80]
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)

def update_table():
	resulttable.delete(*resulttable.get_children())
	data = read_csv()
	for d in data:
		resulttable.insert('',0,value=d)

update_table()
print('GET: CHILD:',resulttable.get_children())

GUI.bind('<Tab>',lambda x : E2.focus())
GUI.mainloop()
