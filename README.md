## ENHANCING SECURITY IN BANKING APPLICATIONS THROUGH IMAGE ENCRYPTION AND DECRYPTION
The integration of image encryption and decryption within banking applications, aimed at securing sensitive visual data such as user IDs and signatures, preventing unauthorized access, and enhancing overall data protection.

## About
With the rapid digitalization of banking services, securing sensitive user data has become a critical concern. Traditional encryption techniques primarily focus on textual and numerical data, leaving visual information like user IDs, signatures, and scanned documents vulnerable to security threats. This project proposes an advanced image encryption and decryption system to enhance security in banking applications, ensuring the confidentiality and integrity of sensitive visual data.

## Features
* Advanced Image Encryption: Secure encryption algorithms like AES, RSA, or Chaos-based encryption to protect banking-related images.
* Secure Key Management: Implementation of a robust key generation and storage mechanism.
* Efficient Decryption Mechanism: Ensures quick and accurate decryption while maintaining security.
* Authentication and Access Control: Only authorized users can access encrypted images.
* Real-time Processing: Low-latency encryption and decryption for seamless banking transactions.

## Requirements
### Hardware:
  A system with a minimum of 8GB RAM and a multi-core processor.
  Secure storage for encryption keys.
### Software:
  Python/C++ with OpenCV, PyCryptodome, or cryptography libraries.
  Database for storing encrypted images (e.g., MySQL, PostgreSQL).
  Banking application frontend (React, Angular, or Flutter).
### Security Protocols:
  SSL/TLS for secure communication.
  
  Multi-factor authentication (MFA).

## System Architecture

![image](https://github.com/user-attachments/assets/ff863e3f-90b9-456b-83a8-2696fa773641)

### Encryption Phase:
1.	Source Image: The input image is taken and prepared for encryption.
2.	Diffusion Operation: The first operation in the encryption process involves XORing the bits of each pixel (vector) with the bits of its neighboring pixel. This spreads the influence of a single
pixel over others, making the image harder to decipher.
3.	Confusion Operation: The second operation involves circular rotating the bits of each vector (pixel) to the right. This adds complexity by altering the bit positions in a manner that doesn’t follow a straightforward pattern.
4.	Secret Key: A secret key (k bits) is used in both the encryption and decryption processes. This ensures that only those with the correct key can decrypt the image.
5.	Rounds: Both the diffusion and confusion operations are repeated over multiple rounds (n rounds and m rounds) to enhance security. The more rounds, the stronger the encryption.
6.	Encrypted Image: After completing the rounds, the image is encrypted and is not visually recognizable.
##### Formula: 
  ```
  C=Pemod nC = P^e \mod nC=Pemodn
  ```

### Decryption Phase:
1.	Encrypted Image: The encrypted image is fed into the decryption process.
2.	Confusion Operation: The first operation in the decryption phase involves circularly rotating the bits of each vector (pixel) to the left (opposite direction compared to encryption).
3.	Diffusion Operation: The second operation involves XORing the bits of each vector with the bits of its neighboring vector (similar to the encryption process but in reverse).
4.	Decrypted Image: After completing the rounds, the encrypted image is returned to its original state (source image) through the decryption process.
5.	Secret Key: The same secret key is used in the decryption phase to reverse the encryption operations.
##### Formula:
  ```
  P=Cdmod nP = C^d \mod nP=Cdmodn
  ```

### Key Concepts:
•	Diffusion: The method used to spread the influence of one pixel over others, making the image appear random.

•	Confusion: The method used to obscure the relationship between the plaintext (original image) and the ciphertext (encrypted image) by rearranging pixel bits.

•	Rounds: Multiple iterations of confusion and diffusion operations to enhance encryption strength.

•	Secret Key: A vital part of the encryption/decryption process, ensuring that the operations are performed consistently on both ends.


## Output

#### Output1 - Encrypted Image
![image](https://github.com/user-attachments/assets/a9fa09db-cf1d-4b6e-b711-4bd0d5c45826)


#### Output2 - Decrypted Image
![input_image](https://github.com/user-attachments/assets/b9a3470c-d04c-4c73-811d-131a4982035c)


## Results and Impact
![image](https://github.com/user-attachments/assets/b856110d-ac46-4986-b410-6bdb1399286b)
#### RSA Algorithm Encrypted histogram

![image](https://github.com/user-attachments/assets/d17ce1a9-b2ea-4cbe-8a42-13652a772f47)
#### RSA Algorithm decrypted histogram

* Enhanced Data Security: Reduces the risk of unauthorized access to banking images.
* Regulatory Compliance: Aligns with security regulations like GDPR, PCI-DSS.
* Fraud Prevention: Protects against image tampering and unauthorized modifications.
* Improved Customer Trust: Provides a secure banking experience.
* Seamless Integration: Can be implemented within existing banking applications with minimal disruptions.

## Articles published / References
[1]	Khan Majid and Noor Munir, "A novel image encryption technique based on generalized advanced encryption standard based on field of any characteristic", Wireless Personal Communications, pp. 1-19, 2024.

[2]	Sari, Christy Atika, Eko Hari Rachmawanto and Edi Jaya Kusuma, "Good Performance Images Encryption Using Selective Bit T-des On Inverted Lsb Steganography", Jurnal Ilmu Komputer dan Informasi, vol. 12.1, pp. 41-49, 2019.

[3]	L Goutham, M S Mahendra, A P Manasa and S N Prajwalasimha, "Modified Hill Cipher Based Image Encryption Technique", International Journal for Research in Applied Science & Engineering Technology, vol. 5, pp. 342-345, 2017.

[4]	Gong Lihua et al., "An optical image compression and encryption scheme based on compressive sensing and RSA algorithm", Optics and Lasers in Engineering, vol. 121, pp. 169- 180, 2019.

[5]	Singh, Laiphrakpam Dolendro and Khumanthem Manglem Singh, "Image encryption using elliptic curve cryptography", Procedia Computer Science, vol. 54, pp. 472-481, 2013.

[6]	Laiphrakpam, Dolendro Singh and Manglem Singh Khumanthem, "A robust image encryption scheme based on chaotic system and elliptic curve over finite field", Multimedia Tools and Applications, vol. 77.7, pp. 8629-8652, 2018.

[7]	N. S, S. S. Nath, U. K. M, S. M. S, Y. B. M and L. Krishnaa M, "Image Display using FPGA with BRAM and VGA Interface for Multimedia Applications," 2023 8th International Conference on Communication and Electronics Systems (ICCES), Coimbatore, India, 2023, pp. 77-83.

[8]	N. Mugabi, "Digitization of agricultural extension services- a case of mobile phone-based extension delivery in central uganda", vol. 4, pp. 1-89, 2019.

[9]	A. J. Amalraj and J. R. Jose, "A survey paper on cryptography techniques", International Journal of Computer Science and Mobile Computing, vol. 5, no. 8, pp. 55-59, 2022.

[10]	X. Zhang, L. Wang, Z. Zhou and Y. Niu, "A chaos-based image encryption technique utilizing hilbert curves and H-fractals", IEEE Access, vol. 7, pp. 74734-74746, 2019.

[11]	B. Jasra and A. H. Moon, "Image Encryption techniques:A Review," 2020 10th International Conference on Cloud Computing, Data Science & Engineering (Confluence), Noida, India, 2020, pp. 221-226.
 
[12]	M. Ruelas Quenaya, A. -A. Villa-Herrera, S. F. Chambi Ytusaca, J. E. Yauri Ituccayasi,
Y. Velazco-Paredes and R. Flores-Quispe, "Image Encryption using an Image Pattern based on Advanced Encryption Standard," 2021 IEEE Colombian Conference on Communications and Computing (COLCOM), Cali, Colombia, 2021, pp. 1-6.

[13]	R. Gupta and R. K. Agrawal, "A Comprehensive Survey on Image Security using Encryption Techniques," 2023 Third International Conference on Secure Cyber Computing and Communication (ICSCCC), Jalandhar, India, 2023, pp. 739-743.

[14]	J. T. G. Kankonkar and N. Naik, "Image security using image encryption and image stitching," 2017 International Conference on Computing Methodologies and Communication (ICCMC), Erode, India, 2017, pp. 151-154.

[15]	R. Ratheesh Kumar and J. Mathew, "Image Encryption:Traditional Methods vs Alternative Methods," 2020 Fourth International Conference on Computing Methodologies and Communication (ICCMC), Erode, India, 2020, pp. 1-7
