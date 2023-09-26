# -*- coding:utf-8 -*-
import win32api,time,win32con,tkinter
import threading
import tkinter as tk
import tkinter.messagebox


# 设置初始速度  
init_speed = 1


class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()
        
        self.func = func
        self.args = args
     
        self.setDaemon(True)
        self.start()    # 在这里开始
        
    def run(self):
        self.func(*self.args)

# 压枪函数
def press_mouse(speed):
    while True:
        if win32api.GetKeyState(0x01)<0: #if mouse left button is pressed
        # x , y = win32api.GetCursorPos()
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, speed, 0, 0)
            time.sleep(0.01)



def check_input():  
    try:  
        value = int(entry.get())
        if value <= 100 and value >= 1:
            init_speed = value
            print("speed : " + str(init_speed))
            press_mouse(init_speed)
        else:
            print(value)
            tk.messagebox.showinfo(title="error",message="输入的数字必须在1到100之间")      
        
    except ValueError as e:
        raise ValueError("输入的数字必须在1到100之间")

  
root = tk.Tk()  
root.title("压枪脚本")
root.iconphoto(True,tk.PhotoImage(file='ico.png'))

root.geometry('300x100')
root.resizable(False,False)

label = tk.Label(root, text="压枪速度大小(1~100之间)：")  # 创建一个标签小部件，并设置文本内容  
label.grid(row=0, column=0, padx=1, pady=1)  # 将标签放在第一行第一列，并设置一些填充和对其方式  

label2 = tk.Label(root, text="开启后若失控请按Alt+F4退出来关闭")  # 创建一个标签小部件，并设置文本内容  
label2.grid(row=1, column=0, padx=1, pady=1)  # 将标签放在第一行第一列，并设置一些填充和对其方式  

entry = tk.Entry(root,width=4)
entry.grid(row=0, column=1, padx=5, pady=5)  # 将输入框放在第一行第二列，并设置一些填充  
  
button = tk.Button(root, text="确定", command=lambda :MyThread(check_input))
button.grid(row=0, column=2, padx=10, pady=10)  # 将按钮放在第二行第一列，并设置一些填充 


if __name__=="__main__":
    root.mainloop()


