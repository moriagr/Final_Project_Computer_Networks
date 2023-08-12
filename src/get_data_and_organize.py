from scapy.all import *


def create_packet_length_and_count_graphs(packets):
    timestamps = []
    packet_lengths = []

    for packet in packets:
        packet_length = len(packet)
        time = packet.time
        timestamps.append(time)
        packet_lengths.append(packet_length)
    return {"timestamps": timestamps, "packet_lengths": packet_lengths, "packets": packets}


def read_pcap_file(file_name):
    # Read the PCAP file
    packets = rdpcap('../resources/'+file_name)
    return create_packet_length_and_count_graphs(packets)


def get_all_pcap_file():
    return {"audio": read_pcap_file("audio with filter.pcapng"),
            "image": read_pcap_file("image with filter.pcapng"),
            "video": read_pcap_file("video with filter.pcapng"),
            "text": read_pcap_file("text with filter.pcapng")}
