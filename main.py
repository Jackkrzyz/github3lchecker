import requests, random, string, multiprocessing
user = ""
shtuf = 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
def _3_letter_check_mixed():
    print('starting 3 letter check (mixed)')
    while True:
        user = str(shtuf[random.randrange(35)]) + str(shtuf[random.randrange(35)]) + str(shtuf[random.randrange(35)])
        proxie_list = []


        with open("https.txt", "r") as f:                   #USE HTTPS PROXIES ONLY
            for proxy in f.readlines():
                proxie_list.append(proxy.replace("\n", ""))
        proxies = {
           'https': random.choice(proxie_list)
        }
        print(user)
        r = requests.get(f'https://github.com/{user}', proxies=proxies, timeout=5)
        if r.status_code == 404:
            with open('3lmixed.txt', 'w') as t:
                t.write(user)
def _3_letter_check_num_only():
    print('starting 3 letter check')
    while True:
        user = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
        print(user)
        r = requests.get(f'https://github.com/{user}')
        if r.status_code == 404:
            with open('3lnumonly.txt', 'w') as t:
                t.write(user)
def _3_letter_check_letter_only():
    print('starting 3 letter check')
    while True:
        user = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        print(user)
        r = requests.get(f'https://github.com/{user}')
        if r.status_code == 404:
            with open('3llettersonly.txt', 'w') as t:
                t.write(user)
processes = []
for x in range(20):
    p = multiprocessing.Process(target=_3_letter_check_mixed)
    if __name__ == "__main__":
        p.start()
        processes.append(p)
for x in range(20):
    p = multiprocessing.Process(target=_3_letter_check_num_only)
    if __name__ == "__main__":
        p.start()
        processes.append(p)
for x in range(20):
    p = multiprocessing.Process(target=_3_letter_check_letter_only)
    if __name__ == "__main__":
        p.start()
        processes.append(p)
for p in processes:
    p.join()
    
