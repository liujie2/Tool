import threading
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Download class
class Download_Thread(treading.Thread):
    def __init__(self, *args, **kwargs):
        super(Download_Thread, self).__init__(*args, *kwargs)
        self.__pause = threading.Event()
        self.__pause.clear()
        self.__running = threading.Event()
        self.__running.set()
        self.flag = False
        # Netease -> 1
        # QQ -> 2
        self.engine = None
        self.sonename = None
        self.downnum = 1
        self.savepath = './results'
    def run(self):
        while self.__running.isSet():
            self.__pause.wait()
            self.flag = True
            if self.engine == '1':
                self.show_start_info()
                try:
                    
t_download = Download_Thread()

# kill process
def stopDemo(root):
    t_download.stop()
    root.quit()
    root.destroy()

# Main Menu
def Demo(options):
    assert len(options) > 0

    # Init
    root = Tk()
    root.title('Music Downloader')
    root.resizable(False, False)
    root.geometry('480x368+400+120')
    image_path = './bgimgs/bg1_demo.jpg'
    bgimg = Image.open(image_path)
    bgimg = ImageTk.PhotoImage(bgimg)
    lb_bgimg = Label(root, image=bgimg)
    lb_bgimg.grid()

    # Menu
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=False)
    filemenu.add_command(label='quite', command=lambda: stopDemo(root), font=('Arial', 10))




if __name__ == '__main__':
    options = ["1.NetEase ", "2. QQ Music"]
    Demo(options)