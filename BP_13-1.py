from turtle import *
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()                 #클래스 안에 거북이 객체 생성 후 저장
        self.turtle.shape("D:\car.gif")
      
    def drive(self):
        self.turtle.forward(self.speed)
        
    def left_turn(self):
        self.turtle.left(90)
        
register_shape("D:\car.gif")                     #터틀 그래픽에서 사용되는 이미지 등록
myCar = Car(200, "orange", "McLaren")
for i in range(100):
    myCar.drive()
    myCar.left_turn()
