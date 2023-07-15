import math
latitude = float(input("위도를 입력하세요(소수 입력 가능): ")) #degree
h = float(input("측점의 고도(지오이드고)를 입력하세요: ")) #m
observed_gravity = float(input("IGSN 71에 따른 관측중력을 입력하세요: ")) #mgal
def sin(degree):
    return math.sin(math.radians(degree))
def cos(degree):
    return math.cos(math.radians(degree))
standard_gravity = 978031.85 * (1 + 0.005278895*sin(latitude)**2 + 0.000023462*sin(latitude)**4) #mgal
