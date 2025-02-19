def base_to_decimal(num,base):
    
    return int(num,base)

def decimal_to_base(a,base):

        if a == 0:
            return "0"
        conv=""
        while a:
            r = int(a%base)
            if r < 10:
                conv += str(r)
            else:
                conv += chr(r - 10 + ord('A'))
            a //= base
        return conv[::-1]

def base_to_base(num, initial_base,final_base):
    
    decimal_value = base_to_decimal(num,initial_base)    
    return decimal_to_base(decimal_value,final_base)

num = input("Enter the Number: ") 
initial_base = int(input("Enter the Initial Base: ")) 
final_base = int(input("Enter the Final Base: ")) 

converted_number = base_to_base(num,initial_base,final_base)
print(f"{num} in base {initial_base} is {converted_number} in base {final_base}")
