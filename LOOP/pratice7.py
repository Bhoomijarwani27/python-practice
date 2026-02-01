
    # find the first non  repeated string
input_str = "teetering"
for char in input_str:
   if input_str.count(char) == 1:
      print("char: ",char)
      break
