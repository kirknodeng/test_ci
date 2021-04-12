def test() : 
  str_a = "hello_world"
  
  return str_a

if "__main__" in __name__ : 
  
  assert test() == "hello_world"
