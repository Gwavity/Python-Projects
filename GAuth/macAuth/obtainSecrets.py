import subprocess
import json

accounts = str(subprocess.check_output(["./extract_otp_secrets_2.4.4_macos_x86_64","example_export.txt"])).split(": ")
accountDict = {}

def endatSpecial(str):
    for i,v in enumerate(str):
        if v == "\\":
            return i

for k,v in enumerate(accounts):
    if "name" in accounts[k-1].lower():
        secret = accounts[k+1][0:endatSpecial(accounts[k+1])].strip()
        type = accounts[k+2][0:endatSpecial(accounts[k+2])].strip()
        name = v[0:v.find("\\n")].strip()
        accountDict[type] = {"name":name,"secret":secret}
print(accountDict)

with open("authSecrets.json","w") as secFile:
    secFile.write(json.dumps(accountDict,indent=2))
