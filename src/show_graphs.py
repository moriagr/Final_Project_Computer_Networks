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
    saved_pic(saved_pic_name)
    # plt.show()


def present_all_single_bar_graph(all_packet_data, saved_pic_name):
    for key in all_packet_data.keys():
        present_single_bar_graph(all_packet_data[key]["timestamps"], all_packet_data[key]["packet_lengths"],
                                 key + "-"+saved_pic_name)


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

    plt.hist(inter_message_delays, bins='auto', density=True, alpha=0.6, label='Inter-Message Delays')
    plt.plot(bin_centers, pdf_fit, 'r-', label='Fitted Exponential Distribution')

    plt.xlabel('Inter-Message Delay')
    plt.ylabel('Probability Density')
    plt.ylim(0, 2)

    plt.title('PDF of Inter-Message Delays and Fitted Exponential Distribution')
    plt.legend()
    saved_pic(saved_pic_name)
    # plt.show()


def present_all_pdf_graph(all_packet_data, saved_pic_name):
    for key in all_packet_data.keys():
        present_pdf_graph(all_packet_data[key]["timestamps"], key + "_"+saved_pic_name)


def calculate_ccdf(packet_lengths):
    """Calculates the CCDF for a list of packet lengths."""
    return 1 - np.arange(1, len(packet_lengths) + 1) / len(packet_lengths)


#  This function present graph just like the graph in the article, fig. 4
def present_ccdf_graph(all_packet_data, saved_pic_name):
    plt.figure(figsize=(10, 6))

    # Plot CCDF for each im_type
    for im_type in all_packet_data.keys():
        x = all_packet_data[im_type]["packet_lengths"]
        y = calculate_ccdf(x)

        plt.loglog(x, y)  # Use log-log scale for CCDF

        plt.xlabel("Packet Length")
        plt.ylabel("CCDF")
        plt.legend([im_type])
    saved_pic(saved_pic_name)
    # plt.show()


#  This function present similar graph like the graph in the article, fig. 8
def present_packet_length_vs_time_graph(all_packet_data, saved_pic_name):
    plt.figure(figsize=(10, 6))

    for key, data in all_packet_data.items():
        plt.bar(data["timestamps"], data["packet_lengths"], label=key)

    plt.xlabel("Time (seconds)")
    plt.ylabel("Packet Length")
    plt.legend()
    plt.ylim(0, 2000)
    plt.title("Packet Length vs Time for Different Types of Messages")
    saved_pic(saved_pic_name)
    # plt.show()


def compare_between_platforms(all_packet_data, saved_pic_name, second_array=None):
    compare_packets = []
    titles = []
    if second_array:
        compare_packets.append(all_packet_data["without"])
        titles.append("Telegram")
        compare_packets.append(second_array["without"])
        titles.append("Whatsapp")
    else:
        compare_packets.append(all_packet_data["with"])
        titles.append("With filter")
        compare_packets.append(all_packet_data["without"])
        titles.append("Without filter")

    # Plot for all packets
    plt.subplot(2, 1, 1)
    plt.bar(compare_packets[0]["timestamps"], compare_packets[0]["packet_lengths"], width=0.1, align='edge',
            color='black')
    plt.xlabel('Timestamp (seconds)')
    plt.ylabel('Packet Count')
    plt.title(titles[0])

    # Plot for filtered packets
    plt.subplot(2, 1, 2)
    plt.bar(compare_packets[1]["timestamps"], compare_packets[1]["packet_lengths"], width=0.1, align='edge',
            color='black')
    plt.xlabel('Timestamp (seconds)')
    plt.ylabel('Packet Count')
    plt.title(titles[1])
    plt.suptitle(saved_pic_name, fontsize=16)

    plt.tight_layout()
    saved_pic(saved_pic_name)
    # plt.show()


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
    compare_between_platforms(telegram_array,
                              "compare between telegram and whatsapp platforms while catching packets with "
                              "filter", whatsapp_array)


# Save the plot to the "res" directory
def saved_pic(saved_pic_name):
    plt.savefig("../res/"+saved_pic_name+".png")
    # Save the plot using pickle
    with open("../res/"+saved_pic_name + '.pickle', 'wb') as f:
        pickle.dump(plt.gcf(), f)
