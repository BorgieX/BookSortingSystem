from tkinter import *
from functools import partial

def cleartext():
   usernameEntry.delete(0, END)
   passwordEntry.delete(0, END)

def clearregistertext():
    UsernameEntry.delete(0, END)
    PasswordEntry.delete(0, END)

def clearaddtext():
    BookNameEntry.delete(0, END)
    GenreEntry.delete(0, END)
    AuthorEntry.delete(0, END)
    IllistratorEntry.delete(0, END)  

def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get(), "\n")

    notfound = False

    for line in open("Login.txt", "r").readlines():

        login_info = line.split()
        if username.get() == login_info[0] and password.get() == login_info[1]:
            print("Login Sucessful")
            showmainmenu()
            hidelogin()
            break
        else:
            notfound = True
        
    if notfound:
        hidelogin()
        LoginFails()

def LoginFails():
    global LoginFail

    LoginFail = Tk()
    LoginFail.deiconify()
    LoginFail.title("Register Failure")
    LoginFail.geometry("200x200")
    LoginFail.resizable(width=False, height=False)
    LoginFail.configure(bg="grey")
    LoginFailLabel = Label(LoginFail, text="Login Not Found")
    LoginFailLabel.place(x=80, y=80)
    LoginFailButton = Button(LoginFail, text="Ok", command=lambda:[HideLoginFail(), showlogin()])
    LoginFailButton.place(x=80, y=125)

def HideLoginFail():
    LoginFail.withdraw()

def showmainmenu():
    global mainmenu
    mainmenu = Tk()
    mainmenu.deiconify()
    mainmenu.title("Main Menu")
    mainmenu.geometry("400x400")
    mainmenu.resizable(width=False, height=False)
    mainmenu.configure(bg="grey")

    LogoutButton = Button(mainmenu, text="Logout",command=lambda:[hidemainmenu(), showlogin()], width=15, height=1)
    LogoutButton.place(x=140, y=360)

    SearchButton = Button(mainmenu, text="Search",command=lambda:[hidemainmenu(), showsearchmenu()], width=15, height=3)
    SearchButton.place(x = 140, y = 50)

    BorrowButton = Button(mainmenu, text="Borrowed",command=lambda:[hidemainmenu(), showborrowmenu()], width=15, height=3)
    BorrowButton.place(x = 140, y = 120)

    AddButton = Button(mainmenu, text="Add",command=lambda:[hidemainmenu(), showaddmenu()], width=15, height=3)
    AddButton.place(x = 140, y = 190)

    DeleteButton = Button(mainmenu, text="Delete",command=lambda:[hidemainmenu(), showdeletemenu()], width=15, height=3)
    DeleteButton.place(x = 140, y = 260)

def showregistermenu():
    global Registermenu
    global UsernameEntry
    global PasswordEntry

    Registermenu = Tk()
    Registermenu.deiconify()
    Registermenu.title("Register")
    Registermenu.geometry("400x400")
    Registermenu.resizable(width=False, height=False)
    Registermenu.configure(bg="grey")
    BackButton = Button(Registermenu, text="Back",command=lambda:[hideregistermenu(), showlogin()])
    BackButton.place(x=0, y=350)

    UsernameEntry = Entry(Registermenu, width=50)
    UsernameEntry.place(x=50, y=185)
    usernamelabel = Label(Registermenu, text="Username")
    usernamelabel.place(x=170, y=200)

    PasswordEntry = Entry(Registermenu, width=50)
    PasswordEntry.place(x=50, y=245)
    passwordlabel = Label(Registermenu, text="Password")
    passwordlabel.place(x=170, y=260)

    RegisterButton = Button(Registermenu, text="Register",command=lambda:[ConfirmRegister(), hideregistermenu()])
    RegisterButton.place(x=173, y=300)

def ConfirmRegister():
    global ConfirmReg
    global RegisterFail
    username = UsernameEntry.get()
    password = PasswordEntry.get()
    found = False

    with open("Login.txt", "r") as file:
        for line in file.readlines():
            login_info = line.strip().split()
            if username == login_info[0] or password == login_info[1]:
                found = True
                break
   
    if found:
        RegisterFail = Tk()
        RegisterFail.title("Register Failure")
        RegisterFail.geometry("200x200")
        RegisterFail.resizable(width=False, height=False)
        RegisterFail.configure(bg="grey")
        RegFailLabel = Label(RegisterFail, text="Username or password already in use")
        RegFailLabel.place(x=80, y=80)
        RegFailButton = Button(RegisterFail, text="Ok", command=lambda:[HideRegFail(), showregistermenu()])
        RegFailButton.place(x=80, y=125)
    else:
        ConfirmReg = Tk()
        ConfirmReg.title("Register Complete")
        ConfirmReg.geometry("200x200")
        ConfirmReg.resizable(width=False, height=False)
        ConfirmReg.configure(bg="grey")
        ConfirmLabel = Label(ConfirmReg, text="Account Registered")
        ConfirmLabel.place(x=80, y=80)
        ConfirmButton = Button(ConfirmReg, text="Ok", command=lambda:[HideConfirmRegister(), showregistermenu(), registertofile(), ReturnEntry(), clearregistertext()])
        ConfirmButton.place(x=80, y=125)

def HideConfirmRegister():
    ConfirmReg.withdraw()

def HideRegFail():
    RegisterFail.withdraw()


def ReturnEntry():
    return UsernameEntry
    return PasswordEntry

def registertofile():
    LoginFile=open("Login.txt", "a")
    LoginFile.write(UsernameEntry.get())
    LoginFile.write(" ")
    LoginFile.write(PasswordEntry.get())
    LoginFile.write("\n")
    LoginFile.close()

def hideregistermenu():
    Registermenu.withdraw()

def hidemainmenu():
    mainmenu.withdraw()

def hidelogin():
    LoginPage.withdraw()

def showlogin():
    LoginPage.deiconify()

def showsearchmenu():
    global searchmenu
    global SearchEntry
    searchmenu = Tk()
    searchmenu.deiconify()
    searchmenu.title("Search")
    searchmenu.geometry("400x400")
    searchmenu.resizable(width=False, height=False)
    searchmenu.configure(bg="grey")
    Back = Button(searchmenu, text="Back",command=lambda:[hidesearchmenu(), showmainmenu()])
    Back.place(x = 0, y = 375)
    SearchButton = Button(searchmenu, text="Search",command=lambda:[hidesearchmenu(), FilterWrite(), ShowBookList()], width=15, height=2)
    SearchButton.place(x = 150, y = 200)
    SearchEntry = Entry(searchmenu, width=50)
    SearchEntry.place(x = 60, y = 150)
    EnterName = Label(searchmenu, text="Enter Book Name")
    EnterName.place(x = 155, y = 110)


def FilterWrite():
    open("FilterSearch.txt",'w').writelines([ line for line in open("BookList.txt") if SearchEntry.get() in line])

def ShowBookList():
    global booklist
    global searchbooks
    booklist = Tk()
    booklist.deiconify()
    booklist.title("Booklist")
    booklist.geometry("600x800")
    booklist.configure(bg="grey")
    booklist.resizable(width=False, height=False)
    Back = Button(booklist, text="Back",command=lambda:[hidebooklist(), showsearchmenu(), clearfiltersearch()])
    Back.place(x = 0, y = 775)
    searchbooks = Text(booklist, wrap=WORD, width=80, height= 25)
    searchbooks.place(x=0, y=0)
    IndexEntry = Entry(booklist,width=55)
    IndexEntry.place(x=130, y=500)
    BorrowButton = Button(booklist, text="Borrow", command=lambda: BorrowBook(int(IndexEntry.get())), width=15, height=2)
    BorrowButton.place(x=235, y=550)
    EnterIndex = Label(booklist, text="Enter Index")
    EnterIndex.place(x = 260, y = 470)
    with open("FilterSearch.txt", "r") as books:
        searchbooks.insert(INSERT, books.read())
        searchbooks.config(state=DISABLED)

def BorrowBook(index):
    with open("FilterSearch.txt", "r") as filter_search_file:
        filter_search_lines = filter_search_file.readlines()

    with open("Booklist.txt", "r") as booklist_file:
        booklist_lines = booklist_file.readlines()
    if 1 <= index <= len(filter_search_lines):
        borrowed_book = filter_search_lines.pop(index - 1)
        with open("FilterSearch.txt", "w") as filter_search_file:
            filter_search_file.writelines(filter_search_lines)

        # Remove the book from the original book list as well
        book_to_remove = booklist_lines.pop(index - 1)
        with open("Booklist.txt", "w") as booklist_file:
            booklist_file.writelines(booklist_lines)

        with open("BorrowedBooks.txt", "a") as borrowed_file:
            borrowed_file.write(borrowed_book)

    # Refresh the displayed book list
    searchbooks.config(state=NORMAL)
    searchbooks.delete(1.0, END)
    searchbooks.insert(INSERT, ''.join(filter_search_lines))
    searchbooks.config(state=DISABLED)
    
def clearfiltersearch():
    with open("FilterSearch.txt",'r+') as file:
        file.truncate(0)
        file.close()

def hidebooklist():
    booklist.withdraw()
    
def hidesearchmenu():
    searchmenu.withdraw()

def showborrowmenu():
    global borrowmenu
    global searchbooks
    borrowmenu = Tk()
    borrowmenu.deiconify()
    borrowmenu.resizable(width=False, height=False)
    borrowmenu.title("Borrow")
    borrowmenu.geometry("600x800")
    borrowmenu.configure(bg="grey")
    Back = Button(borrowmenu, text="Back",command=lambda:[hideborrowmenu(), showmainmenu()])
    Back.place(x = 0, y = 775)
    searchbooks = Text(borrowmenu, wrap=WORD, width=80, height= 25)
    searchbooks.place(x=0, y=0)
    Return = Button(borrowmenu, text="Return", command=lambda:ReturnBook(int(IndexEntry.get())), width=15, height=2)
    Return.place(x=235, y=550)
    IndexEntry = Entry(borrowmenu, width = 55)
    IndexEntry.place(x=130, y=500)
    EnterIndex = Label(borrowmenu, text="Enter Index")
    EnterIndex.place(x = 260, y = 470)
    with open("BorrowedBooks.txt", "r") as books:
        searchbooks.insert(INSERT, books.read())
        searchbooks.config(state=DISABLED)

def ReturnBook(index):
    with open("BorrowedBooks.txt", "r") as filter_search_file:
        filter_search_lines = filter_search_file.readlines()

    with open("BorrowedBooks.txt", "r") as booklist_file:
        booklist_lines = booklist_file.readlines()

    if 1 <= index <= len(filter_search_lines):
        borrowed_book = filter_search_lines.pop(index - 1)
        with open("BorrowedBooks.txt", "w") as filter_search_file:
            filter_search_file.writelines(filter_search_lines)

        # Remove the book from the original book list as well
        book_to_remove = booklist_lines.pop(index - 1)
        with open("BorrowedBooks.txt", "w") as booklist_file:
            booklist_file.writelines(booklist_lines)

        with open("Booklist.txt", "a") as borrowed_file:
            borrowed_file.write(borrowed_book)

    # Refresh the displayed book list
    searchbooks.config(state=NORMAL)
    searchbooks.delete(1.0, END)
    searchbooks.insert(INSERT, ''.join(filter_search_lines))
    searchbooks.config(state=DISABLED)

def hideborrowmenu():
    borrowmenu.withdraw()

def showaddmenu():
    global addmenu
    global BookNameEntry
    global GenreEntry
    global AuthorEntry
    global IllistratorEntry
    
    addmenu = Tk()
    addmenu.deiconify()
    addmenu.resizable(width=False, height=False)
    addmenu.title("Add")
    addmenu.geometry("400x400")
    addmenu.configure(bg="grey")
    Back = Button(addmenu, text="Back",command=lambda:[hideaddmenu(), showmainmenu()])
    Back.place(x = 0, y = 375)
    
    BookNameEntry = Entry(addmenu)
    BookNameEntry.place(x = 140, y = 50)
    BookNameLabel = Label(addmenu, text = "Book Name")
    BookNameLabel.place(x = 170, y = 25)

    GenreEntry = Entry(addmenu)
    GenreEntry.place(x = 140, y = 100)
    GenreLabel = Label(addmenu, text = "Genre")
    GenreLabel.place(x = 170, y = 75)

    AuthorEntry = Entry(addmenu)
    AuthorEntry.place(x = 140, y = 150)
    AuthorLabel = Label(addmenu, text = "Author")
    AuthorLabel.place(x = 170, y = 125)

    IllistratorEntry = Entry(addmenu)
    IllistratorEntry.place(x = 140, y = 200)
    IllistratorLabel = Label(addmenu, text = "Illistrator")
    IllistratorLabel.place(x = 170, y = 175)

    AddButton = Button(addmenu, text = "Add", command = lambda:[ReturnBookEntry(), AddBook(), BookAddedLabel(), clearaddtext()])
    AddButton.place(x = 170, y = 250)

def BookAddedLabel():
    BookAddedLabel = Label(addmenu, text = "Book Added")
    BookAddedLabel.place(x = 150, y = 300)

def ReturnBookEntry():
    return BookNameEntry
    return GenreEntry
    return AuthorEntry
    return IllistratorEntry

def AddBook():
    AddBookFile = open("BookList.txt" , "a")
    AddBookFile.write(BookNameEntry.get() + " | ")
    AddBookFile.write(GenreEntry.get() + " | ")
    AddBookFile.write(AuthorEntry.get() + " | ")
    AddBookFile.write(IllistratorEntry.get() + " ")
    AddBookFile.write("\n")
    AddBookFile.close()

def hideaddmenu():
    addmenu.withdraw()

def showdeletemenu():
    global deletemenu
    global searchbooks
    global IndexEntry

    deletemenu = Tk()
    deletemenu.deiconify()
    deletemenu.title("Delete")
    deletemenu.resizable(width=False, height=False)
    deletemenu.geometry("600x800")
    deletemenu.configure(bg="grey")
    searchbooks = Text(deletemenu, wrap=WORD, width=70, height= 25)
    searchbooks.place(x=0, y=0)
    with open("BookList.txt", "r") as books:
        searchbooks.insert(INSERT, books.read())
        searchbooks.config(state=DISABLED)
    
    IndexEntry = Entry(deletemenu, width = 55)
    IndexEntry.place(x=130, y=500)

    Back = Button(deletemenu, text="Back",command=lambda:[hidedeletemenu(), showmainmenu()])
    Back.place(x = 0, y = 775)
    Delete = Button(deletemenu, text="Delete", command=lambda:[ConfirmDelete(), hidedeletemenu()], width=15, height=2)
    Delete.place(x=235, y=550)
    EnterIndex = Label(deletemenu, text="Enter Index")
    EnterIndex.place(x = 260, y = 470)

def ConfirmDelete():
    global ConfirmDelete1

    ConfirmDelete1 = Tk()
    ConfirmDelete1.deiconify()
    ConfirmDelete1.title("Delete Confirmation")
    ConfirmDelete1.geometry("200x200")
    ConfirmDelete1.resizable(width=False, height=False)
    ConfirmDelete1.configure(bg="grey")

    ConfirmLabel = Label(ConfirmDelete1, text="Are you Sure?")
    ConfirmLabel.place(x=80, y=80)

    YesButton = Button(ConfirmDelete1, text="Yes", command=lambda:[DeleteBook(int(IndexEntry.get())), HideConfirmDelete(), showdeletemenu()])
    YesButton.place(x=80, y=125)
    NoButton = Button(ConfirmDelete1, text="No", command=lambda:[HideConfirmDelete(), showdeletemenu()])
    NoButton.place(x=40, y=125)

def HideConfirmDelete():
    ConfirmDelete1.withdraw()

def DeleteBook(index):
    with open("BookList.txt", "r") as filter_search_file:
        filter_search_lines = filter_search_file.readlines()

    with open("BookList.txt", "r") as booklist_file:
        booklist_lines = booklist_file.readlines()

    if 1 <= index <= len(filter_search_lines):
        borrowed_book = filter_search_lines.pop(index - 1)
        with open("BookList.txt", "w") as filter_search_file:
            filter_search_file.writelines(filter_search_lines)

        # Remove the book from the original book list as well
        book_to_remove = booklist_lines.pop(index - 1)
        with open("BookList.txt", "w") as booklist_file:
            booklist_file.writelines(booklist_lines)

    # Refresh the displayed book list
    searchbooks.config(state=NORMAL)
    searchbooks.delete(1.0, END)
    searchbooks.insert(INSERT, ''.join(filter_search_lines))
    searchbooks.config(state=DISABLED)

def hidedeletemenu():
    deletemenu.withdraw()

# Have to have this for code to work :(
#Login Page

# window
global LoginPage
LoginPage = Tk()
LoginPage.geometry('800x800')
LoginPage.title('Login')
LoginPage.resizable(width=False, height=False)

LoginPage.configure(bg="grey")

TitleLabel = Label(LoginPage, text="Borgies Book Sorter", font=("Arial", 50, "bold"), bg="grey")
TitleLabel.place(x = 80, y = 30)

# username label and text entry box
usernameLabel = Label(LoginPage, text="User Name")
usernameLabel.place(x = 390, y = 170)
username = StringVar()
usernameEntry = Entry(LoginPage, width=50, textvariable=username)
usernameEntry.place(x = 280, y = 220)
# password label and password entry box
passwordLabel = Label(LoginPage, text="Password")
passwordLabel.place(x = 390, y = 300)
password = StringVar()
passwordEntry = Entry(LoginPage, width=50, textvariable=password,show='*')
passwordEntry.place(x = 280, y = 350)

validateLogin = partial(validateLogin, username, password)

# login button
loginButton = Button(LoginPage,  width=50, text="Login",command=lambda:[validateLogin(), cleartext()])
loginButton.place(x = 250, y = 460)
RegisterButton = Button(LoginPage, width=50, text="Register",command=lambda:[showregistermenu(), hidelogin()])
RegisterButton.place(x = 250, y = 500)

LoginPage.mainloop()