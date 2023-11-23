import socket
import threading
import json
import sympy as sp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO

# 創建一個TCP服務器
def start_tcp_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"TCP Server is listening on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handler, args=(client_socket,))
        client_handler.start()

def handler(client_socket):
    data = client_socket.recv(1024).decode()
    data=json.loads(data)
    if data["function"] == "yyyc":
        result = yyyc_solver(array=data["array"])
        client_socket.send(str(result).encode())
        client_socket.close()

    elif data["function"] == "eyyc":
        result = eyyc_solver(array=data["array"])
        client_socket.send(result.encode())
        client_socket.close()
    
    elif data["function"] == "yyec":
        result = yyec_solver(array=data["array"])
        client_socket.send(result.encode())
        client_socket.close()

    elif data["function"] == "yysc":
        result = yysc_solver(array=data["array"])
        client_socket.send(result.encode())
        client_socket.close()

    else:
        # 創建x和y的值範圍
        x = np.linspace(-5, 5, 400)
        y = np.linspace(-5, 5, 400)

        # 創建一個網格以生成(x, y)坐標對
        X, Y = np.meshgrid(x, y)

        # 計算函數的值
        Z = data["array"][0] * X**data["array"][1] + data["array"][2] * Y**data["array"][3] - data["array"][4]

        # 繪製等值線圖
        plt.contour(X, Y, Z, levels=[0], colors='b')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = buffer.read()
        # print(image_data)
        buffer.close()

        # 發送圖像數據給客戶端
        client_socket.send(image_data)

        # 關閉Socket連接
        client_socket.close()

def yyyc_solver(array):
    return -array[1]/array[0]

def eyyc_solver(array):
    # 定義未知數
    x, y = sp.symbols('x y')

    # 創建方程組
    equations = [
        sp.Eq(array[0]*x + array[1]*y, array[2]),
        sp.Eq(array[3]*x + array[4]*y, array[5])
    ]

    # 解方程組
    solutions = sp.solve(equations, (x, y)) # solutions是JSON格式的
    return f"{solutions[x]} {solutions[y]}"

def yyec_solver(array):
    x = sp.symbols('x')

    # 創建一元二次方程
    equation = sp.Eq(array[0]*x**2 + array[1]*x + array[2], array[3])

    # 解方程
    solutions = sp.solve(equation, x)

    result = ""
    for solution in solutions:
        result+=f"{solution}/"

    return result

def yysc_solver(array):
    x = sp.symbols('x')

    # 創建一元三次方程
    equation = sp.Eq(array[0]*x**3 + array[1]*x**2 + array[2]*x + array[3], array[4]) # 例： 2,3,-4,-5,0

    # 解方程
    solutions = sp.solve(equation, x)
    # print(solutions)

    result = ""
    for solution in solutions:
        result+=f"{solution}/"

    return result

if __name__ == "__main__":
    tcp_server_thread = threading.Thread(target=start_tcp_server, args=(8081,))
    tcp_server_thread.start()

