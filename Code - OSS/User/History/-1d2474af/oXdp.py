import os
import random
import string

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def main():
    os.makedirs("data", exist_ok=True)

    with open("data/names.txt", "w") as f:
        for _ in range(1000):  # generate 1000 names
            name = random_string(random.randint(3, 9))
            f.write(name + "\n")

    with open("data/passwords.txt", "w") as f:
        for _ in range(1000):  # generate 1000 passwords
            password = random_string(random.randint(3, 9))
            f.write(password + "\n")

    with open("data/emails.txt", "w") as f:
        for _ in range(1000):  # generate 1000 emails
            local_part = random_string(random.randint(5, 12))
            domain = random_string(random.randint(2, 7))
            f.write(local_part + "@" + domain + ".com\n")

if __name__ == "__main__":
    main()
