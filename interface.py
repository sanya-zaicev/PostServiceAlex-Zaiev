from tkinter import *
from tkinter import ttk
import datetime
import re


class User:
    _id = 0

    _login = ''
    _password = ''
    _name = ''
    _surname = ''
    _phone = None
    _email = None
    _birthdate = None

    _status = 3

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if type(value) != int:
            raise TypeError()
        if value < 0:
            raise ValueError()
        self._id = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        if type(value) != str:
            raise TypeError('sss')
        if len(value) < 8:
            raise TypeError('ss')

        for i in value:
            if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+?/><.,~`':
                raise TypeError('s')
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if type(value) != str:
            raise TypeError()
        if len(value) < 8:
            raise TypeError('sssss')
        for i in value:
            if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+?/><.,~`':
                raise TypeError()
        self._password = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if type(value) != str:
            raise TypeError('sss')
        if len(value) == 0:
            raise TypeError('ss')
        check = [True, True]
        letters_eng = 'abcdefghijklmnopqrstuvwxyz'
        letters_ru = 'абвгдежзийклмнопрстуфхцчшщьыъэюя'
        for i in value:
            if i not in letters_eng:
                check[0] = False
        for i in value:
            if i not in letters_ru:
                check[0] = False
        if not check[0] and not check[1]:
            raise TypeError('ssss')
        if value[0].islower():
            raise TypeError('s')
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value: str):
        if type(value) != str:
            raise TypeError()
        if len(value) == 0:
            raise TypeError()
        check = [True, True]
        letters_eng = 'abcdefghijklmnopqrstuvwxyz'
        letters_ru = 'абвгдежзийклмнопрстуфхцчшщьыъэюя'
        for i in value:
            if i not in letters_eng:
                check[0] = False
        for i in value:
            if i not in letters_ru:
                check[0] = False
        if not check[0] and not check[1]:
            raise TypeError()
        if value[0].islower():
            raise TypeError()
        self._surname = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value: str):
        if value is None:
            self._phone = None
            return
        if type(value) != str:
            raise TypeError()
        if len(value) < 11:
            raise TypeError()
        if value[0] == '8':
            if not value.isnumeric() or not len(value) == 11:
                raise TypeError()
        elif value[0] == '+':
            if not value[1:].isnumeric() or len(value) != 12:
                raise TypeError()
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        VALID_SYMBOLS = " abcdefghijklmnopqrstuvwxyz@_.0123456789 "
        if value is None:
            self._email = None
            return
        if type(value) != str:
            raise TypeError()
        if len(value) < 10:
            raise ValueError("длина почты слишком мала")
        if value.find(".", -4, -2) == -1:
            raise ValueError("некорректный домен")
        if value.find("@", 1) == -1:
            raise ValueError("собака не найдена")
        for i in value:
            if i not in VALID_SYMBOLS:
                raise ValueError("недопустимые символы")
        self._email = value

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value: str):
        if value is None:
            self._birthdate = None
            return
        if type(value) != str:
            raise TypeError()
        nums = list(map(int, value.split('-')))
        date = datetime.date(nums[0], nums[1], nums[2])
        if date > datetime.date.today():
            raise TypeError()
        self._birthdate = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: int):
        if type(value) != int:
            raise TypeError()
        if value < 0:
            raise TypeError()
        self._status = value

    def __init__(self, id: int, login: str, password: str, name: str, surname: str, phone: str, email: str,
                 birthdate: str, status: int):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.birthdate = birthdate
        self.status = status

    def __repr__(self):
        return f'{self._id}. {self._name} {self._surname}'


class Address:
    _id = 0
    _country = ''
    _city = ''
    _street = ''
    _house = ''
    _flat = ''
    _post_index = ''
    _commentary = ''


class Order:
    _id = 0
    _info = ''
    _description = ''
    _sender_id = ''
    _courier_id = ''
    _address_id = ''
    _status = ''


class Window(Tk):
    def __init__(self, add_user_func, load_users_func, get_statuses_dict, redact_user_func):
        super().__init__()
        self.title('Post Service')
        self.geometry('+300+100')

        self.add_user_func = add_user_func
        self.load_users_func = load_users_func
        self.get_statuses_func = get_statuses_dict
        self.redact_user_func = redact_user_func

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)
        frame1 = ttk.Frame(notebook)
        frame1.pack()
        notebook.add(frame1, text='Просмотр пользователей')

        frame2 = ttk.Frame(notebook)
        frame2.pack()
        notebook.add(frame2, text='Создание пользователя')

        frame3 = ttk.Frame(notebook)
        frame3.pack()
        notebook.add(frame3, text='Редактирование пользователя')

        self.add_user_label = Label(text="Редактирование пользователя(В поле 'ID' введите id пользователя которого хотите отредактировать)", master=frame3)
        self.add_user_label.grid(row=0, column=1, padx=3,pady=3)

        self.id_label = Label(text='ID*', master=frame3)
        self.id_label.grid(row=1, column=0, padx=3, pady=3)
        self.id_input = ttk.Entry(master=frame3)
        self.id_input.grid(row=1, column=1, padx=3, pady=3)
        self.id_error = Label(master=frame3)
        self.id_error.grid(row=1, column=2, padx=3, pady=3)
        self.id_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'\d+', self.id_error,
                                        'Неверный id')), '%P'))

        self.login_label_redact = Label(text='Логин*', master=frame3)
        self.login_label_redact.grid(row=2, column=0, padx=3, pady=3)
        self.login_input_redact = ttk.Entry(master=frame3)
        self.login_input_redact.grid(row=2, column=1, padx=3, pady=3)
        self.login_error_redact = Label(master=frame3)
        self.login_error_redact.grid(row=2, column=2, padx=3, pady=3)
        self.login_input_redact.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', self.login_error_redact,
                                         'Неверная длина или символы')), '%P'))
        self.password_label_redact = Label(text='Пароль*', master=frame3)
        self.password_label_redact.grid(row=3, column=0, padx=3, pady=3)
        self.password_input_redact = ttk.Entry(master=frame3)
        self.password_input_redact.grid(row=3, column=1, padx=3, pady=3)
        self.password_error_redact = Label(master=frame3)
        self.password_error_redact.grid(row=3, column=2, padx=3, pady=3)
        self.password_input_redact.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', self.password_error_redact,
                                         'Неверная длина или символы')), '%P'))

        self.name_label_redact = Label(text='Имя*', master=frame3)
        self.name_label_redact.grid(row=4, column=0, padx=3, pady=3)
        self.name_input_redact = ttk.Entry(master=frame3)
        self.name_input_redact.grid(row=4, column=1, padx=3, pady=3)
        self.name_error_redact = Label(master=frame3)
        self.name_error_redact.grid(row=4, column=2, padx=3, pady=3)
        self.name_input_redact.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[A-Z]{1,1}[a-z]*|[А-ЯЁ]{1,1}[а-яё]*)$', self.name_error_redact,
                                         'Значение не является именем')), '%P'))

        self.surname_label_redact = Label(text='Фамилия*', master=frame3)
        self.surname_label_redact.grid(row=5, column=0, padx=3, pady=3)
        self.surname_input_redact = ttk.Entry(master=frame3)
        self.surname_input_redact.grid(row=5, column=1, padx=3, pady=3)
        self.surname_error_redact = Label(master=frame3)
        self.surname_error_redact.grid(row=5, column=2, padx=3, pady=3)
        self.surname_input_redact.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[A-Z]{1,1}[a-z]*|[А-ЯЁ]{1,1}[а-яё]*)$', self.surname_error_redact,
                                         'Значение не является фамилией')), '%P'))

        self.phone_label_redact = Label(text="Телефон:", master=frame3)
        self.phone_label_redact.grid(row=6, column=0, padx=3, pady=3)
        self.phone_input_redact = ttk.Entry(master=frame3)
        self.phone_input_redact.grid(row=6, column=1, padx=3, pady=3)
        self.phone_error_redact = Label(master=frame3)
        self.phone_error_redact.grid(row=6, column=2, padx=3, pady=3)
        self.phone_input_redact.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[8][0-9]{10}|[+]7[0-9]{10})$', self.phone_error_redact,
                                         'Неверная длина или символы')), '%P'))

        self.email_label_redact = Label(text="Почта:", master=frame3)
        self.email_label_redact.grid(row=7, column=0, padx=3, pady=3)
        self.email_input_redact = ttk.Entry(master=frame3)
        self.email_input_redact.grid(row=7, column=1, padx=3, pady=3)
        self.email_error_redact = Label(master=frame3)
        self.email_error_redact.grid(row=7, column=2, padx=3, pady=3)
        self.email_input_redact.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value,
                                         r'^[a-zA-Z0-9!#$%*&*()=_+?/><,~`-]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,3}$',
                                         self.email_error_redact,
                                         'Неверная длина или символы')), '%P'))

        self.birthdate_label_redact = Label(text="Дата рождения:", master=frame3)
        self.birthdate_label_redact.grid(row=8, column=0, padx=3, pady=3)
        self.birthdate_input_redact = ttk.Entry(master=frame3)
        self.birthdate_input_redact.grid(row=8, column=1, padx=3, pady=3)
        self.birthdate_error_redact = Label(master=frame3)
        self.birthdate_error_redact.grid(row=8, column=2, padx=3, pady=3)
        self.birthdate_input_redact.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[1-2][0-9]{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])',
                                         self.birthdate_error_redact,
                                         'Неверная дата(Формат: ГГГГ-ММ-ДД)')), '%P'))

        self.status_label_redact = Label(text='Статус*', master=frame3)
        self.status_label_redact.grid(row=9, column=0, padx=3, pady=3)
        self.statuses_list = list(self.get_statuses_func().keys())
        self.status_combobox_redact = ttk.Combobox(values=self.statuses_list, master=frame3)
        self.status_combobox_redact.grid(row=9, column=1, padx=3, pady=3)
        self.status_error_redact = Label(master=frame3)
        self.status_error_redact.grid(row=9, column=2, padx=3, pady=3)
        self.status_combobox_redact.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, fr'{self.statuses_list[0]}$|{self.statuses_list[1]}$|{self.statuses_list[2]}$', self.status_error_redact,
                                         'Такого статуса нет')), '%P'))

        self.redact_user_button = Button(text='Редактировать пользователя', command=self.redact_user, master=frame3)
        self.redact_user_button.grid(row=10, column=1, padx=3, pady=3)


        columns = ['id', 'login', 'password', 'name', 'surname', 'phone', 'email', 'birthdate', 'status']
        self.users_table = ttk.Treeview(columns=columns, show='headings', master=frame1)

        columns_names = ['ID', 'Login', 'Password', 'Name', 'Surname', 'Phone', 'Email', 'Birthdate', 'Status']
        columns_width = [30, 100, 100, 120, 120, 150, 150, 100, 70]

        for i in range(len(columns)):
            self.users_table.heading(columns[i], text=columns_names[i])
            self.users_table.column(f'#{i+1}', stretch=NO, width=columns_width[i])

        vertical_scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.users_table.yview, master=frame1)
        self.users_table.configure(yscrollcommand=vertical_scrollbar.set)

        horizontal_scrollbar = ttk.Scrollbar(orient=HORIZONTAL, command=self.users_table.xview, master=frame1)
        self.users_table.configure(xscrollcommand=horizontal_scrollbar.set)

        self.load_users_button = ttk.Button(text='Обновить', command=self.load_users_list, master=frame1)
        self.load_users_button.pack(side=BOTTOM, anchor=S)

        vertical_scrollbar.pack(side=RIGHT, fill=Y)
        self.users_table.pack(fill=BOTH, expand=False)

        horizontal_scrollbar.pack(side=BOTTOM, fill=X)




        self.add_user_label = Label(text='Добавление пользователя', master=frame2)
        self.add_user_label.grid(row=0, column=1,  padx=3, pady=3)

        self.login_label = Label(text='Логин*', master=frame2)
        self.login_label.grid(row=1, column=0, padx=3, pady=3)
        self.login_input = ttk.Entry(master=frame2)
        self.login_input.grid(row=1, column=1, padx=3, pady=3)
        self.login_error = Label(master=frame2)
        self.login_error.grid(row=1, column=2, padx=3, pady=3)
        self.login_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', self.login_error,
                                         'Неверная длина или символы')), '%P'))
        self.password_label = Label(text='Пароль*', master=frame2)
        self.password_label.grid(row=2, column=0, padx=3, pady=3)
        self.password_input = ttk.Entry(master=frame2)
        self.password_input.grid(row=2, column=1, padx=3, pady=3)
        self.password_error = Label(master=frame2)
        self.password_error.grid(row=2, column=2, padx=3, pady=3)
        self.password_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', self.password_error,
                                         'Неверная длина или символы')), '%P'))

        self.name_label = Label(text='Имя*', master=frame2)
        self.name_label.grid(row=3, column=0, padx=3, pady=3)
        self.name_input = ttk.Entry(master=frame2)
        self.name_input.grid(row=3, column=1, padx=3, pady=3)
        self.name_error = Label(master=frame2)
        self.name_error.grid(row=3, column=2, padx=3, pady=3)
        self.name_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[A-Z]{1,1}[a-z]*|[А-ЯЁ]{1,1}[а-яё]*)$', self.name_error,
                                         'Значение не является именем')), '%P'))

        self.surname_label = Label(text='Фамилия*', master=frame2)
        self.surname_label.grid(row=4, column=0, padx=3, pady=3)
        self.surname_input = ttk.Entry(master=frame2)
        self.surname_input.grid(row=4, column=1, padx=3, pady=3)
        self.surname_error = Label(master=frame2)
        self.surname_error.grid(row=4, column=2, padx=3, pady=3)
        self.surname_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[A-Z]{1,1}[a-z]*|[А-ЯЁ]{1,1}[а-яё]*)$', self.surname_error,
                                         'Значение не является фамилией')), '%P'))

        self.phone_label = Label(text="Телефон:", master=frame2)
        self.phone_label.grid(row=5, column=0, padx=3, pady=3)
        self.phone_input = ttk.Entry(master=frame2)
        self.phone_input.grid(row=5, column=1, padx=3, pady=3)
        self.phone_error = Label(master=frame2)
        self.phone_error.grid(row=5, column=2, padx=3, pady=3)
        self.phone_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[8][0-9]{10}|[+]7[0-9]{10})$', self.phone_error,
                                         'Неверная длина или символы')), '%P'))

        self.email_label = Label(text="Почта:", master=frame2)
        self.email_label.grid(row=6, column=0, padx=3, pady=3)
        self.email_input = ttk.Entry(master=frame2)
        self.email_input.grid(row=6, column=1, padx=3, pady=3)
        self.email_error = Label(master=frame2)
        self.email_error.grid(row=6, column=2, padx=3, pady=3)
        self.email_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[a-zA-Z0-9!#$%*&*()=_+?/><,~`-]{1,}[@][a-zA-Z]-{1,}[.][a-zA-Z]{2,3}$', self.email_error,
                                         'Неверная длина или символы')), '%P'))

        self.birthdate_label = Label(text="Дата рождения:", master=frame2)
        self.birthdate_label.grid(row=7, column=0, padx=3, pady=3)
        self.birthdate_input = ttk.Entry(master=frame2)
        self.birthdate_input.grid(row=7, column=1, padx=3, pady=3)
        self.birthdate_error = Label(master=frame2)
        self.birthdate_error.grid(row=7, column=2, padx=3, pady=3)
        self.birthdate_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[1-2][0-9]{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])', self.birthdate_error,
                                         'Неверная дата(Формат: ГГГГ-ММ-ДД)')), '%P'))

        self.status_label = Label(text='Статус*', master=frame2)
        self.status_label.grid(row=8, column=0, padx=3, pady=3)
        self.statuses_list = list(self.get_statuses_func().keys())
        self.status_combobox = ttk.Combobox(values=self.statuses_list, master=frame2)
        self.status_combobox.grid(row=8, column=1, padx=3, pady=3)
        self.status_error = Label(master=frame2)
        self.status_error.grid(row=8, column=2, padx=3, pady=3)
        self.status_combobox.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value,
                                         fr'{self.statuses_list[0]}$|{self.statuses_list[1]}$|{self.statuses_list[2]}$',
                                         self.status_error,
                                         'Такого статуса нет')), '%P'))

        self.add_user_button = Button(text='Добавить пользователя', command=self.add_user, master=frame2)
        self.add_user_button.grid(row=9, column=1, padx=3, pady=3)

        self.users_list_variable = Variable()
        self.users_listbox = Listbox(listvariable=self.users_list_variable, master=frame1)


        self.mainloop()

    def add_user(self):
        login = self.login_input.get()
        password = self.password_input.get()
        name = self.name_input.get()
        surname = self.surname_input.get()
        phone = self.phone_input.get() if self.phone_input.get != '' else None
        email = self.email_input.get() if self.email_input.get != '' else None
        birthdate = self.birthdate_input.get() if self.birthdate_input.get != '' else None
        status = self.get_statuses_func().get(self.status_combobox.get())
        user = User(0, login, password, name, surname, phone, email, birthdate, status)
        self.add_user_func(user)

    def redact_user(self):
        id = int(self.id_input.get())
        new_login = self.login_input_redact.get()
        new_password = self.password_input_redact.get()
        new_name = self.name_input_redact.get()
        new_surname = self.surname_input_redact.get()
        new_phone = self.phone_input_redact.get() if self.phone_input_redact.get != '' else None
        new_email = self.email_input_redact.get() if self.email_input_redact.get != '' else None
        new_birthdate = self.birthdate_input_redact.get() if self.birthdate_input_redact.get != '' else None
        new_status = self.get_statuses_func().get(self.status_combobox_redact.get())
        user = User(id, new_login, new_password, new_name, new_surname, new_phone, new_email, new_birthdate, new_status)
        self.redact_user_func(user)

    def load_users_list(self):
        users = self.load_users_func()
        for i in self.users_table.get_children():
            self.users_table.delete(i)

        for user in users:
            self.users_table.insert('', END, values=(user.id, user.login, user.password, user.name, user.surname, user.phone, user.email, user.birthdate,
             user.status))


    # def login_validator(self, value):
    #     pattern = '[a-zA-Z0-9!@#$%^&*()-=_+?/><.,~`]{8,}'
    #     if re.fullmatch(pattern, value) is None:
    #         self.login_error.configure(text='Неверная длина или недопустимые символы')
    #         return False
    #     self.login_error.configure(text='')
    #     return True

    def validator(self, value: str, pattern: str, error_label: Label, error_text: str):
        if re.fullmatch(pattern, value) is None:
            error_label.configure(text=error_text)
            return False
        error_label.configure(text='')
        return True
