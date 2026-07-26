# AIG Shields Up: Cybersecurity — Ransomware Decryption Brute-Force Tool

A Python-based incident response project completed as part of the **AIG Shields Up: Cybersecurity Job Simulation** on Forage, where I worked in the role of **Information Security Analyst, Cyber & Information Security Team**.

## 📌 Role

**Information Security Analyst** — Cyber & Information Security Team, AIG (simulated engagement via Forage)

## 📖 Project Overview

This project simulates a real-world ransomware incident response scenario. It demonstrates how to recover data from a ransomware-encrypted archive **without paying the ransom**, using a brute-force password-cracking approach against a known password wordlist.

## 🧩 Business Scenario

In an earlier stage of this simulation, I investigated and reported on the **Apache Log4j vulnerability (Log4Shell — CVE-2021-44228)**. Before remediation could be completed, an attacker exploited the vulnerability and gained access to an affected server.

The attacker attempted to deploy ransomware, but the **Incident Detection & Response team** intervened and stopped the installation before it could fully execute. The impact was contained to a single encrypted ZIP archive (`enc.zip`), left behind by the attacker — with no decryption key provided.

## 🎯 The CISO's Decision

The Chief Information Security Officer decided **not to pay the ransom**, for well-established reasons:

- Paying does not guarantee a working decryption key will be provided
- Attackers who are paid once are more likely to target the organization again
- Paying ransoms funds and incentivizes further ransomware operations industry-wide

## 🛠️ My Task

As the Information Security Analyst on the response, my objective was to **recover the encrypted file by brute-forcing the decryption password**, using a provided password wordlist rather than relying on the attacker.

### Provided Resources
- `enc.zip` — the ransomware-encrypted ZIP archive
- `rockyou.txt` — a small subset of the well-known RockYou password wordlist, containing common/leaked passwords
- A Python starter template, which I completed and documented

## ⚙️ How the Script Works

1. Opens the encrypted archive (`enc.zip`) using Python's built-in `zipfile` module
2. Opens the password wordlist (`rockyou.txt`) in binary read mode
3. Iterates through each candidate password in the wordlist
4. Attempts to extract the archive using each password via `extractall(pwd=password)`
5. Catches the `RuntimeError` that `zipfile` raises on an incorrect password, and continues to the next candidate
6. Stops and reports success as soon as the correct password is found — or reports that no match was found in the wordlist

See [`ransomware_decryptor.py`](./Task/ransomware_decryptor.py) for the fully commented implementation.

## ▶️ Try It Yourself

If you want to run this yourself:

1. Download `enc.zip` and `rockyou.txt` from this repository
2. Place them in the same directory as `ransomware_decryptor.py`
3. Run:
   ```bash
   python ransomware_decryptor.py
   ```
4. The script will print each password attempt and report the correct password once found

Feel free to use the script provided here, or write your own brute-force logic against the same `enc.zip` file — that's the point of the exercise. It's a good beginner-friendly way to practice Python file handling, exception handling, and basic password-cracking methodology in a safe, contained scenario.

## 🧠 Cybersecurity Concepts Demonstrated

| Concept | Application in This Project |
|---|---|
| **Ransomware** | Understanding how ransomware encrypts data and the incident response decision-making around ransom payment |
| **Brute-force attacks** | Systematically testing candidate passwords until the correct one is found |
| **Incident response** | Working through a realistic breach-to-recovery workflow, including the CISO decision-making context |
| **Password security** | Practical exposure to why weak/common passwords (as found in leaked lists like RockYou) are a major security risk |
| **Python scripting** | File handling, exception handling, binary I/O, and control flow |
| **ZIP archive handling** | Working with Python's `zipfile` module for password-protected archives |

## 🧰 Skills Demonstrated

`Python Scripting` · `File & Exception Handling` · `Password Cracking Methodology` · `Brute-Force Techniques` · `Ransomware Incident Response` · `Data Recovery` · `Security Documentation`

## 📁 Repository Contents

| File | Description |
|---|---|
| `ransomware_decryptor.py` | Fully commented brute-force decryption script |
| `enc.zip` | The ransomware-encrypted archive used in the simulation |
| `rockyou.txt` | Password wordlist subset used to brute-force the archive |
| `certificates/` | Certificate of completion and simulation task summary |

## 📝 Lessons Learned

- Ransomware recovery without payment is possible when weak/common passwords are involved — but this is not a substitute for strong password policy and prevention
- Brute-force recovery is only feasible because the wordlist used (a RockYou subset) contains common, previously leaked passwords — a real attacker using a strong, unique password would make this approach infeasible, which is itself a valuable lesson in password hygiene
- Incident response isn't only technical — the CISO's decision not to pay the ransom is a business and risk-management call as much as a security one
- Proper exception handling (catching `RuntimeError` specifically) is essential when iterating over many attempts, so a single failed guess doesn't crash the whole recovery process

## 🚀 Future Improvements

- Add multithreading/multiprocessing to speed up brute-force attempts against larger wordlists
- Add support for hash-based password cracking tools (e.g., John the Ripper, hashcat) for comparison against pure-Python brute force
- Extend the script to log all attempts with timestamps for a more complete incident response audit trail
- Add unit tests covering correct password, incorrect password, and corrupted-archive edge cases

## ⚠️ Disclaimer

This project was completed as part of a **simulated** cybersecurity job simulation (AIG Shields Up: Cybersecurity, via Forage). The `enc.zip` file and scenario are provided for **educational and training purposes only**, using a deliberately weak password from a well-known public wordlist. This script should not be used against any system, file, or account you do not own or have explicit authorization to test.

---

## 📜 Certification

This project was completed as part of the **AIG Shields Up: Cybersecurity Job Simulation** (via Forage), in the role of **Information Security Analyst, Cyber & Information Security Team**.
