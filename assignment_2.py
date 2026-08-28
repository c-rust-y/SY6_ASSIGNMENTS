#Design a dynamic report generator in Python that uses decorators, class methods, and magic methods to
#customize and format reports. The system should allow users to define report templates and apply various
#formatting options dynamically.

def report_decorator(func):
    def wrapper (self):
        print("__________WE ALL LOVE ADVANCED PYTHON__________")
        func(self)
        print("__________WE ALL LOVE ADVANCED PYTHON__________")
    return wrapper

class Report:

    def __init__(self,name,roll_no , python,english,maths,dsa):
        self.name=name
        self.roll_no=roll_no
        self.python=python
        self.english=english
        self.maths=maths
        self.dsa=dsa

    @report_decorator
    def marks(self):
        print("Name: ", self.name)
        print("roll no: ", self.roll_no)
        print("__________WE ALL LOVE ADVANCED PYTHON__________")
        print("python: ",self.python)
        print("english: ",self.english)
        print("maths: ",self.maths)
        print("dsa: ",self.dsa)

marks1 = Report("Bunty","ADT25SOC1234","A+","A+","B","A")
marks1.marks()    


        
