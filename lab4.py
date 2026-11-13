class Bank:
    """Сутність "Банк"."""

    def __init__(self, name="Невідомо", clients_count=0, loans_count=0,
                 country="Україна", branches_count=0):

        self.__name = name
        self.__clients_count = clients_count
        self.__loans_count = loans_count

        self.country = country
        self.branches_count = branches_count
        print(f"Конструктор: створено об'єкт Bank '{self.__name}'")


    def get_name(self):
        return self.__name

    def get_clients_count(self):
        return self.__clients_count

    def get_loans_count(self):
        return self.__loans_count


    def set_name(self, name):
        self.__name = name

    def set_clients_count(self, clients_count):
        if clients_count < 0:
            print("Кількість клієнтів не може бути від'ємною")
        else:
            self.__clients_count = clients_count

    def set_loans_count(self, loans_count):
        if loans_count < 0:
            print("Кількість кредитів не може бути від'ємною")
        else:
            self.__loans_count = loans_count

    def __str__(self):
        return (f"Банк: {self.__name}\n"
                f"  Кількість клієнтів: {self.__clients_count}\n"
                f"  Кількість виданих кредитів: {self.__loans_count}\n"
                f"  Країна: {self.country}\n"
                f"  Кількість відділень: {self.branches_count}")

    def __repr__(self):
        return (f"Bank(name={self.__name!r}, "
                f"clients_count={self.__clients_count!r}, "
                f"loans_count={self.__loans_count!r}, "
                f"country={self.country!r}, "
                f"branches_count={self.branches_count!r})")

    def __del__(self):
        print(f"Деструктор: об'єкт Bank '{self.__name}' видалено")


def main():
    print("=== Створення об'єктів ===")
    bank1 = Bank()
    bank2 = Bank("ПриватБанк", 20000000, 1500000, "Україна", 1200)
    bank3 = Bank("Монобанк", 9000000, 700000, "Україна", 0)

    print("\n=== Виведення значень полів (через getters) ===")
    for bank in (bank1, bank2, bank3):
        print(f"Назва: {bank.get_name()}")
        print(f"Клієнтів: {bank.get_clients_count()}")
        print(f"Виданих кредитів: {bank.get_loans_count()}")
        print(f"Країна: {bank.country}")
        print(f"Відділень: {bank.branches_count}")
        print("-" * 30)

    print("\n=== Виведення через __str__ ===")
    print(bank1)
    print(bank2)
    print(bank3)

    print("\n=== Виведення через __repr__ ===")
    print(repr(bank1))
    print(repr(bank2))
    print(repr(bank3))

    print("\n=== Завершення програми ===")


if __name__ == "__main__":
    main()