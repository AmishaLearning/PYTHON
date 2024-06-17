# import email.utils

# number = int(input("Enter the number of email addreses : "))

# for i in range(number):
#     email_input = email.utils.formataddr(list(map(str, input("Enter name and email : ").split())))
#     # email_input   = email.utils.formataddr(('VIRUS', '<virus!@variable.:p>'))
#     email_address = email_input.split('<')
#     print(email_address)

#     splitting_username    = email_address[2].split('@')
#     user_name             = splitting_username[0]
#     print(user_name)

#     splitting_domain_name = splitting_username[1].split(".")
#     domain_name           = splitting_domain_name[0]
#     print(domain_name)

#     splitting_extension_name = splitting_domain_name[1].split('>')
#     extension_name = splitting_extension_name[0]
#     print(extension_name)


    # def user_name_func(name):
    #     if name[0].isalpha():
    #         for i in name:
    #             if i in ['_', '-', '.'] :
    #                 name1 = name.replace("-","")
    #                 if name1.isalnum() or name1.isalpha():
    #                     return True
                    
    #                 name2 = name.replace("_","")
    #                 if name2.isalnum() or name2.isalpha():
    #                     return True 
                    
    #                 name3 = name.replace(".", "")
    #                 if name3.isalnum() or name3.isalpha():
    #                     return True                           
    #             elif name.isalpha():
    #                 return True
    #         return False

#     def domain_name_func(domain):        
#         if domain.isalpha(): 
#             return True
#         return False

#     def extension_name_func(extension):        
#         if extension.isalpha() and len(extension) in [1, 2, 3]:
#             return True
#         return False
        
#     if user_name_func(user_name) == True and domain_name_func(domain_name) == True and extension_name_func(extension_name) == True:
#         email_id = user_name + "@" + domain_name + "." + extension_name
#         print(email_id)
#     else:
#         print("Invalid Email Id")

# HACKER RANK --- Failing for Test Case 5

import email.utils

number = int(input("Enter the number of email addreses : "))

for i in range(number):
    email_input = email.utils.formataddr(list(map(str, input("Enter name and email : ").split())))
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

    def user_name_func(name):
        if name[0].isalpha():
            for i in name:
                if i in ['_', '-', '.'] :
                    name1 = name.replace("-","")
                    if name1.isalnum() or name1.isalpha():
                        return True
                    
                    name2 = name.replace("_","")
                    if name2.isalnum() or name2.isalpha():
                        return True 
                    
                    name3 = name.replace(".", "")
                    if name3.isalnum() or name3.isalpha():
                        return True                           
                elif name.isalpha():
                    return True
            return False

    def domain_name_func(domain):        
        if domain.isalpha(): 
            return True
        return False

    def extension_name_func(extension):        
        if extension.isalpha() and len(extension_name) in [1, 2, 3]:
            return True
        return False
        
    if user_name_func(user_name) == True and domain_name_func(domain_name) == True and extension_name_func(extension_name) == True:
        result = email_address[0] + "<" + user_name + "@" + domain_name + "." + extension_name + ">"
        print(result)
    else:
        print("***")

