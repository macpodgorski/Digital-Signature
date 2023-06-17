# Digital-Signature

Here is a list of steps for the user:

1. Launch the program.
2. Choose one of the options:
   - Enter 1 if you want to sign a file.
   - Enter 2 if you want to verify the signature of a file.
   - Enter 3 if you want to exit the program.
3. If you chose option 1 (Sign a file):
   - The program will display a list of files in the current directory.
   - Select the file you want to sign.
   - If the file doesn't exist, the program will display an appropriate notification.
   - Private and public keys will be generated.
   - The file will be signed using the private key.
   - The signed file will be saved in the "signed" directory.
   - The program will display a confirmation message for signing the file.
4. If you chose option 2 (Verify a file):
   - The program will display a list of signed files in the "signed" directory.
   - Select the file whose signature you want to verify.
   - If the file doesn't exist, the program will display an appropriate notification.
   - If the key is damaged, the program will display an appropriate notification.
   - The program will check if the file's signature matches the public key.
   - The program will display a message indicating the validity of the signature.
5. If you chose option 3 (Exit):
   - The program will terminate.
   
Remember to adjust the file paths in the code to your own environment.
