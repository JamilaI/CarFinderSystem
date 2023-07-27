import tkinter as tk
from tkinter import *
from tkinter import messagebox
from experta import *
import random
from PIL import Image, ImageTk

root = tk.Tk()  # create root window
root.iconphoto(False, tk.PhotoImage(file='./icons/car.png'))

carResult = ""
country = StringVar()
carType = StringVar()
fuel = StringVar()
money = StringVar()


class Welcome(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        yield Fact(action="find_car")

    # **** FACTS *******

    # type
    @Rule(Fact(action='find_car'), NOT(Fact(typeCar=W())), salience=1)
    def carType(self):
        self.declare(Fact(typeCar=carType.get()))  # first

    # factory country
    @Rule(Fact(action='find_car'), NOT(Fact(manifactor=W())), salience=1)
    def carManifactor(self):
        self.declare(Fact(manifactor=country.get()))  # first

    # fuel
    @Rule(Fact(action='find_car'), NOT(Fact(fuel=W())), salience=1)
    def carFuel(self):
        self.declare(Fact(fuel=fuel.get()))

    # Prices
    @Rule(Fact(action='find_car'), NOT(Fact(price=W())), salience=1)
    def carPrice(self):
        self.declare(Fact(price=money.get()))

    # **** RULES *******

    @Rule(Fact(action='find_car'), Fact(typeCar="Station"), Fact(manifactor="China"), Fact(fuel="electric"))
    def r1(self):
        self.declare(Fact(carMarque="Peguot"))

    @Rule(Fact(action='find_car'), Fact(typeCar="popular cars"), Fact(manifactor="China"), Fact(fuel="electric"))
    def r2(self):
     self.declare(Fact(carMarque="Peguot"))

    @Rule(Fact(action='find_car'), Fact(typeCar="High range"), Fact(manifactor="China"),Fact(fuel="electric"))
    def r3(self):
      self.declare(Fact(carMarque="Peguot"))

    @Rule(Fact(action='find_car'), Fact(typeCar="Station"), Fact(manifactor="Japan"))
    def r4(self):
        self.declare(Fact(carMarque="toyota"))

    @Rule(Fact(action='find_car'), Fact(typeCar="High range"), Fact(manifactor="Germany"))
    def r5(self):
        self.declare(Fact(carMarque="mercides"))

    @Rule(Fact(action='find_car'), Fact(carMarque="mercides"), Fact(price="[180-600]"))
    def r6(self):
        self.declare(Fact(car="mercidez_Luxury"))

    @Rule(Fact(action='find_car'), Fact(carMarque="Peguot"), Fact(price="[70-180]"))
    def r7(self):
        self.declare(Fact(car="Peugot_Luxury"))

    @Rule(Fact(action='find_car'), Fact(carMarque="mercides"), Fact(price="[70-180]"))
    def r8(self):
        self.declare(Fact(car="mercides-class-A"))

    @Rule(Fact(action='find_car'), Fact(typeCar="High range"), Fact(manifactor="USA"), Fact(fuel="electric"))
    def r9(self):
        self.declare(Fact(carMarque="Tesla"))

    @Rule(Fact(action='find_car'), Fact(carMarque="Tesla"), Fact(price="[70-180]"))
    def r10(self):
        self.declare(Fact(car="Tesla model 3"))

    @Rule(Fact(action='find_car'), Fact(typeCar="sport"), Fact(manifactor="Germany"), Fact(fuel="petrol"))
    def r11(self):
        self.declare(Fact(carMarque="Audi"))

    @Rule(Fact(action='find_car'), Fact(carMarque="Audi"), Fact(price="[180-600]"))
    def r12(self):
        self.declare(Fact(car="Audi_Rs3"))

    @Rule(Fact(action='find_car'), Fact(carMarque="toyota"), Fact(price="[30-70]"))
    def r13(self):
        self.declare(Fact(car="Toyota Hilux"))

    @Rule(Fact(action='find_car'), Fact(carMarque="mercides"), Fact(price="[30-70]"))
    def r14(self):
        self.declare(Fact(car="merz_e63amg"))

    @Rule(Fact(action='find_car'), Fact(carMarque="mercides"), Fact(price="[180-600]"))
    def r15(self):
        self.declare(Fact(car="mercidez_Luxury"))

    @Rule(Fact(action='find_car'), Fact(typeCar="popular cars"), Fact(manifactor="Germany"))
    def r16(self):
        self.declare(Fact(carMarque="mercides"))

    @Rule(Fact(action='find_car'), Fact(typeCar="sport"), Fact(manifactor="Germany"))
    def r17(self):
        self.declare(Fact(carMarque="mercides"))

    @Rule(Fact(action='find_car'), Fact(carMarque="Peguot"), Fact(price="[180-600]"))
    def r18(self):
        self.declare(Fact(car="Peguot_sport"))

    @Rule(Fact(action='find_car'), Fact(carMarque="Peguot"), Fact(price="[30-70]"))
    def r19(self):
        self.declare(Fact(car="Peugot-E-208"))

    @Rule(Fact(action='find_car'), Fact(typeCar="sport"), Fact(manifactor="China"), Fact(fuel="electric"))
    def r20(self):
        self.declare(Fact(carMarque="Peguot"))

    @Rule(Fact(action='find_car'), Fact(typeCar="High range"), Fact(manifactor="China"), Fact(fuel="electric"))
    def r21(self):
        self.declare(Fact(carMarque="Peguot"))

    @Rule(Fact(action='find_car'), Fact(typeCar="sport"), Fact(manifactor="Japan"))
    def r22(self):
        self.declare(Fact(carMarque="toyota"))

    @Rule(Fact(action='find_car'), Fact(typeCar="High range"), Fact(manifactor="Japan"))
    def r23(self):
        self.declare(Fact(carMarque="toyota"))

    @Rule(Fact(action='find_car'), Fact(typeCar="popular cars"), Fact(manifactor="Japan"))
    def r23(self):
        self.declare(Fact(carMarque="toyota"))

    @Rule(Fact(action='find_car'), Fact(carMarque="toyota"), Fact(price="[70-180]"))
    def r24(self):
        self.declare(Fact(car="Camry_popular"))

    @Rule(Fact(action='find_car'), Fact(carMarque="toyota"), Fact(price="[180-600]"))
    def r25(self):
        self.declare(Fact(car="Camry_Luxury"))

    @Rule(Fact(action='find_car'), Fact(typeCar="popular cars"), Fact(manifactor="USA"), Fact(fuel="electric"))
    def r26(self):
        self.declare(Fact(carMarque="Tesla"))

    @Rule(Fact(action='find_car'), Fact(typeCar="station"), Fact(manifactor="USA"), Fact(fuel="electric"))
    def r27(self):
        self.declare(Fact(carMarque="Tesla"))

    @Rule(Fact(action='find_car'), Fact(typeCar="sport"), Fact(manifactor="USA"), Fact(fuel="electric"))
    def r28(self):
        self.declare(Fact(carMarque="Tesla"))

    @Rule(Fact(action='find_car'), Fact(carMarque="Tesla"), Fact(price="[180-600]"))
    def r29(self):
        self.declare(Fact(car="tesla_2023_X"))

    @Rule(Fact(action='find_car'), Fact(carMarque="Tesla"), Fact(price="[30-70]"))
    def r30(self):
        self.declare(Fact(car="tesla_Remake"))

    @Rule(Fact(action='find_car'), Fact(typeCar="station"), Fact(manifactor="USA"), Fact(fuel="electric"))
    def r31(self):
        self.declare(Fact(carMarque="Tesla"))

    @Rule(Fact(action='find_car'), Fact(typeCar="station"), Fact(manifactor="Germany"), Fact(fuel="petrol"))
    def r32(self):
        self.declare(Fact(carMarque="Audi"))

    @Rule(Fact(action='find_car'), Fact(typeCar="High range"), Fact(manifactor="Germany"), Fact(fuel="petrol"))
    def r33(self):
        self.declare(Fact(carMarque="Audi"))

    @Rule(Fact(action='find_car'), Fact(typeCar="popular cars"), Fact(manifactor="Germany"), Fact(fuel="petrol"))
    def r34(self):
        self.declare(Fact(carMarque="Audi"))

    @Rule(Fact(action='find_car'), Fact(carMarque="Audi"), Fact(price="[70-180]"))
    def r35(self):
        self.declare(Fact(car="Audi a4"))

    @Rule(Fact(action='find_car'), Fact(carMarque="Audi"), Fact(price="[30-70]"))
    def r36(self):
        self.declare(Fact(car="Audi rs"))




    @Rule(Fact(action='find_car'), Fact(car=MATCH.car), salience=-998)
    def bestCar(self, car):
        print("\n Your preferred car is " + car + "\n")
        global carResult
        carResult = car

    @Rule(Fact(action='find_car'), NOT(Fact(car=MATCH.car)), salience=-999)
    def not_bestCar(self):
        print("need more info to make a decision\n")
        global carResult
        carResult = "no idea"


# GUI coding, for background coloring, texts and title.

backgroundvalue = "#004643"  # dark green background
bgFrames = "#194D33"  # green color for the boxes
textColors = "#1B1B1B"  # black for the texts above the options
optionsColor = "#8EA604"  # olive green color the option color of the questios
titleColor = "#fffffe"  # white color for the above titles
engine = Welcome()


def openResultWindow():
    engine.reset()
    engine.run()

    windowRes = Tk()
    windowRes.title = ""
    windowRes.iconphoto(False, PhotoImage(master=windowRes, file='./icons/car.png'))

    # specify the max size and min size that the window can expand to
    windowRes.maxsize(700, 500)
    windowRes.config(bg=backgroundvalue)  # specify background color
    # windowRes.maxsize(1000, 1000)

    # Create left and right frames

    headFrame = Frame(windowRes, width=600, height=100, bg=backgroundvalue)
    headFrame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    BodyFrame = Frame(windowRes, width=700, height=300, bg=backgroundvalue)
    BodyFrame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    if (carResult == "no idea"):

        # generating random car from the popular list:
        carName = random.choice(
            ["Toyota prado", "Chery Tiggo 2"])

        Label(headFrame, text="Sorry, we couldn't find a car in our system base with your preferences",
              font=("arial italic", 10), bg=backgroundvalue, fg=titleColor).grid(row=0, column=1, padx=5, pady=5)
        Label(headFrame, text="but we recommend you \t", font=(
            "arial italic", 10), bg=backgroundvalue, fg=titleColor).grid(row=1, column=1, padx=5, pady=5)
        title1 = Label(headFrame, text=carName, font=(
            "arial italic", 18, "bold"), bg=backgroundvalue, fg=titleColor).grid(row=3, column=1, padx=5, pady=5)
        resImage = PhotoImage(
            master=BodyFrame, file="./images/" + carName + ".gif").subsample(2, 2)
    else:
        Label(headFrame, text="Based on your choices, we recommend \t\t", font=(
            "arial italic", 10), bg=backgroundvalue, fg=titleColor).grid(row=0, column=1, padx=5, pady=5)
        title1 = Label(headFrame, text=carResult, font=(
            "arial italic", 18, "bold"), bg=backgroundvalue, fg=titleColor).grid(row=2, column=1, padx=5, pady=5)
        resImage = PhotoImage(
            master=BodyFrame, file="./images/" + carResult + ".gif").subsample(2, 2)

    Label(BodyFrame, image=resImage).grid(row=0, column=1, padx=20, pady=20)
    windowRes.mainloop()


root.title("Car Finder")  # title of the GUI window
root.maxsize(1000, 1000)  # specify the max size the window can expand to
root.config(bg=backgroundvalue)  # specify background color

# Create left and right frames

headFrame = tk.Frame(root, width=600, height=150, bg=backgroundvalue)
headFrame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

# to set the title with font: Times roman, 36 size, identify its color and  to place a widget
# like a Frame or Label at row 0 and column 1 of the parent widget. padx and pady is the pixels on x and y axes
title1 = tk.Label(headFrame, text="  Car Finder ", font=(
    "Times", 36, "bold"), bg=backgroundvalue, fg=titleColor).grid(row=0, column=1, padx=5, pady=5)

subTitle2 = tk.Label(headFrame, text="", font=(
    "Times", 15), bg=backgroundvalue, fg=backgroundvalue).grid(row=2, column=1, padx=5, pady=5)
subTitle1 = tk.Label(headFrame, text="\tDo you want to find the right car for you?"
                                     "\nHere is Car Finder", font=(
    "Times", 20), bg=backgroundvalue, fg=titleColor).grid(row=1, column=1, padx=5, pady=5)

subTitle2 = tk.Label(headFrame, text="", font=(
    "Times", 15), bg=backgroundvalue, fg=backgroundvalue).grid(row=2, column=1, padx=5, pady=5)

BodyFrame = tk.Frame(root, width=600, height=400, bg=backgroundvalue)
BodyFrame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

left_frame = tk.Frame(BodyFrame, width=400, height=400, bg=bgFrames)
left_frame.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

right_frame = tk.Frame(BodyFrame, width=400, height=400, bg=bgFrames)
right_frame.grid(row=1, column=1, padx=20, pady=5, sticky="nsew")

footerFrame = tk.Frame(root, width=600, height=150, bg=backgroundvalue)
footerFrame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

# title left frame
tk.Label(BodyFrame, text="Choose from the options that suits you:", wraplength=350, font=("Times", 15),
         bg=backgroundvalue, fg=textColors). \
    grid(row=0, column=0, padx=5, pady=5, sticky="w")

# group1
# factory country China / Germany / Japan / USA
group1 = Frame(left_frame, width=400, height=185, bg=bgFrames)
group1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Create the first group of radio buttons
Label(group1, text="Manufacturing country\t", bg=bgFrames, fg=textColors, font=(
    "arial", 16, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

country.set(None)

Radiobutton(group1, text="China", variable=country, value="China", bg=bgFrames, fg=optionsColor,
            justify="left", borderwidth=3, relief="flat") \
    .grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

Radiobutton(group1, text="Germany", justify="left", variable=country, value="Germany", bg=bgFrames,
            fg=optionsColor, font=("arial", 12,)) \
    .grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

Radiobutton(group1, text="USA", justify="left", variable=country, value="USA", bg=bgFrames, fg=optionsColor) \
    .grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

Radiobutton(group1, text="Japan", variable=country, value="Japan", bg=bgFrames, fg=optionsColor) \
    .grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

# group2
# type CAR
group2 = Frame(left_frame, width=400, height=185, bg=bgFrames)
group2.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
Label(group2, text="car type:\t\t", bg=bgFrames, fg=textColors, font=("arial", 16, "bold")).grid(row=0, column=0,
                                                                                                 padx=5, pady=5,
                                                                                                 sticky="nsew")

# type of cars like sport, popular, station, high range.
carType.set(None)

Radiobutton(group2, text="Sport", variable=carType, value="sport", bg=bgFrames, fg=optionsColor,
            justify="left", borderwidth=3, relief="flat").grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

Radiobutton(group2, text="Popular Cars", justify="left", variable=carType, value="popular cars",
            bg=bgFrames, fg=optionsColor).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

Radiobutton(group2, text="Station", justify="left", variable=carType, value="Station", bg=bgFrames,
            fg=optionsColor, font=("arial", 12,)).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

Radiobutton(group2, text="High range", variable=carType, value="High range", bg=bgFrames,
            fg=optionsColor).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

# group3
# setting fuel type
group3 = Frame(right_frame, width=400, height=185, bg=bgFrames)
group3.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Label(group3, text="Fuel type:\t", bg=bgFrames, fg=textColors, font=("arial", 16, "bold")).grid(row=0, column=0, padx=5,
                                                                                                pady=5, sticky="nsew")

fuel.set(None)

Radiobutton(group3, text="diseal", variable=fuel, value="fuel oil", bg=bgFrames, fg=optionsColor,
            justify="left", borderwidth=3, relief="flat", font=("arial", 12,)).grid(row=1, column=0, padx=5, pady=5,
                                                                                    sticky="nsew")

Radiobutton(group3, text="petrol", justify="left", variable=fuel, value="petrol", bg=bgFrames,
            fg=optionsColor, font=("arial", 12,)).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

Radiobutton(group3, text="electric car", justify="left", variable=fuel, value="electric",
            bg=bgFrames, fg=optionsColor, font=("arial", 12,)).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

# group4
# Price range (budget)
group4 = Frame(right_frame, width=400, height=185, bg=bgFrames)
group4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
Label(group4, text="Budget:\t\t", bg=bgFrames, fg=textColors, font=(
    "arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

money.set(None)

Radiobutton(group4, text="From 30K AED - 70K AED ", variable=money, value="[30-70]", bg=bgFrames, fg=optionsColor,
            font=("arial", 12,),
            justify="left", borderwidth=3, relief="flat").grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

Radiobutton(group4, text="From 70K AED - 180K AED  ", justify="left", variable=money, value="[70-180]", bg=bgFrames,
            fg=optionsColor, font=("arial", 12,)).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

Radiobutton(group4, text="From 180K AED - 600K AED ", justify="left", variable=money, value="[180-600]",
            font=("arial", 12),
            bg=bgFrames, fg=optionsColor).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")


def on_submit():
    if (country.get() == "None" or carType.get() == "None" or fuel.get() == "None" or money.get() == "None"):
        messagebox.showwarning("warning", "need to choose options")
    else:
        openResultWindow()


def resetInput():
    country.set(None)
    carType.set(None)
    fuel.set(None)
    money.set(None)


Label(footerFrame, text="\t\t\t\t\t\t", bg=backgroundvalue, fg=textColors).grid(
    row=0, column=0, padx=5, pady=5, sticky="nsew")

footerFrame = tk.Frame(root, width=600, height=150, bg="#004643")
footerFrame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

# Create the transparent buttons
img_reset = Image.open("./icons/restlm.gif")
img_reset = img_reset.resize((img_reset.width // 6, img_reset.height // 6))
img_reset = ImageTk.PhotoImage(img_reset)

# Create the transparent buttons
resetBTN = Button(footerFrame, command=resetInput, text="Reset", compound=LEFT,
                  fg="#1B1B1B", font=("Arial", 16, "bold"), bd=0, activeforeground="#FFFFFF",
                  highlightthickness=0, relief="flat", overrelief="flat", bg="SystemButtonFace")
resetBTN.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

searchBTN = Button(footerFrame, command=on_submit, text="Search", compound=LEFT,
                   fg="#1B1B1B", font=("Arial", 12, "bold"), bd=0, activeforeground="#FFFFFF",
                   highlightthickness=0, relief="flat", overrelief="flat", bg="SystemButtonFace")
searchBTN.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# Center the buttons
footerFrame.grid_rowconfigure(0, weight=1)
footerFrame.grid_columnconfigure(0, weight=1)
footerFrame.grid_columnconfigure(3, weight=1)


root.mainloop()
