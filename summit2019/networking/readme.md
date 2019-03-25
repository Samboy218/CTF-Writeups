##JPG
relevant files:
* pcap.pcap
* image.jpg

This is a very simple one, open the pcap in wireshark and use the filter "frame contains jpg",
right click on the packet to follow the TCP stream, and then save the data. I had to remove the http
header from the file (just open it in vim and edit it), and then it is just a jpg image with the flag
