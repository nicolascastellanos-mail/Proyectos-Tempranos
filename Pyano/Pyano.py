from playsound import playsound
from tkinter import Tk, Button
from threading import Thread

piano_30 = "Assets/30.mp3"
piano_31 = "Assets/31.mp3"
piano_32 = "Assets/32.mp3"
piano_33 = "Assets/33.mp3"
piano_34 = "Assets/34.mp3"
piano_35 = "Assets/35.mp3"
piano_36 = "Assets/36.mp3"
piano_37 = "Assets/37.mp3"
piano_38 = "Assets/38.mp3"
piano_39 = "Assets/39.mp3"
piano_40 = "Assets/40.mp3"
piano_41 = "Assets/41.mp3"
piano_42 = "Assets/42.mp3"
piano_43 = "Assets/43.mp3"
piano_44 = "Assets/44.mp3"
piano_45 = "Assets/45.mp3"
piano_46 = "Assets/46.mp3"
piano_47 = "Assets/47.mp3"
piano_48 = "Assets/48.mp3"
piano_49 = "Assets/49.mp3"
piano_50 = "Assets/50.mp3"
piano_51 = "Assets/51.mp3"
piano_52 = "Assets/52.mp3"
piano_53 = "Assets/53.mp3"
piano_54 = "Assets/54.mp3"
piano_55 = "Assets/55.mp3"
piano_56 = "Assets/56.mp3"
piano_57 = "Assets/57.mp3"
piano_58 = "Assets/58.mp3"
piano_59 = "Assets/59.mp3"
piano_60 = "Assets/60.mp3"
piano_61 = "Assets/61.mp3"
piano_62 = "Assets/62.mp3"
piano_63 = "Assets/63.mp3"
piano_64 = "Assets/64.mp3"
piano_65 = "Assets/65.mp3"
piano_66 = "Assets/66.mp3"
piano_67 = "Assets/67.mp3"
piano_68 = "Assets/68.mp3"
piano_69 = "Assets/69.mp3"
piano_70 = "Assets/70.mp3"
piano_71 = "Assets/71.mp3"
piano_72 = "Assets/72.mp3"
piano_73 = "Assets/73.mp3"
piano_74 = "Assets/74.mp3"
piano_75 = "Assets/75.mp3"
piano_76 = "Assets/76.mp3"
piano_77 = "Assets/77.mp3"
piano_78 = "Assets/78.mp3"
piano_79 = "Assets/79.mp3"
piano_80 = "Assets/80.mp3"
piano_81 = "Assets/81.mp3"
piano_82 = "Assets/82.mp3"
piano_83 = "Assets/83.mp3"
piano_84 = "Assets/84.mp3"
piano_85 = "Assets/85.mp3"
piano_86 = "Assets/86.mp3"
piano_87 = "Assets/87.mp3"
piano_88 = "Assets/88.mp3"
piano_89 = "Assets/89.mp3"
piano_90 = "Assets/90.mp3"

window = Tk()
window.title("Pyano")
window.geometry("1248x150+0+0")
window.resizable(0, 0)

def play_piano(note):
	play_process = Thread(target=playsound, args=(note,))
	play_process.start()

button_31 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_31), text="G")
button_33 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_33), text="A")
button_35 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_35), text="B")
button_36 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_36), text="C")
button_38 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_38), text="D")
button_40 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_40), text="E")
button_41 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_41), text="F")
button_43 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_43), text="G")
button_45 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_45), text="A")
button_47 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_47), text="B")
button_48 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_48), text="C")
button_50 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_50), text="D")
button_52 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_52), text="E")
button_53 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_53), text="F")
button_55 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_55), text="G")
button_57 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_57), text="A")
button_59 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_59), text="B")
button_60 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_60), text="C")
button_62 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_62), text="D")
button_64 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_64), text="E")
button_65 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_65), text="F")
button_67 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_67), text="G")
button_69 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_69), text="A")
button_71 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_71), text="B")
button_72 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_72), text="C")
button_74 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_74), text="D")
button_76 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_76), text="E")
button_77 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_77), text="F")
button_79 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_79), text="G")
button_81 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_81), text="A")
button_83 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_83), text="B")
button_84 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_84), text="C")
button_86 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_86), text="D")
button_88 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_88), text="E")
button_89 = Button(window, bg="white", activebackground="white", anchor="s", command=lambda: play_piano(piano_89), text="F")

button_30 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_30), text="F#")
button_32 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_32), text="G#")
button_34 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_34), text="A#")
button_37 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_37), text="C#")
button_39 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_39), text="D#")
button_42 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_42), text="F#")
button_44 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_44), text="G#")
button_46 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_46), text="A#")
button_49 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_49), text="C#")
button_51 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_51), text="D#")
button_54 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_54), text="F#")
button_56 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_56), text="G#")
button_58 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_58), text="A#")
button_61 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_61), text="C#")
button_63 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_63), text="D#")
button_66 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_66), text="F#")
button_68 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_68), text="G#")
button_70 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_70), text="A#")
button_73 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_73), text="C#")
button_75 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_75), text="D#")
button_78 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_78), text="F#")
button_80 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_80), text="G#")
button_82 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_82), text="A#")
button_85 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_85), text="C#")
button_87 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_87), text="D#")
button_90 = Button(window, bg="black", activebackground="black", fg="white", activeforeground="white", command=lambda: play_piano(piano_90), text="F#")

button_31.place(x=10, y=0, width=35, height=150)
button_33.place(x=45, y=0, width=35, height=150)
button_35.place(x=80, y=0, width=35, height=150)
button_36.place(x=115, y=0, width=35, height=150)
button_38.place(x=150, y=0, width=35, height=150)
button_40.place(x=185, y=0, width=35, height=150)
button_41.place(x=220, y=0, width=35, height=150)
button_43.place(x=255, y=0, width=35, height=150)
button_45.place(x=290, y=0, width=35, height=150)
button_47.place(x=325, y=0, width=35, height=150)
button_48.place(x=360, y=0, width=35, height=150)
button_50.place(x=395, y=0, width=35, height=150)
button_52.place(x=430, y=0, width=35, height=150)
button_53.place(x=465, y=0, width=35, height=150)
button_55.place(x=500, y=0, width=35, height=150)
button_57.place(x=535, y=0, width=35, height=150)
button_59.place(x=570, y=0, width=35, height=150)
button_60.place(x=605, y=0, width=35, height=150)
button_62.place(x=640, y=0, width=35, height=150)
button_64.place(x=675, y=0, width=35, height=150)
button_65.place(x=710, y=0, width=35, height=150)
button_67.place(x=745, y=0, width=35, height=150)
button_69.place(x=780, y=0, width=35, height=150)
button_71.place(x=815, y=0, width=35, height=150)
button_72.place(x=850, y=0, width=35, height=150)
button_74.place(x=885, y=0, width=35, height=150)
button_76.place(x=920, y=0, width=35, height=150)
button_77.place(x=955, y=0, width=35, height=150)
button_79.place(x=990, y=0, width=35, height=150)
button_81.place(x=1025, y=0, width=35, height=150)
button_83.place(x=1060, y=0, width=35, height=150)
button_84.place(x=1095, y=0, width=35, height=150)
button_86.place(x=1130, y=0, width=35, height=150)
button_88.place(x=1165, y=0, width=35, height=150)
button_89.place(x=1200, y=0, width=35, height=150)

button_30.place(x=0, y=0 ,width=25, height=120)
button_32.place(x=32, y=0, width=25, height=120)
button_34.place(x=67, y=0, width=25, height=120)
button_37.place(x=137, y=0, width=25, height=120)
button_39.place(x=172, y=0, width=25, height=120)
button_42.place(x=242, y=0, width=25, height=120)
button_44.place(x=277, y=0, width=25, height=120)
button_46.place(x=312, y=0, width=25, height=120)
button_49.place(x=382, y=0, width=25, height=120)
button_51.place(x=417, y=0, width=25, height=120)
button_54.place(x=487, y=0, width=25, height=120)
button_56.place(x=522, y=0, width=25, height=120)
button_58.place(x=557, y=0, width=25, height=120)
button_61.place(x=627, y=0, width=25, height=120)
button_63.place(x=662, y=0, width=25, height=120)
button_66.place(x=732, y=0, width=25, height=120)
button_68.place(x=767, y=0, width=25, height=120)
button_70.place(x=802, y=0, width=25, height=120)
button_73.place(x=872, y=0, width=25, height=120)
button_75.place(x=907, y=0, width=25, height=120)
button_78.place(x=977, y=0, width=25, height=120)
button_80.place(x=1012, y=0, width=25, height=120)
button_82.place(x=1047, y=0, width=25, height=120)
button_85.place(x=1117, y=0, width=25, height=120)
button_87.place(x=1152, y=0, width=25, height=120)
button_90.place(x=1222, y=0, width=25, height=120)

window.mainloop()
