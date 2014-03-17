from matric_hash import *
validate_set = {
  "1022751": "d",
  "1240101": "g",
  "1020305": "k",
  "1021230": "j",
  "1122857": "f",
  "1320141": "j",
  "1320184": "c",
  "1320579": "j",
  "1322965": "d",
  "1322790": "j",
  "1021388": "k",
  "1321467": "g",
  "1321829": "f",
  "1322455": "g",
  "1320195": "j",
  "1320544": "h",
  "1320905": "k",
  "1323047": "j",
  "1322929": "l",
  "1321324": "l",
  "1320914": "l",
  "1321259": "k",
  "1020592": "e",
  "1322989": "k",
  "1322920": "e",
  "1321445": "f",
  "1240045": "g",
  "1321427": "d",
  "1320576": "g",
  "1320670": "e",
  "1122762": "f",
  "1320551": "d",
  "1321647": "d",
  "1310836": "f",
  "1310924": "e",
  "1221043": "h",
  "1322169": "j",
  "1122884": "j",
  "1020285": "c",
  "1120840": "a",
  "1220441": "h",
  "1320782": "k",
  "1322294": "j",
  "1220827": "b",
  "1222309": "g",
  "1322968": "f",
  "1321638": "c",
  "1321154": "a",
  "1330863": "f",
  "1320940": "f",
  "1322652": "j",
  "1320793": "e",
  "1320793": "e",
  "1320646": "d",
  "1100187": "b",
  "1320619": "a",
  "1020768": "h",
  "1320560": "e",
  "1123165": "k",
  "1020145": "j",
  "1020597": "a",
  "1320087": "c",
  "1320187": "e",
  "1320605": "d",
  "1220816": "g",
  "1322402": "d",
  "1220504": "j",
  "1020131": "a",
  "1121329": "d",
  "1122983": "c",
  "1220768": "l",
  "1322950": "k",
  "1122995": "f",
  "1120129": "h",
  "1231062": "l",
  "1121587": "b",
  "1122036": "h",
  "1220521": "c",
  "1321622": "a",
  "1322766": "h",
  "1022785": "h",
  "1040013": "e",
  "1022986": "j",
  "1240289": "b",
  "1120733": "c",
  "1220811": "l",
  "1320561": "b",
  "1122859": "l",
  "1221127": "b",
  "1020121": "c",
  "1323045": "d",
  "1221881": "l",
  "1221128": "k",
  "1220062": "d",
  "1020768": "h",
  "1320560": "e",
  "1321808": "b",
  "1321978": "a",
  "1322402": "d",
  "1321465": "e",
  "1120733": "c",
  "1122643": "e",
}
weight = [10, 7, 4, 3, 2, 9, 8] # calculated by matric_hash.py
offset = 0

def validate():
  for key, item in validate_set.items():
    temp = map(lambda x: int(x), " ".join(key).split(" "))
    check_sum = calculate_check_sum(temp, weight)
    if candiates_sum[(check_sum+offset)%11]==item:
      print key
    else:
      print "Wrong: ",key


def guess():
  numbers = [
    "1310088", #g
    "1210269", #e
    "1122741", #b
    "1110005", #g
  ]
  print "Guessing..."
  for number in numbers:
    temp = map(lambda x: int(x), " ".join(number).split(" "))
    check_sum = calculate_check_sum(temp, weight)
    print candiates_sum[(check_sum+offset)%11]


if __name__=="__main__":
  validate()
  guess()
