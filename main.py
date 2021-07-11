from tkinter import *

root = Tk()
root.title("CoVin - Corona Info")
bubbles = []


canvas = Canvas(root, width=350, height=500,bg="lightgrey")
canvas.grid(row=0,column=0,columnspan=3)



class ChatBubble:
    def __init__(self,master,user,message=""):
        if user==1:
            colour="#e64980"
            xpos=50
            ypos=450
            col=1
        else: 
            colour="#ffd700"
            xpos=250
            ypos=450
            col=2
            
        self.master = master
        self.frame = Frame(master)        
        lbl=Label(self.frame, text=message,bg=colour,wraplength=200, anchor=W)
        lbl.pack()
        if user == 1:
            self.window = self.master.create_window(xpos,ypos,anchor=SW,window=self.frame)
            self.master.create_polygon(self.draw_triangle(self.window), fill=colour)
        else:
            self.window= self.master.create_window(xpos,ypos,anchor = SE,window=self.frame)
            self.master.create_polygon(self.draw_triangle_1(self.window), fill=colour)


    def draw_triangle(self,widget):
        global user
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x1, y2 - 10, x1 - 15, y2 - 10, x1, y2

    def draw_triangle_1(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x1, y2 - 10, x1 + 15, y2 - 10, x1, y2
        
        

def send_message(user,message):
    if bubbles:
        canvas.move(ALL, 0, -35)    
    a = ChatBubble(canvas,user,message)
    bubbles.append(a)


def send():
    message=entry.get
    send_message(2,entry.get())
    entry.delete(0,END)
    
send_message(1,"Hello! I am CoVin. I can tell you any information About Corona Virus")
send_message(1,"What is Your Name?")

    
entry = Entry(root,width=50)
entry.grid(row=1,column=0,columnspan=2)
Button(root,text="Send",width=5,command=send).grid(row=1,column=2)
root.mainloop()
