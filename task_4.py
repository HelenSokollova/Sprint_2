class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, name, rest_days, email):
        return cls(name, (7 - rest_days) * 8, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        return cls(name, hours, rest_days, f"{name}@email.com")
    
    @classmethod
    def set_hourly_payment(cls, hourly_payment_new):
        cls.hourly_payment = hourly_payment_new

    def salary(self, hours, hourly_payment):
        self.salary_summ = hours * hourly_payment
