import os.path
from sys import platform
import os 
from termcolor import colored
os.system('clear') 
print ("\n\n\t\t\t    ------------------")
print(colored('\t\t\t      Ceaser Cipher  ', 'yellow'))
print ("\t\t\t    ------------------")
print(colored('\n\t\t     * Written by : ', 'green'),end="")
print(colored(' Hussein Adel', 'white'),end="")
print ("\n\t\t\t\t     ------------\n")
print (" ===========================================================================\n")
print (colored('\t\t\t\t  ------------','white'))
print(colored('\t\t\t\t    Hello \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ------------\n','white'))

#------------------------------------------------------------------------  

def encryption(plain_Text,secret_Key):
   Cipher_Text = ""
   plaintext_Len=len(plain_Text)
   for i in range(plaintext_Len):
      if (plain_Text[i].isupper()):
         asciichar=(ord(plain_Text[i]) + secret_Key) % 90
         Cipher_Text =Cipher_Text+ chr(asciichar)
      else:
         asciichar=(ord(plain_Text[i]) + secret_Key) % 122
         Cipher_Text =Cipher_Text+ chr(asciichar)
   return Cipher_Text
def decryption(Cipher_Text,secret_Key):
   plain_Text = ""
   ciphertext_Len=len(Cipher_Text)
   for i in range(ciphertext_Len):
      if (Cipher_Text[i].isupper()):
         asciichar=(ord(Cipher_Text[i]) - secret_Key) % 90
         plain_Text =plain_Text+ chr(asciichar)
      else:
         asciichar=(ord(Cipher_Text[i]) - secret_Key) % 122
         plain_Text =plain_Text+ chr(asciichar)
   return plain_Text
def decryption_Brute_Force(Cipher_Text):
    plain_Text = ""
    ciphertext_Len=len(Cipher_Text)
    secret_Key=1
    while secret_Key!=26:
        print(end="")
        for i in range(ciphertext_Len):
            if (Cipher_Text[i].isupper()):
                asciichar=(ord(Cipher_Text[i]) - secret_Key) % 90
                plain_Text =plain_Text+ chr(asciichar)
            else:
                asciichar=(ord(Cipher_Text[i]) - secret_Key) % 122
                plain_Text =plain_Text+ chr(asciichar)
        print(plain_Text)
        print("\n")
        plain_Text=""
        secret_Key=secret_Key+1

#------------------------------------------------------------------------  

var =int(input(colored("\n1- Encryption\n2- Decryption\n3- Decryption By Brute Force\n\nChoice '1' or '2' or '3': ", 'white')))
if var ==1:
   var2 =int(input(colored("\n1- Message/Text\n2- Text File\n\nChoice '1' or '2' : ", 'white')))
   if var2 == 1:
      plain_Text =str(input(colored("\nEnter Your Message That You Wanna encrypt :  " , 'green')))
      secret_Key= int(input(colored("Enter The Secret key : " , 'green')))
      print(colored("\nYour Encrypted Message is  : " , 'green')+ encryption(plain_Text,secret_Key),end="")
   if var2 == 2:
      file=input(" * Enter the file name with its path and extention : ")
      with open(file) as f:
            contents = f.read()
            if len(contents)==0:
               print(" * There is nothing")
            else:
               secret_Key= int(input(colored("Enter The Secret key : " , 'green')))
               result=encryption(contents,secret_Key)
               with open("encrypted_File.txt", mode = "w") as fi:
                  fi.write(result)
               fi.close()
if var==2:
   var2 =int(input(colored("\n1- Message/Text\n2- Text File\n\nChoice '1' or '2' : ", 'white')))
   if var2 == 1:
      Cipher_Text =str(input("\nEnter Your Cipher Message That You Wanna Decrypt : "))
      secret_Key= int(input("Enter The Secret key : "))
      print(colored("\nYour Decrypted Message is  : ", 'green')+ decryption(Cipher_Text,secret_Key),end="")
   if var2 == 2:
      file=input(" * Enter the encrypted file name with its path and extention : ")
      with open(file) as f:
            contents = f.read()
            if len(contents)==0:
               print(" * There is nothing")
            else:
               secret_Key= int(input(colored("Enter The Secret key : " , 'green')))
               result=decryption(contents,secret_Key)
               with open("decrypted_File.txt", mode = "w") as fi:
                  fi.write(result)
               fi.close()
if var==3:
   var2 =int(input(colored("\n1- Message/Text\n2- Text File\n\nChoice '1' or '2' : ", 'white')))
   if var2 == 1:
      Cipher_Text =str(input("\nEnter Your Cipher Message That You Wanna Decrypt : "))
      print(colored("\nYour Decrypted Message is  :- \n", 'green'),end="")
      decryption_Brute_Force(Cipher_Text)
   if var2 == 2:
      file=input(" * Enter the encrypted file name with its path and extention : ")
      with open(file) as f:
            contents = f.read()
            if len(contents)==0:
               print(" * There is nothing")
            else:
               result=decryption_Brute_Force(contents)
               with open("decrypted_File.txt", mode = "w") as fi:
                  fi.write(result)
               fi.close()

#---------------------------------------------------------------------------------------

print (colored('\n\n\t\t\t\t  ----------','white'))
print(colored('\t\t\t\t    Done \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ----------\n','white'))

