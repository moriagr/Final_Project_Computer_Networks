import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pickle


#  This function present graph just like the graph in the article, fig. 2
def present_single_bar_graph(timestamps, packet_lengths, saved_pic_name):
    plt.bar(timestamps, packet_lengths, width=0.1, align='edge', color='black')
    plt.xlabel('Time (Seconds)')
    plt.ylabel('Packet Length (Bytes)')
    plt.title(saved_pic_name)
    if saved_pic_name.find("video") == -1:
        plt.ylim(0, 2000)
    else:
        # Find common x-axis limits
        x_min = min(timestamps)
        x_max = max(timestamps)
        y_min = min(packet_lengths)
        y_max = max(packet_lengths)
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)

    saved_pic(saved_pic_name)
    plt.show()


def present_all_single_bar_graph(all_packet_data, saved_pic_name):
    for key in all_packet_data.keys():
        present_single_bar_graph(all_packet_data[key]["timestamps"], all_packet_data[key]["packet_lengths"],
                                 key + "-" + saved_pic_name)


#  This function present graph just like the graph in the article, fig. 3
def present_pdf_graph(timestamps, saved_pic_name):
    inter_message_delays = []
    timestamps = np.array(timestamps, dtype=float)  # Convert to a NumPy array with float data type

    for i in range(len(timestamps) - 1):
        inter_message_delays.append(timestamps[i + 1] - timestamps[i])
    inter_message_delays = np.array(inter_message_delays)
    # Create histogram
    hist, bin_edges = np.histogram(inter_message_delays, bins='auto', density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # Fit exponential distribution
    scale = stats.expon.fit(inter_message_delays)[1]
    pdf_fit = stats.expon.pdf(bin_centers, scale=scale)

    plt.figure(figsize=(8, 6))

    plt.hist(inter_message_delays, bins='auto', density=True, alpha=0.6, label='Histogram of Inter Message Delays')
    plt.plot(bin_centers, pdf_fit, 'r-', label='Fitted Exponential Distribution')

    plt.xlabel('Inter-Message Delay')
    plt.ylabel('Probability Density')
    plt.ylim(0, 2)

    plt.title(saved_pic_name)
    plt.legend()
    saved_pic(saved_pic_name)
    plt.show()


def present_all_pdf_graph(all_packet_data, saved_pic_name):
    for key in all_packet_data.keys():
        present_pdf_graph(all_packet_data[key]["timestamps"], key + " " + saved_pic_name)


def calculate_ccdf(packet_lengths):
    """Calculates the CCDF for a list of packet lengths."""
    data_sorted = np.sort(packet_lengths)
    ccdf = 1 - np.arange(1, len(data_sorted) + 1) / len(data_sorted)
    return data_sorted, ccdf


#  This function present graph just like the graph in the article, fig. 4
def present_ccdf_graph(all_packet_data, saved_pic_name):
    plt.figure(figsize=(10, 6))
    markers = ['o', '*', '^', 's']
    # Plot CCDF for each im_type
    for index, im_type in enumerate(all_packet_data.keys()):
        x = all_packet_data[im_type]["packet_lengths"]
        x_sorted, y = calculate_ccdf(x)

        plt.loglog(x_sorted, y, label=im_type, marker=markers[index])  # Use log-log scale for CCDF

    plt.xlabel('Normalized message sizes to their maximum')
    plt.ylabel('CCDF')
    plt.title('Complementary CDF (CCDF) of Packet Size Distributions')
    plt.legend(loc='upper right')

    saved_pic(saved_pic_name)
    plt.show()


def compare_between_platforms(all_packet_data, saved_pic_name):
    compare_packets = []
    titles = []

    compare_packets.append(all_packet_data["with"])
    titles.append("With filter")
    compare_packets.append(all_packet_data["without"])
    titles.append("Without filter")
    plt.subplot(2, 1, 1)
    plt.bar(compare_packets[0]["timestamps"], compare_packets[0]["packet_lengths"], width=0.1, align='edge',
            color='black')
    plt.xlabel('Timestamp (seconds)')
    plt.ylabel('Packet Count')
    plt.title(titles[0])

    plt.subplot(2, 1, 2)
    plt.bar(compare_packets[1]["timestamps"], compare_packets[1]["packet_lengths"], width=0.1, align='edge',
            color='black')
    plt.xlabel('Timestamp (seconds)')
    plt.ylabel('Packet Count')
    plt.title(titles[1])

    # Add a title for the entire plot
    plt.suptitle(saved_pic_name, fontsize=12)

    saved_pic(saved_pic_name)
    plt.show()


def compare_between_platforms_with_and_without_filter(all_packet_data):
    telegram_array = {}
    whatsapp_array = {}
    for key in all_packet_data.keys():
        if key.find("telegram") != -1:
            if key.find("without") != -1:
                telegram_array["without"] = all_packet_data[key]
            else:
                telegram_array["with"] = all_packet_data[key]

        else:
            if key.find("without") != -1:
                whatsapp_array["without"] = all_packet_data[key]
            else:
                whatsapp_array["with"] = all_packet_data[key]

    compare_between_platforms(whatsapp_array, "compare between whatsapp packets with and without filter")
    compare_between_platforms(telegram_array, "compare between telegram packets with and without filter")


# Save the plot to the "res" directory
def saved_pic(saved_pic_name):
    # Save the plot using pickle
    with open("../res/" + saved_pic_name + '.pickle', 'wb') as f:
        pickle.dump(plt.gcf(), f)
