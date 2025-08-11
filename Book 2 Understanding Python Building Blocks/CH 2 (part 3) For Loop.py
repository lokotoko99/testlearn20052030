for x in range(1,8):
    print(x)
print("All done!")

country = "JAPAN"
for x in country:
    print(x)
print("done!")

countries = ["Japan","Pakistan","Mexico","Russia","Israel","United Kingdom"]

#break

for x in countries:
    if x == "Israel":
        print("STOP ACCEPTANCE!")
        break
    print(x)
print("Loop is done...")

#continue

for x in countries:
    if x == "Israel":
        print("STOP ACCEPTANCE!")
        continue
    print(x)
print("Loop is done...")


#<<<<<Nesting Loops>>>>>

# Outer Loop
numbering = ["First","Second","Third"]
for outer in numbering:
    print(outer)
    #Inner Loop
    for inner in range(3):
        print(inner + 1)
print("Both Loops are done!")