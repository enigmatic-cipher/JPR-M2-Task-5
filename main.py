"""
Given a string as input, create a new string where the latter half appears first. If the string is of odd length then the middle char remains in its position.
Input: "123456" / "HELLO"
Output: 456123 / LOLHE
"""

st = "123456"
ln = len(st)
st1 = ""
for i in range(0,ln):
  ch = st[i]
  if(ln%2==0):
    st1 = st1 + ch
    