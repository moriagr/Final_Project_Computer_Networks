import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


#  This function present graph just like the graph in the article, fig. 8
def present_single_bar_graph(timestamps, packet_lengths, saved_pic_name):
    plt.bar(timestamps, packet_lengths, width=0.1, align='edge', color='black')
    # plt.ylim(0, 1500)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Packet Length (MTU-sized chunks)')
    plt.title('Packet Length over Time (Bar Plot)')
    # Save the plot to the "res" directory
    saved_pic(saved_pic_name)
    plt.show()


#  This function present graph just like the graph in the article, fig. 3
#  Need to fix the code - need to see first the zoom and then see exactly what he want us to do
def present_pdf_graph(timestamps, saved_pic_name):
    inter_message_delays = []
    timestamps = np.array(timestamps, dtype=float)  # Convert to a NumPy array with float data type

    for i in range(len(timestamps) - 1):
        inter_message_delays.append(timestamps[i + 1] - timestamps[i])
    inter_message_delays = np.array(inter_message_delays)
    pdf = np.histogram(inter_message_delays, bins=100, density=True)
    mu, sigma = stats.expon.fit(inter_message_delays)

    plt.plot(pdf[1][:-1], pdf[0], label='PDF')
    plt.plot(np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100),
             stats.expon.pdf(np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100), loc=mu, scale=sigma),
             label='Fitted Exponential Distribution')
    plt.legend()
    saved_pic(saved_pic_name)
    plt.show()


#  This function present graph just like the graph in the article, fig. 4
def present_ccdf_graph(all_packet_data, saved_pic_name):
    plt.figure(figsize=(10, 6))

    # Plot CCDF for each im_type
    for im_type in all_packet_data.keys():
        x = np.sort(all_packet_data[im_type]["packet_lengths"])
        y = 1 - np.arange(1, len(x) + 1) / len(x)  # Calculate CCDF values

        plt.loglog(x, y)  # Use log-log scale for CCDF

        plt.xlabel("Packet Length")
        plt.ylabel("CCDF")
        plt.legend([im_type])
    saved_pic(saved_pic_name)
    plt.show()


def saved_pic(saved_pic_name):
    plt.savefig("../res/"+saved_pic_name)
