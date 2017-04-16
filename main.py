from tkinter import *
from tkinter import messagebox
from random import randint

program=Tk()
program.title("9 Men's Morris")
program.resizable(width=False, height=False)

class parameter:
    def __init__(self):
        self.whoseturn = -1 # 0: x, 1: v
        self.xpp = 0
        self.vpp = 0
        self.xap = 9
        self.vap = 9
        self.state = -1 # 0: add
                        # 1: select
                        # 2: move
                        # 3: remove

global current_parameter
current_parameter = parameter()

def window_center():
    return
    program.update()
    # lines below this:
    x = program.winfo_screenwidth()/2 - program.winfo_width()/2
    y = program.winfo_screenheight()/2 - program.winfo_height()/2
    program.geometry("+%d+%d" % (x, y))
    # referenced from: https://bbs.archlinux.org/viewtopic.php?id=149559
    # author: vadmium
    # modified

def start_interface():
    button1a.grid(row=6, column=1)
    button1d.grid(row=6, column=4)
    button1g.grid(row=6, column=7)
    button2b.grid(row=5, column=2)
    button2d.grid(row=5, column=4)
    button2f.grid(row=5, column=6)
    button3c.grid(row=4, column=3)
    button3d.grid(row=4, column=4)
    button3e.grid(row=4, column=5)    
    button4a.grid(row=3, column=1)
    button4b.grid(row=3, column=2)
    button4c.grid(row=3, column=3)
    button4e.grid(row=3, column=5)
    button4f.grid(row=3, column=6)
    button4g.grid(row=3, column=7)
    button5c.grid(row=2, column=3)
    button5d.grid(row=2, column=4)
    button5e.grid(row=2, column=5)
    button6b.grid(row=1, column=2)
    button6d.grid(row=1, column=4)
    button6f.grid(row=1, column=6)
    button7a.grid(row=0, column=1)
    button7d.grid(row=0, column=4)
    button7g.grid(row=0, column=7)
    coord_1.grid(row=6, column=0)
    coord_2.grid(row=5, column=0)
    coord_3.grid(row=4, column=0)
    coord_4.grid(row=3, column=0)
    coord_5.grid(row=2, column=0)
    coord_6.grid(row=1, column=0)
    coord_7.grid(row=0, column=0)
    coord_a.grid(row=7, column=1)
    coord_b.grid(row=7, column=2)
    coord_c.grid(row=7, column=3)
    coord_d.grid(row=7, column=4)
    coord_e.grid(row=7, column=5)
    coord_f.grid(row=7, column=6)
    coord_g.grid(row=7, column=7)
    state_frame.grid(row=0, column=8, rowspan=9)
    legend_frame.grid(row=8, column=0, columnspan=9)

def op(state, index):
    if state == 0 and place(current_parameter.whoseturn, index):
        if not board_check():
            turn_change()
        board_change()
        state_check()
    if state == 3:
        remove_turn(index)

def remove_turn(index):
    if button_state_list[index] == -1 or current_parameter.whoseturn == button_state_list[index]:
        messagebox.showwarning("", "Not valid selection")
    else:
        button_state_list[index] = -1
        button_checked_list[index] = 0
        current_parameter.state = 0
        if current_parameter.whoseturn == 0:
            button_list[index].config(image=xb_image)
        if current_parameter.whoseturn == 1:
            button_list[index].config(image=vb_image)
        turn_change()
        board_change()
        state_check()

def turn_change():
    if current_parameter.whoseturn == 0:
        current_parameter.whoseturn = 1
        turn_image.config(image=v_image)
        return
    if current_parameter.whoseturn == 1:
        current_parameter.whoseturn = 0
        turn_image.config(image=x_image)
        return

def board_change():
    i=0
    for e in button_list:
        if button_state_list[i] == -1 and current_parameter.whoseturn == 0:
            e.config(image=xb_image)
        if button_state_list[i] == -1 and current_parameter.whoseturn == 1:
            e.config(image=vb_image)
        i+=1

def remove():
    pass

def state_check():
    if current_parameter.state == 0:
        action_image.config(image=a_image)
    if current_parameter.state == 1:
        action_image.config(image=s_image)
    if current_parameter.state == 2:
        action_image.config(image=m_image)
    if current_parameter.state == 3:
        action_image.config(image=r_image)

def board_check():
    if button_state_list[0] == button_state_list[1] and\
        button_state_list[0] == button_state_list[2] and\
        button_state_list[1] == button_state_list[2] and\
        button_state_list[0] != -1 and\
        (button_checked_list[0] == 0 or\
        button_checked_list[1] == 0 or\
        button_checked_list[2] == 0):
        button_checked_list[0] = 1
        button_checked_list[1] = 1
        button_checked_list[2] = 1
        current_parameter.state = 3
        return True
    if button_state_list[3] == button_state_list[4] and\
        button_state_list[3] == button_state_list[5] and\
        button_state_list[4] == button_state_list[5] and\
        button_state_list[3] != -1 and\
        (button_checked_list[3] == 0 or\
        button_checked_list[4] == 0 or\
        button_checked_list[5] == 0):
        button_checked_list[3] = 1
        button_checked_list[4] = 1
        button_checked_list[5] = 1
        current_parameter.state = 3
        return True
    if button_state_list[6] == button_state_list[7] and\
        button_state_list[6] == button_state_list[8] and\
        button_state_list[7] == button_state_list[8] and\
        button_state_list[6] != -1 and\
        (button_checked_list[6] == 0 or\
        button_checked_list[7] == 0 or\
        button_checked_list[8] == 0):
        button_checked_list[6] = 1
        button_checked_list[7] = 1
        button_checked_list[8] = 1
        current_parameter.state = 3
        return True
    if button_state_list[9] == button_state_list[10] and\
        button_state_list[9] == button_state_list[11] and\
        button_state_list[10] == button_state_list[11] and\
        button_state_list[9] != -1 and\
        (button_checked_list[9] == 0 or\
        button_checked_list[10] == 0 or\
        button_checked_list[11] == 0):
        button_checked_list[9] = 1
        button_checked_list[10] = 1
        button_checked_list[11] = 1
        current_parameter.state = 3
        return True
    if button_state_list[12] == button_state_list[13] and\
        button_state_list[12] == button_state_list[14] and\
        button_state_list[13] == button_state_list[14] and\
        button_state_list[12] != -1 and\
        (button_checked_list[12] == 0 or\
        button_checked_list[13] == 0 or\
        button_checked_list[14] == 0):
        button_checked_list[12] = 1
        button_checked_list[3] = 1
        button_checked_list[14] = 1
        current_parameter.state = 3
        return True
    if button_state_list[15] == button_state_list[16] and\
        button_state_list[15] == button_state_list[17] and\
        button_state_list[16] == button_state_list[17] and\
        button_state_list[15] != -1 and\
        (button_checked_list[15] == 0 or\
        button_checked_list[16] == 0 or\
        button_checked_list[17] == 0):
        button_checked_list[15] = 1
        button_checked_list[16] = 1
        button_checked_list[17] = 1
        current_parameter.state = 3
        return True
    if button_state_list[18] == button_state_list[19] and\
        button_state_list[18] == button_state_list[20] and\
        button_state_list[19] == button_state_list[20] and\
        button_state_list[19] != -1 and\
        (button_checked_list[18] == 0 or\
        button_checked_list[19] == 0 or\
        button_checked_list[20] == 0):
        button_checked_list[18] = 1
        button_checked_list[19] = 1
        button_checked_list[20] = 1
        current_parameter.state = 3
        return True
    if button_state_list[21] == button_state_list[22] and\
        button_state_list[21] == button_state_list[23] and\
        button_state_list[22] == button_state_list[23] and\
        button_state_list[21] != -1 and\
        (button_checked_list[21] == 0 or\
        button_checked_list[22] == 0 or\
        button_checked_list[23] == 0):
        button_checked_list[21] = 1
        button_checked_list[22] = 1
        button_checked_list[23] = 1
        current_parameter.state = 3
        return True
    if button_state_list[0] == button_state_list[9] and\
        button_state_list[0] == button_state_list[21] and\
        button_state_list[9] == button_state_list[21] and\
        button_state_list[0] != -1 and\
        (button_checked_list[0] == 0 or\
        button_checked_list[9] == 0 or\
        button_checked_list[21] == 0):
        button_checked_list[0] = 1
        button_checked_list[9] = 1
        button_checked_list[21] = 1
        current_parameter.state = 3
        return True
    if button_state_list[18] == button_state_list[10] and\
        button_state_list[18] == button_state_list[3] and\
        button_state_list[10] == button_state_list[3] and\
        button_state_list[18] != -1 and\
        (button_checked_list[18] == 0 or\
        button_checked_list[10] == 0 or\
        button_checked_list[3] == 0):
        button_checked_list[18] = 1
        button_checked_list[10] = 1
        button_checked_list[3] = 1
        current_parameter.state = 3
        return True
    if button_state_list[15] == button_state_list[11] and\
        button_state_list[15] == button_state_list[6] and\
        button_state_list[11] == button_state_list[6] and\
        button_state_list[15] != -1 and\
        (button_checked_list[11] == 0 or\
        button_checked_list[6] == 0 or\
        button_checked_list[15] == 0):
        button_checked_list[6] = 1
        button_checked_list[11] = 1
        button_checked_list[15] = 1
        current_parameter.state = 3
        return True
    if button_state_list[22] == button_state_list[19] and\
        button_state_list[22] == button_state_list[16] and\
        button_state_list[19] == button_state_list[16] and\
        button_state_list[22] != -1 and\
        (button_checked_list[22] == 0 or\
        button_checked_list[19] == 0 or\
        button_checked_list[16] == 0):
        button_checked_list[16] = 1
        button_checked_list[19] = 1
        button_checked_list[22] = 1
        current_parameter.state = 3
        return True
    if button_state_list[7] == button_state_list[4] and\
        button_state_list[7] == button_state_list[1] and\
        button_state_list[4] == button_state_list[1] and\
        button_state_list[7] != -1 and\
        (button_checked_list[4] == 0 or\
        button_checked_list[7] == 0 or\
        button_checked_list[1] == 0):
        button_checked_list[4] = 1
        button_checked_list[1] = 1
        button_checked_list[7] = 1
        current_parameter.state = 3
        return True
    if button_state_list[17] == button_state_list[12] and\
        button_state_list[17] == button_state_list[8] and\
        button_state_list[12] == button_state_list[8] and\
        button_state_list[17] != -1 and\
        (button_checked_list[17] == 0 or\
        button_checked_list[12] == 0 or\
        button_checked_list[8] == 0):
        button_checked_list[17] = 1
        button_checked_list[12] = 1
        button_checked_list[8] = 1
        current_parameter.state = 3
        return True
    if button_state_list[20] == button_state_list[13] and\
        button_state_list[20] == button_state_list[5] and\
        button_state_list[13] == button_state_list[5] and\
        button_state_list[20] != -1 and\
        (button_checked_list[13] == 0 or\
        button_checked_list[20] == 0 or\
        button_checked_list[5] == 0):
        button_checked_list[20] = 1
        button_checked_list[5] = 1
        button_checked_list[13] = 1
        current_parameter.state = 3
        return True
    if button_state_list[23] == button_state_list[14] and\
        button_state_list[23] == button_state_list[2] and\
        button_state_list[14] == button_state_list[2] and\
        button_state_list[23] != -1 and\
        (button_checked_list[23] == 0 or\
        button_checked_list[14] == 0 or\
        button_checked_list[2] == 0):
        button_checked_list[23] = 1
        button_checked_list[14] = 1
        button_checked_list[2] = 1
        current_parameter.state = 3
        return True
    return False

def place(player, index):
    if player == 0 and button_state_list[index] == -1:
        button_list[index].config(image=x_image)
        button_state_list[index] = player
        if current_parameter.xap>0:
            current_parameter.xap-=1
            current_parameter.xpp+=1
        return True
    if player == 1 and button_state_list[index] == -1:
        button_list[index].config(image=v_image)
        button_state_list[index] = player
        if current_parameter.vap>0:
            current_parameter.vap-=1
            current_parameter.vpp+=1
        return True

v_image = PhotoImage(file="images/v.gif").subsample(2,2)
x_image = PhotoImage(file="images/x.gif").subsample(2,2)
vb_image = PhotoImage(file="images/vb.gif").subsample(2,2)
xb_image = PhotoImage(file="images/xb.gif").subsample(2,2)
a_image = PhotoImage(file="images/a.gif").subsample(2,2)
r_image = PhotoImage(file="images/r.gif").subsample(2,2)
s_image = PhotoImage(file="images/s.gif").subsample(2,2)
m_image = PhotoImage(file="images/m.gif").subsample(2,2)
legend_frame = Frame(program)
a_action_frame = Frame(legend_frame)
a_action_label = Label(a_action_frame, text="Add")
a_action_image = Label(a_action_frame, image=a_image)
a_action_label.pack(side="top")
a_action_image.pack(side="top")
r_action_frame = Frame(legend_frame)
r_action_label = Label(r_action_frame, text="Remove")
r_action_image = Label(r_action_frame, image=r_image)
r_action_label.pack(side="top")
r_action_image.pack(side="top")
s_action_frame = Frame(legend_frame)
s_action_label = Label(s_action_frame, text="Select")
s_action_image = Label(s_action_frame, image=s_image)
s_action_label.pack(side="top")
s_action_image.pack(side="top")
m_action_frame = Frame(legend_frame)
m_action_label = Label(m_action_frame, text="Move")
m_action_image = Label(m_action_frame, image=m_image)
m_action_label.pack(side="top")
m_action_image.pack(side="top")
a_action_frame.pack(side="left")
r_action_frame.pack(side="left")
s_action_frame.pack(side="left")
m_action_frame.pack(side="left")
state_frame = Frame(program)
turn_frame = Frame(state_frame)
turn_label = Label(turn_frame, text="Whose Turn")
turn_image = Label(turn_frame, image=None)
action_frame = Frame(state_frame)
action_label = Label(action_frame, text="Turn Action")
action_image = Label(action_frame, image=None)
action_label.pack(side="top")
action_image.pack(side="top")
turn_label.pack(side="top")
turn_image.pack(side="top")
turn_frame.pack(side="top")
action_frame.pack(side="top")
button1a = Button(image=None, command=lambda: op(current_parameter.state, 0))
button1d = Button(image=None, command=lambda: op(current_parameter.state, 1))
button1g = Button(image=None, command=lambda: op(current_parameter.state, 2))
button2b = Button(image=None, command=lambda: op(current_parameter.state, 3))
button2d = Button(image=None, command=lambda: op(current_parameter.state, 4))
button2f = Button(image=None, command=lambda: op(current_parameter.state, 5))
button3c = Button(image=None, command=lambda: op(current_parameter.state, 6))
button3d = Button(image=None, command=lambda: op(current_parameter.state, 7))
button3e = Button(image=None, command=lambda: op(current_parameter.state, 8))
button4a = Button(image=None, command=lambda: op(current_parameter.state, 9))
button4b = Button(image=None, command=lambda: op(current_parameter.state, 10))
button4c = Button(image=None, command=lambda: op(current_parameter.state, 11))
button4e = Button(image=None, command=lambda: op(current_parameter.state, 12))
button4f = Button(image=None, command=lambda: op(current_parameter.state, 13))
button4g = Button(image=None, command=lambda: op(current_parameter.state, 14))
button5c = Button(image=None, command=lambda: op(current_parameter.state, 15))
button5d = Button(image=None, command=lambda: op(current_parameter.state, 16))
button5e = Button(image=None, command=lambda: op(current_parameter.state, 17))
button6b = Button(image=None, command=lambda: op(current_parameter.state, 18))
button6d = Button(image=None, command=lambda: op(current_parameter.state, 19))
button6f = Button(image=None, command=lambda: op(current_parameter.state, 20))
button7a = Button(image=None, command=lambda: op(current_parameter.state, 21))
button7d = Button(image=None, command=lambda: op(current_parameter.state, 22))
button7g = Button(image=None, command=lambda: op(current_parameter.state, 23))
button_list = [button1a, button1d, button1g,
                button2b, button2d, button2f,
                button3c, button3d, button3e,
                button4a, button4b, button4c,
                button4e, button4f, button4g,
                button5c, button5d, button5e,
                button6b, button6d, button6f,
                button7a, button7d, button7g]
coord_1 = Label(text="1")
coord_2 = Label(text="2")
coord_3 = Label(text="3")
coord_4 = Label(text="4")
coord_5 = Label(text="5")
coord_6 = Label(text="6")
coord_7 = Label(text="7")
coord_a = Label(text="a")
coord_b = Label(text="b")
coord_c = Label(text="c")
coord_d = Label(text="d")
coord_e = Label(text="e")
coord_f = Label(text="f")
coord_g = Label(text="g")
button1a_state = -1
button1d_state = -1
button1g_state = -1
button2b_state = -1
button2d_state = -1
button2f_state = -1
button3c_state = -1
button3d_state = -1
button3e_state = -1
button4a_state = -1
button4b_state = -1
button4c_state = -1
button4e_state = -1
button4f_state = -1
button4g_state = -1
button5c_state = -1
button5d_state = -1
button5e_state = -1
button6b_state = -1
button6d_state = -1
button6f_state = -1
button7a_state = -1
button7d_state = -1
button7g_state = -1
button1a_checked = 0
button1d_checked = 0
button1g_checked = 0
button2b_checked = 0
button2d_checked = 0
button2f_checked = 0
button3c_checked = 0
button3d_checked = 0
button3e_checked = 0
button4a_checked = 0
button4b_checked = 0
button4c_checked = 0
button4e_checked = 0
button4f_checked = 0
button4g_checked = 0
button5c_checked = 0
button5d_checked = 0
button5e_checked = 0
button6b_checked = 0
button6d_checked = 0
button6f_checked = 0
button7a_checked = 0
button7d_checked = 0
button7g_checked = 0
button_state_list = [button1a_state, button1d_state, button1g_state,
                    button2b_state, button2d_state, button2f_state,
                    button3c_state, button3d_state, button3e_state,
                    button4a_state, button4b_state, button4c_state,
                    button4e_state, button4f_state, button4g_state,
                    button5c_state, button5d_state, button5e_state,
                    button6b_state, button6d_state, button6f_state,
                    button7a_state, button7d_state, button7g_state]
button_checked_list = [button1a_checked, button1d_checked, button1g_checked,
                    button2b_checked, button2d_checked, button2f_checked,
                    button3c_checked, button3d_checked, button3e_checked,
                    button4a_checked, button4b_checked, button4c_checked,
                    button4e_checked, button4f_checked, button4g_checked,
                    button5c_checked, button5d_checked, button5e_checked,
                    button6b_checked, button6d_checked, button6f_checked,
                    button7a_checked, button7d_checked, button7g_checked]

start_interface()
window_center()
if randint(1,10)%2 == 0:
    current_parameter.whoseturn = 0 # x
    turn_image.config(image=x_image)
    for e in button_list:
        e.config(image=xb_image)
else:
    current_parameter.whoseturn = 1 # v
    turn_image.config(image=v_image)
    for e in button_list:
        e.config(image=vb_image)
current_parameter.state = 0
action_image.config(image=a_image)
program.mainloop()