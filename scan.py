import subprocess
import ipaddress
def findranges():
    asn = input("ASN: ")
    asnmap = ["asnmap", "-a", f"{asn}"]
    result = subprocess.run(asnmap, capture_output=True, text=True, check=True)
    out = result.stdout.strip().split('\n')
    return out

def findips(file):
    range = findranges()
    for _ in range:
        with open(f"{file}", "a") as f:
            try:
                n = ipaddress.ip_network(_)
                for ips in n:
                    f.write(f"{ips}\n")
            except ValueError as e:
                print("bad ip range?")
                break

def attack():
    findips("ips.txt")
    with open("ips.txt", "r") as f:
        for line in f:
            nuclei = ["nuclei", "-u", f"{line}", "-silent", "-j", "-or", "-ot", "-nm", "-es", "info","low"]
            result = subprocess.run(nuclei, capture_output=True, text=True, check=True)
            print(result.stdout)
            with open("result.txt", "a") as res:
                res.write(f"TARGET {line}\n{result.stdout}\n")
attack()
