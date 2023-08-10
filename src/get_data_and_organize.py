from scapy.all import *


def create_packet_length_and_count_graphs(packets):
    timestamps = []
    packet_lengths = []

    for packet in packets:
        packet_length = len(packet)
        time = packet.time
        timestamps.append(time)
        packet_lengths.append(packet_length)
    return timestamps, packet_lengths, packets


def read_pcap_file():
    # Read the PCAP file
    packets = rdpcap('../resources/all with filter from whatsapp.pcapng')
    return create_packet_length_and_count_graphs(packets)

