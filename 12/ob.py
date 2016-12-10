#encoding: utf-8

class User(object):
    NUM_EYES = 2
    NUM_FOOT = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    @classmethod
    def get_num_eyes(cls):
        return cls.NUM_EYES

    @staticmethod
    def get_num_foot():
        return User.NUM_FOOT

class ThreeEyeUser(object):
    NUM_EYES = 3
    NUM_FOOT = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    @classmethod
    def get_num_eyes(cls):
        return cls.NUM_EYES

    @staticmethod
    def get_num_foot():
        return User.NUM_FOOT


class ThreeEyeUser2(User):
    NUM_EYES = 3

    def __init__(self, name, age):
        super(ThreeEyeUser2, self).__init__(name, age)
        self.sex = 1

    def get_name(self):
        print '三目:' + self.name


# def get_num_foot():
#     return User.NUM_FOOT

if __name__ == '__main__':
    # zhoufucheng = User('xiaozhou', 29)
    # print zhoufucheng.get_name()
    # print zhoufucheng.age
    # print User.get_num_eyes()
    # print zhoufucheng.get_num_eyes()
    # print User.get_num_foot()
    # print zhoufucheng.get_num_foot()
    t1 = ThreeEyeUser('1', 1)
    t2 = ThreeEyeUser2('2', 2)
    print t1.NUM_EYES
    print t1.get_name()
    print t2.NUM_EYES
    print t2.get_name()
    t2.set_name('aaaaa')
    print t2.get_name()
    print t2.age