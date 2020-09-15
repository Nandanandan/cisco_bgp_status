from netmiko import ConnectHandler
import getpass
from bgp_inventory import inventory
import time

class ssh:

    def __init__(self, device_type, hostname, ip, usern, passw):
          self.device_type = device_type
          self.hostname = hostname
          self.ip = ip
          self.user = usern
          self.passw = passw
    def ssh_device(self):

        net_connect = ""

        try:
            with open('BGP_neighborship_logs_output_file', "a+") as file:
                net_connect = ConnectHandler(device_type=self.device_type,ip=self.ip,username=self.user,password=self.passw)
                output = net_connect.send_command("sh ip bgp summary | begin Neighbor")
                file.write(f"\n\n----{self.hostname}-{self.ip}----\n\n")
                file.write(output)
                file.write("\n\nx------------------xxx------------xxx----------------x\n\n")
        except Exception as e:
               print(e)

if __name__ == "__main__":

    print("please provide credentials...")
    usern = input(r"user:")
    passw = getpass.getpass("Pass:")
    device_type = "cisco_ios"
    print("\n\n Script execution initiated...")
    start_time = time.time()
    for hostname, ip in inventory.items():
         obj = ssh(device_type, hostname, ip, usern, passw)
         obj.ssh_device()
         print(f"{hostname}/{ip} : DONE")

    total_time = time.time() - start_time
    print(f"script execution completed in {total_time:0.3f} seconds...")

