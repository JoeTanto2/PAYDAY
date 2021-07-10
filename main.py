from enum import Enum, auto
from dataclasses import dataclass
from abc import ABC, abstractmethod

class VacationError (Exception):
    def __init__(self, days_requested: int, vac_days_left: int, message: str):
        self.days_request = days_requested
        self.vac_days_left = vac_days_left
        self.message = message


class Position (Enum):
    ACCOUNTANT = auto()
    CLERK = auto()
    SOFTWARE_DEV = auto()
    LEAD = auto()
    MANAGER = auto()

@dataclass
class Employee (ABC):
    name: str
    position: Position
    vacation_days: int = 14


    @abstractmethod
    def pay (self) -> None:
        '''method called when paying'''

    def holiday (self, days_requested: int):
        if self.vacation_days < days_requested:
            raise VacationError (
                days_requested=1,
                vac_days_left=self.vacation_days,
                message=f"You don't have enough of vacation days left, you've requested {days_requested} day(s)"
                        f"but you have only {self.vacation_days} day(s) left"
            )
        self.vacation_days = self.vacation_days - days_requested
        print(f'You you have requested {days_requested} day(s), you have {self.vacation_days} day(s) left')

@dataclass
class PAYMENT (Employee):
    hourly_pay: float = 15
    amount_of_hours: float = 10
    def pay (self):
        amount_paid = (self.hourly_pay * self.amount_of_hours)
        print (f"We payed {self.name} {amount_paid} for {self.amount_of_hours} at {self.hourly_pay} per hr rate")


class Company:
    def __init__(self):
        self.employees: list[Employee] = []

    def add_employee (self, employee: Employee):
        self.employees.append(employee)


def main ():
    company = Company()

    company.add_employee(PAYMENT(name='David', position=Position.MANAGER, hourly_pay=62.5, amount_of_hours=45))
    company.add_employee(PAYMENT(name='Paul', position=Position.SOFTWARE_DEV, hourly_pay=50, amount_of_hours=40))
    company.add_employee(PAYMENT(name="Josh", position=Position.CLERK))
    company.employees[0].pay()
    company.employees[1].pay()
    company.employees[0].holiday(12)
    company.employees[2].pay()


if __name__ == "__main__":
    main()
