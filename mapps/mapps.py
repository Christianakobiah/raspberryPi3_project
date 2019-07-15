#def is_even():
#    a = int(input("Enter num1 "))
#    b = int(input("Enter num2 "))
#    c = a + b
#    if(c % 2 == 0):
#        print("is true, you did it")
#    else:
#        print("This is false, try harder")
#        
#is_even()



#
#
#def func():
#    numbers = [1,56,234,87,4,76,24,69,90,135]
#    
#    a = [number for number in numbers if number % 2 == 0]
#    print(a)
#       
#func()
#
#numbers = [1,56,234,87,4,76,24,69,90,135]
#is_even = filter((lambda x : x % 2 == 0) , numbers)
#print(list(is_even))


numbers = [1,56,234,87,4,76,24,69,90,135]
is_even = map((lambda x : x % 2 == 0) , numbers)
print(list(is_even))

