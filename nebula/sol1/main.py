
from collections import defaultdict

PRESTATES = {
    1: (
        ((1,0),(0,0)),
        ((0,1),(0,0)),
        ((0,0),(1,0)),
        ((0,0),(0,1))
    ),
    0: (
        ((0, 1), (0, 1)),
        ((0, 1), (1, 1)),
        ((1, 0), (1, 1)),
        ((1, 1), (0, 0)),
        ((1, 1), (1, 0)),
        ((0, 1), (1, 0)),
        ((0, 0), (0, 0)),
        ((1, 0), (1, 0)),
        ((1, 0), (0, 1)),
        ((1, 1), (0, 1)),
        ((0, 0), (1, 1)),
        ((1, 1), (1, 1))
    )
}

def col_preimg_generator(c1, c2):
    for pre_c1 in c1:
        for pre_c2 in c2:
            if pre_c1[-1] == pre_c2[0]:
                # returns a generator object
                # each element is a 2x? matrix which has one additional column appended
                # according to the given rule
                yield tuple(pre_c1)+(pre_c2[1],)


def get_col_preimages(col):
    # PRESTATES[col[0]] gets the prestates for the first entry in the column
    # noticed that preimages is now exactly the same as PRESTATES[col[0]] on the heap
    # so all the changes make to preimages are also make in PRESTATES
    # and all changes are carried over permanently
    preimages = PRESTATES[col[0]]
    # just a fancy for loop; it does convert col to an generator object, so that might be faster
    # than using a typical for loop
    for _, cell in filter(lambda k: k[0]>0, enumerate(col)):
        # generates preimages from the current set of preimages. 
        # Remember, this list of preimages grows each time col_preimg_generator is called on it
        # This avoids recursion by using the fact that preimages is stored on the heap
        preimages = col_preimg_generator(preimages, PRESTATES[cell])
    # This fancy line does the following
        # pre is a type of duples ((a, b), (c, d), ..., (y, z))
        # zip(*pre) = (a, c, e, ..., y), (b, c, e, ..., z)
        # Group this into a tuple with tuple(zip(*pre))
        # Then we have the his comprenension, and finally the tuple converter at the end. 
        # For some reason, the author is preferring to keep everything as a tuple instead of a list.
        # Notice that tuples are immutable, so you cannot manipulate them like you would a list
    return tuple([tuple(zip(*pre)) for pre in preimages])


if __name__ == "__main__":
    col = [True, False]

    print(get_col_preimages(col))
