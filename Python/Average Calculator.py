"""Average Calculator (Language: Python)"""
p1 = int(input("P1: "))
p2 = int(input("P2: "))
p3 = int(input("P3: "))
p4 = int(input("P4: "))
p5 = int(input("P5: "))
av = (p1 + p2 + p3 + p4 + p5) / (5)
print("\n",av)
if(av >= 50):
    print("Passed!")
elif(av < 50):
    print("Stayed...")