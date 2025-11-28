class Subject:
    def __init__(self, name: str, code: str):
        self.__name = name
        self.__code = code

    def getInfo(self) -> str:
        return f"课程：{self.__name}（{self.__code}）"

class Instructor:
    def __init__(self, name: str, instructor_id: str):
        self.__name = name
        self.__id = instructor_id
        self.__departments = []  # 隶属于的系（1..*）
        self.__subjects = []     # 教授的课程（1..3）

    def addDepartment(self, department: 'Department') -> None:
        """添加所属系"""
        if department not in self.__departments:
            self.__departments.append(department)

    def addSubject(self, subject: Subject) -> bool:
        """添加教授的课程（最多3门）"""
        if len(self.__subjects) < 3 and subject not in self.__subjects:
            self.__subjects.append(subject)
            return True
        return False

    def getTeachingSubjects(self) -> list:
        """获取教授的课程"""
        return [sub.getInfo() for sub in self.__subjects]

class Department:
    def __init__(self, name: str):
        self.__name = name
        self.__instructors = []  # 拥有的教师（1..*）
        self.__subjects = []     # 提供的课程（1..*）

    def addInstructor(self, instructor: Instructor) -> None:
        """添加教师"""
        if instructor not in self.__instructors:
            self.__instructors.append(instructor)
            instructor.addDepartment(self)  # 双向关联：教师隶属于该系

    def addSubject(self, subject: Subject) -> None:
        """添加课程"""
        if subject not in self.__subjects:
            self.__subjects.append(subject)

class School:
    def __init__(self, name: str):
        self.__name = name
        self.__departments = []  # 包含的系（1..*）
        self.__students = []     # 拥有的学生（0..*）

    def addDepartment(self, department: Department) -> None:
        """添加系"""
        if department not in self.__departments:
            self.__departments.append(department)

    def addStudent(self, student: 'Student') -> None:
        """添加学生"""
        if student not in self.__students:
            self.__students.append(student)

class Student:
    def __init__(self, name: str, student_id: str):
        self.__name = name
        self.__id = student_id
        self.__subjects = []  # 学习的课程（1..5）

    def addSubject(self, subject: Subject) -> bool:
        """添加学习的课程（最多5门）"""
        if len(self.__subjects) < 5 and subject not in self.__subjects:
            self.__subjects.append(subject)
            return True
        return False

    def getEnrolledSubjects(self) -> list:
        """获取已选课程"""
        return [sub.getInfo() for sub in self.__subjects]

# 测试代码（回归测试用例）
if __name__ == "__main__":
    # 创建学院、系
    school = School("XX大学")
    cs_dept = Department("计算机系")
    school.addDepartment(cs_dept)
    
    # 创建教师、课程
    teacher = Instructor("张老师", "INS001")
    cs_dept.addInstructor(teacher)
    sub1 = Subject("数据结构", "CS101")
    sub2 = Subject("操作系统", "CS102")
    sub3 = Subject("计算机网络", "CS103")
    sub4 = Subject("人工智能", "CS104")
    cs_dept.addSubject(sub1)
    cs_dept.addSubject(sub2)
    cs_dept.addSubject(sub3)
    cs_dept.addSubject(sub4)
    
    # 教师最多教授3门课程
    assert teacher.addSubject(sub1) is True
    assert teacher.addSubject(sub2) is True
    assert teacher.addSubject(sub3) is True
    assert teacher.addSubject(sub4) is False  # 第4门添加失败
    
    # 学生最多选5门课程
    student = Student("小李", "STU2023001")
    school.addStudent(student)
    for i in range(5):
        sub = Subject(f"课程{i+1}", f"CODE{i+1}")
        assert student.addSubject(sub) is True
    assert student.addSubject(Subject("课程6", "CODE6")) is False  # 第6门添加失败
    
    print("A1-3 测试通过！")