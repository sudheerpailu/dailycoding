'''Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression
and returns whether or not the string matches the regular expression.
'''
def first_char(s, r):
    return s[0] == r[0] or (r[0] == '.' and len(s) > 0)

def re_matches(s, r):
    if r == '':
        return s == ''

    if len(r) == 1 or r[1] != '*':
        if first_char(s, r):
            return re_matches(s[1:], r[1:])
        else:
            return False
    else:
        if matches(s, r[2:]):
            return True
        i = 0
        while first_char(s[i:], r):
            if re_matches(s[i+1:], r[2:]):
                return True
            i += 1
            
s=input()
r=input()
print(re_matches(s,r))