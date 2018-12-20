"""
pickling and unpickling or serialization and deserialization
"""

import pickle

class Rectangle(object):
    '''
    Rectangle class	
    '''
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width
        self.area = self.getArea()

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return "len: {0:.2f} width: {1:.2f} area: {2:.2f}".format(
            self.length, self.width, self.area)


def main():
    """
	main function
	"""
    fileName = 'binary.pickle'
    try:
        with open(fileName, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        r = Rectangle(10, 5)
        data = {'a': ['apple', 'a2dsaf3@##', 'a$fdw'],
                'b': ['ball', 'black', 'basket'],
                'c': ('cat', 'c!dsfera'),
                'r': r
                }
        with open(fileName, 'wb') as f:
            pickle.dump(data, f)
            print('file {0} not found! Pickle file {0} created.'.format(fileName))
    else:
        if isinstance(data, dict):
            for key in data:
                print(key, '->', data[key])


if __name__ == "__main__":
    main()
