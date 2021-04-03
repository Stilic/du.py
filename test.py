from dudb import DUapi, RequestError

def chk(s):
    if s == 200:
        print("OK")

du = DUapi("")

print("Check for a real ID")
chk(du.checkStatus("466262009256869889"))

print("\nCheck for a fake id")
try:
    chk(du.checkStatus("007"))
except RequestError:
    print("Not OK")