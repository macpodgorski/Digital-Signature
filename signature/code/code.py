from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pss
import os
import random

def generate_keys(random_bits_file, signed):
    with open(random_bits_file, 'rb') as f:
        random_seed = f.read()

    bytearray_data = bytearray(random_seed)  # Convert bytes to a mutable bytearray
    random.shuffle(bytearray_data)  # Shuffle the elements
    random_seed = bytes(bytearray_data)

    random.seed(random_seed)

    private_key = RSA.generate(2048, random.randbytes)
    public_key = private_key.publickey()

    with open('/Users/mp/Desktop/semestr6/bst/laby/signature/keys/public_key_'+signed+'.pem', 'wb') as f:
        f.write(public_key.export_key('PEM'))
        
    return private_key, public_key

choice = 0

while (choice >= 0):
    print("\nWhat would you like to do?")
    print("1. Sign a file")
    print("2. Verify a file")
    print("3. Exit")

    choice = int(input())
    print("\n")

    if choice == 1:
        path = "/Users/mp/Desktop/semestr6/bst/laby/signature"
        dirs = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

        for file in dirs:
            print(file)
            
        while True:
            download_file = input("Which file do you want to sign? ")
            try:
                open_file = open(download_file, "rb")
                read_file = open_file.read()
                break
            except FileNotFoundError:
                print("File not found!")


        file_name = download_file.split(".")[0]

        random_bits_file = '/Users/mp/Desktop/semestr6/bst/laby/signature/seed/bitslfsr1.bin'
        pri, pub = generate_keys(random_bits_file, file_name)

        hash = SHA256.new()
        hash.update(read_file)
        signature = pss.new(pri).sign(hash)

        fsave=open("/Users/mp/Desktop/semestr6/bst/laby/signature/signed/signed_"+file_name+".txt", "wb")
        fsave.write(signature)
        fsave.close()
        print("File signed!")

    elif choice == 2: 
        path = "/Users/mp/Desktop/semestr6/bst/laby/signature"
        dirs = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

        for file in dirs:
            print(file)

        while True:
            download_file_verify = input("Which file do you want to verify? ")
            try:
                file_verify = open(download_file_verify, "rb")
                file_verify_open = file_verify.read()
                signed = download_file_verify.split(".")[0]

                hash2 = SHA256.new()
                hash2.update(file_verify_open)

                with open('/Users/mp/Desktop/semestr6/bst/laby/signature/keys/public_key_'+signed+'.pem', 'rb') as f:
                    public_key_pem = f.read()
                    if len(public_key_pem) < 450:
                        raise ValueError
                    pub = RSA.import_key(public_key_pem)

                break
            except FileNotFoundError:
                print("File not found!")
            except ValueError:
                print("The key is damaged.")

        print("\n")
            
        verifier = pss.new(pub)
        
        path = "/Users/mp/Desktop/semestr6/bst/laby/signature/signed/"
        dirs = os.listdir(path)

        for file in dirs:
            print(file)

        print("\n")

        while True:
            download_file_sign = input("Select a signed file: ")
            try:
                file_sign = open('/Users/mp/Desktop/semestr6/bst/laby/signature/signed/'+download_file_sign, "rb")
                file_sign_open = file_sign.read()

                break
            except (FileNotFoundError, IOError):
                print("File not found!")

        try:
            verifier.verify(hash2, file_sign_open)
            print("Signature is valid!\n")
        except(ValueError, TypeError):
            print("Signature is not valid!\n")
    
    elif choice == 3:
        choice = -1
