def palindrome(str):
    for i in range(o,int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return false
    return true
s = 'madam'
ok = palindrome(s)
if (ok):
    print('true')
else:
    print('no')
