from matric_hash import *
validate_set = {
  "1220076": "d",
  "1220822": "a",
  "1220145": "f",
  "1220767": "a",
  "1222684": "c",
  "1220113": "a",
  "1220827": "b",
  "1120096": "b",
  "1222494": "a",
  "1222432": "f",
  "1220530": "b",
  "1321664": "d",
  "1321666": "j",
  "1221238": "c",
  "1021550": "l",
  "1021352": "a",
  "1020216": "c",
  "1010118": "b",


}
weight = [9, 7, 4, 3, 2, 9, 8] 
offset = 1
if __name__=="__main__":
  for key, item in validate_set.items():
    temp = map(lambda x: int(x), " ".join(key).split(" "))
    check_sum = calculate_check_sum(temp, weight)
    if candiates_sum[(check_sum+offset)%11]==item:
      print key
    else:
      print "Wrong: ",key