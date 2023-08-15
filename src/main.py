from get_data_and_organize import *
from show_graphs import *

if __name__ == "__main__":
    all_packet_data = get_all_pcap_file()
    present_all_single_bar_graph(all_packet_data, "Shape of traffic")
    present_all_pdf_graph(all_packet_data, "pdf graph")
    present_ccdf_graph(all_packet_data, "CCDF graph")
    present_packet_length_vs_time_graph(all_packet_data, "packet length vs time")
    compare_packet_data = get_telegram_vs_whatsapp_pcap_file()
    compare_between_platforms_with_and_without_filter(compare_packet_data)
