from BeautifulSoup import BeautifulSoup
from sys import argv
import urllib


def main(url, target):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r)
    print(soup.prettify())


if __name__ == '__main__':
    main(argv[1], argv[2])
