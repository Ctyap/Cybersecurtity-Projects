'''
Whenever verifying a user or something similar with a password,
you must never store the password in plaintext. If an attacker
finds a database of plaintext passwords, they can easily be used
in combination with matching emails to login to the associated site/account
and even used to attempt to log into other accounts since a lot of people use the same password.
'''
import hashlib, binascii, os

def hash_password(password):
    
    #Generates random salt that is added to pass, then extracts string reprsentation
    #of hashed salt as a set of hexadecimal numbers
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    
    #pbkdf2_hmac requires bytes as input (.encode) -- returns bytes
    pwdhash = hashlib.pbkdf2_hmac('sha512', #the hash digest algorithm for HMAC
                          password.encode('utf-8'), #converts password to bytes
                          salt, #Adds the salt
                          100000 #100k iterations of Sha256
                          )
    #Return the hexadecimal representation of the binary data.
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]#64 is length of the salt
    stored_password = stored_password[64:]
    
    pwdhash = hashlib.pbkdf2_hmac('sha512', #the hash digest algorithm for HMAC
                          provided_password.encode('utf-8'), #converts password to bytes
                          salt.encode('ascii'), #Adds the salt
                          100000 #100k iterations of Sha256
                          )
    
    #Converts it into a string
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
    

if __name__ == "__main__":
    '''
    hash_password can be used to hash the user password for storage on disk or database.
    verify_password verifies the pasword against the stored on when a user tries to log back in.
    '''
    
    stored_password = hash_password(input("Enter password you would like to Hash:"))
    print("Hashed password: ", stored_password)
    
    while True:
            
        verify_pass = input("\nEnter a passowrd until its verified with hashed password: ")
        if verify_password(stored_password, verify_pass) is True:
            print("Password Matches.")
        else:
            print("Password fails to match. Please try again.")


    
