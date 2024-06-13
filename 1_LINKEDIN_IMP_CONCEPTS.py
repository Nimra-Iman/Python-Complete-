def foo(x=[]):
    x.append(1)
    return x

print(foo())  # Output: [1]
print(foo())  # Output: [1, 1]

# jab bhi kisi mutable data type k saath is trah ka case kryn k hm by_default koi value
# daal di us m , to first time function call pr vo default vali value hi consider kry ga 
# of course but 2nd time call pr vo defualt vali value consider nhi kry ga bal k 
# pichli call pr jo value return hui usi ko consider kry ga or usi value s agy start le ga
# but immutable data types k case m esa nhi ho ga


#!!!!!!!!!!!!!!!!! Mutable Data Types: The same default argument is used across all
                    #  calls, so changes in one call persist and affect 
                    # subsequent calls.  !!!!!!!!!!!!!!!!!!!!!!

#!!!!!!!!!!!!!!!!!!!  Immutable Data Types: Each function call gets a fresh default
                    #  argument, so changes in one call do not affect the next.



