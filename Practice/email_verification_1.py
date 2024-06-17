# import email.utils

# print(email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
# print(email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))

# import email.utils

# email_input = email.utils.formataddr(list(map(str, input("Enter name and email : ").split())))
# #email_input   = email.utils.formataddr(('DEXTER', 'dexter@hotmail.com'))
# email_address = email_input.split('<')
# print(email_address)

# splitting_username    = email_address[2].split('@')
# user_name             = splitting_username[0]
# print(user_name)

# splitting_domain_name = splitting_username[1].split(".")
# domain_name           = splitting_domain_name[0]
# print(domain_name)

# splitting_extension_name = splitting_domain_name[1].split('>')
# extension_name = splitting_extension_name[0]
# print(extension_name)

# is_valid = True

# if not user_name.isalpha() or not user_name.isalpha():
#     is_valid = False
# else:
#     is_valid = True
    
# if not domain_name.isalpha(): 
#     is_valid = False
# else:
#     is_valid = True
    
# if not extension_name.isalpha() and not len(extension_name) in [1, 2, 3]:
#     is_valid = False
# else:
#     is_valid = True
    
# if is_valid:
#     email_id = user_name + "@" + domain_name + "." + extension_name
#     print(email_id)
# else:
#     print("Invalid Email Id")


