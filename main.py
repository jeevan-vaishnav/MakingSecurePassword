
# for eg my password thisisGoodBoy its week
# eg. BlackBoard123
SECURE = (('s', '1s'), ('and', '1and'), ('a', '1a'), ('o', '10'), ('i', '1i'))

# teking password


def securePassword(password):
    for a, b in SECURE:
        password = password.replace(a, b)
    return password


# Start with main fuction
if __name__ == "__main__":
    password = input("Enter your password ")
    password = securePassword(password)
    print(f'You secure password is :  {password}')
