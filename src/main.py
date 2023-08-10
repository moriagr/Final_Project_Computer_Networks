

from get_data_and_organize import *
from show_graphs import *

if __name__ == "__main__":
     timestamps, packet_lengths, packets = read_pcap_file()
     present_single_bar_graph(timestamps, packet_lengths)

     # im_sizes = {}
     # for i in range(len(packet_lengths)):
     #      im_type = packets[i].getlayer('IP').dst
     #      if im_type not in im_sizes:
     #           im_sizes[im_type] = []
     #      im_sizes[im_type].append(packet_lengths[i])
     #
     # ccdf = {}
     # for im_type in im_sizes:
     #      x = np.sort(im_sizes[im_type])
     #      y = np.arange(len(x)) / len(x)
     #      ccdf[im_type] = y
     #
     # for im_type in im_sizes:
     #      plt.plot(x, ccdf[im_type], label=im_type)
     # plt.legend()
     # plt.show()



