# Создать телефонный справочник с возможностью импорта и экспорта данных 
# в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые 
# должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для 
# поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной


# ================= ДОМАШНЕЕ ЗАДАНИЕ ====================
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления 
# данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных.
import re

def user_choice():
    choice = -1
    while choice != 0:
        choice = input("Что вы хотите сделать? 1 - ввод, 2 - поиск, 3 - вывести все контакты, 4 - заменить контакт, 5 - удалить контакт, -1 - выход: ")
        if choice == '1':
            user_input()
        elif choice == '2':
            user_search()
        elif choice == '3':
            all_contacts()
        elif choice == '4':
            change_contact()
        elif choice == '5':
            delete_contact()
        else:
            break

def user_input():
    with open("new.txt", "a", encoding="utf-8") as data:
        a = input("Введите Ф.И.О и номер телефона: ") + "\n"
        data.write(a)


def user_search():
    with open("new.txt", "r", encoding="utf-8") as dat:
        b = input("Кого ищем?: ")
        s = dat.readlines()
        for i in s:
            if b in i:
                print(i)

def all_contacts():
    with open("new.txt", "r", encoding="utf-8") as da:
        print(da.read()) + "\n"


def change_contact():
    data_str = input("Введите контакт: ")
    user_lst = []
    with open("new.txt", "r", encoding="utf-8") as d:
        lst = d.readlines()
        for line in lst:
            if data_str in line:
                user_lst.append(line)
    print(*user_lst)
    answer = int(input("Введите строчку, которую хотите заменить: "))
    new_contact = input("Введите новый контакт: ") + "n"
    
    with open("new.txt", "w", encoding="utf-8") as d:
        for line in lst:
            if user_lst[answer - 1] != line:
                d.write(line)
            else:
                d.write(new_contact)
    print("Готово!")

def delete_contact():
    data_str = input("Введите контакт, который хотите удалить: ")
    user_lst = []
    with open("new.txt", "r", encoding="utf-8") as d:
        lst = d.readlines()
        for line in lst:
            if data_str in line:
                user_lst.append(line)
    print(*user_lst)
    answer = int(input("Введите строчку, которую хотите удалить: "))

    with open("new.txt", "w", encoding="utf-8") as d:
        for line in lst:
            if user_lst[answer - 1] != line:
                d.write(line)
            else:
                continue
    print("Готово!")

user_choice()