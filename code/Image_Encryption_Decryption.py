from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
import os
import psutil # type: ignore

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def save_key(key, file_path):
    with open(file_path, 'wb') as key_file:
        key_file.write(key)

def encrypt_image(file_path, public_key_path, encrypted_file_path):
    # Load the public key
    with open(public_key_path, 'rb') as key_file:
        public_key = RSA.import_key(key_file.read())
    cipher = PKCS1_OAEP.new(public_key)
    
    # Read the image
    with open(file_path, 'rb') as file:
        image_data = file.read()
    
    # Encrypt in chunks
    encrypted_data = b""
    chunk_size = 190  # PKCS1_OAEP padding limit for 2048-bit RSA
    for i in range(0, len(image_data), chunk_size):
        chunk = image_data[i:i+chunk_size]
        encrypted_data += cipher.encrypt(chunk)
    
    # Write the encrypted data to a file
    with open(encrypted_file_path, 'wb') as enc_file:
        enc_file.write(encrypted_data)

def decrypt_image(encrypted_file_path, private_key_path, output_file_path):
    # Load the private key
    with open(private_key_path, 'rb') as key_file:
        private_key = RSA.import_key(key_file.read())
    cipher = PKCS1_OAEP.new(private_key)
    
    # Read the encrypted data
    with open(encrypted_file_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()
    
    # Decrypt in chunks
    decrypted_data = b""
    chunk_size = 256  # RSA block size for 2048-bit key
    for i in range(0, len(encrypted_data), chunk_size):
        chunk = encrypted_data[i:i+chunk_size]
        decrypted_data += cipher.decrypt(chunk)
    
    # Write the decrypted image data to a file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(decrypted_data)

def measure_performance_metrics(input_image, encrypted_file, decrypted_image, private_key_path, public_key_path):
    metrics = {}

    # Measure encryption time
    start_time = time.time()
    encrypt_image(input_image, public_key_path, encrypted_file)
    metrics['encryption_time'] = time.time() - start_time

    # Measure decryption time
    start_time = time.time()
    decrypt_image(encrypted_file, private_key_path, decrypted_image)
    metrics['decryption_time'] = time.time() - start_time

    # Measure size overhead
    original_size = os.path.getsize(input_image)
    encrypted_size = os.path.getsize(encrypted_file)
    metrics['size_overhead'] = ((encrypted_size - original_size) / original_size) * 100

    # Measure throughput
    metrics['encryption_throughput'] = original_size / metrics['encryption_time']  # Bytes per second

    # Measure memory usage
    process = psutil.Process()
    metrics['memory_usage'] = process.memory_info().rss / (1024 * 1024)  # MB

    # Verify decryption accuracy
    with open(input_image, 'rb') as original, open(decrypted_image, 'rb') as decrypted:
        metrics['decryption_accuracy'] = original.read() == decrypted.read()

    # Additional metrics
    metrics['original_file_size'] = original_size / (1024 * 1024)  # MB
    metrics['encrypted_file_size'] = encrypted_size / (1024 * 1024)  # MB
    metrics['chunk_size'] = 190
    metrics['rsa_key_size'] = 2048

    return metrics

def main():
    # File paths
    input_image = "input_image.jpg"  # Replace with your input image path
    encrypted_file = "encrypted_image.enc"
    decrypted_image = "decrypted_image.jpg"
    private_key_path = "private.pem"
    public_key_path = "public.pem"
    
    # Generate RSA keys
    print("Generating RSA keys...")
    private_key, public_key = generate_keys()
    save_key(private_key, private_key_path)
    save_key(public_key, public_key_path)
    print("Keys saved.")

    # Measure and display performance metrics
    print("Measuring performance metrics...")
    metrics = measure_performance_metrics(input_image, encrypted_file, decrypted_image, private_key_path, public_key_path)
    
    print("Performance Metrics:")
    print(f"- Encryption Time: {metrics['encryption_time']:.2f} seconds")
    print(f"- Decryption Time: {metrics['decryption_time']:.2f} seconds")
    print(f"- Size Overhead: {metrics['size_overhead']:.2f}%")
    print(f"- Encryption Throughput: {metrics['encryption_throughput'] / (1024 * 1024):.2f} MB/s")
    print(f"- Memory Usage: {metrics['memory_usage']:.2f} MB")
    print(f"- Decryption Accuracy: {'Successful' if metrics['decryption_accuracy'] else 'Failed'}")
    print(f"- Original File Size: {metrics['original_file_size']:.2f} MB")
    print(f"- Encrypted File Size: {metrics['encrypted_file_size']:.2f} MB")
    print(f"- Chunk Size: {metrics['chunk_size']} bytes")
    print(f"- RSA Key Size: {metrics['rsa_key_size']} bits")

if __name__ == "__main__":
    main()