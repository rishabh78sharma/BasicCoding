import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser,filedialog,messagebox
import os

main_application=tk.Tk()
main_application.geometry('1200x800')
main_application.title('first gui')




################################################## main menu ##################################################
#-------------------------------------------------- end main menu --------------------------------------------#
main_menu=tk.Menu()
#file icons
new_icon=tk.PhotoImage(file='D:hari/addfile.png')
open_icon=tk.PhotoImage(file='D:/hari/folder.png')
save_icon=tk.PhotoImage(file='D:/hari/save.png')
save_as_icon=tk.PhotoImage(file='D:/hari/saveas.png')
exit_icon=tk.PhotoImage(file='D:/hari/exit.png')

file=tk.Menu(main_menu, tearoff=False)

file.add_command(label='New',image=new_icon,compound=tk.LEFT)
file.add_command(label='Open',image=open_icon,compound=tk.LEFT)
file.add_command(label='Save',image=save_icon,compound=tk.LEFT)
file.add_command(label='Saveas',image=save_as_icon,compound=tk.LEFT)
file.add_command(label='Save',image=exit_icon,compound=tk.LEFT)
edit=tk.Menu(main_menu, tearoff=False)
view=tk.Menu(main_menu, tearoff=False)
color_theme=tk.Menu(main_menu, tearoff=False)
#cascade
main_menu.add_cascade(label='file',menu=file)
main_menu.add_cascade(label='edit',menu=edit)
main_menu.add_cascade(label='view',menu=view)
main_menu.add_cascade(label='color Theme',menu=color_theme)


################################################## tool bar ##################################################
#-------------------------------------------------- end tool bar --------------------------------------------#



################################################## text editor ##################################################
#-------------------------------------------------- end text editor --------------------------------------------#




################################################## main menu functionalily ##################################################
#-------------------------------------------------- end main menu functionality --------------------------------------------#




################################################## main menu ##################################################
#-------------------------------------------------- end main menu --------------------------------------------#


main_application.config(menu=main_menu)
main_application.mainloop()