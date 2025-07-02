# Class WordplayStr is a subclass of class str
# It inherits all the features of str

# The first parameter of every method has to have the same type as the class in which it is defined
class WordplayStr(str):
    """ A string that can report wheter it has interesting properties. """

    def same_start_and_end(self):
        """ (WordplayStr) -> bool

        >>> s = WordplayStr("abracadabra")
        >>> s.same_start_and_end()
        True
        >>> s = WordplayStr("canoe")
        >>> s.same_start_and_end()
        False
        """
        return self[0] == self[-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
