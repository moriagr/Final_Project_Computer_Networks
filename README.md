# Final Project - Computer Networks
This project was created in reference to the article: "Practical Traffic Analysis Attacks on Secure Messaging Applications" by Alireza Bahramali, Amir Houmansadr, Ramin Soltani, Dennis Goeckel, and Don Towsley, University of Massachusetts Amherst

https://www.ndss-symposium.org/wp-content/uploads/2020/02/24347-paper.pdf 
## Install necessary packages
To run this project you will need to have on your computer the following platforms and installations:
* git
* python3
* scapy
* stats: to install - pip install statsmodels <br />
To install git, python3 and scapy - use the following link:
https://scapy.readthedocs.io/en/latest/installation.html

## Running the project
To run the project you will need the following:
* Install the git itself using the command:
`git install https://github.com/moriagr/Final_Project_Computer_Networks.git`
* Enter the command line
* In the command line go to the folder where you saved the project, and into the project itself (Final_Project_Computer_Networks)
* Enter to res folder with the command: `cd src`
* Run the project with this line: `python3 main.py`

## Project Results
In this project, we recorded communication between 4 different IM groups in WhatsApp. Each group sends a different type of message: text, image, audio, and video.
<br />In addition, we recorded a call in WhatsApp that includes all the message types, and we also recorded the same conversations in Telegram.
<br />At first, we will represent the graphs of all the different groups by the size of the packets:
<br />
### Shape of Traffic Graphs

<img width="317" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/d82adc99-3265-4924-a463-2e0d1d4ab1a1">
<br />
In the "text-Shape of traffic" graph, you can see, similar to what we saw in Table 2 in the article, that the size of a text message is small compared to the other types of messages as we will see later and the average size of a text message is about 250B.
<br />
<img width="319" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/0d537b2a-b1dc-46f5-b721-c9d363d406de">
<br />
In the "image-Shape of traffic" graph, you can see that some of the packets are larger than 1500B and some are smaller than 250B and in the range between 250B-1500B there are no packets at all.
<br />
In our estimation, images that are particularly small in size according to the given graph, are small because WhatsApp uses a method to prevent duplication, in which they send a reference or pointer to an image that has been sent several times in the same conversation.
<br />
<img width="321" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/bf3c71eb-b7ca-4d80-af2f-aa0e7c312144">
<br />
In the "audio-Shape of traffic" graph, you can see a wide range of sizes. This is according to the length of the recordings we sent (between 1 second and 3 minutes).
<br />
<img width="832" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/e126b223-b397-4c97-8991-73ae942c906a">
<br />
In the "video-Shape of traffic" graph you can see, similar to what we saw in Table 2 in the article, that the size of a video message is large compared to the other types of messages and the average size for a video message is about 1500B, a figure that is different from what we saw in Table 2 in the article. 
<br />In our opinion, this happens because of WhatsApp's optimization methods.

### PDF Graphs
<img width="384" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/937e591f-e8ca-40a3-a9bb-5473e2620c2f">
<br />

<img width="371" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/8984f690-70f5-45f1-aded-914a5bd00615">
<br />

<img width="368" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/a4430b0b-daef-4da2-8ebd-86860700cf88">
<br />

<img width="371" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/1fb4a837-19ec-4ed0-889f-0a3e779a84a3">
<br />


In these graphs, you can see the PDF as a function of the length of the delay between the messages as well as the exponential curve approximated according to the data. <br />
Since text messages are sent more frequently than other types of messages, the exponent corresponding to the approximation decays faster.<br />
In addition, since video messages are rarely sent compared to the rest, there are higher delay values, ​​and at more distant time points, therefore the value from which the approximate exponent starts is lower.

*The inter-message delay time is measured in seconds.

### CCDF Graph

<img width="468" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/f9b85224-d681-44e7-ae59-534738735cbe">

In this graph, we show the CCDF function.
<br />
This function shows the probability that a value will be greater than or equal to a certain value.

### Packets with VS without Filters Graph

<img width="805" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/79010006-7bb3-4821-9e91-69a4c96ba8b7">


<br />

<img width="777" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/e061d364-48e4-4b78-9c24-b5fd12b06895">

<br />

We used the filter (tcp || tls) and tcp.port == 443 to filter out background noise. According to these graphs, you can see that WhatsApp had more background noise than Telegram.
<br />

### Unique characteristics for each group:
1) **Size -** A characteristic we referred to earlier is the average size for a message in each group as well as the size ranges in each group.
2) **Latency -** Since video messages, for example, are sent less often compared to text messages that are sent very frequently, the delay times are longer.
<br />
We chose to make the recordings in Wireshark as follows: <br />
In each recording, we sent one type of message to the group. We did this for each message type (text, image, audio, video).
<br />
After that, we created another recording in which we sent all types of messages to the group.

<br />
<br />
In the case where the attacked user is always active (at most) in one IM group, the attacker can look for patterns in traffic that are unique to the group. For example, the time of day when the user is active, the frequency of sending messages, or the size of messages.
<br />
In the case where the attacked user is active in several IM groups simultaneously, the task becomes more complex for the attacker, because it is more difficult to find patterns. <br />
However, the attacker can try to cross reference between WhatsApp message and the packets that were captured by time and packet size to find patterns.
