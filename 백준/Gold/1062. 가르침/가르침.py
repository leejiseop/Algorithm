import sys
from itertools import combinations


def word_to_bit(word):
  bit = 0
  for c in word:
    bit = bit | (1 << ord(c) - ord('a'))
  return bit


input = sys.stdin.readline

# n, k = list(map(int, input().split()))
# word_bits = []
# teach_bits = []
# all_alphabets = 0
# answer = 0

# for _ in range(n):
#   word_bit = word_to_bit(input().rstrip())
#   word_bits.append(word_bit)
#   all_alphabets = all_alphabets | word_bit



n, k = list(map(int, input().split()))
words = [input().rstrip() for _ in range(n)]
word_bits = list(map(word_to_bit, words))
base_bit = word_to_bit('antic')


if k < 5:
  print(0)
else:
  alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
      
  answer = 0
  for combi in combinations(alphabet, k-5):
    know_bit = sum(combi) | base_bit
    cnt = 0
    for word_bit in word_bits:
      if word_bit & know_bit == word_bit:
        cnt += 1
    answer = max(answer, cnt)
  print(answer)