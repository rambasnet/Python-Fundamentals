"""
File I/O Lab
By: FIXME0

CSCI 110
Date: FIXME0

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""

from typing import List

totalInts = 10


def readData() -> List[int]:
    """Read data from a file.

    Returns:
        List[int]: List of integers
    """
    intList = []
    # FIXME1 (20 points):
    # Prompt user to input file name
    # open the file; read each number one line at a time;
    # and store it into intList list
    # close the file
    # return the intList
    return intList


def sortListInAscendingOrder(lstInts: List[int]):
    # FIXME2
    # sort lstInts list in ascending order
    pass


def sortListInDescendingOrder(lstInts):
    # FIXME3
    # sort lstInts in descending order
    pass


def printList(printFile, lstInts: List[int]):
    for n in lstInts:
        # FIXME4
        # write each value one line at a time to file
        # handled by printFile object.
        pass
    printFile.write('\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    # FIXME5
    # Call sortListInDescendingOrder function

    # FIXME6
    # Write the sorted list in descending order to the output file

    # FIXME7
    # Print the largest number to the output file

    # FIXME8
    # Print the smallest number to the output file

    printFile.close()
    print('Done executing the program! Check the output file for results.')


# FIXME9
# Call main function if this module is run as the main module
