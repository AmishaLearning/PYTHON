import email.utils

def user_name_func(name):
    if name[0].isalpha():
        name1 = list(name)
        for char in ['_', '-', '.']:
            while char in name1:
                name1.remove(char)
        cleaned_name = "".join(name1)
        if cleaned_name.isalnum() or cleaned_name.isalpha():
            return True
        return False         
           
def domain_name_func(domain):        
    email_address = email_input.split()
    new_email = email_address[1].split('@')
    count = 0
    for i in new_email[1]:
        if '.' in i:
            count += 1
    if count > 1:
        return False
    
    # if domain.isalpha(): 
    #      return True
    

def extension_name_func(extension):        
    if extension.isalpha() and len(extension_name) in [1, 2, 3]:
        return True
    return False

# number = int(input("Enter the number of email addreses : "))
number = 1

for i in range(number):
    # email_input = email.utils.formataddr(list(map(str, input("Enter name and email : ").split())))
    email_input = email.utils.formataddr(('vineet', '<vineet@gma.il.co.m>'))
    email_address = email_input.split('<')
   
    try: 
        splitting_username    = email_address[2].split('@')
        user_name             = splitting_username[0]
        print(user_name)
        
        splitting_domain_name = splitting_username[1].split(".")
        domain_name           = splitting_domain_name[0]
        print(domain_name)

        splitting_extension_name = splitting_domain_name[1].split('>')
        extension_name = splitting_extension_name[0]
        print(extension_name)
        print(len(extension_name))
        
    except Exception as e:
        pass


if user_name_func(user_name) == True and domain_name_func(domain_name) == True and extension_name_func(extension_name) == True:
    result = email_address[0] + "<" + user_name + "@" + domain_name + "." + extension_name + ">"
    print(result)
else:
    print("Invalid")
    print("***")


