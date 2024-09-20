# Image-Steganograpgy-using-Python

Steganography (\Steg`a*nog"ra*phy\) is the study and practice of concealing messages within ordinary-looking containers, such as digital files, so that only the sender and intended recipient know a message exists. The hidden message is embedded in a medium, like an image, called a stego file, without altering its appearance significantly. Steganography, derived from Greek meaning "covered writing," differs from cryptography, which focuses on hiding the content rather than the existence of a message. While this technique protects information, it becomes vulnerable once the presence of hidden data is suspected, reducing their effectiveness.
Steganography, originating in ancient Greece, has evolved through various applications and remains relevant today. Its first recorded use dates back to 440 BC when Dermeratus warned Sparta of Xerxes' invasion by concealing a message on a wooden tablet, covered with wax, to pass unnoticed by enemy sentries. In World War II, Germans employed "null ciphering," a method of encoding messages in plain sight, such as hiding the message "Pershing sails for NY June 1" by extracting the second letter of each word from an otherwise innocent message. During the American Revolution, both British and American forces used invisible ink, which became visible when exposed to heat, to communicate secretly. In modern times, steganography is used in banknotes with special inks for hidden security messages, and in the entertainment industry through digital watermarking and fingerprinting of audio and video to protect copyrights.

Software Requirements
1.	At least 32 bit windows 7, windows 8 and windows 10 Operating system.
2.	Python Windows Installer Package.
3.	PIL or Pillow package.

Input Requirement

The steganography system requires PNG image file.
The algorithm used for encoding and decoding in this system requires using only the LSB layer of image

Selecting Cover Image to Encode

Click on “Upload Image” button. A dialog box will display as shown, specify which image file to be used as a carrier image and click on Open button to upload it into the system.

![Selecting_Image](https://github.com/user-attachments/assets/74df885c-e431-45fe-9656-590a6272390e)

Typing Information to be Encoded

Enter the information to be encoded in the box “Input Message” & the name of the intended Stego-Image with (.PNG) extension then click "Encode" Button 

![Encoding_Msg](https://github.com/user-attachments/assets/b879b406-e804-4a3b-8e60-332d0f7be7d5)

Decoding a Stego-Iage (Encrypted PNG Image File)

Click on the “Upload Image” button, a dialog box will be displayed select which encoded PNG image file to be decoded and click on open button to upload it into the system.
Then click on "Decode" Button to display the message.

![Decoding_Msg](https://github.com/user-attachments/assets/44a41805-22a3-4999-9656-9973b5c195ff)

Screenshot of both Sample & Stego-Image 


![Sample   Stego-image](https://github.com/user-attachments/assets/6eeec49f-c968-4842-aeee-5e98a14004b2)


