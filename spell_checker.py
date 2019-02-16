# A decorater for speeding up recursive functions
# We will discuss memoize in a later lecture. Don't worry about its meaning/implementation
class Memoize:
    def __init__(self,f):
        self.f = f
        self.cache = {}

    def __call__(self,*args):
        if args in self.cache:
            return self.cache[args]
        else:
            answer = self.f(*args)
            self.cache[args] = answer
        return answer


# Computes distance between two words recursively: 1 for every addition, deletion, substitution
# Use memoization for dynamic programming speedupt
@Memoize
def min_dist(s1 : str, s2 : str) -> int:
    if s1 == '' or s2 == '':
        return len(s1)+len(s2)
    else:
        return min(1+min_dist(s1,s2[1:]), 1+min_dist(s1[1:],s2), (0 if s1[0]==s2[0] else 1)+ min_dist(s1[1:],s2[1:]))

#by Richard Pattis