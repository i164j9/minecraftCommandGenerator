from tunnel import Tunnel
import tkinter
from tkinter import *

tk = tkinter

mw = Tk(None,None,'Minecraft Calculator',1)
mw.title("Minecraft Calculator")

#                x   y    z     x   y    z
#mycoordinates=[5318,113,-3326,5323,118,-3872]
#mycoordinates=[5260,50,0, 5255,45,-30000]#north
#mycoordinates=[5242, 45, 0, 5252, 50, 31000]#south
#mycoordinates=[5253, 45, 0, 30000, 50, 10]#east
mycoordinates=[-26400, 45, 0, -30000, 50, 10]#west
t = Tunnel('fill','fill', mycoordinates,'air','glass','w')

# label_bx = tk.Label(mw,text="Beginning X")
# input_bx = tk.Text(mw,width=10,height=1,)

# label_by = tk.Label(mw,text="Beginning Y")
# input_by = tk.Text(mw,width=10,height=1,)

# label_bz = tk.Label(mw,text="Beginning Z")
# input_bz = tk.Text(mw,width=10,height=1,)

# label_ex = tk.Label(mw,text="Ending X")
# input_ex = tk.Text(mw,width=10,height=1,)

# label_ey = tk.Label(mw,text="Ending Y")
# input_ey = tk.Text(mw,width=10,height=1,)

# label_ez = tk.Label(mw,text="Ending Z")
# input_ez = tk.Text(mw,width=10,height=1,)

# label_dir = tk.Label(mw,text="Direction")
# input_dir = tk.Text(mw,width=10,height=1,)

# btn_xit = tk.Button(mw, text='Exit', width=10, height=1, command=mw.destroy,background="red")
# btn_calc = tk.Button(mw, text='Calculate', width=10, height=1, command=mw.destroy,background="green")


# label_bx.grid()
# input_bx.grid()

# label_by.grid()
# input_by.grid()

# label_bz.grid()
# input_bz.grid()

# label_ex.grid()
# input_ex.grid()

# label_ey.grid()
# input_ey.grid()

# label_ez.grid()
# input_ez.grid()

# btn_calc.grid()
# btn_xit.grid()

# mw.mainloop()

'''beginning coordinates ending coordinates
in the order of bx by bz ex ey ez'''


myaxis=[20,5,2000]
# t.calculateTunnel(mycoordinates,'n')
# t.findLongestAxis(myaxis)