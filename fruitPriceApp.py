import tkinter as tk
#水果价格计算器
class FruitPrice:
    #定义水果价格
    def __init__(self,price_apple,price_strawberry,price_mango):
        self.price_apple = price_apple
        self.price_strawberry = price_strawberry
        self.price_mango = price_mango
        self.totalprice = 0
    #顾客A购买价格函数
    def price_A(self,apple,strawberry):
        total_price  = apple*self.price_apple + strawberry*self.price_strawberry  #A购买苹果和草莓总价
        self.totalprice = total_price
        return total_price
    #顾客B购买价格函数
    def price_B(self,apple,strawberry,mango):
        total_price = apple*self.price_apple + strawberry*self.price_strawberry + mango*self.price_mango #B购买苹果，草莓，芒果总价
        return total_price
    #顾客C购买价格函数
    def price_C(self,apple,strawberry,mango):
        total_price = apple*self.price_apple + strawberry*self.price_strawberry + mango*self.price_mango*0.8 #C购买苹果，草莓，芒果总价,其中芒果价格打8折
        return total_price
    #顾客D购买价格函数
    def price_D(self,apple,strawberry,mango):
        total_price = apple*self.price_apple + strawberry*self.price_strawberry + mango*self.price_mango #D购买苹果，草莓，芒果,计算水果总价
        if total_price < 100: #当水果总价小于100时，返回购买总价为水果总价
            return total_price
        else:   #水果总价大于等于100时，返回购买总价为水果总价减满减价格
            num = total_price / 100
            dele_price = int(num) * 10  #计算满减价格
            total_price = total_price - dele_price  #返回购买价格为水果总价 减去 满减价格
            return total_price

class FruitPriceApp:
    def __init__(self,width = 500,height = 500):
        self.w = width
        self.h = height
        self.title = "水果计算器"
        self.root = tk.Tk(className=self.title)
        self.totalpriceA = tk.StringVar()
        self.totalpriceA.set("")
        self.totalpriceB = tk.StringVar()
        self.totalpriceB.set("")
        self.totalpriceC = tk.StringVar()
        self.totalpriceC.set("")
        self.totalpriceD = tk.StringVar()
        self.totalpriceD.set("")
        self.apple = tk.IntVar()
        self.apple.set(0)
        self.strawberry = tk.IntVar()
        self.strawberry.set(0)
        self.mango = tk.IntVar()
        self.mango.set(0)
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        frame_4 = tk.Frame(self.root)
        frame_5 = tk.Frame(self.root)
        frame_6 = tk.Frame(self.root)
        #菜单
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        fruitPrice = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='FruitPriceCount', menu=fruitPrice)

        groop = tk.Label(frame_1,text = '水果计算器',font=('楷体',12),padx=10,pady=10)
        #顾客A计算价格
        label1 = tk.Label(frame_2,text = '苹果:',font=('楷体',16))
        entry1 = tk.Entry(frame_2,textvariable=self.apple,highlightcolor='Fuchsia',highlightthickness=1,width=5)
        label2 = tk.Label(frame_2, text='草莓:',font=('楷体',16))
        entry2 = tk.Entry(frame_2, textvariable=self.strawberry, highlightcolor='Fuchsia', highlightthickness=1, width=5)
        label3 = tk.Label(frame_2, text='芒果:',font=('楷体',16))
        entry3 = tk.Entry(frame_2, textvariable=self.mango, highlightcolor='Fuchsia', highlightthickness=1, width=5)
        commitA = tk.Button(frame_3,text='计算',font=('楷体',16),fg='red',width=5,height=1,command=self.price_A)
        labelA1 = tk.Label(frame_3,text="  A总价：",font=('楷体',16))
        price_labelA = tk.Label(frame_3, textvariable=self.totalpriceA, font=('楷体',16), width=20)
        #顾客B计算价格
        commitB = tk.Button(frame_4,text='计算',font=('楷体',16),fg='red',width=5,height=1,command=self.price_B)
        labelB1 = tk.Label(frame_4,text="  B总价：",font=('楷体',16))
        price_labelB = tk.Label(frame_4, textvariable=self.totalpriceB, font=('楷体',16), width=20)
        #顾客C计算价格
        commitC = tk.Button(frame_5,text='计算',font=('楷体',16),fg='red',width=5,height=1,command=self.price_C)
        labelC1 = tk.Label(frame_5,text="  C总价：",font=('楷体',16))
        price_labelC = tk.Label(frame_5, textvariable=self.totalpriceC, font=('楷体',16), width=20)
        #顾客D计算价格
        commitD = tk.Button(frame_6,text='计算',font=('楷体',16),fg='red',width=5,height=1,command=self.price_D)
        labelD1 = tk.Label(frame_6,text="  D总价：",font=('楷体',16))
        price_labelD = tk.Label(frame_6, textvariable=self.totalpriceD, font=('楷体',16), width=20)
        #控件布局
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
        frame_5.pack()
        frame_6.pack()
        groop.grid(row = 0,column = 0)
        label1.grid(row = 0,column =0)
        entry1.grid(row = 0,column =1)
        label2.grid(row =0,column = 2)
        entry2.grid(row = 0,column = 3)
        label3.grid(row = 0,column = 4)
        entry3.grid(row = 0,column = 5)
        #A计算
        commitA.grid(row =0,column = 0)
        labelA1.grid(row = 0,column = 1)
        price_labelA.grid(row=0, column=2)
        #B计算
        commitB.grid(row =0,column = 0)
        labelB1.grid(row = 0,column = 1)
        price_labelB.grid(row=0, column=2)
        #C计算
        commitC.grid(row =0,column = 0)
        labelC1.grid(row = 0,column = 1)
        price_labelC.grid(row=0, column=2)
        #D计算
        commitD.grid(row =0,column = 0)
        labelD1.grid(row = 0,column = 1)
        price_labelD.grid(row=0, column=2)

    #定义水果价格
    price = FruitPrice(8,13,20)
    def price_A(self):
        apple = self.apple.get()
        strawberry = self.strawberry.get()
        totalprice = self.price.price_A(apple,strawberry)
        self.totalpriceA.set(totalprice)

    def price_B(self):
        apple = self.apple.get()
        strawberry = self.strawberry.get()
        mango = self.mango.get()
        totalprice = self.price.price_B(apple, strawberry,mango)
        self.totalpriceB.set(totalprice)

    def price_C(self):
        apple = self.apple.get()
        strawberry = self.strawberry.get()
        mango = self.mango.get()
        totalprice = self.price.price_C(apple, strawberry,mango)
        self.totalpriceC.set(int(totalprice))

    def price_D(self):
        apple = self.apple.get()
        strawberry = self.strawberry.get()
        mango = self.mango.get()
        totalprice = self.price.price_D(apple, strawberry,mango)
        self.totalpriceD.set(totalprice)


    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def loop(self):
        # 禁止修改窗口大小
        self.root.resizable(False, False)
        # 窗口居中
        self.center()
        self.root.mainloop()

if __name__ == '__main__':
    #实例一个水果价格计算器
    app = FruitPriceApp()
    app.loop()