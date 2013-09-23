#!/usr/bin/env python

class Stirling(object):
    """
    Stirling numbers of the first and second kind,
    as used in Ane et al. (2006)
    """

    def __init__(self):
        self.s1memo = dict()
        self.s2memo = dict()

    def a(n, k):

        if (n,k) in self.s1memo:
            return self.s1memo[(n,k)]

        if n == k:
            return 1

        if k > n:
            return 0 

        if (n > 0) and (k == 0):
            return 0

        answer = self.a(n-1, k-1) + (n-1)*self.a(n-1, k)
        self.s1memo[(n,k)] = answer
        return answer

    def S(n, k):

        if (n,k) in self.s2memo:
            return self.s2memo[(n,k)]

        if n == k:
            return 1

        if k > n:
            return 0 

        if (n > 0) and (k == 0):
            return 0

        if (n > 0) and (k == 1):
            return 1        

        answer = self.S(n-1, k-1) + k*self.S(n-1, k)
        self.s2memo[(n,k)] = answer
        return answer
