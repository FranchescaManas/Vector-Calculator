from tkinter import *
from tkinter import messagebox
import sys
import turtle
import math


## DEFAULTS ##
info_v = []
info_d = []
info_a = []
info_x = []
info_y = []
sum_v = 0
rely = .1


## FUNCTIONS ##
def NewData():
	global sum_v
	global info_v
	global info_d
	global info_a
	global info_x
	global info_y
	global rely
	delete = .1
	for object in range(len(info_v)):
		text = " " * 500
		delete += .05
		clear = Label(top)
		clear.configure(text=text)
		clear.place(relx=.45, rely=delete)
	info_v = []
	info_d = []
	info_a = []
	info_x = []
	info_y = []
	draw.clear()
	draw2.clear()
	draw3.clear()
	draw.color('black')
	draw2.penup()
	draw2.home()
	draw2.pendown()
	drawAxis()
	sum_v = 0
	rely = .1


def saveData():
	info = open('impormasyon.txt', 'w')
	info.write("Vector Qty : " + str(info_v) + '\n' + "Direction : " + str(info_d) + '\n'
	           + "Angle : " + str(info_a) + '\n' + "xComponent : " + str(info_x) + '\n' + "yComponent : " + str(info_y))
	info.close()


def hihi(vector, angle):
	global draw3
	if sum_v <= 1:
		draw2.setheading(angle)
		draw2.forward(vector)
		draw2.dot()
	else:
		draw2.setheading(angle)
		draw2.forward(vector)
		draw2.dot()

		if sum_v >= 3:
			draw3.clear()
		else:
			pass
		draw3 = turtle.RawTurtle(fbod_diagram)
		draw3.shape('blank')
		stamp = draw3.stamp()
		draw3.reset()
		draw3.color('Green')
		draw3.setpos(draw2.xcor(), draw2.ycor())
		draw3.pendown()
		draw3.goto(0, 0)


def hehe(vector, angle):
	draw.color('Purple')
	draw.setheading(angle)
	draw.forward(vector)
	draw.home()


def drawAxis():
	draw.penup()
	draw.goto(-100, 0)
	draw.pendown()
	draw.goto(100, 0)

	draw.penup()
	draw.goto(0, -100)
	draw.pendown()
	draw.goto(0, 100)
	draw.home()


def erase():
	ent_vector_qty.delete(0, END)
	ent_angle_qty.delete(0, END)
	selected.set('Choose')
	ent_vector_qty.focus()


def annex():
	global rely
	global sum_v
	try:
		vector = float(ent_vector_qty.get())
		angle = float(ent_angle_qty.get())
		direction = selected.get()
	except:
		messagebox.showinfo('Error', 'Please fill in all required data')
	else:
		pass
	if angle >= 90:
		messagebox.showinfo('Error', 'Angle must not be greater than 89')
	else:
		if direction == drp_direction_list[0]:
			sum_v += 1
			angle = 90
			xcomp = 0
			ycomp = vector

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[1]:
			sum_v += 1
			angle = 0
			xcomp = vector
			ycomp = 0

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)


			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[2]:
			sum_v += 1
			angle = 270
			xcomp = 0
			ycomp = -vector

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[3]:
			sum_v += 1
			angle = 180
			xcomp = -vector
			ycomp = 0

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[4]:
			sum_v += 1
			angle = angle
			xcomp = vector * math.cos(math.radians(angle))
			ycomp = vector * math.sin(math.radians(angle))

			xcomp = round(xcomp, 6)
			ycomp = round(ycomp, 6)

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[5]:
			sum_v += 1
			angle = 90 - angle
			xcomp = vector * math.cos(math.radians(angle))
			ycomp = vector * math.sin(math.radians(angle))

			xcomp = round(xcomp, 6)
			ycomp = round(ycomp, 6)

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[6]:
			sum_v += 1
			angle = 90 + angle
			xcomp = vector * math.cos(math.radians(angle))
			ycomp = vector * math.sin(math.radians(angle))

			xcomp = round(xcomp, 6)
			ycomp = round(ycomp, 6)

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[7]:
			sum_v += 1
			angle = 180 - angle
			xcomp = vector * math.cos(math.radians(angle))
			ycomp = vector * math.sin(math.radians(angle))

			xcomp = round(xcomp, 6)
			ycomp = round(ycomp, 6)

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[8]:
			sum_v += 1
			angle = 180 + angle
			xcomp = vector * math.cos(math.radians(angle))
			ycomp = vector * math.sin(math.radians(angle))

			xcomp = round(xcomp, 6)
			ycomp = round(ycomp, 6)

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[9]:
			sum_v += 1
			angle = 270 - angle
			xcomp = vector * math.cos(math.radians(angle))
			ycomp = vector * math.sin(math.radians(angle))

			xcomp = round(xcomp, 6)
			ycomp = round(ycomp, 6)

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[10]:
			sum_v += 1
			angle = 270 + angle
			xcomp = vector * math.cos(math.radians(angle))
			ycomp = vector * math.sin(math.radians(angle))

			xcomp = round(xcomp, 6)
			ycomp = round(ycomp, 6)

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)

		elif direction == drp_direction_list[11]:
			sum_v += 1
			angle = 360 - angle
			xcomp = vector * math.cos(math.radians(angle))
			ycomp = vector * math.sin(math.radians(angle))

			xcomp = round(xcomp, 6)
			ycomp = round(ycomp, 6)

			s_v = str(vector)
			s_a = str(angle)
			s_xc = str(xcomp)
			s_yc = str(ycomp)

			rely +=.05
			info_v.append(s_v)
			info_d.append(direction)
			info_a.append(s_a)
			info_x.append(s_xc)
			info_y.append(s_yc)

			caca_v = Label(top, text = vector)
			caca_v.place(relx = .45, rely = rely)
			caca_d = Label(top, text = direction)
			caca_d.place(relx = .56, rely = rely)
			caca_a = Label(top, text = angle)
			caca_a.place(relx = .645, rely = rely)
			caca_x = Label(top, text = xcomp)
			caca_x.place(relx = .715, rely = rely)
			caca_y = Label(top, text = ycomp)
			caca_y.place(relx = .83, rely = rely)

			hehe(vector, angle)
			hihi(vector, angle)
	erase()


def checker(inp):
	if inp.isdigit():
		return True
	elif inp is "":
		return True
	else:
		messagebox.showinfo("Error", 'Numerical Values Only')
		return False


top = Tk()
# root geometry (dimension x, y : offset: x, y)
top.geometry("872x504+120+50")
top.resizable(0, 0)
top.title('Physics Calculator - Vector Addition')

frame_entry = Frame(top)
frame_entry.place(relx = 0.03, rely = 0.08, relheight = 0.22, relwidth = 0.30)
frame_entry.configure(relief = GROOVE)
frame_entry.configure(borderwidth = "2")
frame_entry.configure(width = 195)

check = top.register(checker)

lbl_vector_qty = Label(frame_entry)
lbl_vector_qty.place(relx = 0.05, rely = 0.1, height = 21, width = 62)
lbl_vector_qty.configure(disabledforeground = "#a3a3a3")
lbl_vector_qty.configure(foreground = "#000000")
lbl_vector_qty.configure(text = '''Vector Qty''')

ent_vector_qty = Entry(frame_entry)
ent_vector_qty.place(relx = 0.38, rely = 0.1, relheight = 0.17, relwidth = 0.29)
ent_vector_qty.configure(background = "white")
ent_vector_qty.configure(disabledforeground = "#a3a3a3")
ent_vector_qty.configure(font = "TkFixedFont")
ent_vector_qty.configure(foreground = "#000000")
ent_vector_qty.configure(insertbackground = "black")
ent_vector_qty.configure(width = 84)
ent_vector_qty.configure(validate = "key", validatecommand = (check, '%P'))

lbl_vector_qty = Label(frame_entry)
lbl_vector_qty.place(relx = 0.04, rely = 0.27, height = 21, width = 62)
lbl_vector_qty.configure(disabledforeground = "#a3a3a3")
lbl_vector_qty.configure(foreground = "#000000")
lbl_vector_qty.configure(text = '''Direction''')

selected = StringVar()
drp_direction_list = ["North", "East", "South", "West", "North of East", \
                      "East of North", "West of North", "North of West", "South of West", \
                      "West of South", "East of South", "South of East"]

drp_choice = OptionMenu(frame_entry, selected, *drp_direction_list)
selected.set('Choose')
drp_choice.place(relx = 0.37, rely = 0.27, relheight = 0.22, relwidth = 0.40)

lbl_angle_qty = Label(frame_entry)
lbl_angle_qty.place(relx = 0.01, rely = 0.43, height = 21, width = 62)
lbl_angle_qty.configure(disabledforeground = "#a3a3a3")
lbl_angle_qty.configure(foreground = "#000000")
lbl_angle_qty.configure(text = '''Angle''')

ent_angle_qty = Entry(frame_entry)
ent_angle_qty.place(relx = 0.38, rely = 0.48, relheight = 0.15, relwidth = 0.12)
ent_angle_qty.configure(background = "white")
ent_angle_qty.configure(disabledforeground = "#a3a3a3")
ent_angle_qty.configure(font = "TkFixedFont")
ent_angle_qty.configure(foreground = "#000000")
ent_angle_qty.configure(insertbackground = "black")
ent_angle_qty.configure(width = 84)
ent_angle_qty.configure(validate = "key", validatecommand = (check, '%P'))

vec_add = Button(frame_entry)
vec_add.configure(text = 'Result')
vec_add.place(relx = 0.45, rely = 0.67, height = 25, width = 54)
vec_add.configure(command = annex)

vec_del = Button(frame_entry)
vec_del.configure(text = 'Cancel')
vec_del.place(relx = 0.70, rely = 0.67, height = 25, width = 54)
vec_del.configure(command = erase)

fbod_diagram = Canvas(top)
fbod_diagram.place(relx = 0.4, rely = 0.39, relheight = 0.5, relwidth = 0.32)
fbod_diagram.configure(background = "white")
fbod_diagram.configure(borderwidth = "2")
fbod_diagram.configure(insertbackground = "black")
fbod_diagram.configure(relief = RIDGE)
fbod_diagram.configure(selectbackground = "#c4c4c4")
fbod_diagram.configure(selectforeground = "black")
fbod_diagram.configure(width = 276)

cvas_diagram = Canvas(top)
cvas_diagram.place(relx = 0.02, rely = 0.39, relheight = 0.5, relwidth = 0.32)
cvas_diagram.configure(background = "white")
cvas_diagram.configure(borderwidth = "2")
cvas_diagram.configure(insertbackground = "black")
cvas_diagram.configure(relief = RIDGE)
cvas_diagram.configure(selectbackground = "#c4c4c4")
cvas_diagram.configure(selectforeground = "black")
cvas_diagram.configure(width = 276)

but_sav = Button(top)
but_sav.configure(text = 'Save')
but_sav.place(relx = 0.78, rely = 0.84, height = 25, width = 54)
but_sav.configure(command = saveData)

but_new = Button(top)
but_new.configure(text = 'New')
but_new.place(relx = 0.85, rely = 0.84, height = 25, width = 54)
but_new.configure(command = NewData)

but_qui = Button(top)
but_qui.configure(text = 'Quit')
but_qui.place(relx = 0.92, rely = 0.84, height = 25, width = 54)
but_qui.configure(command = top.destroy)

lbl_vector_qty = Label(top)
lbl_vector_qty.place(relx = 0.45, rely = 0.1, height = 21, width = 62)
lbl_vector_qty.configure(disabledforeground = "#a3a3a3")
lbl_vector_qty.configure(foreground = "#000000")
lbl_vector_qty.configure(text = '''Vector Qty''')

lbl_direction = Label(top)
lbl_direction.place(relx = 0.55, rely = 0.1, height = 21, width = 62)
lbl_direction.configure(disabledforeground = "#a3a3a3")
lbl_direction.configure(foreground = "#000000")
lbl_direction.configure(text = '''Direction''')

lbl_angle = Label(top)
lbl_angle.place(relx = 0.63, rely = 0.1, height = 21, width = 62)
lbl_angle.configure(disabledforeground = "#a3a3a3")
lbl_angle.configure(foreground = "#000000")
lbl_angle.configure(text = '''Angle''')

lbl_xcomp = Label(top)
lbl_xcomp.place(relx = 0.70, rely = 0.1, height = 21, width = 100)
lbl_xcomp.configure(disabledforeground = "#a3a3a3")
lbl_xcomp.configure(foreground = "#000000")
lbl_xcomp.configure(text = '''xComponent''')

lbl_ycomp = Label(top)
lbl_ycomp.place(relx = 0.815, rely = 0.1, height = 21, width = 100)
lbl_ycomp.configure(disabledforeground = "#a3a3a3")
lbl_ycomp.configure(foreground = "#000000")
lbl_ycomp.configure(text = '''yComponent''')

draw = turtle.RawTurtle(cvas_diagram)
drawAxis()
draw2 = turtle.RawTurtle(fbod_diagram)
ent_vector_qty.focus()

top.mainloop()