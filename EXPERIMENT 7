Experiment 7: Wireshark Analysis of a WPA2 EAPOL Handshake
Objective
To identify and examine the four EAPOL-Key frames involved in a WPA2 four-way handshake using an existing Wireshark capture.

Software / Capture
Wireshark
Capture file: Network_Join_Nokia_Mobile.pcap
Working Principle
The WPA2 four-way handshake exchanges authentication and key-establishment information between an access point and a client. ANonce, SNonce, MIC and replay counters are used during the exchange.

Procedure
Open the supplied PCAP file in Wireshark.
Filter the packets with:
eapol
Locate the complete four-message EAPOL-Key sequence.
For analysis, use frames 726, 728, 733 and 738.
Open the 802.1X Authentication section of each selected packet.
Inspect the Key Information, Replay Counter, Nonce and MIC fields.
Note the sender and receiver for every message.
Record the observed parameters in the results table.
Handshake Sequence
             WPA2 KEY ESTABLISHMENT

       Siemens / AP                 Nokia / Client
             |                             |
             |       M1: ANonce            |
             |---------------------------->|
             |                             |
             |       M2: SNonce + MIC      |
             |<----------------------------|
             |                             |
             |       M3: ANonce + MIC      |
             |---------------------------->|
             |                             |
             |       M4: MIC               |
             |<----------------------------|
             |                             |
             |          COMPLETE            |
Packet Observations
Frame	EAPOL Message	Direction	Key Information	Replay Counter	Nonce / MIC
726	Message 1 of 4	Siemens → Nokia	0x0089	0	ANonce, MIC zero
728	Message 2 of 4	Nokia → Siemens	0x0109	0	SNonce, MIC present
733	Message 3 of 4	Siemens → Nokia	0x01c9	1	ANonce, MIC present
738	Message 4 of 4	Nokia → Siemens	0x0109	1	Nonce zeroed, MIC present
Additional Capture Detail
Frame 728 contained a WPA Information Element showing:

Multicast cipher: TKIP
Unicast cipher: TKIP
Authentication / Key Management: PSK
Analysis
The capture contains a complete four-message EAPOL-Key exchange. The access point begins the exchange with an ANonce, the client responds with an SNonce and MIC, and the final two messages confirm the key exchange.

Conclusion
The WPA2 four-way handshake was successfully located and analyzed from the supplied PCAP file. The relevant EAPOL-Key frames and their security parameters were documented using Wireshark.

Evidence Screenshots
eapol filtered packet list
Frame 726: Message 1
Frame 728: Message 2
Frame 733: Message 3
Frame 738: Message 4
