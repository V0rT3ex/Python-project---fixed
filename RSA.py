import sys
from math import gcd
from random import randint
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def is_prime(n):
    """
    This function receives a number - n.
    It returns whether n is prime or not.
    Time complexity is O(n**0.5) in the worst case.
    """

    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False

    # Looping until i reaches the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_prime_file(a, path):
    """
    This function creates a list of prime numbers under the upper boundary denoted by a.
    It also writes the list to a file.
    """

    # Creating a list of prime numbers.
    prime_list = [i for i in range(a + 1) if is_prime(i)]

    # Opening a file in the path passed as a parameter, to write to.
    with open(path, mode='wt', encoding='utf-8') as f:
        # Writing each number to the file delimited by comma(,).
        for number in prime_list:
            f.write(str(number) + ",")


def generate_primes(path):
    """
    This function receives a path of a file.
    The file contains prime numbers which will be read into a list.
    The function returns two different random prime numbers - p and q.
    If an error occurs, p and q will be -1 in default.
    """

    p, q = -1, -1

    # Opening a file to read from the prime numbers.
    with open(path, mode='rt', encoding='utf-8') as f:
        chunk_size = 256
        # Reading from the file until there is no content.
        prime_list = f.read(chunk_size)
        while True:
            content = f.read(chunk_size)
            if not content:
                break
            prime_list += content
        # Transforming the data from str to a list and delimiting by the comma.
        prime_list = prime_list.split(',')
        # Setting the list to be from its beginning to the end excluding the last item.
        prime_list = prime_list[:-1]

        # Looping until p and q, two random numbers from the list, are different.
        while True:
            p = int(prime_list[randint(0, len(prime_list) - 1)])
            q = int(prime_list[randint(0, len(prime_list) - 1)])
            if p != q:
                break
    return p, q


def generate_keys():
    """ This function creates the public and private key and returns them."""

    Tk().withdraw()
    # Asking the server's user to insert a path to create a text file in.
    path = askopenfilename()

    p, q = generate_primes(path)
    if p == -1 or q == -1:
        print("Something went wrong! Please make sure everything is alright.")
        sys.exit()

    # Creating the modulus(n).
    n = p * q

    # Creating the totient(phi).
    phi = (p - 1) * (q - 1)

    # Creating the public key.
    e = randint(2, phi - 1)
    # Looping until e is relatively prime to phi.
    while True:
        if gcd(e, phi) == 1:
            break
        e = randint(2, phi - 1)

    # Creating the private_key.
    k = 1
    while True:
        d = (1 + k * phi) / e
        if d - int(d) == 0:
            d = int(d)
            break
        k += 1

    return (e, n), (d, n)


def encrypt(message, pub_key):
    """
    This function receives a message to encrypt and a public-key(denoted by pub_key).
    It returns a string which represents a sequence of encrypted numbers.
    """

    e, n = pub_key

    # Transforming each character in the message to its ascii.
    cipher = [ord(char) for char in message]
    # Encrypting
    cipher = [(number ** e % n) for number in cipher]
    # Creating a list which contains each number from cipher and a comma.
    string_cipher = [str(number) + ',' for number in cipher]
    # Transforming the list to a string.
    string_cipher = ''.join(string_cipher)
    return string_cipher


def decrypt(string_cipher, pri_key):
    """
    This function receives a message(string_cipher) to decrypt and a private-key(pri_key).
    It returns a string which represents the original message.
    """

    d, n = pri_key
    # Splitting by each comma.
    cipher = string_cipher.split(',')

    # Setting the list to be from its beginning to the end excluding the last item.
    cipher = cipher[:-1]

    # Decrypting
    cipher = [(int(item) ** d % n) for item in cipher if item != '']

    # Transforming each item to a character.
    decrypted_data = [chr(item) for item in cipher]
    # Transforming the list into a string.
    decrypted_data = ''.join(decrypted_data)
    return decrypted_data


if __name__ == '__main__':
    # path = input("Enter a path to create a prime file:\t")
    # generate_prime_file(200, path)
    # pub_key, priv_key = generate_keys()
    # print(priv_key, pub_key)
    # message = input("Enter a message you'd like to encrypt:\t")
    # e = encrypt(message, pub_key)
    # print("Encrypted data:\t{}".format(e))
    # print("Decrypted data:\t{}".format(decrypt(e, priv_key)))
    pub_key = (3049, 10349)
    pub_key = str(pub_key)
    data = ''
    flag = True
    for i in range(1, len(pub_key) - 1):
        if ord(pub_key[i]) - ord('0') >= 0 and ord(pub_key[i]) - ord('0') <= 9:
            data += pub_key[i]
        elif flag:
            data += ','
            flag = False
    data = data.split(',')
    print(data)
    data = (int(data[0]), int(data[1]))
    print(data)

