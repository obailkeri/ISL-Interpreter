import tkinter as tk
from tkinter.font import Font
import cv2
from tkinter import *


def fun1():
    window = tk.Toplevel(root)
    window.geometry("900x900")
    window.title("Smart Communication ")
    window['bg']='white'
    my_font = Font(family="Times New Roman", size=45, weight="bold", slant="italic", underline=1)
    label = Label(window, text= "Smart Communication", font=my_font, fg='#008B00', bg='white').pack()

    scan2=PhotoImage(file='exit1.png')
    scan_button2=Button(window, text="BACK", image=scan2, bg='white', relief=RAISED, borderwidth=0,font="helv19",command = window.destroy )
    scan_button2['border']='0'
    scan_button2.config(image=scan2, compound=TOP, bd='0', font=('Rekha', 20, 'italic'))
    tmi2=scan2.subsample(4, 4)
    scan_button2.config(image=tmi2)
    scan_button2.pack(side=BOTTOM)
    window.geometry("900x900")
    label = Label(window,text="\n\n\n\n\n\n USER MANUAL:\n\n\n\n\n1. BUTTON SCAN:A) CONVERTS SIGN LANGUAGE TO TEXT \n B) THE ALGORITHM SCANS ONLY THE HAND GESTURES AND NOT THE FACIAL EXPRESSIONS  \n\n C) ONLY KEEP YOUR HAND IN THE FRAME \n\n 2. BUTTON TEXT TO SIGN: \n\n A) COVERTS THE TEXT INPUT TO SIGN LANGUAGE \n\n B) GIVE VALID TEXT INPUT TO THE SYSTEM \n\n 3. BUTTON EXIT: \n\n A) EXIT THE PROGRAM EXECUTION \n\n 4. BUTTON HELP \n\n A) GIVES THE REQUIRED INSTRUCTIONS TO THE USER" ,  bg = 'white' )

    #this creates a new label to the GUI

    label.pack(side = TOP , pady = 100)

    window.mainloop()


def fun():
    # Convolutional Neural Network

    from keras.models import load_model

    classifier = load_model('my_model.h5')

    from keras.preprocessing import image
    import numpy as np

    import playsound
    from gtts import gTTS

    import cv2

    import os

    camera = cv2.VideoCapture(0)

    num_frames = 0
    num = 0
    i = 0

    recog = []

    while True:
        # get the current frame
        (grabbed, frame) = camera.read()

        frame = cv2.flip(frame, 1)

        num_frames += 1

        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (50, 460)
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 2

        frame1 = cv2.resize(frame, (64, 64))
        # frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        img = image.img_to_array(frame1)
        img = np.expand_dims(img, axis=0)
        result = classifier.predict(img)
        # training_set.class_indices

        print(result)

        if result[0][0] == max(result[0]):
            rst = 'fine'
        elif result[0][1] == max(result[0]):
            rst = 'help'
        elif result[0][2] == max(result[0]):
            rst = 'I'
        elif result[0][3] == max(result[0]):
            rst = 'make'
        elif result[0][4] == max(result[0]):
            rst = 'me'
        elif result[0][5] == max(result[0]):
            rst = 'please'
        elif result[0][6] == max(result[0]):
            rst = 'we'
        else:
            rst = ''

        cv2.putText(frame, rst,
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    lineType)

        # display the frame with segmented hand
        cv2.imshow("Video Feed", frame)

        num += 1

        '''
        if num == 100:
            tts = gTTS(text=rst, lang='en')
            music = "temp" + str(i) + ".mp3"
            tts.save(music)
            playsound.playsound(music, True)
            os.remove(music)
            i += 1

        if num == 150:
            num = 0
        '''

        # observe the keypress by the user
        keypress = cv2.waitKey(1) & 0xFF

        if keypress == ord("c"):
            recog.append(rst)

        # if the user pressed "q", then stop looping
        if keypress == ord("q"):
            break

    with open("simple movie reviews", "r") as file:
        documents = file.read().splitlines()
    # print(documents)
    probab = []
    recog = list(dict.fromkeys(recog))
    print(recog)
    for k in range(len(documents)):
        # print(len(documents))
        sen = documents[k].split()
        count = 0
        for i in range(len(recog)):
            for j in range(len(sen)):
                if (recog[i] == sen[j]):
                    # probab[0]+=1
                    count = count + 1
        probab.append(count)
        # print(probab)
    # print(probab)
    most = max(probab)
    index = probab.index(most)
    # print(index)
    str = documents[index]
    print(str)

    from sklearn.feature_extraction.text import CountVectorizer
    import pandas as pd

    # Step 2. Design the Vocabulary
    # The default token pattern removes tokens of a single character. That's why we don't have the "I" and "s" tokens in the output
    count_vectorizer = CountVectorizer()

    # Step 3. Create the Bag-of-Words Model
    bag_of_words = count_vectorizer.fit_transform(documents)
    # print(bag_of_words)

    # Show the Bag-of-Words Model as a pandas DataFrame
    feature_names = count_vectorizer.get_feature_names()
    # print(feature_names)
    pd.DataFrame(bag_of_words.toarray(), columns=feature_names)

    # free up memory
    camera.release()
    cv2.destroyAllWindows()


def create_window():
    window = tk.Toplevel(root)
    window.geometry("900x900")
    window.title("Smart Communication ")
    window['bg'] = 'white'
    my_font = Font(family="Times New Roman", size=45, weight="bold", slant="italic", underline=1)
    label = Label(window, text="Smart Communication", font=my_font, fg='#008B00', bg='white').pack(side=TOP)

    scan2 = PhotoImage(file='exit1.png')
    scan_button2 = Button(window, text="BACK", image=scan2, bg='white', relief=RAISED, borderwidth=0, font="helv19",
                          command=window.destroy)
    scan_button2['border'] = '1'
    scan_button2.config(image=scan2, compound=TOP, bd='0', font=('Rekha', 20, 'italic'))
    tmi2 = scan2.subsample(4, 4)
    scan_button2.config(image=tmi2)
    scan_button2.pack(side=BOTTOM, pady=100)

    # label_1 = Label(window, text="FullName",width=50,font=("bold", 50) , bg = 'white')
    # label_1.place(x=80,y=130)

    # entry_1 = Entry(window)
    # entry_1.place(x=240,y=130)

    # frame = LabelFrame(window, text="Input", pady=300,width=150,font=("bold", 35) , bg = 'white')

    # entry = Entry(frame)
    # entry.pack()

    # def mhello():
    #    pass
    #    return

    def text_2_img():
        # ment = input("What do you want to say? ")
        # entry = Entry(window)
        # entry.pack()
        mtext = ment.get()
        lis = mtext.split()
        print(lis)
        nlabel2 = Label(window, text=mtext).pack()

        # print(mtext)

        for i in range(len(mtext)):
            if str(lis[i]) == "fine":
                img = cv2.imread("C:\\Users\\omkar\\PycharmProject\\ImgRead\\dataset\\train_gest\\fine\\fine.jpg")
                height, width = img.shape[:2]

                thumbnail = cv2.resize(img, (500, 500))

                cv2.imshow("window", thumbnail)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif str(lis[i]) == "help":
                img = cv2.imread("C:\\Users\\omkar\\PycharmProject\\ImgRead\\dataset\\train_gest\\Help\\help.jpg")
                height, width = img.shape[:2]

                thumbnail = cv2.resize(img, (500, 500))

                cv2.imshow("window", thumbnail)
                cv2.waitKey(-1)
                cv2.destroyAllWindows()

            elif str(lis[i]) == "I":
                img = cv2.imread("C:\\Users\\omkar\\PycharmProject\\ImgRead\\dataset\\train_gest\\I\\I.jpg")
                height, width = img.shape[:2]

                thumbnail = cv2.resize(img, (500, 500))

                cv2.imshow("window", thumbnail)
                cv2.waitKey(12)
                cv2.destroyAllWindows()

            elif str(lis[i]) == "make":
                img = cv2.imread("C:\\Users\\omkar\\PycharmProject\\ImgRead\\dataset\\train_gest\\Make\\make.jpg")
                height, width = img.shape[:2]

                thumbnail = cv2.resize(img, (500, 500))

                cv2.imshow("window", thumbnail)
                cv2.waitKey(12)
                cv2.destroyAllWindows()
            elif str(lis[i]) == "me":
                img = cv2.imread("C:\\Users\\omkar\\PycharmProject\\ImgRead\\dataset\\train_gest\\me\\me.jpg")
                height, width = img.shape[:2]

                thumbnail = cv2.resize(img, (500, 500))

                cv2.imshow("window", thumbnail)
                cv2.waitKey(-1)
                cv2.destroyAllWindows()
            elif str(lis[i]) == "please":
                img = cv2.imread("C:\\Users\\omkar\\PycharmProject\\ImgRead\\dataset\\train_gest\\Please\\please.jpg")
                height, width = img.shape[:2]

                thumbnail = cv2.resize(img, (500, 500))

                cv2.imshow("window", thumbnail)
                cv2.waitKey(-1)
                cv2.destroyAllWindows()
            elif str(lis[i]) == "we":
                img = cv2.imread("C:\\Users\\omkar\\PycharmProject\\ImgRead\\dataset\\train_gest\\We\\we.jpg")
                height, width = img.shape[:2]

                thumbnail = cv2.resize(img, (500, 500))

                cv2.imshow("window", thumbnail)
                cv2.waitKey(-1)

                cv2.destroyAllWindows()
            else:
                print("Invalid gesture!")

            cv2.waitKey(15)
            cv2.destroyAllWindows()

    ment = StringVar()

    # nlabel  = Label(window , text = 'Submit'  ).pack()
    nbutton = Button(window, text='CONVERT', command=text_2_img).pack()

    mEntry = Entry(window, textvariable=ment).pack()
    # mEntry.place(width=150, height=150)

    window.geometry("900x900")

    window.mainloop()


root = Tk()

root.configure(background='#16e116')

# root['bg']='white'
root.title("Smart Communication ")
root['bg'] = 'white'
my_font = Font(family="Times New Roman", size=45, weight="bold", slant="italic", underline=1)
label = Label(root, text="Smart Communication", font=my_font, fg='#008B00', bg='white').pack()

scan1 = PhotoImage(file='help1.png')
scan_button1 = Button(root, text="Help", image=scan1, bg='white', relief=RAISED, borderwidth=0, font="helv19", command=fun1)
scan_button1['border'] = '0'
scan_button1.config(image=scan1, compound=TOP, bd='0')
tmi1 = scan1.subsample(2, 2)
scan_button1.config(image=tmi1)
scan_button1.pack(side = LEFT, padx=80)

scan = PhotoImage(file='button.png')
scan_button = Button(root, text="Scan", image=scan, bg='white', relief=RAISED, borderwidth=0, font="helv19", command=fun)
scan_button['border'] = '0'
scan_button.config(image=scan, compound=TOP, bd='0')
tmi = scan.subsample(2, 2)
scan_button.config(image=tmi)
scan_button.pack(side = RIGHT, padx=80)

scan3 = PhotoImage(file='text2.png')
scan_button3 = Button(root, text="Text to Sign", image=scan3, bg='white', relief=RAISED, borderwidth=0, font="helv19",
                      command=create_window)
scan_button3['border'] = '0'
scan_button3.config(image=scan1, compound=TOP, bd='0')
tmi3 = scan3.subsample(2, 2)
scan_button3.config(image=tmi3)
scan_button3.pack(side = TOP, pady=80)

scan2 = PhotoImage(file='exit1.png')
scan_button2 = Button(root, text="EXIT", image=scan2, bg='white', relief=RAISED, borderwidth=0, font="helv19",
                      command=root.destroy)
scan_button2['border'] = '0'
scan_button2.config(image=scan2, compound=TOP, bd='0', font=('Rekha', 20, 'italic'))
tmi2 = scan2.subsample(4, 4)
scan_button2.config(image=tmi2)
scan_button2.pack(side = BOTTOM, pady=80)

# scan_button.grid()
root.geometry("900x900")
root.mainloop()
