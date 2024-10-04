import re
from typing import Callable

import regex
from colorama import Fore


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n)


# 55
result1 = fibonacci(10)

#610
result2 = fibonacci(15)
print(result1)
print(result2)

if __name__ == '__main__':
    t = "Загальний дохід працівника складається з декількох частин: " \
        "1000.01 як основний дохід, доповнений додатковими надходженнями" \
        " 27.45 і 324.00 "


    def generator_numbers(text: str) -> str:
        pattern = r"[^\d.]"
        res = re.sub(pattern, " ", text)
        for rea in res.split(" "):
            if rea != '':
                yield float(rea)


    def sum_profit(text: str, func: Callable[[str], float]) -> float:
        sum = 0
        for res in generator_numbers(text):
            sum += res
        return sum

    # print(sum_profit(t, generator_numbers))

# ///////////////////////////////////////////////////////////


if __name__ == '__main__':
    dictList = {}


    def main():
        print(F"{Fore.LIGHTBLUE_EX}Hello my Friend")
        print("I am assistant bot!")
        while True:
            print("select a command", "--->__add_Name_and_Phone<---> add")
            print("select a command", "--->__change_Phone<---> change")
            print("select a command", "--->__show_Name_by_Phone<---> show")
            print("select a command", "--->__all_Name_and_Phone<---> all")
            command = input().__str__().lower().strip()
            if command == "add":
                print(F"{Fore.LIGHTYELLOW_EX}Your name and number Phone")

                name = input(F"{Fore.LIGHTYELLOW_EX}please your name:").strip().lower()
                phone = input(F"{Fore.LIGHTYELLOW_EX}please your phone :").strip().lower()
                user = add_contact(name, phone)
                if user is not None:
                    print(f"Your number phone {phone} is add database")
            if command == "change":
                print("enter your name and the new number you want to replace")
                name1 = input("your name :").strip().lower()
                number1 = input("your new phone :").strip().lower()
                change_contact(name1.__str__(), number1.__str__())
            if command == "show":
                namePhoneFind = input("your name: ").strip().lower()
                print(show_phone(namePhoneFind))
            if command == "all":
                input("click go to see all phone numbers : ")
                result = show_all()
                if result is None:
                    print("the database is empty")
                else:
                    print(result)
            if command in ["close", "exit"]:
                print("Good bye my Friend!")
                break


    # @input_error
    # def firstProb(a :int, b :int):
    #     return a/b
    #
    #
    # result = firstProb(2,0)
    # print(result)

    def input_error_add_and_change_contact(func):
        def inner(a, b):
            if func(a, b) is None:
                print("Give correct name and phone please.")
            else:
                return func

        return inner


    def input_error_show_by_phone(func):
        def inner(a):
            res = func(a)
            if res != None:
                return res
            else:
                print("Give correct name and phone please.")

        return inner


    @input_error_add_and_change_contact
    def add_contact(name: str, phone: str):
        pettern1 = r"\D"
        matches = regex.sub(pettern1, "", phone)
        checkNumber = bool(regex.search(r"^380\d{9}$", matches))
        checkNum = bool(regex.search(r"^0\d{9}$", matches))
        checkN = bool(regex.search(r"^+380\d{9}$", matches))
        if checkNumber:
            number = "+" + matches
            dictNamePhone = dictList[name] = number
            return dictNamePhone
        elif checkNum:
            number1 = "+38" + matches
            dictNamePhone1 = dictList[name] = number1
            return dictNamePhone1
        elif checkN:
            dictNamePhone2 = dictList[name] = matches
            return dictNamePhone2


@input_error_add_and_change_contact
def change_contact(nameCh: str, phoneCh: str):
    newPhone = 0
    pettern1 = r"\D"
    matches = regex.sub(pettern1, "", phoneCh)
    checkNumber = bool(regex.search(r"^380\d{9}$", matches))
    checkNum = bool(regex.search(r"^0\d{9}$", matches))
    checkN = bool(regex.search(r"^+380\d{9}$", matches))
    if checkNumber:
        newPhone = "+" + matches
        return updateDictByKey(dictList, nameCh, newPhone)
    elif checkNum:
        newPhone = "+38" + matches
        return updateDictByKey(dictList, nameCh, newPhone)
    elif checkN:
        newPhone = matches
        return updateDictByKey(dictList, nameCh, matches)


@input_error_show_by_phone
def show_phone(showName):
    for k, v in dictList.items():
        if k == str(showName):
            return v
        else:
            print("Your name and phone is not dataBase")


def show_all():
    for k, v in dictList.items():
        return k, v


def updateDictByKey(dictList, name, value):
    for k, v in dictList.items():
        if k == name:
            dictList[k] = value
            return value
        else:
            print("Your name is not dataBase")


main()
