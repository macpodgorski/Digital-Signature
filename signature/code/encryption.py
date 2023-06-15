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
    print("\nCo chcesz zrobic?")
    print("1. Podpisać plik")
    print("2. Sprawdzić plik")
    print("3. Wyjść")

    choice = int(input())
    print("\n")

    if choice == 1:
        path = "/Users/mp/Desktop/semestr6/bst/laby/signature"
        dirs = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

        for file in dirs:
            print(file)
            
        while True:
            download_file = input("Jaki plik chcesz podpisać? ")
            try:
                open_file = open(download_file, "rb")
                read_file = open_file.read()
                break
            except FileNotFoundError:
                print("Nie ma takiego pliku!")


        file_name = download_file.split(".")[0]

        random_bits_file = '/Users/mp/Desktop/semestr6/bst/laby/signature/seed/bitslfsr1.bin'
        pri, pub = generate_keys(random_bits_file, file_name)

        hash = SHA256.new()
        hash.update(read_file)
        signature = pss.new(pri).sign(hash)

        fsave=open("/Users/mp/Desktop/semestr6/bst/laby/signature/signed/signed_"+file_name+".txt", "wb")
        fsave.write(signature)
        fsave.close()
        print("Plik podpisany!")

    elif choice == 2: 
        path = "/Users/mp/Desktop/semestr6/bst/laby/signature"
        dirs = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

        for file in dirs:
            print(file)

        while True:
            download_file_verify = input("Jaki plik chcesz sprawdzic? ")
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
                print("Nie ma takiego pliku!")
            except ValueError:
                print("Klucz jest uszkodzony")

        print("\n")
            
        verifier = pss.new(pub)
        
        path = "/Users/mp/Desktop/semestr6/bst/laby/signature/signed/"
        dirs = os.listdir(path)

        for file in dirs:
            print(file)

        print("\n")

        while True:
            download_file_sign = input("Wybierz podpisany plik ")
            try:
                file_sign = open('/Users/mp/Desktop/semestr6/bst/laby/signature/signed/'+download_file_sign, "rb")
                file_sign_open = file_sign.read()

                break
            except (FileNotFoundError, IOError):
                print("Nie ma takiego pliku!")

        try:
            verifier.verify(hash2, file_sign_open)
            print("Podpis sie zgadza!\n")
        except(ValueError, TypeError):
            print("Podpis sie nie zgadza!\n")
    
    elif choice == 3:
        choice = -1