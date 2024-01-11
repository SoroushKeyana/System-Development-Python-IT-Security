from OpenSSL import crypto

def generate_self_signed_certificate():
    # Generate a private key
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # Generate a self-signed certificate
    cert = crypto.X509()
    cert.get_subject().C = "US"
    cert.get_subject().ST = "State"
    cert.get_subject().L = "City"
    cert.get_subject().O = "Organization"
    cert.get_subject().OU = "Organizational Unit"
    cert.get_subject().CN = "localhost"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365*24*60*60)  # Valid for one year
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')

    return key, cert

def save_to_files(key, cert, key_filename='localhost.key', cert_filename='localhost.crt'):
    # Save the certificate and private key to files
    with open(cert_filename, 'wb') as cert_file:
        cert_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

    with open(key_filename, 'wb') as key_file:
        key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

if __name__ == "__main__":
    key, cert = generate_self_signed_certificate()
    save_to_files(key, cert)
