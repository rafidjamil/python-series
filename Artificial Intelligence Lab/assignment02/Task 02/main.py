
import textkit
from textkit import rle_encode
import textkit as tk

strings = ["aaabbc", "", "aaaa", "hello"]

for s in strings:
    assert tk.rle_decode(tk.rle_encode(s)) == s

assert rle_encode("aaabbc") == "a3b2c1"
assert rle_encode("") == ""
assert rle_encode("aaaa") == "a4"

assert textkit.rle_decode("x12y1") == "xxxxxxxxxxxxy"
assert textkit.rle_decode("") == ""
assert textkit.rle_decode("a3b2") == "aaabb"

assert tk.caesar_encrypt("hello", 3) == "khoor"
assert tk.caesar_encrypt("", 5) == ""
assert tk.caesar_encrypt("Hello 123!", 2) == "Jgnnq 123!"

assert tk.caesar_decrypt("khoor", 3) == "hello"
assert tk.caesar_decrypt("", 5) == ""
assert tk.caesar_decrypt("Jgnnq 123!", 2) == "Hello 123!"

assert tk.is_palindrome("madam") == True
assert tk.is_palindrome("Hello") == False
assert tk.is_palindrome("") == True
assert tk.is_palindrome("RaceCar") == True

print("All tests passed")
