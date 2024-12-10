result = ""

with open("fileslist.txt", "r+") as file:
  for line in file:
    if not line.isspace():
      result += line



  file.seek(0)
  file.write(result)

result = result.replace(".nwc", "")
result = result.replace(".nwd", "")
result = result.replace(".ifc", "")
result = result.replace(".dwg", "")
result = result.replace("Project Files/06_Shared/01_Federated Model/01_Navis", "")
result = result.split("\n")

result.sort()

from transmittal_func import*

v = 84

print("Federated model V%s:" % (v))
for n in result:
  transmittalnotes(n)

print(result)
