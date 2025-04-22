import requests
class Employee:
    """A sample employee class"""

    raise_amt = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    #### Mocking ####
    def monthly_schedule(self, month):
        """
        A sample method that will go to a site to pull down an employee schedule for a given month
        """
        reponse = requests.get(f"http://company.com/{self.last}/{month}")
        if reponse.ok:
            return reponse.text
        else:
            return 'Bad Response!'



emp1 = Employee('Adam', 'Willson', 70000)
email1 = emp1.email
print(email1)