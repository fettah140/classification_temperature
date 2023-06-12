from  tkinter import *
from model_training import my_model_test
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.app_width = 1000
        self.app_height = 600
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.x = (self.width / 2) - (self.app_width / 2)
        self.y = (self.height / 2) - (self.app_height / 2)
        self.geometry(f"{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}")
        self.title("KNN")
        self.resizable(False, False)
        self.canvas=Canvas(self,highlightthickness=0,bg='cyan')
        self.canvas.place(x=0,y=0,width=self.app_width,height=self.height)
        self.background=PhotoImage(file='image/bg.png')
        self.canvas.create_image(0, 0, anchor=NW, image=self.background)
        self.submit_image_before=PhotoImage(file='image/submits.png')
        self.submit_image_after = PhotoImage(file='image/submit_hovers.png')
        self.bt_submit=self.canvas.create_image(660,200,anchor=NW,image=self.submit_image_before)
        self.canvas.tag_bind(self.bt_submit,"<Enter>",self.bt_submit_enter)
        self.canvas.tag_bind(self.bt_submit, "<Leave>", self.bt_submit_Leave)
        self.canvas.tag_bind(self.bt_submit,'<Button-1>',self.result)
        self.entry1 = Entry(self, width=18, highlightthickness=0, background='#B3B3B3',highlightcolor="#B3B3B3", fg="white", font=('underline', 15),highlightbackground='#B3B3B3', foreground="black", bd=0)
        self.entry1.place(x=243, y=159)
        self.entry2 = Entry(self, width=18, highlightthickness=0, background='#B3B3B3',highlightcolor="#B3B3B3", fg="white", font=('underline', 15),highlightbackground='#B3B3B3', foreground="black", bd=0)
        self.entry2.place(x=243, y=237)
        self.entry3 = Entry(self, width=18, highlightthickness=0, background='#B3B3B3',highlightcolor="#B3B3B3", fg="white", font=('underline', 15),highlightbackground='#B3B3B3', foreground="black", bd=0)
        self.entry3.place(x=243, y=315)
        self.radiobutton_image_after = PhotoImage(file='image/checkyess.png')
        self.var = IntVar()
        self.kppv=Radiobutton(self,  value=1,border=0,variable=self.var,highlightthickness=0,bd=0,bg="#2c2c2c",borderwidth=0,command=self.check_val,activebackground="#2c2c2c",activeforeground="#2c2c2c")
        self.kppv.place(x=225,y=404)
    def check_val(self):
        self.data=self.var.get()
        if int(self.data):
            self.label_kppv=Label(self,image=self.radiobutton_image_after,highlightthickness=0,bd=0,border=0,bg="#2c2c2c",borderwidth=0)
            self.label_kppv.place(x=310,y=402)
    def bt_submit_enter(self,e):
        self.canvas.itemconfig(self.bt_submit,image=self.submit_image_after)
    def bt_submit_Leave(self,e):
        self.canvas.itemconfig(self.bt_submit,image=self.submit_image_before)
    def result(self,e):
        try:
            self.val_g = self.entry1.get()
            self.val_f = self.entry2.get()
            self.val_d = self.entry3.get()
            self.res = my_model_test(int(self.val_g), int(self.val_d), int(self.val_f))
            self.label_res= Label(self, text=self.res, bg="#202020", font=("Arial Bold", 22), fg="white")
            self.label_res.place(x=220, y=510)
        except:pass
def main():
    a = App()
    a.mainloop()
if "__main__" == __name__:
    main()
