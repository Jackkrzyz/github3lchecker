import requests, random, string, multiprocessing
shtuf = 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
Checked = []
def _3_letter_check_mixed():
    print('starting 3 letter check (mixed)')
    while True:
        user = str(shtuf[random.randrange(35)]).lower() + str(shtuf[random.randrange(35)]).lower() + str(shtuf[random.randrange(35)]).lower()
        proxie_list = []
        with open("https.txt", "r") as f:                   
            for proxy in f.readlines():
                proxie_list.append(proxy.replace("\n", ""))
        proxies = {
           'https://': random.choice(proxie_list)
        }
        if user not in Checked:
            Checked.append(user)
            try:
                r = requests.get(f'https://github.com/{user}', proxies=proxies, timeout=5)
            except:
                print('REQUEST FAILED')
            if r.status_code == 404:
                with open('usernames.txt', 'a') as t:
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
        if user not in Checked:
            Checked.append(user)
            try:
                r = requests.get(f'https://github.com/{user}', proxies=proxies, timeout=5)
            except:
                print('REQUEST FAILED')
            if r.status_code == 404:
                with open('usernames.txt', 'a') as t:
                    print(f'{user} : AVAILABLE')
                    t.write(user + '\n')
            else:
                print(f'{user} : taken')
def _3_letter_check_letter_only():
    print('starting 3 letter check')
    while True:
        user = random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower()
        proxie_list = []
        with open("https.txt", "r") as f:                   
            for proxy in f.readlines():
                proxie_list.append(proxy.replace("\n", ""))
        proxies = {
           'https://': random.choice(proxie_list)
        }
        if user not in Checked:
            Checked.append(user)
            try:
                r = requests.get(f'https://github.com/{user}', proxies=proxies, timeout=5)
            except:
                print('REQUEST FAILED')
            if r.status_code == 404:
                with open('usernames', 'a') as t:
                    print(f'{user} : AVAILABLE')
                    t.write(user + '\n')
            else:
                print(f'{user} : taken')
processes = []

for i in range(5):
    p = multiprocessing.Process(target=_3_letter_check_mixed)
    if __name__ == "__main__":
        p.start()
        processes.append(p)
for i in range(5):
    p = multiprocessing.Process(target=_3_letter_check_num_only)
    if __name__ == "__main__":
        p.start()
        processes.append(p)
for i in range(5):  
    p = multiprocessing.Process(target=_3_letter_check_letter_only)
    if __name__ == "__main__":
        p.start()
        processes.append(p)
for p in processes:
    p.join()
    
