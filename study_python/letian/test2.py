import sys
import re

"""
5
A123
1ABC
A1B2C3
123ABC
A!23

"""

def package_cat(pkg_id):
    pkg_id = pkg_id.replace("\n", "")
    print(pkg_id)
    if re.fullmatch(r'[A-Za-z]+[0-9]+', pkg_id):
        return "standard"
    elif re.fullmatch(r'[0-9]+[A-Za-z]+', pkg_id):
        return "speical"
    elif re.fullmatch(r'[A-Za-z]+[A-Za-z0-9]+', pkg_id):
        return "mix"
    else:
        return "invalid"

def package_cat_new(pkg_id):
    pkg_id = pkg_id.replace("\n", "")

    n =len(pkg_id)


    for i in range(n):
        if not str(pkg_id[i]).isalpha() and not str(pkg_id[i]).isdigit():
            return "invalid"

    prefix_alpha_num = 0
    for i in range(n):
        if str(pkg_id[i]).isalpha():
            prefix_alpha_num +=1
        else:
            break;


    if prefix_alpha_num == n:
        return "invalid"
    elif prefix_alpha_num >0:

        substr = pkg_id[prefix_alpha_num:]
        substr =str(substr)
        for i in substr:
            if str(i).isalpha():
                return "mix"

        return "standard"

    else:

        alpha_index = 1

        for  i, val in enumerate(pkg_id):
            if str(val).isalpha():
                alpha_index = i
                break

        for i in pkg_id[alpha_index:]:
            if str(i).isdigit():
                return "mix"

        return "specail"


s = sys.stdin.readline()
n = int(s)

for i in  range(n):
    package_id = sys.stdin.readline()
    print(package_cat_new(package_id))






