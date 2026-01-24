class Person:
    name = "张三"
    age = 18
    sex = "男"

    def eat(self):
        print("我踏马吃吃吃吃吃吃")

    def drink(self):
        print("我踏马喝喝喝喝喝喝")

    def sleep(self, time):
        self.drink()  # 如果想在方法中调用类自己的方法，则使用self.方法名()
        print('在睡觉，睡了' + time)