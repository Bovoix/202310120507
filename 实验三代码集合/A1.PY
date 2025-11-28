from datetime import datetime

class Thoroughbred:
    def __init__(self, birthyear: int, father: 'Thoroughbred' = None, mother: 'Thoroughbred' = None):
        # 私有属性（Python 中用双下划线模拟私有）
        self.__birthyear = birthyear
        self.__father = father
        self.__mother = mother

    def getCurrentAge(self) -> int:
        """计算当前年龄：当前年份 - 出生年份"""
        current_year = datetime.now().year
        return current_year - self.__birthyear

    def getFather(self) -> 'Thoroughbred':
        """获取父亲信息"""
        return self.__father

    def getMother(self) -> 'Thoroughbred':
        """获取母亲信息"""
        return self.__mother

# 测试代码（回归测试用例）
if __name__ == "__main__":
    # 创建亲代马
    sire = Thoroughbred(2010)
    dam = Thoroughbred(2012)
    # 创建子代马
    foal = Thoroughbred(2020, sire, dam)
    
    # 验证年龄计算
    assert foal.getCurrentAge() == datetime.now().year - 2020, "年龄计算错误"
    # 验证亲代信息
    assert foal.getFather() == sire, "父亲信息获取错误"
    assert foal.getMother() == dam, "母亲信息获取错误"
    
    print("A1-1 测试通过！")