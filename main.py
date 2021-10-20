st = 'zZ'
st_list = list(st)
n = 4
# Z = 90 z= 122 ' ' = 32 A=65 a=97
for item in st_list:
  item_ascii = ord(item)
  if item_ascii == ord(' '):
      item = chr(item_ascii)
      continue
  if item_ascii + n >= ord('Z'):
    
