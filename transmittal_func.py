def transmittalnotes(single_file_name):
#  print(single_file_name)
  if "FCC" not in single_file_name and "FFW" not in single_file_name and "VC1" not in single_file_name and "LOG" not in single_file_name and "PRO" not in single_file_name and "IL19" not in single_file_name:
    list = single_file_name.split("_")
    if list[1] == "BU":
      discipline = "BUILDING"
    elif list[1] == "HV":
      discipline = "HVAC"
    elif list[1] == "BI":
      discipline = "Structure"
    else:
      discipline= "<update discipline codification>"
    if list[2] == "VLG":
      originator = "Van Looy"
    elif list[2] == "DDE":
      originator = "DD Engineering"
    else:
      originator = "<update originator codification>"
    Number = "Design"
  else:
    list = single_file_name.split("-")
    if list[1] == "SWE":
      originator = "Sweco"
    elif list[1] == "ITD":
      originator = "ITD"
    elif list[1] == "BPR":
      originator = "Blue Projects"
    elif list[1] == "AGI":
      originator = "Agidens"
    elif list[1] == "CLG":
      originator = "Cleangrad"
    elif list[1] == "HYL":
      originator = "Hyline"
    elif list[1] == "ABB":
      originator = "ABBS"
    elif list[1] == "GIE":
      originator = "GIEC"
    elif list[1] == "HOB":
      originator = "Hooyberghs"
    elif list[1] == "NOP":
      originator = "Nopek"
    elif list[1] == "ACT":
     originator = "Actemium"
    elif list[1] == "STE":
      originator = "Steyaert"
    elif list[1] == "ERG":
      originator = "Ergon/D Concrete"
    elif list[1] == "PFR":
      originator = "Pfizer"
    elif list[1] == "STS":
      originator = "STS Engineering"
    elif list[1] == "DDE":
      originator = "DD Engineering"
    elif list[1] == "VLG":
      originator = "Van Looy Group"
    elif list[1] == "ATI":
      originator = "AlfaTI"
    elif list[1] == "ABE":
      originator = "Abetec"
    elif list[1] == "EQU":
      originator = "Equans"
    elif list[1] == "IBS":
      originator = "IBS"
    else:
      originator = "<update company name>"
    discipline = list[7]
    list[6] = int(list[6])
    if list[6] in range(0, 1000):
      Number = "Design"
    elif list[6] in range(1000, 2000):
      Number = "For Approv"
    elif list[6] in range(2000, 3000):
      Number = "Approved"
    elif list[6] in range(9000, 10000):
      Number = "As Built"
    else:
      Number = "<update number codification>"
  print("- updated %s %s %s model" % (originator, discipline, Number))