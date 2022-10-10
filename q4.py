import sys
from cryptography.fernet import Fernet


def decrypt(infile, outfile):
    # INfile is the ciphertext, outfile is plaintext.
    # input_file = open(infile, 'r')
    # output_file = open(outfile, 'w')
    # key_input = input("Enter the secret key: ")
    # Fernet.decrypt()
    # input_file.close()
    # output_file.close()
    print("decrypted    ")


def encrypt(infile, outfile):
    #Infile is plaintext, outfile is ciphertext
    input_file = open(infile, 'r')
    output_file = open(outfile, 'w')
    input_lines = input_file.read()
    input_binary = bytes(input_lines, 'utf-8')
    key_input = input("Enter the secret key: ")
    f = Fernet(key_input)
    token = f.encrypt(input_binary)
    output_file.write(token)
    input_file.close()
    output_file.close()
    exit(0)


def main():
    if len(sys.argv) == 4:
        if sys.argv[1] == "-d":
            decrypt(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "-e":
            encrypt(sys.argv[2], sys.argv[3])
    else:
        print("Usage: python3 q4.py -d <input_file> <output_file>\nUsage: python3 q4.py -e <input_file> <output_file>")


if __name__ == '__main__':
    main()
