class Building:
    def __init__(self, name: str, address: str):
        self.__name = name  # 私有属性
        self.__address = address

    def getInfo(self) -> str:
        """返回建筑信息"""
        return f"建筑名称：{self.__name}，地址：{self.__address}"

class Course:
    def __init__(self, name: str, code: str):
        self.__name = name
        self.__code = code
        self.__location = None  # 关联的建筑，初始为None

    def setLocation(self, building: Building) -> None:
        """设置课程所在建筑（满足约束）"""
        self.__location = building

    def getLocation(self) -> Building:
        """获取课程所在建筑"""
        return self.__location

    def getInfo(self) -> str:
        """返回课程信息"""
        location_info = self.__location.getInfo() if self.__location else "未指定建筑"
        return f"课程名称：{self.__name}，编号：{self.__code}，{location_info}"

class College:
    def __init__(self, name: str):
        self.__name = name
        self.__buildings = []  # 聚合关系：存储建筑实例（可独立存在）
        self.__courses = []    # 组合关系：存储课程实例（不可独立存在）

    def addBuilding(self, building: Building) -> None:
        """添加建筑（聚合）"""
        if building not in self.__buildings:
            self.__buildings.append(building)

    def removeBuilding(self, building: Building) -> None:
        """移除建筑（聚合关系可分离）"""
        if building in self.__buildings:
            self.__buildings.remove(building)

    def addCourse(self, course: Course) -> None:
        """添加课程（组合）"""
        if course not in self.__courses:
            self.__courses.append(course)

    def removeCourse(self, course: Course) -> None:
        """移除课程（组合关系分离后课程无意义）"""
        if course in self.__courses:
            self.__courses.remove(course)

    def getCourseInfo(self) -> list:
        """获取所有课程信息"""
        return [course.getInfo() for course in self.__courses]

# 测试代码（回归测试用例）
if __name__ == "__main__":
    # 创建建筑
    lib = Building("图书馆", "校园中路1号")
    lab = Building("计算机实验室", "科技楼3层")
    
    # 创建学院
    cs_college = College("计算机与信息学院")
    cs_college.addBuilding(lib)
    cs_college.addBuilding(lab)
    
    # 创建课程并绑定建筑
    python_course = Course("Python编程", "CS202301")
    python_course.setLocation(lab)
    cs_college.addCourse(python_course)
    
    # 验证课程信息
    course_info = cs_college.getCourseInfo()[0]
    assert "Python编程" in course_info and "计算机实验室" in course_info, "课程与建筑关联错误"
    
    print("A1-2 测试通过！")