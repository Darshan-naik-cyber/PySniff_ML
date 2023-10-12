import pyshark
from openpyxl import Workbook

# Create a list to store packet data
packet_info_list = []

# Start capturing packets on the specified network interface
capture = pyshark.LiveCapture(interface='Wi-Fi', bpf_filter='tcp')
capture.sniff(packet_count=1000)

# Iterate over the captured packets and process them
for pkt in capture:
    if 'IP' in pkt and 'TCP' in pkt:
        packet_info = {
            "Source IP": pkt.ip.src,
            "Destination IP": pkt.ip.dst,
            "Source Port": pkt.tcp.srcport,
            "Destination Port": pkt.tcp.dstport,
            # Add more fields as needed
        }
        packet_info_list.append(packet_info)

# Create an Excel workbook
workbook = Workbook()
sheet = workbook.active

# Write headers to the sheet
headers = ["Source IP", "Destination IP", "Source Port", "Destination Port"]  # Add more headers as needed
sheet.append(headers)

# Write packet data to the sheet
for packet_info in packet_info_list:
    sheet.append([packet_info[field] for field in headers])

# Save the workbook to a file
workbook.save("packet_data.xlsx")
