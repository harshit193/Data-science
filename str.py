##string is immutable -> cannot be changed
## denoted by - '' , "" , """ """
# print(name)
# print(type(name))
##accsessing methods 
# print(name.upper())
# print(name.lower())   
# print(name.title())
# print(name.capitalize())
# print(name.casefold())
# print(name.swapcase())
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())
# print(name.replace("pvt","ltd"))
# print(name.split("f"))
# print(name.partition("d"))
# print(name.startswith("u"))
# print(name.endswith("d"))
# print(name.isalpha())
# print(name.isalnum())
# print(name.isdecimal())
# print(name.isdigit())
# print(name.isnumeric())
# print(name.isspace())
# print(name.islower())
# print(name.isupper())

##ascii , utf-8
# print(name.encode())
# print(name.encode("utf-8"))
# print(name.encode("ascii"))
# print(name.removeprefix("Upf"))
# print(name.removesuffix("2632"))
# print(name.zfill(20))
# print(name.center(30,"*"))
# print(name.ljust(30,"*"))
# print(name.rjust(30,"*"))

##indexing and slicing 
##indexing -- accessing single character from the string
##slicing -- accessing multiple characters from the string

## h e l l o 
## 0 1 2 3 4  - positive 
##-5-4-3-2-1  -- neg 

# print(name[0])
# print(name[-1])

#[start:end:step/skip]
# name = "UpfLairspvt"
# print(name[-3:])

##formattted string //f-string
# age = 10 
# text = "my age is" + age
# text = f"my age is {age}"
# print(text) 

# text = "my name is \"jai\""
# print(text)