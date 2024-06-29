import tkinter as tk
from tkinter import ttk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def init():
  # window
  window = tk.Tk()
  window.title("Graphing Calc")
  window.geometry('800x600')
  
  frame = ttk.Frame(window, style='TFrame')
  frame.pack(fill = 'both', expand = True)

  fig = Figure(figsize=(6,4), dpi=100)
  ax = fig.add_subplot(111)

  # customize bob man
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('center')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  ax.yaxis.set_label_coords(-0.05, 1.02)
  # TODO: fix

  # f=x^2
  x = [xi / 100 for xi in range(0, 100)]
  f = [xi ** 2 for xi in x]

  ax.plot(x, f, label = 'x^2')

  ax.set_xlim(-1, 1)
  ax.set_ylim(-1, 1)

  ax.legend()

  canvas = FigureCanvasTkAgg(fig, master=frame)
  canvas.draw()
  canvas.get_tk_widget().pack(fill='both',expand=True)

  info_frame = ttk.Frame(window, relief='raised', padding="10")
  info_frame.place(x=5, y=5)

  info_label = ttk.Label(info_frame, text='x^2')
  info_label.pack()

#   label = ttk.Label(frame, text='Graphing Calculator')
#   label.grid(row = 1, column = 0, padx = 20)

#   label2 = ttk.Label(frame, text='label 2')
#   label2.grid(row = 2, column = 0)

  return window

def run(window):
  window.mainloop()






  