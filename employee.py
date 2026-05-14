class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

    def calculate_pay(self):  # Programmer forgot self parameter
        return self.wage * self.hours_worked


alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f"Alice earned {alice.calculate_pay():.2f}")