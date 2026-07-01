print("Enter Marks Obtained in 4 Subjects")
math =int(input("maths :"))
english =int(input("english :"))
physics =int(input("physics :"))
chemistry =int(input("chemistry :"))
socialscience =int(input("social science :"))
tamil =int(input("tamil :"))

sum = math+english+physics+chemistry+socialscience+tamil
print("Math , English , Physics , Chemistry , Social Science , Tamil")

perc = (sum/600)*100

print("Percentage Mark = ")
print(perc)
