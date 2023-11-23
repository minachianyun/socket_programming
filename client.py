import tkinter as tk
import socket
import json
from io import BytesIO
from PIL import Image, ImageTk

def subWindow1():
    sw=tk.Toplevel(client_window)
    sw.title("一元一次方程")
    sw.geometry(f"270x100+{(screen_width-270)//2}+{(screen_height-100)//2}")
    sw.resizable(False,False)

    entry1 = tk.Entry(sw)
    entry1.place(x=20,y=10,width=35,height=35)

    label1 = tk.Label(sw, text="x   +", anchor="center", font=("Helvetica", 16))
    label1.place(x=60,y=10,width=50,height=35)

    entry2 = tk.Entry(sw)
    entry2.place(x=120,y=10,width=35,height=35)

    label2 = tk.Label(sw, text="=", anchor="center", font=("Helvetica", 16))
    label2.place(x=170,y=10,width=25,height=35)

    label = tk.Label(sw, text="0", anchor="center", font=("Helvetica", 16))
    label.place(x=200,y=10,width=30,height=35)

    label2 = tk.Label(sw, text="port:", anchor="center", font=("Helvetica", 16))
    label2.place(x=20,y=55,width=50,height=35)

    entry3 = tk.Entry(sw, textvariable="port")
    entry3.place(x=75,y=55,width=60,height=35)

    def send_to_server():
        data={
            "function":"yyyc",
            "array":[int(entry1.get()), int(entry2.get())],
            "port":int(entry3.get())
        }

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('0.0.0.0', data["port"]))
        client_socket.send(json.dumps(data).encode('utf-8'))
        response = client_socket.recv(1024).decode()
        ssw=tk.Toplevel(sw)
        ssw.title("結果")
        ssw.geometry(f"270x100+{(screen_width-270)//2}+{(screen_height-100)//2}")
        ssw.resizable(False,False)
        label3 = tk.Label(ssw, text=f"計算結果為: x = {response}", anchor="center", font=("Helvetica", 16))
        label3.place(x=20,y=10,width=230,height=80)
        client_socket.close()

    bt = tk.Button(sw, text="開始計算", command=send_to_server)
    bt.place(x=155,y=55,width=90,height=35)



def subWindow2():
    sw=tk.Toplevel(client_window)
    sw.title("二元一次方程")
    sw.geometry(f"280x170+{(screen_width-280)//2}+{(screen_height-170)//2}")
    sw.resizable(False,False)

    entry1 = tk.Entry(sw)
    entry1.place(x=20,y=10,width=35,height=35)

    label1 = tk.Label(sw, text="x   +", anchor="center", font=("Helvetica", 16))
    label1.place(x=60,y=10,width=50,height=35)

    entry2 = tk.Entry(sw)
    entry2.place(x=120,y=10,width=35,height=35)

    label2 = tk.Label(sw, text="y   =", anchor="center", font=("Helvetica", 16))
    label2.place(x=170,y=10,width=50,height=35)

    entry3 = tk.Entry(sw)
    entry3.place(x=230,y=10,width=35,height=35)


    entry4 = tk.Entry(sw)
    entry4.place(x=20,y=70,width=35,height=35)

    label3 = tk.Label(sw, text="x   +", anchor="center", font=("Helvetica", 16))
    label3.place(x=60,y=70,width=50,height=35)

    entry5 = tk.Entry(sw)
    entry5.place(x=120,y=70,width=35,height=35)

    label4 = tk.Label(sw, text="y   =", anchor="center", font=("Helvetica", 16))
    label4.place(x=170,y=70,width=50,height=35)

    entry6 = tk.Entry(sw)
    entry6.place(x=230,y=70,width=35,height=35)


    label5 = tk.Label(sw, text="port:", anchor="center", font=("Helvetica", 16))
    label5.place(x=20,y=120,width=50,height=35)

    entry7 = tk.Entry(sw, textvariable="port")
    entry7.place(x=75,y=120,width=60,height=35)

    def send_to_server():
        data={
            "function":"eyyc",
            "array":[int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get()), int(entry6.get())],
            "port":int(entry7.get())
        }

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('0.0.0.0', data["port"]))
        client_socket.send(json.dumps(data).encode("utf-8"))
        response = client_socket.recv(1024).decode().split(" ")
        ssw=tk.Toplevel(sw)
        ssw.title("結果")
        ssw.geometry(f"300x100+{(screen_width-300)//2}+{(screen_height-100)//2}")
        ssw.resizable(False,False)
        label6 = tk.Label(ssw, text=f'計算結果為: x = {response[0]}  y = {response[1]}', anchor="center", font=("Helvetica", 16))
        label6.place(x=20,y=10,width=260,height=80)
        client_socket.close()


    bt = tk.Button(sw, text="開始計算", command=send_to_server)
    bt.place(x=165,y=120,width=100,height=35)

def subWindow3():
    sw=tk.Toplevel(client_window)
    sw.title("一元二次方程")
    sw.geometry(f"345x100+{(screen_width-345)//2}+{(screen_height-100)//2}")
    sw.resizable(False,False)

    entry1 = tk.Entry(sw)
    entry1.place(x=20,y=10,width=35,height=35)

    label1 = tk.Label(sw, text="x\u00B2   +", anchor="center", font=("Helvetica", 16))
    label1.place(x=60,y=10,width=50,height=35)

    entry2 = tk.Entry(sw)
    entry2.place(x=120,y=10,width=35,height=35)

    label2 = tk.Label(sw, text="x   +", anchor="center", font=("Helvetica", 16))
    label2.place(x=160,y=10,width=50,height=35)

    entry3 = tk.Entry(sw)
    entry3.place(x=220,y=10,width=35,height=35)

    label3 = tk.Label(sw, text="=", anchor="center", font=("Helvetica", 16))
    label3.place(x=260,y=10,width=25,height=35)

    entry4 = tk.Entry(sw)
    entry4.place(x=290,y=10,width=35,height=35)

    label4 = tk.Label(sw, text="port:", anchor="center", font=("Helvetica", 16))
    label4.place(x=50,y=55,width=50,height=35)

    entry5 = tk.Entry(sw, textvariable="port")
    entry5.place(x=110,y=55,width=60,height=35)

    def send_to_server():
        data={
            "function":"yyec",
            "array":[int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get())],
            "port":int(entry5.get())
        }

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('0.0.0.0', data["port"]))
        client_socket.send(json.dumps(data).encode("utf-8"))
        response = client_socket.recv(1024).decode().split("/")
        ssw=tk.Toplevel(sw)
        ssw.title("結果")
        ssw.geometry(f"200x250+{(screen_width-200)//2}+{(screen_height-250)//2}")
        ssw.resizable(False,False)
        label5 = tk.Label(ssw, text=f'計算結果為:\n\n x1 = {response[0]}\n\nx2 = {response[1]}', anchor="center", font=("Helvetica", 16))
        label5.place(x=20,y=10,width=160,height=230)
        client_socket.close()

    bt = tk.Button(sw, text="開始計算", command=send_to_server)
    bt.place(x=190,y=55,width=90,height=35)

def subWindow4():
    sw=tk.Toplevel(client_window)
    sw.title("一元三次方程")
    sw.geometry(f"445x100+{(screen_width-445)//2}+{(screen_height-100)//2}")
    sw.resizable(False,False)

    entry1 = tk.Entry(sw)
    entry1.place(x=20,y=10,width=35,height=35)

    label1 = tk.Label(sw, text="x\u00B3   +", anchor="center", font=("Helvetica", 16))
    label1.place(x=60,y=10,width=50,height=35)

    entry2 = tk.Entry(sw)
    entry2.place(x=120,y=10,width=35,height=35)

    label2 = tk.Label(sw, text="x\u00B2   +", anchor="center", font=("Helvetica", 16))
    label2.place(x=160,y=10,width=50,height=35)

    entry3 = tk.Entry(sw)
    entry3.place(x=220,y=10,width=35,height=35)

    label3 = tk.Label(sw, text="x   +", anchor="center", font=("Helvetica", 16))
    label3.place(x=260,y=10,width=50,height=35)

    entry4 = tk.Entry(sw)
    entry4.place(x=320,y=10,width=35,height=35)

    label4 = tk.Label(sw, text="=", anchor="center", font=("Helvetica", 16))
    label4.place(x=360,y=10,width=25,height=35)

    entry5 = tk.Entry(sw)
    entry5.place(x=390,y=10,width=35,height=35)

    label5 = tk.Label(sw, text="port:", anchor="center", font=("Helvetica", 16))
    label5.place(x=100,y=55,width=50,height=35)

    entry6 = tk.Entry(sw, textvariable="port")
    entry6.place(x=160,y=55,width=60,height=35)

    def send_to_server():
        data={
            "function":"yysc",
            "array":[int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get())],
            "port":int(entry6.get())
        }

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('0.0.0.0', data["port"]))
        client_socket.send(json.dumps(data).encode("utf-8"))
        response = client_socket.recv(1024).decode().split("/")
        ssw=tk.Toplevel(sw)
        ssw.title("結果")
        ssw.geometry(f"200x250+{(screen_width-200)//2}+{(screen_height-250)//2}")
        ssw.resizable(False,False)
        label6 = tk.Label(ssw, text=f'計算結果為:\n\n x1 = {response[0]}\n\nx2 = {response[1]}\n\nx3 = {response[2]}', anchor="center", font=("Helvetica", 16))
        label6.place(x=20,y=10,width=160,height=230)
        client_socket.close()

    bt = tk.Button(sw, text="開始計算", command=send_to_server)
    bt.place(x=250,y=55,width=90,height=35)

def subWindow5():
    sw=tk.Toplevel(client_window)
    sw.title("繪製函數圖")
    sw.geometry(f"385x100+{(screen_width-385)//2}+{(screen_height-100)//2}")
    sw.resizable(False,False)

    entry1 = tk.Entry(sw)
    entry1.place(x=20,y=10,width=35,height=35)

    label1 = tk.Label(sw, text="x^", anchor="center", font=("Helvetica", 16))
    label1.place(x=60,y=10,width=30,height=35)

    entry2 = tk.Entry(sw)
    entry2.place(x=95,y=10,width=35,height=35)

    label2 = tk.Label(sw, text="+", anchor="center", font=("Helvetica", 16))
    label2.place(x=135,y=10,width=30,height=35)
    
    entry3 = tk.Entry(sw)
    entry3.place(x=170,y=10,width=35,height=35)

    label3 = tk.Label(sw, text="y^", anchor="center", font=("Helvetica", 16))
    label3.place(x=210,y=10,width=30,height=35)

    entry4 = tk.Entry(sw)
    entry4.place(x=245,y=10,width=35,height=35)

    label4 = tk.Label(sw, text="=", anchor="center", font=("Helvetica", 16))
    label4.place(x=290,y=10,width=30,height=35)

    entry5 = tk.Entry(sw)
    entry5.place(x=330,y=10,width=35,height=35)

    label5 = tk.Label(sw, text="port:", anchor="center", font=("Helvetica", 16))
    label5.place(x=70,y=55,width=50,height=35)

    entry6 = tk.Entry(sw, textvariable="port")
    entry6.place(x=140,y=55,width=60,height=35)

    def send_to_server():
        data={
            "function":"draw",
            "array":[int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get())],
            "port":int(entry6.get())
        }

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('0.0.0.0', data["port"]))
        client_socket.send(json.dumps(data).encode("utf-8"))
        response = client_socket.recv(10000000)
        # print(response)

        # 將二進製數據轉換為圖像
        image = Image.open(BytesIO(response))
        photo = ImageTk.PhotoImage(image)

        ssw=tk.Toplevel(sw)
        ssw.title("結果")
        ssw.geometry(f"800x800+{(screen_width-800)//2}+{(screen_height-800)//2}")
        ssw.resizable(False,False)
        label6 = tk.Label(ssw, image=photo)
        label6.image = photo
        label6.place(x=0,y=0,width=800,height=800)
        client_socket.close()

    bt = tk.Button(sw, text="開始繪圖", command=send_to_server)
    bt.place(x=220,y=55,width=90,height=35)

# 創建GUI窗口
client_window = tk.Tk()
client_window.title("Client")

# Get the screen width and height
screen_width = client_window.winfo_screenwidth()
screen_height = client_window.winfo_screenheight()

# Calculate the center position
x = (screen_width - 820) // 2  # Centered horizontally
y = (screen_height - 100) // 2  # Centered vertically

client_window.geometry(f"820x100+{x}+{y}")
client_window.resizable(False,False)

bt1 = tk.Button(text="一元一次方程", command=subWindow1)
bt1.place(x=10,y=10,width=150,height=80)

bt2 = tk.Button(text="二元一次方程", command=subWindow2)
bt2.place(x=170,y=10,width=150,height=80)

bt3 = tk.Button(text="一元二次方程", command=subWindow3)
bt3.place(x=330,y=10,width=150,height=80)

bt4 = tk.Button(text="一元三次方程", command=subWindow4)
bt4.place(x=490,y=10,width=150,height=80)

bt5 = tk.Button(text="繪製函數圖", command=subWindow5)
bt5.place(x=650,y=10,width=150,height=80)

client_window.mainloop()

