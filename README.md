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
<img width="317" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/bb649195-0293-4496-ab90-a1f569cd8dd1">

<br />
In the "text-Shape of traffic" graph, you can see, similar to what we saw in Table 2 in the article, that the size of a text message is small compared to the other types of messages as we will see later and the average size of a text message is about 250B.
<br />
<img width="319" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/5407bf0d-9df4-430a-9200-1aa0ceaebf57">

<br />
In the "image-Shape of traffic" graph, you can see that some of the packets are larger than 1500B and some are smaller than 250B and in the range between 250B-1500B there are no packets at all.
<br />
In our estimation, images that are particularly small in size according to the given graph, are small because WhatsApp uses a method to prevent duplication, in which they send a reference or pointer to an image that has been sent several times in the same conversation.
<br />
<img width="321" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/33405c28-1208-4b74-b691-6a7ee4ee0a3e">
<br />
In the "audio-Shape of traffic" graph, you can see a wide range of sizes. This is according to the length of the recordings we sent (between 1 second and 3 minutes).
<br />
<img width="832" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/9aeefb3e-f0d2-4929-9588-902c717a05f3">
<br />
In the "video-Shape of traffic" graph you can see, similar to what we saw in Table 2 in the article, that the size of a video message is large compared to the other types of messages and the average size for a video message is about 1500B, a figure that is different from what we saw in Table 2 in the article. 
<br />In our opinion, this happens because of WhatsApp's optimization methods.

### PDF Graphs
<img width="371" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/07a209e5-6b83-461f-aa70-d436e4d57979">
<br />
<img width="371" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/c7761160-4d35-42ed-b0ea-54d02d252a33">
<br />
<img width="384" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/aa29a60b-099f-4c08-b7ff-ebfefdbde97d">
<br />
<img width="368" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/08fb6513-19f4-4393-ab79-1f47aa80e0cc">
<br />
<br />


In these graphs, you can see the PDF as a function of the length of the delay between the messages as well as the exponential curve approximated according to the data. <br />
Since text messages are sent more frequently than other types of messages, the exponent corresponding to the approximation decays faster.<br />
In addition, since video messages are rarely sent compared to the rest, there are higher delay values, ​​and at more distant time points, therefore the value from which the approximate exponent starts is lower.

*The inter-message delay time is measured in seconds.

### CCDF Graph
<img width="468" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/73fcd942-c169-4add-afa1-ca158e24baa2">


In this graph, we show the CCDF function.
<br />
This function shows the probability that a value will be greater than or equal to a certain value.

### Packets with VS without Filters Graph
<img width="805" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/c5c74d6e-042d-4022-81ad-845a8e259fbf">

<br />

<img width="777" alt="image" src="https://github.com/moriagr/Final_Project_Computer_Networks/assets/99357654/a16e94d1-6002-4fee-8c12-6d6e2c3a9102">

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
<br />
<br />

*The changes in the last commit (uploading pictures again) are due to a known problem after changing from private to public. For more information: https://github.com/orgs/community/discussions/56049  
