def arrayCheck(nums):
    # CODE GOES HERE
    for i in range(len(nums)-2):
        if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
            return True
        else:
            return False
print(arrayCheck([1, 1, 2, 1, 3]))

def stringBits(str):
  # CODE GOES HERE
    newstring = ''
    for i in range (len(str)):
        if(i%2==0):
            newstring=newstring+str[i]
    return newstring

print(stringBits("Heeololeo"))


def end_other(a, b):
  # CODE GOES HERE
    if(len(a)>len(b)):
        for i in range(1,len(b)):
            if(b[-1*i].lower()!=a[-1*i].lower()):
                return False
    else:
        for i in range(1,len(a)):
            if(b[-1*i].lower()!=a[-1*i].lower()):
                return False
    return True

print(end_other('abc', 'abXabCd'))

def doubleChar(str):
  # CODE GOES HERE
    newstr = ''
    for i in range(len(str)):
        newstr=newstr+str[i]+str[i]
    return newstr

print(doubleChar('Hi-There'))

def no_teen_sum(a, b, c):
  # CODE GOES HERE
    return(fix_teen(a)+fix_teen(b)+fix_teen(c))

def fix_teen(n):
  # CODE GOES HERE
    if(n<13 or n==15 or n==16):
        return n
    else:
        return 0

print(no_teen_sum(1, 2, 3))

def count_evens(nums):
  # CODE GOES HERE
    count=0
    for i in range(len(nums)):
        if(nums[i]%2==0):
            count+=1
    return count

print(count_evens([2, 1, 0]))
