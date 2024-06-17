# str1="Welcome@@2To%%Python**Programming@!!^%%@$"

# for i in str1:
#     if i=='@' or i=="%" or i=="!" or i=='^':
#         print("Yes! Special Character is there")
#     else:
#         print("NO Special Character")

import re

str2="Welcome@@2To%%Python**Programming@!!^%%@$"

regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')

if regex.search(str2) == None:
    print("No Special Character in String")
else:
    print("String contains special character")