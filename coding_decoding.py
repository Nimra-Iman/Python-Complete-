import random
import string
f_three=""
l_three=""
encoded_text=""
text=input("enter text to encode")
word=(text.split(" "))
for i in word:
    # print(i)
    if (len(i)<3):
        converted=(i[::-1])
        # print(converted)
        encoded_text=encoded_text+converted+" "
    else:
        first_letter=i[0]
        x=(i+first_letter)
        without_random_letters=(x[1:])
        # print(without_random_letters)
        for i in range(3):
            if(len(f_three)==3 or len(l_three)==3):
                f_three=f_three.replace(f_three,"") #yani f_three ko empty kr do vrna 
                # second time jab loop first iteration s chalna start ho gi to
                # random letter jo f_three k ander ay ga vo f_three ka phla random
                # letter nhi ho ga bal k us k ander phly s kuch random letters mojod
                # ho gy jo k is case m 3 ho gy q k jab phly loop chali to vo random
                # letters already us k ander pry huy th
                l_three=l_three.replace(l_three,"")
            random_letter=random.choice(string.ascii_lowercase)
            f_three=f_three+random_letter
            random_letter=random.choice(string.ascii_lowercase)
            l_three=l_three+random_letter
        # print(f_three)
        final_coding=f_three+without_random_letters+l_three
        # print(final_coding)
        encoded_text=encoded_text+final_coding+" "
print (encoded_text)

# DECODING
str= input("enter text to decode")
final_decoded_string=" "
word=str.split(" ")
# print(word)
for i in word:
    # print(i)
    if(len(i)<3):
        reverse=i[::-1]
        final_decoded_string=final_decoded_string+reverse+" "
    else:
        first_remove=i[3:]
        # print(first_remove)
        last_remove=first_remove[:-3]
        # print(last_remove)
        last_index=last_remove[-1]
        word_without_last_letter=last_remove[:-1]
        decoded_word= last_index+ word_without_last_letter
        # print(decoded_word)
        final_decoded_string=final_decoded_string+decoded_word+" "
print(final_decoded_string)
        