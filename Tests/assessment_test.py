import pytest
from Code import python2

def test_one():
    assert python2.one("The") == "TTThhheee"
    assert python2.one("AAbb") == "AAAAAAbbbbbb"
    assert python2.one("Hi-There") == "HHHiii---TTThhheeerrreee"
    assert python2.one("") == ""
    assert python2.one("IoT") == "IIIoooTTT"

def test_two():
    assert python2.two(3) == True
    assert python2.two(8) == False
    assert python2.two(2) == True
    assert python2.two(20) == False
    assert python2.two(73) == True

def test_three():
    assert python2.three(9) == 11106
    assert python2.three(5) == 6170
    assert python2.three(2) == 2468
    assert python2.three(7) == 8638
    assert python2.three(4) == 4936

def test_four():
    assert python2.four("String","Fridge") == "SFtrriidngge"
    assert python2.four("Dog","Cat") == "DCoagt"
    assert python2.four("True","Tree") == "TTrrueee"
    assert python2.four("return","letter") == "rleettutrenr"
    assert python2.four("Cat","Dog") == "CDaotg"

def split(input):
    if len(input) != 5:
        return False
    else:
        for i in input:
            if i % 2 != 0 or 100 > i or i > 200:
                return False
        return True

def test_five():
    assert split(python2.five()) == True
    assert split(python2.five()) == True
    assert split(python2.five()) == True
    assert split(python2.five()) == True
    assert split(python2.five()) == True

def test_six():
    assert python2.six("ilovepy") == True
    assert python2.six("welovepy") == True
    assert python2.six("welovepyforreal") == False
    assert python2.six("pyiscool") == False
    assert python2.six("hurrayforpY") == True

def test_seven():
    assert python2.seven(2,4,6) == True
    assert python2.seven(4,6,2) == True
    assert python2.seven(4,6,3) == False
    assert python2.seven(4,60,9) == False
    assert python2.seven(2,2,2) == True

def test_eight():
    assert python2.eight("Hello", 3) == "Ho"
    assert python2.eight("Chocolate", 3) == "Choate"
    assert python2.eight("Chocolate", 1) == "Choclate"
    assert python2.eight("Water", 1) == "Waer"
    assert python2.eight("Water", 5) == ""

def test_nine():
    assert python2.nine("god", "dog") == True
    assert python2.nine("tree", "tiredest") == True
    assert python2.nine("cat", "dog") == False
    assert python2.nine("tripping", "gin") == True
    assert python2.nine("computer", "python") == False

def test_ten():
    assert python2.ten(3,2) == [[0,0,0],[0,1,2]]
    assert python2.ten(2,1) == [[0,0]]
    assert python2.ten(3,4) == [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]
    assert python2.ten(2,5) == [[0,0],[0,1],[0,2],[0,3],[0,4]]
    assert python2.ten(4,5) == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9], [0, 4, 8, 12]]