import tkinter
#import time
#from selenium.webdriver import Chrome
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException,UnexpectedAlertPresentException,WebDriverException
from requests.exceptions import ConnectionError
#from selenium.webdriver.support.wait import WebDriverWait
#import selenium.webdriver.support.expected_conditions as ec
#from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os.path, time
import datetime
import threading



def on_keyrelease(event):

    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()

    # get data from test_list
    if value == '':
        data = ''
    else:
        data = []
        listbox.pack()
        listbox.place(relx=0.1,rely=0.35,anchor='nw')
        for item in test_list1 if btn1.get()==1 else test_list:
            if value in item.lower():
                data.append(item)

                # update data in listbox
    listbox_update(data)


def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
    E3.delete(0,END)
    E3.insert(0,listbox.get(ANCHOR))
    #time.sleep(1)
    listbox.pack_forget()
    listbox.place_forget()

def toggle_password():
    global E2, checkbutton
    if checkbutton.var.get():
        E2['show'] = "*"
    else:
        E2['show'] = ""



test_list = []
test_list1 = []
len_listbox=1
len_listbox1=1

def func1():
    global test_list1
    with open('sub.txt', 'r+') as f:
        for line in f:
            test_list1.append(line)

func1()

def func2():
    global test_list
    with open('batch.txt', 'r+') as f:
        for line in f:
            test_list.append(line)

func2()

def func3():
    global len_listbox
    for item in test_list:
        if len(item)>= len_listbox:
            len_listbox=len(item)

func3()

def func4():
    global len_listbox1
    for item in test_list1:
        if len(item)>= len_listbox1:
            len_listbox1=len(item)

func4()

window1=tkinter.Tk()
sub_var=tkinter.StringVar()
uname_var=tkinter.StringVar()
pass_var=tkinter.StringVar()
path_var=tkinter.StringVar()
btn1=tkinter.IntVar(None,1)
btn2=tkinter.IntVar(None,1)
btn1_admin=tkinter.IntVar(None,1)
batch_var=tkinter.StringVar()
path1_var=tkinter.StringVar()
window1.geometry("800x500")


window1.title("Welcome to Automatic Attendence App")
label=tkinter.Label(window1,text="").pack()


tabControl = ttk.Notebook(window1)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='User')
tabControl.add(tab2, text ='Admin')
tabControl.pack(expand = 1, fill ="both")

L1 = Label(tab1, text="User Name")
L1.pack()
L1.place(relx=0.0,rely=0.4,anchor='nw')
E1 = Entry(tab1,textvariable = uname_var, bd =5)
E1.pack()
E1.place(relx=0.1,rely=0.4,anchor='nw')
L2 = Label(tab1, text="Password")
L2.pack()
L2.place(relx=0.0,rely=0.5,anchor='nw')
E2 = Entry(tab1,textvariable = pass_var, bd =5,show='*')
E2.pack()
E2.place(relx=0.1,rely=0.5,anchor='nw')

checkbutton = tkinter.Checkbutton(tab1,
                                  text="Hide password",
                                  onvalue=True,
                                  offvalue=False,
                                  command=toggle_password)
checkbutton.var = tkinter.BooleanVar(value=True)
checkbutton['variable'] = checkbutton.var
checkbutton.pack()
checkbutton.place(relx=0.3,rely=0.5,anchor='nw')
L3 = Label(tab1
           , text="Subject")
L3.pack()
L3.place(relx=0.0,rely=0.3,anchor='nw')





E3 = Entry(tab1,textvariable = sub_var,bd =5,width=len_listbox1+5 if btn1.get()==1 else len_listbox+5 )
E3.pack()
E3.place(relx=0.1,rely=0.3,anchor='nw')
E3.bind('<KeyRelease>', on_keyrelease)

listbox = tkinter.Listbox(tab1,width=len_listbox1+5 if btn1.get()==1 else len_listbox+5)
listbox.pack()
listbox.pack_forget()
listbox.bind('<<ListboxSelect>>', on_select)

L4 = Label(tab1, text="Path")
L4.pack()
L4.place(relx=0.5,rely=0.2,anchor='nw')
E4 = Entry(tab1,textvariable = path_var, width=50)
E4.pack()
E4.place(relx=0.55,rely=0.2,anchor='nw')

r1=Radiobutton(tab1,text="Subjectwise",value=1,variable=btn1).pack(anchor='nw')
r2=Radiobutton(tab1,text="Batchwise",value=2,variable=btn1).pack(anchor='nw')

l1=Radiobutton(tab1,text="Lect:1",value=1,variable=btn2).pack(anchor='nw')
l2=Radiobutton(tab1,text="Lect:2",value=2,variable=btn2).pack(anchor='nw')
l3=Radiobutton(tab1,text="Lect:3",value=3,variable=btn2).pack(anchor='nw')
progress =ttk.Progressbar(tab1, orient = HORIZONTAL,
                          length = 300, mode = 'determinate')


x1='test.txt'
x2='test2.txt'
present_lines=[]

isclicked=False
creation_date=''
def init(fname):
    global fil
    fil = open(fname, 'w+')

def init1(fname):
    global f1
    f1 = open(fname, 'w+')


init(x1)
init1(x2)

def func5():
    with open('test1.txt', 'a+') as f:
        f.write('onetime'+'\n')

func5()

def func6():
    with open('test1.txt', 'a+') as f:
        f.seek(0)
        E1.insert(0,f.readline().rstrip('\n'))
        E2.insert(0,f.readline().rstrip('\n'))

func6()


def open_file():
    global fil
    global creation_date
    global path_var
    global isclicked
    global f1
    f = filedialog.askopenfile(initialdir="E:/", title="Select A File", filetypes=(("csv files", "*.csv"),("all files", "*.*")))
    fil = f
    f1=f
    #print(time.ctime(os.path.getctime("{}".format(f.name))))
    #path_var=f.name
    try:
        E4.insert(0,f.name)
        isclicked=True
        f1.readline()
        f1.readline()

        creation_date=datetime.datetime.strptime((f1.readline().strip('\n')).split('\t')[2].split(',')[0].replace("\0","").strip('"'),"%m/%d/%Y").strftime("%d-%m-%Y")
        print(fil)
        f.seek(0)
    except AttributeError:
        E4.delete(0,END)
        E4.insert(0,"")



save_password=False



def Validation_Final():
    global isclicked
    progress['value'] = 5

    progress.pack()
    progress.place(relx=0.3,rely=0.1,anchor='nw')
    tab1.update_idletasks()
    if(not(sub_var.get())):
        messagebox.showerror("showerror", "Subject Not entered")
    else:
        pass
    if(not(uname_var.get())):
        messagebox.showerror("showerror", "Username Not entered")
    else:
        pass
    if(not(pass_var.get())):
        messagebox.showerror("showerror", "Password Not entered")
    else:
        pass
    if(not(btn1.get())):
        messagebox.showerror("showerror", "Subjectwise or Batchwise")
    else:
        pass
    if(not(btn2.get())):
        messagebox.showerror("showerror", "Lecture Not Selected")
    else:
        pass
    if(not(isclicked)):
        messagebox.showerror("showerror", "Select csv attendance file")
    else:
        pass

    def save_username():
        global save_password
        with open('test1.txt', 'r+') as f:
            #f.seek(0)
            if (save_password==True):
                f.write(uname_var.get()+"\n")
                f.write(pass_var.get()+"\n")
                save_password=False



    def call():
        global save_password
        res = messagebox.askquestion('Save Password',
                                     'Do you want to save Password?')

        if res == 'yes' :
            save_password=True
            save_username()

        else :
            pass

    def call_control():
        with open('test1.txt', 'r+') as f:
            f.seek(0)
            for line in f:
                present_lines.append(line)
            f.seek(0)

            if((uname_var.get()+'\n' not in present_lines) or (pass_var.get()+'\n' not in present_lines) or ('onetime\n' not in present_lines)):
                call()
            else:
                pass


    call_control()


    #start_progress()

    if isclicked:

        threading.Thread(target=automation).start()
    else:
        pass

btn = Button(tab1, text ='Select Attendance file(.csv)', command =lambda :open_file())
Upload_Attendance= Button(tab1, text ='Upload Attendance in MIS', command =lambda :Validation_Final())
btn.pack()
btn.place(relx=0.35,rely=0.2,anchor='nw')
Upload_Attendance.pack()
Upload_Attendance.place(relx=0.5,rely=0.5,anchor='nw')







def open_file_text():
    global sub_ufile
    sub_ufile = filedialog.askopenfile(initialdir="E:/", title="Select A File", filetypes=(("text files", "*.txt"),("all files", "*.*")))

    path1_var=sub_ufile.name
    E_update.insert(0,sub_ufile.name)


def Update_Final():
    if btn1_admin.get()==1:
        sub_ufile.seek(0)
        with open('sub.txt', 'r+') as f_sub:
            for line in sub_ufile:
                f_sub.write(line+'\n')
    else:
        sub_ufile.seek(0)
        with open('batch.txt', 'r+') as f_batch:
            for line in sub_ufile:
                f_batch.write(line+'\n')

    messagebox.showinfo("showinfo", "Updation Comple"
                                    "ted")



admin_button=Button(tab2, text ='Select Subject updation text file', command =lambda :open_file_text())
admin_button.pack()
admin_button.place(relx=0.35,rely=0.3,anchor='nw')
Upload_Updation_File= Button(tab2, text ='Upload Updation File', command =lambda :Update_Final())
Upload_Updation_File.pack()
Upload_Updation_File.place(relx=0.5,rely=0.4,anchor='nw')
r3=Radiobutton(tab2,text="Subjectwise",value=1,variable=btn1_admin)

r3.pack(anchor='nw')
r3.place(relx=0.1,rely=0.3,anchor='nw')
r4=Radiobutton(tab2,text="Batchwise",value=2,variable=btn1_admin)
r4.pack(anchor='nw')
r4.place(relx=0.22,rely=0.3,anchor='nw')
E_update = Entry(tab2,textvariable = path1_var, width=50)
E_update.pack()
E_update.place(relx=0.6,rely=0.3,anchor='nw')

def automation():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-setuid-sandbox")

    chromeOptions.add_argument("--remote-debugging-port=9222")  # this

    chromeOptions.add_argument("--disable-dev-shm-using")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("start-maximized")
    chromeOptions.add_argument("disable-infobars")
    #chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")
    #chromeOptions.add_argument("--headless")







    global fil
    try:
        try:
            driver= webdriver.Chrome(ChromeDriverManager().install(),options=chromeOptions)

            #chromeOptions.add_argument("--window-size=800x500")
            #path="Driver/chromedriver.exe"
            progress['value'] = 10


            tab1.update_idletasks()

            driver.get("https://pict.ethdigitalcampus.com/PICT/")
            driver.maximize_window()
            progress['value'] = 25
            tab1.update_idletasks()
        except ConnectionError:
            messagebox.showerror("showerror", 'Check Internet Connection')
            print("line 650")
            driver.quit()
            #return



        driver.implicitly_wait(3)
        driver.find_element_by_name("loginid").clear()
        driver.find_element_by_name("loginid").send_keys(uname_var.get().strip('\n'))
        driver.find_element_by_name("password").send_keys(pass_var.get().strip('\n'))
        progress['value'] = 30
        tab1.update_idletasks()





        driver.find_element_by_xpath("//input[contains(@value,'Sign In')]").click()
        progress['value'] = 35
        tab1.update_idletasks()

        try:
            if driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table[1]/tbody/tr/td/p/b[contains(text(),'Your last login attempt was not successful due to one of the following reasons:')]"):
                messagebox.showerror("Show error","Enter correct  username/password")
                progress.stop()
                tab1.update()
                driver.quit()
                #return


            else:
                pass

        except NoSuchElementException:
            pass

        driver.find_element_by_partial_link_text("Activities").click()
        progress['value'] = 40
        tab1.update_idletasks()

        driver.find_element_by_partial_link_text("Student Attendance").click()
        progress['value'] = 45
        tab1.update_idletasks()

        driver.find_element_by_partial_link_text("Mark Student Attendance").click()
        progress['value'] = 50
        tab1.update_idletasks()

        x=btn1.get()
        if (x==1):
            try:
                driver.find_element_by_xpath("//input[contains(@id,'{}')]".format(x)).click()
                subject=sub_var.get().replace("\0", "").rstrip('\n')
                driver.find_element_by_xpath("//*[@id='theory_subject_combo']/option[contains(text(), '{}')]".format(subject.upper())).click()
                datefield=driver.find_element_by_name("attendanceDate_txt")
                datefield.clear()
                datefield.send_keys(creation_date)
                driver.find_element_by_xpath("//input[@value='{}']".format(btn2.get())).click()
                driver.find_element_by_xpath("//input[contains(@value,'Show')]").click()
                progress['value'] = 55
                tab1.update_idletasks()
                time.sleep(2)
                try:
                    if driver.find_element_by_xpath("//*[@id='msg_display']/b[contains(text(), 'Attendance Allready Marked')]"):
                        messagebox.showerror("showerror", "Attendance Allready Marked")
                        progress['value'] = 0
                        tab1.update_idletasks()
                        driver.quit()
                        #return
                    # progress.stop()
                    #driver.quit()

                except NoSuchElementException:
                    pass
            except UnexpectedAlertPresentException as e3:
                messagebox.showerror("showerror", "{}".format(e3.msg))
                progress['value'] = 0
                tab1.update_idletasks()
                driver.quit()
                #return


                #driver.close()

            att_list=[]
            print(fil)
            fil.seek(0)

            for eachline5 in fil:
                att_list.append(eachline5.split(' ')[0][:10])


            Not_none_values=filter(None.__ne__,att_list)
            list_of_value=list(Not_none_values)

            new_list_of_value=sorted(list_of_value)
            final_list=[]
            for element2 in new_list_of_value:
                if (element2 not in final_list and element2 != '\x00'):

                    final_list.append(element2)

            #for element3 in final_list:
                #print(element3)
            progress['value'] = 55
            tab1.update_idletasks()
            try:
                for i4 in final_list:

                    i2=i4.replace("\0", "")
                    xpath2="//input[contains(@value,'{}')]/parent::td/following-sibling::td[1]/input".format(i2)
                    driver.find_element_by_xpath(xpath2).click()

            except NoSuchElementException:
                pass


            driver.find_element_by_xpath("//input[contains(@value,'MarkPresent')]").click()
            progress['value'] = 60
            tab1.update_idletasks()

            obj=driver.switch_to.alert()

            obj.accept()
            try:
                if  UnexpectedAlertPresentException:
                    obj=driver.switch_to.alert()
                    messagebox.showerror("showerror", "{}".format(obj.text)+'     Check Attendance file batch/class')
                    progress['value'] = 0
                    tab1.update_idletasks()
                    driver.quit()
                    #return
                    #progress.stop()
                    #driver.quit()
                else:
                    pass

            except NoAlertPresentException:
                pass


            driver.find_element_by_xpath("//input[contains(@value,'Submit')]").click()
            progress['value'] = 80
            tab1.update_idletasks()
            try:
                if driver.find_element_by_xpath("//*[contains(@id,'msg_display')]"):
                    progress['value'] = 100
                    tab1.update_idletasks()

                    messagebox.showinfo("showinfo", "Attendance Marked Successfully")
                    driver.quit()
                    #progress.stop()
                    #return

                    #driver.close()




            except NoSuchElementException:
                pass




        else:

            driver.find_element_by_xpath("//input[contains(@id,'{}')]".format(x)).click()
            subject=sub_var.get().replace("\0", "").rstrip('\n').rstrip()
            driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/table[1]/tbody/tr[3]/td[2]/select/option[contains(text(), '{}')]".format((subject).upper())).click()


            datefield=driver.find_element_by_name("attendanceDate_txt")
            datefield.clear()
            datefield.send_keys(creation_date)

            driver.find_element_by_xpath("//input[@value='{}']".format(btn2.get())).click()
            driver.find_element_by_xpath("//input[contains(@value,'Show')]").click()
            progress['value'] = 55
            tab1.update_idletasks()

            time.sleep(2)
            try:
                if driver.find_element_by_xpath("//*[@id='msg_display']/b[contains(text(), 'Attendance Allready Marked')]"):
                    messagebox.showerror("showerror", "Attendance Allready Marked")
                    progress['value'] = 0
                    tab1.update_idletasks()
                    driver.close()

                    #progress.stop()
                    return
                    #driver.close()

            except NoSuchElementException:
                pass
            except UnexpectedAlertPresentException as e3:
                messagebox.showerror("showerror", "{}".format(e3.msg))
                progress['value'] = 0
                tab1.update_idletasks()
                driver.close()
                return
                #progress.stop()
                #driver.close()

            progress['value'] = 60
            tab1.update_idletasks()
            att_list=[]
            print(fil)
            fil.seek(0)

            for eachline5 in fil:
                att_list.append(eachline5.split(' ')[0][:10])


            Not_none_values=filter(None.__ne__,att_list)
            list_of_value=list(Not_none_values)

            new_list_of_value=sorted(list_of_value)
            final_list=[]
            for element2 in new_list_of_value:
                if (element2 not in final_list and element2 != '\x00'):

                    final_list.append(element2)

            #for element3 in final_list:
                #print(element3)
            progress['value'] = 65
            tab1.update_idletasks()

            for i4 in final_list:
                try:

                        i2=i4.replace("\0", "")
                        xpath2="//input[contains(@value,'{}')]/parent::td/following-sibling::td[1]/input".format(i2)
                        driver.find_element_by_xpath(xpath2).click()

                except NoSuchElementException:
                    continue


            driver.find_element_by_xpath("//input[contains(@value,'MarkPresent')]").click()
            progress['value'] = 80
            tab1.update_idletasks()

            obj=driver.switch_to.alert()

            obj.accept()
            try:
                if  UnexpectedAlertPresentException:
                    obj=driver.switch_to.alert()
                    messagebox.showerror("showerror", "{}".format(obj.text)+'     Check Attendance file batch/class/date')
                    progress['value'] = 0
                    tab1.update_idletasks()
                    driver.close()
                    return

                    #progress.stop()
                    #driver.quit()
                else:
                    pass


            except NoAlertPresentException:

                pass


            driver.find_element_by_xpath("//input[contains(@value,'Submit')]").click()
            try:
                if driver.find_element_by_xpath("//*[contains(@id,'msg_display')]"):
                    progress['value'] = 100
                    tab1.update_idletasks()
                    messagebox.showinfo("showinfo", "Attendance Marked Successfully")
                    progress['value'] = 0
                    tab1.update_idletasks()

                    #progress.stop()
                    driver.close()
                    return

            except NoSuchElementException:
                pass



    except NoSuchElementException as e:
        print("line 646")
        messagebox.showerror("showerror", "{}".format(e))
        driver.close()
        return


window1.mainloop()



        #progress.stop()

#bar1()

