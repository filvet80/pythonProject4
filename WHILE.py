def function(a, b, c):
  while a < c:
      print(a + b)
      a += b
      if a >= c:
        break
  print("The Cycle is Over")
function(9, 3, 18)