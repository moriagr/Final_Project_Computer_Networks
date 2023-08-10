from get_data_and_organize import *
from show_single_graph import *

if __name__ == "__main__":
     timestamps, packet_lengths = read_pcap_file()
     present_graph(timestamps, packet_lengths)

