import matplotlib.pyplot as plt


#  This function present graph just like the graph in the article, fig. 8
def present_graph(timestamps, packet_lengths):
    plt.bar(timestamps, packet_lengths, width=0.1, align='center', color='black')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Packet Length (MTU-sized chunks)')
    plt.title('Packet Length over Time (Scatter Plot)')
    plt.show()
