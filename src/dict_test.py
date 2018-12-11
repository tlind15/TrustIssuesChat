x = {5: None, 6: " ", 7: None, 8: "hello"}

list = [entry for entry in x if x[entry] is not None and x[entry].strip() != ""]
print(list)
