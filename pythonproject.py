from tkinter import *
import pickle
import os
from tkinter import StringVar
from tkinter import scrolledtext
from tkinter import messagebox

add_dict = []
retrieve = []
retrieveback = []
count = -1
showallindex = 0
tcount = 0
delete_count = 0
delete_index_list = []
a =[]  # global variable for tranfering content from binary to text file

root = Tk()
mystring1 = StringVar(root)
mystring2 = StringVar(root)
mystring3 = StringVar(root)
mystring4 = StringVar(root)
mystring5 = StringVar(root)
searchstring = StringVar(root)
deletestring = StringVar(root)

#####################################      Main window          #################################################

def mainwindow(root):

    Frame(root, width=3000, height=1000, bg='steelblue').place(x=0, y=0)
    lbl = Label(root, text="Rana Sales", bg="yellow", fg="steelblue", font=("arial bold", 50))
    lbl.place(x=450, y=1)
    btn = Button(root, text="  SmartPhones ", bg="black", fg="white", font=("arial bold", 25),command=lambda: phone(root))
    btn.place(x=10, y=150)
    Button(root, text="     Feedback    ", bg="black", fg="white", font=("arial bold", 25), command=lambda: feedback(root)).place(x=10, y=220)
    Button(root, text="          Exit         ", bg="black", fg="white", font=("arial bold", 25), command=lambda: quit(root)).place(x=10, y=290)

    pfile = open("phone.bin", "rb")

    temp = []  # for getting count of records in binary file

    global count , delete_index_list

    delete_index_list.clear()

    while 1:  # this helps in counting how many recotrds are present currently in file

        try:

            temp = pickle.load(pfile)


        except(EOFError) :
                  break



    pfile.close()

    with open("deletedentries","rb") as dfile :

        while 1:  # this helps in counting how many recotrds are present currently in file

            try:
                delete_index_list = pickle.load(dfile)

            except(EOFError):  # in case the file  reaches its end

                break


            except:  # in case the file  initially , has no content
                break

    count = len(temp) -1
    print("length in file rn : ",len(temp))
    print("count in file rn : ", count )

# end of mainwindow method



##########################    WHENEVER USER HITS THE SMARTPHONES BUTTON  CONTROL REACHES HERE         #########################

def phone(root):

    frame = Frame(root, width=860, height=600, bg="lightgreen").place(x=500, y=100) # MINI WINDOW OF SMARTPHONES RECORD

    p1 = Button(frame, text=" ADD RECORD ", bg="black", fg="white", font=("arial bold", 16), command=lambda: add(root))

    p1.place(x=510, y=104)

    p1 = Button(root, text=" DELETE RECORD ", bg="black", fg="white", font=("arial bold", 16),command=lambda: delete(root))

    p1.place(x=695, y=104)

    p1 = Button(frame, text=" UPDATE RECORD", bg="black", fg="white", font=("arial bold", 16), command=lambda: update(root))

    p1.place(x=915, y=104)

    p1 = Button(frame, text=" SEARCH RECORD ", bg="black", fg="white", font=("arial bold", 16),command=lambda: search(root))

    p1.place(x=1130, y=104)

    p1 = Button(frame, text=" DELETE ALL RECORDS ", bg="black", fg="white", font=("arial bold", 16), command=lambda: delete_all(root))

    p1.place(x=1050, y=650)

    p1 = Button(frame, text=" SHOW ALL RECORDS ", bg="black", fg="white", font=("arial bold", 16),command=lambda: showall(root))
    p1.place(x=515, y=650)



############################        THIS FUNCTION DISPLAYS A SPECIFIC  RECORD     ############################

def display(root , showallindex , temp_list) :     # CALLED IN VARIOUS OTHER FUNCTIONS

    name = temp_list[showallindex][0]

    color = temp_list[showallindex][1]

    price = temp_list[showallindex][2]

    mp = temp_list[showallindex][3]

    ram = temp_list[showallindex][4]

    phone(root)

    Label(root, text=" RECORD NUMBER %s " % (showallindex + 1), font="ariel 20 bold ", bg="black", fg="white",
          bd=7, width=30).place(x=750, y=170)

    Label(root, text=" Phone Name ", font="ariel 14 bold ").place(x=550, y=250)

    Label(root, text=" %s " % name, bd=7, width=40).place(x=800, y=250)

    Label(root, text=" Color  ", font="ariel 14 bold ").place(x=550, y=300)

    Label(root, text=" %s " % color, bd=7, width=40).place(x=800, y=300)

    Label(root, text=" Price ", font="ariel 14 bold ").place(x=550, y=350)

    Label(root, text=" %s " % price, bd=7, width=40).place(x=800, y=350)

    Label(root, text=" Rear Camera MP  ", font="ariel 14 bold ").place(x=550, y=400)

    Label(root, text=" %s " % mp, bd=7, width=40).place(x=800, y=400)

    Label(root, text=" RAM SIZE", font="ariel 14 bold ").place(x=550, y=450)

    Label(root, text=" %s " % ram, bd=7, width=40).place(x=800, y=450)



#################                 WHEN USER HITS TH PREV BUTTON                #################################


def navigateprev(root, showallindex , temp_list):

    try:

        breakcount = 1
        if showallindex > 0 :  # if index is present in the file !!

            showallindex -= 1       # decrementing the index by 1

            if (showallindex) in delete_index_list:  # if the record was deleted by the user

                navigateprev(root, showallindex, temp_list)
                breakcount = 0

            if showallindex < 0 :     # even the very first record has been shown
                i - s

            if breakcount :

                display(root ,showallindex ,temp_list)
                Button(root, text=" NEXT ", font=" ariel 14 bold ",
                       command = lambda: navigatenext(root, showallindex, temp_list)).place( x=950, y=550)

                Button(root, text=" PREV ", font=" ariel 14 bold ",
                       command = lambda: navigateprev(root, showallindex, temp_list)).place( x=850,  y=550)

                Button(root, text=" CLOSE ", font=" ariel 14 bold", command=lambda: phone(root)).place(x=1100, y=550)


        else :    # if user is on first record and tries to see the previous record

                    messagebox.showinfo(" important message ! " , " No Previous records  !!")
                    phone(root)

    except:

        messagebox.showinfo(" important message ! ", " Error in displaying the previous record !!")



######################      *       #################################     *     ######################

def navigatenext(root , showallindex ,temp_list):    # when user hits the  NEXT  button

        try :

            if  showallindex < len(temp_list) :         # if index is present in the file !!

                showallindex += 1
                global delete_index_list
                breakcount = 1
                print(" delete index list :",delete_index_list)
                print("showallindex :", showallindex)


                if showallindex >= len(temp_list):   # chcking if it crosses the last element index
                    print(" yes ...)")
                    i - s             # control will go to the except block


                if (showallindex) in delete_index_list :  # if the record was deleted by the user

                    navigatenext(root,showallindex , temp_list)
                    breakcount = 0


                print("showallindex new : ", showallindex)


                print(temp_list)

                if breakcount :   # this checks if index has not been deleted earlier

                    display(root, showallindex, temp_list)

                    Button(root, text=" NEXT ", font=" ariel 14 bold ",
                           command=lambda: navigatenext(root, showallindex, temp_list)).place(x=950, y=550)

                    Button(root, text=" PREV ", font=" ariel 14 bold ",
                           command=lambda: navigateprev(root, showallindex, temp_list)).place(x=850, y=550)

                    Button(root, text=" CLOSE ", font=" ariel 14 bold", command=lambda: phone(root)).place(x=1100, y=550)


        except Exception as e:

            messagebox.showinfo(" important message ! ", " all records shown !!")
            print(str(e))


##########################         WHWNEVER USER HITS THE SHOW ALL BUTTON ,CONTROL REACHES HERE !           ###########################


def showall(root):

            try :

                phone(root)
                temp_list = []
                global showallindex
                showallindex = 0

                with open("phone.bin", "rb") as myFile:

                    while 1:

                        try:
                            temp_list = pickle.load(myFile)
                            print(temp_list)

                        except(EOFError):

                            print("entered in eof error block")
                            break

                        except:  # in case file initially, has no content

                            temp_list = []
                            messagebox.showinfo("  ********* IMPPORTANT MESSAGE ******** ", " NO RECORD TO SHOW !")
                            phone(root)
                            break  # coming out of the loop

                if len(delete_index_list) == len(temp_list):  # if all the records have been deleted by the user
                    error

                if (showallindex) in delete_index_list:  # if the first record was deleted by the user

                    navigatenext(root, showallindex, temp_list)

                display(root, showallindex, temp_list)  # calling the display function to display the records


                Button(root, text=" NEXT ", font=" ariel 14 bold ",
                       command=lambda: navigatenext(root, showallindex, temp_list)).place(x=950, y=550)


                Button(root, text=" PREV ", font=" ariel 14 bold ",
                       command=lambda: navigateprev(root, showallindex, temp_list)).place(x=850, y=550)


                Button(root, text=" CLOSE ", font=" ariel 14 bold", command=lambda: phone(root)).place(x=1100, y=550)

            except :

                 messagebox.showinfo( "  *******  IMPORTANT MESSAGE  ****** " , " NO RECORD TO SHOW !! ")

##########################         WHWNEVER USER HITS THE DELETE ALL BUTTON ,CONTROL REACHES HERE !           ###########################


def delete_all(root):

    phone(root)

    Label(root, text=" ARE YOU SURE ? ", font="ariel 14 bold", bg='black', fg='white').place(x=750, y=200)


    Button(root, text="  Yes  ", font="ariel 14 bold", bg='black', fg='white', command=lambda: truncfile(root)).place(x=750, y=250)

    Button(root, text="  No  ", font="ariel 14 bold", bg='black', fg='white', command=lambda: phone(root)).place(x=850,y=250)


    def truncfile(root):

        with open("phone.bin", "wb") as pfile:

            pfile.truncate()

        with open("deletedentries", "wb") as pfile:  # also we will have to truncate this file

            pfile.truncate()


        with open("finalphone.txt", "w+") as pfile:

            pfile.truncate()

        global delete_index_list , count

        delete_index_list.clear()
        count = -1
        phone(root)

        messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORDS HAVE BEEN DELETED ! ')
        phone(root)



##########################         WHWNEVER USER HITS THE ADD RECORD BUTTON ,CONTROL REACHES HERE !           ###########################


def add(root):

    phone(root)
    mystring1.set("")        # SETTING VALUES TO NOTHING SO THAT ENTRY BOXES BECOME EMPTY WHENEVER THE BUTTON IS CLICKED AGAIN
    mystring2.set("")
    mystring3.set("")
    mystring4.set("")
    mystring5.set("")

    add1 = Label(root, text=" Phone Name ", font="ariel 14 bold ").place(x=550, y=200)

    entry1 = Entry(root, textvariable=mystring1, bd=7, width=40).place(x=800, y=200)


    add2 = Label(root, text=" Color  ", font="ariel 14 bold ").place(x=550, y=250)

    entry2 = Entry(root, textvariable=mystring2, bd=7, width=40).place(x=800, y=250)

    add3 = Label(root, text=" Price ", font="ariel 14 bold ").place(x=550, y=300)

    entry3 = Entry(root, textvariable=mystring3, bd=7, width=40).place(x=800, y=300)

    add1 = Label(root, text=" Rear Camera MP  ", font="ariel 14 bold ").place(x=550, y=350)

    entry4 = Entry(root, textvariable=mystring4, bd=7, width=40).place(x=800, y=350)

    add1 = Label(root, text=" RAM SIZE", font="ariel 14 bold ").place(x=550, y=400)

    entry5 = Entry(root, textvariable=mystring5, bd=7, width=40).place(x=800, y=400)

    def e5():  # this function is called when add information button is clicked by the user

        add_list = []
        temp_list = []
        add1_list = []

        if  mystring1.get()!="" and mystring2.get()!="" and mystring3.get()!="" and mystring4.get()!="" and mystring5.get()!="" :  # to make sure no entry box is left empty

            add_list.append(mystring1.get())
            add_list.append(mystring2.get())
            add_list.append(mystring3.get())
            add_list.append(mystring4.get())
            add_list.append(mystring5.get())
            global add_dict, count

            if count > -1:           # IF RECORDS ARE PRESENT IN THE FILE INITIALLY

                print("initial count in add  :", count)

                with open("phone.bin", "rb") as myFile:


                    while 1:

                        try:

                            temp_list = pickle.load(myFile)

                        except(EOFError):

                            break

                        except:  # in case file initially, has no content

                            temp_list = []
                            break  # coming out of the loop

                count = len(temp_list)-1
                add_dict.clear()  # clearing the list so that new data can be stored
                add_dict = temp_list[:]  # cloning the list
                add_dict.append(add_list)  # adding the add list to the add dict list

                count += 1
                r = str(count + 1)  # for serial number

                with open("phone.bin", "ab") as myFile:

                    pickle.dump(add_dict, myFile)  # this statement dumps the data of the list add_list into the file phone.txt


                transfer()      # content gets transferred to text file


            else:     # if there is no record in the file !

                count = 0
                r = str(count + 1)  # for serial number

                with open("phone.bin", "ab") as myFile:

                    add1_list.append(add_list)
                    pickle.dump(add1_list, myFile)  # this statement dumps the data of the list add_list into the file phone.txt


                transfer()  # content gets transferred to text file

            print("add dict which is being written in file : ", add1_list)  # checking purpose

            pfile = open("phone.bin", "r")  # opens the file in read mode

            messagebox.showinfo('        ******** NOTIFICATION ********'," Your Information has been added and your \n INFORMATION SERIAL NUMBER IS : %s  !!!" % r)

            addbutton = Button(root, text=" ADD MORE ", font=" ariel 16 bold", width=22,command=lambda: add(root)).place(x=900, y=500)


        else :     # case where user leaves an entry box empty

            messagebox.showinfo(" ******Important Message ******* " , " ENTER THE DETAILS PROPERLY !! ")
            add(root)

    Button(root, text=" ADD THE INFORMATION ", font=" ariel 16 bold", command=e5).place(x=900,y=500)



##########################         WHWNEVER USER HITS THE DELETE RECORD BUTTON ,CONTROL REACHES HERE !           ###########################

def delete(root):  # delete function which deletes the record when delte button is clicked by the user

    phone(root)
    pfile = open("phone.bin", 'rb')  # opening file in read binary mode

    global retrieve, retrieveback
    retrieve.clear()  # erasing initial stored data so that new data from the list which got edited at some point can be stored


    while 1:

        try:  # till the end of file is reached

            retrieveback = pickle.load(pfile)

        except (EOFError):  # when file reaches its end

            break  # go out of while loop

        except:

            messagebox.showinfo(' IMPORTANT MESSAGE !! ', "  RECORD CAN NOT BE DELETED .FILE IS EMPTY !!")
            phone(root)
            break


    deletestring.set("")

    retrieve = retrieveback[:]

    pfile.close()

    phone(root)

    Label(root, text=" ENTER THE SERIAL NUMBER  ", font=" ariel 17 bold ").place(x=550, y=250)

    Entry(root, textvariable=deletestring, bd=13).place(x=1000, y=250)

    Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: tempdel(root)).place(x=800, y=350)  # if okay button is clicked then temp del function is called


    def tempdel(root):

        phone(root)

        Label(root, text=" ARE YOU SURE THAT YOU WANT TO DELETE ? ", font="ariel 14 bold", bg='black', fg='white').place(x=750, y=200)

        Button(root, text="  Yes  ", font="ariel 14 bold", bg='black', fg='white',command=lambda: confirm_delete(root)).place(x=750, y=250)

        Button(root, text="  No  ", font="ariel 14 bold", bg='black', fg='white', command=lambda: phone(root)).place(x=850, y=250)

        def confirm_delete(root):  # if the user hits the yes button

            global delete_index_list

            try:

                index = int(deletestring.get()) - 1  # Index = (index entered by the user -1)


                if index in delete_index_list:  # in case record was already been deleted

                    phone(root)
                    messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD HAS ALREADY BEEN DELETED ! ')
                    phone(root)


                else:

                    if count < 0:  # case when file is empty and user tries to search for record

                        messagebox.showinfo(' IMPORTANT MESSAGE !! ', " NO RECORD IS PRESENT IN THE FILE !")
                        phone(root)


                    else:  # if user tries to delete some records  in a non-empty file !

                        if index in range(0, len(retrieve)):  # if user enters the index present in file !

                            global delete_count
                            delete_index_list.clear()


                            with open("deletedentries", "rb") as dfile:

                                while 1:

                                    try:
                                        delete_index_list = pickle.load(dfile)

                                    except:  # In case when initially file is  empty
                                        break

                            delete_count = len(delete_index_list)
                            delete_index_list.insert(delete_count, index)


                            with open("deletedentries", "wb") as dfile:
                                pickle.dump(delete_index_list, dfile)

                            retrieve.pop(index)  # deleting desired index record
                            retrieve.insert(index, [0])


                            with open("phone.bin", "wb+") as pfile:  # here we are deleting the old content of file and adding the new updated content

                                pfile.truncate()
                                pickle.dump(retrieve, pfile)


                            transfer()   # content will be transfered to text file

                            phone(root)

                            messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD HAS BEEN DELETED ! ')

                            phone(root)


                        else:  # if user tries to delete a record which is not present in the file

                            messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD NOT FOUND ! ')
                            phone(root)

            except:  # control will come in this block if user enters a string in the serial number entry box

                messagebox.showinfo(' IMPORTANT MESSAGE !! ', " PLEASE ENTER A VALID SERIAL NUMBER  !")
                phone(root)



##########################         WHWNEVER USER HITS THE SEARCH RECORD BUTTON ,CONTROL REACHES HERE !           ###########################

def search(root):

    phone(root)

    searchstring.set("")

    print("search string is : ", searchstring.get())

    Label(root, text=" ENTER THE SERIAL NUMBER  ", font=" ariel 17 bold ").place(x=550, y=250)

    Entry(root, textvariable=searchstring, bd=13).place(x=1000, y=250)

    Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: tempsearch()).place(x=800, y=350)


    def tempsearch():

        global delete_index_list , count
        search_retrieve = []
        searchretrieve_back = []

        try:

            index = int(searchstring.get()) - 1


            if count < 0:  # case when file is empty and user tries to search for record

                messagebox.showinfo(' IMPORTANT MESSAGE !! ', " NO RECORD IS PRESENT IN THE FILE !")
                phone(root)


            else:  # in case when file has content i.e. , the file is not empty

                with open("deletedentries", "rb") as dfile:

                    while 1:

                        try:

                            delete_index_list = pickle.load(dfile)


                        except:  # In case when initially file is  empty

                            break


                if index in delete_index_list:  # if user deleted a record and is searching for the same

                    phone(root)
                    messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD WAS DELETED  SO YOU CAN\'T SEARCH FOR IT!! ')
                    phone(root)

                else:  # otherwise the normal searching process

                    pfile = open("phone.bin", 'rb')
                    searchretrieve_back.clear()  # to delete the previous content so that new can be loaded

                    while 1:

                        try:  # till the end of file is reached

                            searchretrieve_back = pickle.load( pfile)  # loading the data from the file to the list named search_retrieve

                        except (EOFError):  # when file reaches its end

                            break  # go out of while loop

                    search_retrieve = searchretrieve_back[:]
                    pfile.close()


                    if index in range(0, len(search_retrieve)):        # if record is present in file

                        display(root , index , search_retrieve)         # calling the display function to display the record

                    else:         # if record is not in the file

                        messagebox.showinfo(' IMPORTANT MESSAGE !! ', " SEARCHED RECORD IS NOT IN THE FILE !")
                        phone(root)

        except:  # control will come in this block if user enters a string in the serial number entry box

            messagebox.showinfo(' IMPORTANT MESSAGE !! ', " PLEASE ENTER A VALID SERIAL NUMBER  !")
            phone(root)



##########################         WHWNEVER USER HITS THE UPDATE BUTTON ,CONTROL REACHES HERE !           ###########################

def update(root):

    phone(root)

    updatestring = StringVar(root)
    upstring1 = StringVar(root)
    upstring2 = StringVar(root)
    upstring3 = StringVar(root)
    upstring4 = StringVar(root)
    upstring5 = StringVar(root)

    upstring1.set("")  # so that user comes to that particular window , the entry boxes are empty
    upstring2.set("")
    upstring3.set("")
    upstring4.set("")
    upstring5.set("")

    phone(root)

    Label(root, text=" ENTER THE SERIAL NUMBER  ", font=" ariel 17 bold ").place(x=550, y=250)

    Entry(root, textvariable=updatestring, bd=13).place(x=1000, y=250)

    Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: tempupdate(root)).place(x=800, y=350)


    def tempupdate(root):

        temp_list = []

        try:

            index = int(updatestring.get()) - 1

            with open("phone.bin", "rb") as pfile:

                while 1:  # this block is used to load all the content of main file (phone.bin) in the temp list

                    try:

                        temp_list = pickle.load( pfile)  # this list is used in this method to count the no of records in file

                    except:  # In case when either the file is empty  initially or it reaches END OF FILE
                        break


            if index in range(0, len(temp_list)):  # if the index entered by the user is  present in the file

                if count < 0:  # case when file is empty and user tries to update a record

                    messagebox.showinfo(' IMPORTANT MESSAGE !! ', " NO RECORD IS PRESENT IN THE FILE !")
                    phone(root)


                else:  # when file has some content to be updated

                    global delete_index_list

                    with open("deletedentries", "rb") as dfile:

                        while 1:  # this block is used to load the content of 'delete file' in delete index list

                            try:

                                delete_index_list = pickle.load(dfile)

                            except:  # In case when initially file is  empty OR when it reaches the end of file

                                break


                    if index in delete_index_list:  # if user deleted a record and wants to update the same

                        phone(root)
                        messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD WAS DELETED  SO YOU CAN\'T UPDATE IT!! ')
                        phone(root)


                    else:

                        phone(root)

                        Label(root, text="New Phone Name ", font="ariel 14 bold ").place(x=550, y=200)

                        Entry(root, textvariable=upstring1, bd=7, width=40).place(x=800, y=200)

                        Label(root, text="New Color  ", font="ariel 14 bold ").place(x=550, y=250)

                        Entry(root, textvariable=upstring2, bd=7, width=40).place(x=800, y=250)

                        Label(root, text="New Price ", font="ariel 14 bold ").place(x=550, y=300)

                        Entry(root, textvariable=upstring3, bd=7, width=40).place(x=800, y=300)

                        Label(root, text="New Rear Camera MP  ", font="ariel 14 bold ").place(x=550, y=350)

                        Entry(root, textvariable=upstring4, bd=7, width=40).place(x=800, y=350)

                        Label(root, text="New RAM Size ", font="ariel 14 bold ").place(x=550, y=400)

                        Entry(root, textvariable=upstring5, bd=7, width=40).place(x=800, y=400)

                        Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: doneupdate(root)).place(x=900, y=550)


                        def doneupdate(root):

                            update_retrieve = []

                            with open("phone.bin", "rb") as pfile:

                                while 1:

                                    try:

                                        update_retrieve = pickle.load(pfile)

                                    except (EOFError):

                                        break


                            print("update after reading from file :", update_retrieve)

                            update_retrieve[index][0] = upstring1.get()

                            update_retrieve[index][1] = upstring2.get()

                            update_retrieve[index][2] = upstring3.get()

                            update_retrieve[index][3] = upstring4.get()

                            update_retrieve[index][4] = upstring5.get()


                            with open("phone.bin", "wb") as pfile:

                                pfile.truncate()
                                pickle.dump(update_retrieve, pfile)


                            transfer()    # content will be tranfered to text file

                            display(root , index , update_retrieve)            # calling the display function to display the record

                            Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: phone(root)).place(x=900, y=500)


            else:  # if the index entered by the user is not present in the file

                messagebox.showinfo(' IMPORTANT MESSAGE !! ', "  RECORD IS NOT IN THE FILE !")
                phone(root)

        except:

            messagebox.showinfo(' IMPORTANT MESSAGE !! ', "  PLEASE ENTER A VALID SERIAL NUMBER !! ")
            phone(root)



##########################         WHWNEVER USER HITS THE FEEDBACK BUTTON ,CONTROL REACHES HERE !           ###########################

def feedback(root):         # DEFINITION OF THE METHOD BEGINS

    feed_list = []

    mainwindow(root)

    Label(root, text=" FEEDBACK ", font=("arial", 15)).place(x=15, y=370)

    txt = scrolledtext.ScrolledText(root, width=40, height=10)
    txt.place(x=10, y=400, )

    Button(root, text=" DONE ", command=lambda: clearfeed(root)).place(x=300, y=580)


    def clearfeed(root):

        txt.insert(END, " \n\n\n Thank You !! \n Your Feedback holds importance for us !\n\n")

        Button(root, text=" OKAY ", command=lambda: mainwindow(root)).place(x=300, y=580)
        '''txt.get(1.0 ,feed_list)
        print(feed_list)'''



##########################         THIS FUNCTION TRANSFERS ALL THE CONTET FROM TH BINARY FILE TO THE TEXT FILE           ###########################

def transfer():       # this method transfers content of binary file to text file

    global a
    filecount = 0


    with open("phone.bin", "rb") as pfile:

        while 1:

            try:

               a = pickle.load(pfile)

            except (EOFError) :

              break

    with open("finalphone.txt", "w") as textfile:

            textfile.truncate()


    while filecount<len(a):

        try:

            with open("finalphone.txt", "a") as textfile:

                str1 = a[filecount][0]
                str2 = a[filecount][1]
                str3 = a[filecount][2]
                str4 = a[filecount][3]
                str5 = a[filecount][4]
                totalspace =20
                print("1 : %d\n " % filecount, str1, str2, str3, str4, str5)
                ind = str(filecount+1)
                textfile.write(" RECORD NO. ")
                textfile.write(ind)
                textfile.write(" :  ")
                textfile.write(str1)
                textfile.write(" "*(totalspace-len(str1)) )
                textfile.write(str2)
                textfile.write(" "*(totalspace-len(str2)) )
                textfile.write(str3)
                textfile.write(" "*(totalspace-len(str3)) )
                textfile.write(str4)
                textfile.write(" "*(totalspace-len(str4)) )
                textfile.write(str5)
                textfile.write("\n \n")
                filecount += 1

        except :  # when deleted record is referred

                 filecount += 1
                 continue


###########################         WHWNEVER USER HITS THE QUIT BUTTON ,CONTROL REACHES HERE !           ###########################

def quit(root) :  # WHEN USER HITS QUIT BUTTON

    root.destroy()  # root get destroys and tkinter window shuts down


##########################      THIS BLOCK IS RESPONSIBLE FOR CALLING THE MAIN WINDOW FRAME OF TKINTER           ###########################

mainwindow(root)

root.title("Welcome to Priya's project")  # renames the title of the tkinter window

root.geometry('300x300')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

root.geometry("%dx%d+0+0" % (w, h))  # this statement opens the tkinter window in maximized form

mainloop()