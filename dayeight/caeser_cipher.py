'''

Caeser cipher project:
user enters their message and the shift number to shift the alphabet
program encrypt or decrypt the message it sent.

'''
alphabet_list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def shift_alpha(shift,text):
    s_alpha =[]
    ind = shift
    x=0
    while x<=25:
        #s_alpha.append(alphabet_list[ind])
         s_alpha.append(alphabet_list[ind])
         ind += 1
         if(ind == 25):
             ind =0
         x +=1
    return s_alpha

def encrypt_text(s_alpha,text):
    encrypt =""
    for i in range(0,len(text)):
        for j in range(0,26):
            if(text[i] ==alphabet_list[j]):
                encrypt += s_alpha[j]
    print("Your encrypted text is: "+encrypt)

def decrypt_text(s_alpha,text):
    decrypt =""
    for i in range(0,len(text)):
        for j in range(0,26):
            if(text[i] ==s_alpha[j]):
                decrypt +=alphabet_list[j]
    print("Your encrypted text is: "+decrypt)

user_choice = input("Do you wnat to encrypt or decrypt your text: ").lower()
user_text = input("Enter the text you wanted "+user_choice).lower()
user_shift = int(input("Enter the shift number: "))

alpha =shift_alpha(user_shift,user_text)
if(user_choice == "encrypt"):
    encrypt_text(alpha,user_text)
elif(user_choice == "decrypt"):
    decrypt_text(alpha,user_text)
