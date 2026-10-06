# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random, os

class Course:
    """
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    """
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cid=cid
        self.cname=cname
        self.credits=credits

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"{self.cid}({self.credits}): {self.cname}"

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
       return isinstance(other, Course) and self.cid == other.cid


class Catalog:
    """
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    """

    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings={}

    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings:
            return "Course already added"
        self.courseOfferings[cid] = Course(cid, cname, credits)
        return "Course added successfully"

    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        if cid not in self.courseOfferings:
            return "Course not found"
        del self.courseOfferings[cid]
        return "Course removed successfully"

    def _loadCatalog(self, file):
        target_path = os.path.join(os.path.dirname(__file__), file)
        with open(target_path, "r") as f:
            course_info = f.readlines()
        # YOUR CODE STARTS HERE
        for course in course_info:
            cid, cname, credits = course.strip().split(",")
            self.addCourse(cid, cname, int(credits))


class Semester:
    """
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    """


    def __init__(self):
        # --- YOUR CODE STARTS HERE
        self.courses = {}

    def __str__(self):
        # YOUR CODE STARTS HERE
        if not self.courses:
            return "No courses"
        return "; ".join(self.courses)

    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid in self.courses:
            return "Course already added"
        self.courses[course.cid] = course

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid not in self.courses:
            return "No such course"
        del self.courses[course.cid]

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        return sum(course.credits for course in self.courses.values())

    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        return self.totalCredits >= 12


class Loan:
    """
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    """
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.amount = amount
        self.loan_id = self.__getloanID

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Balance: ${self.amount}"

    __repr__ = __str__

    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        return random.randint(10000, 99999)


class Person:
    """
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    """

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name = name
        self.__ssn = ssn

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Person({self.name}, ***-**-{self.__ssn[-4:]})"

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return self.__ssn

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        return isinstance(other, Person) and self.__ssn == other.get_ssn()


class Staff(Person):
    """
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    """
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn)
        self.__supervisor = supervisor

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Staff({self.name}, {self.id})"

    __repr__ = __str__

    @property
    def id(self):
        # YOUR CODE STARTS HERE
        initials = "".join(part[0].lower() for part in self.name.split())
        return f"905{initials}{self.get_ssn()[-4:]}"

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self.__supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor, Staff):
            self.__supervisor = new_supervisor
            return "Completed!"

    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = True
            return "Completed!"

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = False
            return "Completed!"

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.active = False
            return "Completed!"

    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        if isinstance(person, Person):
            return Student(person.name, person.get_ssn(), "Freshman")


class Student(Person):
    """
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    """
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn)
        self.classCode = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Student({self.name}, {self.id}, {self.classCode})"

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        if self.active:
            return StudentAccount(self)

    @property
    def id(self):
        # YOUR CODE STARTS HERE
        initials = "".join(part[0].lower() for part in self.name.split())
        return f"{initials}{self.get_ssn()[-4:]}"

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        if not self.active or self.hold:
            return "Unsuccessful operation"

        semester_number = max(self.semesters, default=0) + 1
        self.semesters[semester_number] = Semester()

        if semester_number <= 2:
            self.classCode = "Freshman"
        elif semester_number <= 4:
            self.classCode = "Sophomore"
        elif semester_number <= 6:
            self.classCode = "Junior"
        else:
            self.classCode = "Senior"

    def enrollCourse(self, cid, catalog):
        # YOUR CODE STARTS HERE
        if not self.active or self.hold or not self.semesters:
            return "Unsuccessful operation"
        if cid not in catalog.courseOfferings:
            return "Course not found"

        current_semester = self.semesters[max(self.semesters)]
        if cid in current_semester.courses:
            return "Course already enrolled"

        course = catalog.courseOfferings[cid]
        current_semester.addCourse(course)
        self.account.chargeAccount(course.credits * StudentAccount.CREDIT_PRICE)
        return "Course added successfully"

    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        if not self.active or self.hold:
            return "Unsuccessful operation"
        if not self.semesters:
            return "Course not found"

        current_semester = self.semesters[max(self.semesters)]
        if cid not in current_semester.courses:
            return "Course not found"

        course = current_semester.courses[cid]
        current_semester.dropCourse(course)
        refund = course.credits * StudentAccount.CREDIT_PRICE / 2
        self.account.makePayment(refund)
        return "Course dropped successfully"

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        if not self.active:
            return "Unsuccessful operation"
        if not self.semesters:
            return "Not full-time"

        current_semester = self.semesters[max(self.semesters)]
        if not current_semester.isFullTime:
            return "Not full-time"

        loan = Loan(amount)
        self.account.loans[loan.loan_id] = loan
        self.account.makePayment(amount)


class StudentAccount:
    """
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    """
    
    CREDIT_PRICE = 1000

    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        self.balance = 0
        self.loans = {}

    def __str__(self):
        # YOUR CODE STARTS HERE
        return (f"Name: {self.student.name}\n"
                f"ID: {self.student.id}\n"
                f"Balance: ${self.balance}")

    __repr__ = __str__

    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        self.balance -= amount
        return self.balance

    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        self.balance += amount
        return self.balance


def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
    #doctest.run_docstring_examples(Course, globals(), name='HW2',verbose=True)   

if __name__ == "__main__":
    run_tests()
