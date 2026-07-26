"""
AIG Shields Up: Cybersecurity Job Simulation (Forage)
Ransomware Incident Response — ZIP Brute-Force Decryption Tool

Role: Information Security Analyst, Cyber & Information Security Team

Context:
A server was compromised via the Log4Shell (CVE-2021-44228) vulnerability
before remediation was completed. The attacker attempted to deploy
ransomware; the Incident Detection & Response team stopped the attack
before it fully executed, but one ZIP archive (enc.zip) was encrypted
before containment. The CISO chose not to pay the ransom. This script
was written to recover the encrypted archive by testing candidate
passwords from a wordlist (rockyou.txt) against the encrypted ZIP file.

Usage:
    python ransomware_decryptor.py

Requires (in the same directory):
    enc.zip       - the ransomware-encrypted archive
    rockyou.txt   - newline-separated password candidates
"""

from zipfile import ZipFile


def attempt_extract(zf_handle, password):
    """
    Attempt to extract the contents of an open ZIP file using the
    supplied password.

    Args:
        zf_handle: an open ZipFile object (e.g. from `with ZipFile(...) as zf`)
        password (bytes): the password candidate to test

    Returns:
        bool: True if the password successfully decrypted and extracted
              the archive, False otherwise.
    """
    try:
        zf_handle.extractall(pwd=password)
        return True
    except RuntimeError:
        # Raised by zipfile when the password is incorrect
        return False
    except Exception:
        # Catch-all for any other unexpected extraction error
        return False


def main():
    print("[+] Beginning bruteforce")

    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:

            for line in f:
                password = line.strip()

                if attempt_extract(zf, password):
                    print("[+] Password found!")
                    print("[+] Password:", password.decode('utf-8'))
                    return
                else:
                    print("[-] Incorrect password:", password.decode('utf-8'))

    print("[+] Password not found in list")


if __name__ == "__main__":
    main()
