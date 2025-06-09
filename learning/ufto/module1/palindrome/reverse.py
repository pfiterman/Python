def reverse(s):
   """ (str) -> str
   Return a reversed version of s.

   >>> reverse('hello')
   'olleh'
   >>> reverse('a')
   'a'
   """

   rev = ''

   # For each character in s, add that char to the beginning of rev
   for ch in s:
       rev = ch + rev

   return rev 