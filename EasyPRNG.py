A = input("Enter number A = ")
B = input("Enter number B = ")
M = input("Enter number M = ")
G = 0
X = (A * G + B)%M
N = input("How much do you wanna show? ")
for i in range(0, N-1):
    print(X)
    X = (A * X + B)%M