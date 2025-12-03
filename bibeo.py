s = input ("Enter 3 real number (separated by space):")
s = s.split()
a= float (s[0])
b= float (s[1])
c= float (s[2])
print (f"a={a},b={b},c={c}")
# 8 # Enter your code from here
delta = b**2 - 4*a*c

#Kiểm tra điều kiện
if a == 0:
    #Phương trình bậc nhất
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        # bx + c = 0 -> x = -c/b
        x = -c / b
        print(f"Since a = 0, this is a linear equation. It has one solution x = {x}")
else:
    #Phương trình bậc hai
    #Tính và phân loại nghiệm dựa trên delta
    if delta > 0:
        #Hai nghiệm phân biệt
        import math
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"The equation has two distinct real solutions: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        #Nghiệm kép
        x = -b / (2*a)
        print(f"The equation has one double real solution: x = {x}")
    else:
        # Vô nghiệm trong tập số thực
        print("Vô nghiệm trong tập số thực.")