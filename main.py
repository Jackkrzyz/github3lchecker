import requests, random, string, multiprocessing
user = ""
shtuf = 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
mixedChecked = []
numChecked = []
alphaChecked = []
def _3_letter_check_mixed():
    print('starting 3 letter check (mixed)')
    while True:
        user = str(shtuf[random.randrange(35)]) + str(shtuf[random.randrange(35)]) + str(shtuf[random.randrange(35)])
        proxie_list = []
        with open("https.txt", "r") as f:                   
            for proxy in f.readlines():
                proxie_list.append(proxy.replace("\n", ""))
        proxies = {
           'https://': random.choice(proxie_list)
        }
        if user not in mixedChecked:
            mixedChecked.append(user)
            r = requests.get(f'https://github.com/{user}', proxies=proxies, timeout=5)
            if r.status_code == 404:
                with open('3lmixed.txt', 'a') as t:
                    print(f'{user} : AVAILABLE')
                    t.write(user + '\n')
            else:
                print(f'{user} : taken')
def _3_letter_check_num_only():
    print('starting 3 letter check')
    while True:
        user = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
        proxie_list = []
        with open("https.txt", "r") as f:                   
            for proxy in f.readlines():
                proxie_list.append(proxy.replace("\n", ""))
        proxies = {
           'https://': random.choice(proxie_list)
        }
        if user not in numChecked:
            numChecked.append(user)
            r = requests.get(f'https://github.com/{user}', proxies=proxies, timeout=5)
            if r.status_code == 404:
                with open('3lnumonly.txt', 'a') as t:
                    print(f'{user} : AVAILABLE')
                    t.write(user + '\n')
            else:
                print(f'{user} : taken')
def _3_letter_check_letter_only():
    print('starting 3 letter check')
    while True:
        user = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        proxie_list = []
        with open("https.txt", "r") as f:                   
            for proxy in f.readlines():
                proxie_list.append(proxy.replace("\n", ""))
        proxies = {
           'https://': random.choice(proxie_list)
        }
        if user not in alphaChecked:
            alphaChecked.append(user)
            r = requests.get(f'https://github.com/{user}', proxies=proxies, timeout=5)
            if r.status_code == 404:
                with open('3llettersonly.txt', 'a') as t:
                    print(f'{user} : AVAILABLE')
                    t.write(user + '\n')
            else:
                print(f'{user} : taken')
processes = []

p = multiprocessing.Process(target=_3_letter_check_mixed)
if __name__ == "__main__":
    p.start()
    processes.append(p)
p = multiprocessing.Process(target=_3_letter_check_num_only)
if __name__ == "__main__":
    p.start()
    processes.append(p)

p = multiprocessing.Process(target=_3_letter_check_letter_only)
if __name__ == "__main__":
    p.start()
    processes.append(p)
for p in processes:
    p.join()
    
