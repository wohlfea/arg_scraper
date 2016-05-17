from BeautifulSoup import BeautifulSoup
from sys import argv
from pprint import pprint
import urllib


def main(url, target):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r)
    pprint(soup)


if __name__ == '__main__':
    main(argv[1], argv[2])
