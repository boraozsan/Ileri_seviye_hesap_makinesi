def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
close_calculator=False
while close_calculator is not True:
 n1 =float(input("First number:"))
 islem=input("Select Operation:\n+\n*\n-\n/\n")
 n2=float(input("Second number:"))
 calculator_dic={"*":multiply(n1,n2),"-":substract(n1,n2),"/":divide(n1,n2),"+":add(n1,n2)}
 sonuc=calculator_dic[islem]
 print(sonuc)
 end=input(f"If you want to continue with {sonuc} write 'c', to make a new calculation write 'n', to close the calculator write 'q'.")
 if end=="q":
    close_calculator=True
    print("Have a nice day. :)")
 elif end=="c":
     while end is "c":
         islem = input("Select Operation:\n+\n*\n-\n/\n")
         n1=sonuc
         n2 =float(input("Second number:"))
         calculator_dic = {"*": multiply(n1, n2), "-": substract(n1, n2), "/": divide(n1, n2), "+": add(n1, n2)}
         sonuc = calculator_dic[islem]
         end = input(f"If you want to continue with {sonuc} write 'c', to make a new calculation write 'n', to close the calculator write 'q'.")
         if end=="q":
          close_calculator=True
          print("Have a nice day. :)")

