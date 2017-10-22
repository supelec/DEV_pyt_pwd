#!/usr/bin/python3
# coding: utf-8

import sys
import os
import platform

import multiprocessing

def available_cpu_count():
    try:
        res = open('/proc/cpuinfo').read().count('processor\t:')
        if res > 0:
            return res
    except IOError:
        pass


def main(argv):
    if (len(argv) < 1):
        print("Pas d'arguments")
        return 2
    print("Arguments")
    return 0

print(available_cpu_count())

if __name__ == "__main__":
    valok = []
    print("Fin")
    valok = str(sys.path[0])
    print(sys.path[0])
    print(sys.platform)
    print(os.name)
    print(platform.processor())
    print(platform.uname())
    print(len(os.sched_getaffinity(0)))
    print(os.cpu_count())
    print(multiprocessing.cpu_count())
    sys.exit(main(sys.argv[1:])) # Quitte proprement le programme avec les erreurs convenue
