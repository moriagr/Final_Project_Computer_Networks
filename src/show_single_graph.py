import matplotlib.pyplot as plt


#  This function present graph just like the graph in the article, fig. 8
def present_graph(timestamps, packet_lengths):
    plt.bar(timestamps, packet_lengths, width=0.1, align='edge', color='black')
    # plt.ylim(0, 1500)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Packet Length (MTU-sized chunks)')
    plt.title('Packet Length over Time (Bar Plot)')
    # Save the plot to the "res" directory
    plt.savefig("../res/example_plot.png")

    plt.show()

