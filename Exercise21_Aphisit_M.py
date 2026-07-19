from tkinter import *
import math

def leftClickButton(event):
    BMI = float(textBoxWeight.get()) / math.pow(float(textBoxHigh.get()) / 100,2)

    if BMI < 18.5:
        status = "ผอมเกินไปนะ (น้ำหนักน้อย)"
    elif BMI < 23:
        status = "หุ่นดีปกติ (สมส่วน)"
    elif BMI < 25:
        status = "ตัวท้วมๆ นะ (น้ำหนักเกิน)"
    elif BMI < 30:
        status = "ตัวอ้วนนะ (น้ำหนักเกินมาก)"
    else:
        status = "ลดน้ำหนักด่วนนน! (น้ำหนักเกิ๊นนนน)"

    labelBMIResult.configure(text=f"{BMI:.2f}")
    labelStatusResult.configure(text=status)

MainWindow = Tk()
labelHigh = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHigh.grid(row=0, column=0)
textBoxHigh = Entry(MainWindow)
textBoxHigh.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.bind("<Button-1>", leftClickButton)
calculateButton.grid(row=2, column=0)
labelBMIResult = Label(MainWindow,text= "BMI Result")
labelBMIResult.grid(row=2, column=1)
labelStatusResult = Label(MainWindow,text= "Status Result")
labelStatusResult.grid(row=3, column=1)
MainWindow.mainloop()