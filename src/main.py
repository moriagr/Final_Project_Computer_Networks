
from get_data_and_organize import *
from show_graphs import *
import scipy.stats


if __name__ == "__main__":
     all_packet_data = get_all_pcap_file()
     present_ccdf_graph(all_packet_data, "ccdf_graph.png")


