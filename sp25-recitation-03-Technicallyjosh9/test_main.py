from main import *


## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(10)) == 5 * 10
    assert quadratic_multiply(BinaryNumber(9999),
                              BinaryNumber(5555)) == 9999 * 5555
    assert quadratic_multiply(BinaryNumber(3194), BinaryNumber(1)) == 3194 * 1
    assert quadratic_multiply(BinaryNumber(12), BinaryNumber(7)) == 12 * 7
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(9)) == 2 * 9
    assert quadratic_multiply(BinaryNumber(680),
                              BinaryNumber(720)) == 680 * 720
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(81)) == 0 * 81
