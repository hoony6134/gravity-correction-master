import math

global rock_density
global water_density
global standard_gravity
global observed_gravity
global latitude
global h
global g
global BC
global FAC
global air_correction
global TC
global perfect_BC

print("Gravity Correction Master v1.0")
print("Developed by JeongHoon Lim")
print("--------------------")
print("본 프로그램은 중력 측정값을 입력하면, 다양한 오차를 보정하여 중력의 각 보정값을 계산해주는 프로그램입니다.")
print("본 프로그램은 IGSN 71에 따른 관측 중력값을 입력할 때를 기준으로 셜계되었으며, 해당 기준에 맞게 측정한 관측 중력값을 입력해 주시기를 권장드립니다.")
print("중력 관측 시에는 계기 오차를 줄이기 위해 여러 번 측정한 후 평균값을 입력해 주시기를 권장드립니다.")
print("--------------------")
latitude = float(input("위도를 입력하세요(소수 입력 가능): ")) #degree
h = float(input("측점의 고도(지오이드고)를 입력하세요(m): ")) #m
observed_gravity = float(input("관측중력값을 입력하세요. IGSN 71에 따른 중력값을 입력하는 것을 권장드립니다(mgal): ")) #mgal

def sin(degree):
    return math.sin(math.radians(degree))
def cos(degree):
    return math.cos(math.radians(degree))
def tan(degree):
    return math.tan(math.radians(degree))

standard_gravity = 978031.85 * (1 + 0.005278895*sin(latitude)**2 + 0.000023462*sin(latitude)**4) #mgal
FAC = 0.3086*h #mgal
is_water = input("바다에서 측정했나요?(y/n): ")
if is_water == "y" or is_water == "Y" or is_water == "예" or is_water == "네":
    if (input("측정 지점에서의 물(액체)의 밀도를 알고 있나요?(y/n): ") == "y"):
        water_density = float(input("측정 지점에서의 물(액체)의 밀도(g/cm^3)를 입력하세요: ")) #g/cm^3
    else:
        water_density = 1.03 #g/cm^3
    if (input("측정 지점에서의 암석의 밀도를 알고 있나요?(y/n): ") == "y"):
        rock_density = float(input("측정 지점에서의 암석의 밀도(g/cm^3)를 입력하세요: "))
    else:
        rock_density = 2.67  # g/cm^3 (화강암 밀도)
    BC = 0.0419*(water_density-rock_density)*h #mgal
elif is_water == "n" or is_water == "N" or is_water == "아니요" or is_water == "아니오":
    if (input("측정 지점에서의 암석의 밀도를 알고 있나요?(y/n): ") == "y"):
        rock_density = float(input("측정 지점에서의 암석의 밀도(g/cm^3)를 입력하세요: "))
    else:
        rock_density = 2.67  # g/cm^3 (화강암 밀도)
    BC = 0.0419*rock_density*h #mgal
else:
    raise Exception("잘못된 입력입니다.")

air_correction = 0.87-0.0000965*h #mgal
TC = float(input("지형 보정값을 입력해 주세요: ")) #mgal
perfect_BC = standard_gravity + FAC - BC + air_correction + TC #mgal

if (input("조석 보정을 진행할까요?(y/n): ") == "y"):
    perfect_BC += 1.2 #mgal (지구 조석 보정값)

if(input("표시 단위를 선택하세요(mgal/gal): ") == "mgal"):
    mgal = 1
else:
    mgal = 0
print("--------------------")
if(mgal==1):
    print("측정 지점에서의 중력은", perfect_BC, "mgal 입니다.")
    print("측정 지점에서의 완전부게이상은",perfect_BC-standard_gravity, "mgal 입니다.\n")
    print("측정 지점에서의 표준 중력은", standard_gravity, "mgal 입니다.")
    print("측정 지점에서의 프리에어 보정값은", FAC, "mgal 입니다.")
    print("측정 지점에서의 단순 부게 보정값은", BC, "mgal 입니다.")
    print("측정 지점에서의 대기 보정값은", air_correction, "mgal 입니다.")
    print("측정 지점에서의 지형 보정값은", TC, "mgal 입니다.")
else:
    print("측정 지점에서의 중력은", perfect_BC/1000, "gal 입니다.")
    print("측정 지점에서의 완전부게이상은", (perfect_BC-standard_gravity)/1000, "gal 입니다.\n")
    print("측정 지점에서의 표준 중력은", standard_gravity / 1000, "gal 입니다.")
    print("측정 지점에서의 프리에어 보정값은", FAC / 1000, "gal 입니다.")
    print("측정 지점에서의 단순 부게 보정값은", BC / 1000, "gal 입니다.")
    print("측정 지점에서의 대기 보정값은", air_correction / 1000, "gal 입니다.")
    print("측정 지점에서의 지형 보정값은", TC / 1000, "gal 입니다.")
print("--------------------")