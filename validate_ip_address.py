import re
from ping3 import ping

while True:
    user_input = input("Do you want to enter an ip address? (Yes/No) :").lower()

    if user_input == 'no':
        file_read = open("ip_address.txt", "r")
        print(file_read.read())
        break

    if user_input == 'yes':
        # it should be contain four octes
        input_ip_address = input("Enter the ip address, each octet should be within 0-255 :")
        pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        ip_address = re.match(pattern, input_ip_address)


        if ip_address:
            octets = input_ip_address.split(".")
            ip = [i for i in octets if int(i) <= 255]
            if len(ip) == 4:
                valid_ip = ip_address.group()
                response_time = ping(valid_ip)

                with open("ip_address.txt", "a") as file_write:
                    if response_time is not None:
                        file_write.write(f"validate_ip: {valid_ip} (Response time: {response_time} ms)\n")
                    else:
                        file_write.write(f"invalidate_ip: {valid_ip} (Unreachable)\n")
        else:
            with open("ip_address.txt", "a") as file_write:
                file_write.write(f"invalid_ip_format: {input_ip_address}\n")
