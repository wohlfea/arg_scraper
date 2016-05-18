# _*_ encoding: utf-8 _*_
from bs4 import BeautifulSoup
from sys import argv
from pprint import pprint
import urllib

CSS_TARGETS = {'.': 'class',
               '#': 'id',
               }


def main(url, target):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")
    if target[0] == 'class':
        words = soup.find_all(class_=target[1])
    else:
        words = soup.find_all(id=target[1])
    if words:
        pprint(words)
    else:
        print("There are no results for the {} of '{}'".format(target[0],
                                                                target[1]))


def parse(target):
    """Parse target input. Return tuple to then target correct source."""
    if target[0] not in CSS_TARGETS.keys() or len(target) is 1:
        raise TypeError
    else:
        return (CSS_TARGETS[target[0]], target[1:])


if __name__ == '__main__':
    main(argv[1], parse(argv[2]))
