i = 1
flutter=0
javascript=0
python=0
while i<=5:
    sub = str(input("Enter subject :"))
    if sub == "flutter":
        flutter+=1
    elif sub == "javascript":
        javascript+=1
    elif sub == "python":
        python+=1

print(f" flutter = {flutter}")
print(f" javascript = {javascript}")
print(f" python = {python}")

    