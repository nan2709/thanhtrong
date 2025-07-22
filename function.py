# def hello():
#     print("Hello")
# def add(num1,num2):
#     return num1+num2
# #1.Viet ham ktr so nguyen to
# def ktr_SNT(num):
#     if num < 2:
#         return False
#     else:
#         for i in range(2, num-1):
#             if num%i==0:
#                 return False
#     return True
# #2.Viet ham ktr so chinh phuong
# def ktr_SCP(num):
#     if num >0:
#         for i in range(1,int(num/2)+2):
#             if i*i==num:
#                 return True
#     return False
# #3.Viet ham ktr so hoan thien
# def ktr_SHT(num):
#     tong=0
#     if num>0:
#         for i in range(1,num-1):
#             if num%i==0:
#                 tong+=i
#     return tong==num
# if __name__== '__main__':
#     hello()
#     #f-> , bth thi +
#     print(f"Gia tri",add(1,2))
#     num=eval(input("Nhap so ban muon ktr: "))
#     if ktr_SNT(num):
#         print(num, f" la so nguyen to")
#     else:
#         print(num, f" khong la so nguyen to")
#     if ktr_SCP(num):
#         print(num, f" la so chinh phuong")
#     else:
#         print(num, f" khong la so chinh phuong")
#     if ktr_SHT(num):
#         print(num, f" la so hoan thien")
#     else:
#         print(num, f" khong la so hoan thien")
#1
def traNguyenDu(num1,num2):
    if num2==0:
        return None,None
    return num1//num2,num1%num2
# if __name__== '__main__':
#     num1=eval(input("Nhap so ban muon ktr: "))
#     num2=eval(input("Nhap so ban muon ktr: "))
#     print(traNguyenDu(num1,num2))
#2
def tbc(n1,n2,n3,n4):
    return (n1+n2+n3+n4)/4
# if __name__== '__main__':
#    n1=eval(input("Nhap a:"))
#    n2=eval(input("Nhap b:"))
#    n3=eval(input("Nhap c:"))
#    n4=eval(input("Nhap d:"))
#    print("trung binh cong: ",tbc(n1,n2,n3,n4))
#3
def tonggiay(n1,n2,n3):
    return n1*3600+n2*60+n3
# if __name__== '__main__':
#     n1=eval(input("Nhap gio: "))
#     n2=eval(input("nhap phut: "))
#     n3=eval(input("Nhap giay: "))
#     print("tong giay: ",tonggiay(n1,n2,n3))
#4
def tongNguyenDu(n1,n2):
    if n2==0:
        return None
    return n1//n2+n1%n2
# if __name__== '__main__':
#     n1=eval(input("Nhap so ban muon ktr: "))
#     n2=eval(input("Nhap so ban muon ktr: "))
#     if tongNguyenDu(n1,n2)==None:
#         print("ko co gia tri")
#     else:
#         print("tong phan nguyen va du la: ",tongNguyenDu(n1,n2))
#5
def xetchan(n1):
    if n1%2==0:
        print("chan")
    else:
        print("ko chan")
# if __name__== '__main__':
#     while True:
#         try:
#             n1 = int(input("Nhap mot so co 2 chu so: "))
#             if 10 > n1 or n1> 99:
#                 print(" Vui long nhap so co dung 2 chu so!")
#             else:
#                 break
#         except ValueError:
#             print(" Chi duoc nhap so nguyen!")   
#     xetchan(n1)
#6
def xettongcolon10(n1):
    if (n1//10+n1%10)>10:
        print("lon hon 10")
    else:
        print("nho hon 10")
    if __name__== '__main__':
     while True:
         try:
             n1=int(input("Nhap so co 2 chu so: "))
             if not(10 <=n1<= 99):
                 print(" Vui long nhap so co dung 2 chu so!")
             else:
                 break
         except ValueError:
            print(" Chi duoc nhap so nguyen!") 
     xettongcolon10(n1)