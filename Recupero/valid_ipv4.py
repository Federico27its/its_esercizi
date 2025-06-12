def is_valid_ipv4(ip: str) -> bool:
    if ip.count(".") != 3:
        return False
    ip = ip.split(".")
    for n in ip:
        if not(n.isdigit()):
            return False
        if not(0 <= int(n) <= 255):
            return False
    return True

print(is_valid_ipv4("192.168.0.1")) # True
print(is_valid_ipv4("255.255.255.255")) # True
print(is_valid_ipv4("256.100.10.1")) # False (256 è fuori range)
print(is_valid_ipv4("192.168.1")) # False (solo 3 parti)
print(is_valid_ipv4("192.168.1.a")) # False (parte non numerica)
print(is_valid_ipv4("a.v.e.c"))