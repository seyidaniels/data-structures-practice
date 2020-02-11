#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPrimeStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def countPrimeStrings(s):
    root = Node(s)

    share(root, s)
    candidates = root.children[0:len(s)]
    count = 0

    while candidates:
        node = candidates.pop(0)
        if is_prime(int(node.value)):
            share(node, s[len(node.get_value()):])
            if node.children:
                candidates.extend(node.children)
            else:
                count += 1

    return count


def share(parent, string):
    for i in range(len(string)):
        child = Node(string[0:i+1])
        parent.add_child(child)


def is_prime(number):
    if number > 1:
        divisor = number // 2
        for i in range(2, divisor+1):
            if number % i == 0:
                return False
        return True
    return False


class Node:
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_value(self):
        v = self.value
        parent = self.parent
        while parent.parent:
            v = parent.get_value() + v
            parent = parent.parent
        return v


print(countPrimeStrings("11373"))
