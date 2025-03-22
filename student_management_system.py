from abc import ABC, abstractmethod
from datetime import date, datetime

class College(ABC):
    @abstractmethod
    def display_result(self):
        pass
    @abstractmethod
    def salary(self):
        pass

class Student(College):
    def __init__(self, name: str, roll_no: int, branch: str, year_of_admission: int, subjects: dict) -> None:
        self._name = name
        self.roll_no = roll_no
        self.branch = branch
        self.year_of_admission = year_of_admission
        self.subjects = subjects
    def display_result(self) -> None:
        print("\nStudent Details: ")
        print("Roll No: ", self.roll_no)
        print("Student Name: ", self._name)
        print("Year of Admission: ", self.year_of_admission)
        print("Branch: ", self.branch)
        print("Subjects and Marks: ")
        for sub in self.subjects:
            print(sub, ":", self.subjects[sub])
        print("Total Marks: ", (self.subjects.__len__()) * 100)
        print("Marks Obtained: ", sum(self.subjects.values()))
        print("Percentage: ", sum(self.subjects.values()) / len(self.subjects))
    def salary(self) -> None:
        pass

class Faculty(College):
    designation: str = None
    def __init__(self, name: str, course: str, qualification: list, experience: int) -> None:
        self._name = name
        self.course = course
        self.qualification = qualification
        self.experience = experience
    def display_result(self) -> None:
        print("\nFaculty Details: ")
        print("Faculty Name: ", self._name)
        print("Course: ", self.course)
        print("Qualification: ", ", ".join(self.qualification))
        print("Experience in years: ", self.experience)
        designations: dict = {
            range(1, 6): "Assistant Professor",
            range(6, 11): "Associate Professor",
            range(11, 16): "Professor",
            range(16, 21): "Senior Professor",
            range(21, 26): "HOD",
            range(26, 31): "Dean"
        }
        self.designation = next((title for exp_range, title in designations.items() if self.experience in exp_range), "Enter valid experience")
        print("Designation: ", self.designation)
    def salary(self) -> None:
        pay_structure = {
            "BASIC": 60000,
            "HRA": 20000,
            "TA": 5000,
            "DA": 2000, 
            "PF Deduction": -5000
        }
        base_pay: int = sum(pay_structure.values())
        additional_pay: dict = {
            "Assistant Professor": 0,
            "Associate Professor": (pay_structure["BASIC"] * 0.1),
            "Professor": (pay_structure["BASIC"] * 0.2),
            "Senior Professor": (pay_structure["BASIC"] * 0.3),
            "HOD": (pay_structure["BASIC"] * 0.4),
            "Dean": (pay_structure["BASIC"] * 0.5)
        }
        total_pay: int = base_pay + additional_pay.get(self.designation, 0)
        print("Total Salary: ", total_pay if self.designation in additional_pay else "Enter valid experience")
                
class Staff(College):
    def __init__(self, name: str, role: str, date_of_joining: str) -> None:
        self._name = name
        self.role = role
        self.date_of_joining = datetime.strptime(date_of_joining, "%Y-%m-%d").date()
    def display_result(self) -> None:
        print("\nStaff Details: ")
        print("Staff Name: ", self._name)
        print("Role: ", self.role)
        print("Date of Joining (yyyy-mm-dd): ", self.date_of_joining)
        print("Current Date: ", date.today())
        print("Experience in years: ", (datetime.now().year - self.date_of_joining.year))
    def salary(self) -> None:
        roles = ("CLERK", "LAB ASSISTANT", "PEON", "SECURITY GUARD", "SWEEPER")
        experience = (datetime.now().year - self.date_of_joining.year)
        if self.role.upper() in roles:
            pay_structure = {
                "CLERK": 20000,
                "LAB ASSISTANT": 15000,
                "PEON": 10000,
                "SECURITY GUARD": 12000,
                "SWEEPER": 8000
            }
            print("Salary: ", pay_structure[self.role.upper()] + (pay_structure[self.role.upper()] * (experience * 0.05)))
        else:
            print("Enter valid role")

def get_valid_input(prompt: int, expected_type: type = str, condition: callable = lambda x: True, error_msg: str = "Invalid input: ") -> any:
    while True:
        try:
            value = expected_type(input(prompt).strip().upper())
            if condition(value):
                return value
        except ValueError as e:
            print(error_msg, repr(e))
            print("Please provide a valid value!!")

def get_valid_multiple_input(prompt: str, num_value: int) -> list:
    while True:
        values: list = input(prompt).strip().split(",")  
        if len(values) == num_value:
            return [v.strip().upper() for v in values]  
        print(f"Please provide valid {num_value} comma-separated values.")

def main() -> None:
    print(""" 
    Welcome to College Management System
    ====================================
    Please select a role:
    1. Student
    2. Faculty
    3. Staff
          """)
    while True:
        try:
            roles: str = input("\nEnter your role: ").strip().upper()  
            
            if roles == "STUDENT":
                name, roll_no, branch, year_of_admission = get_valid_multiple_input("Enter your name, roll no, branch, year of admission (comma separated): ", 4)
                no_of_subjects = get_valid_input("Enter the number of subjects: ", int, lambda x: x > 0, "Must be a positive number")
                subjects = {
                    sub: int(marks)
                    for sub, marks in (input("Enter the subject and marks (space separated): ").upper().split() for _ in range(no_of_subjects))
                }
                student = Student(name.strip(), int(roll_no.strip()), branch.strip(), int(year_of_admission.strip()), subjects)
                student.display_result()
                student.salary()
                
            elif roles == "FACULTY":
                name, course = get_valid_multiple_input("Enter your name, course (comma separated): ", 2)
                qualification = list(map(str, input("Enter your qualification (space separated): ").strip().upper().split()))
                experience = get_valid_input("Enter your experience in years: ", int, lambda x: x > 0, "Must be a positive number")
                faculty = Faculty(name.strip(), course.strip(), qualification, experience)
                faculty.display_result()
                faculty.salary()
                
            elif roles == "STAFF":
                name, role, date_of_joining = get_valid_multiple_input("Enter your name, role, date of joining (yyyy-mm-dd) (comma separated): ", 3)
                staff = Staff(name.strip(), role.strip(), date_of_joining.strip())
                staff.display_result()
                staff.salary()
                
            if get_valid_input("\nDo you want to continue? (yes/no): ", str, lambda x: x.lower() in ["yes", "no"], "Please enter YES or NO.") == "no":
                break
        except (TypeError, RuntimeError) as e:
            print("\nError!!")
            print("The Error was: ", repr(e))
            continue
        finally:
            print("\nThank you for using College Management System")

if __name__ == "__main__":
    main()