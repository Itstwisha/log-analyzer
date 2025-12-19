# Log Analyzer & Alert Script

A Python-based tool that scans system authentication logs to detect suspicious security events.  
This project demonstrates basic SOC analysis skills such as failed login monitoring, brute force detection, and root access alerts.

---

## Features

- Detects repeated failed login attempts  
- Flags suspicious IP addresses from a blacklist  
- Detects root login attempts  
- Generates clean alerts for SOC-style monitoring

---

## Project Structure

```

log-analyzer/
│── src/
│     └── analyzer.py
│── logs/
│     └── auth.log
│── data/
│     └── suspicious_ips.txt
│── README.md

````

---

## How to Run

Clone the repo:

```bash
git clone https://github.com/Itstwisha/log-analyzer.git
cd log-analyzer
````

Run the analyzer:

```bash
python3 src/analyzer.py
```

---

## Sample Output

```
--- ALERTS GENERATED ---
[ALERT] Suspicious IP detected: 185.22.10.5
[ALERT] Suspicious IP detected: 104.168.23.44
[ALERT] Possible brute force from 104.168.23.44 (2 failures)
[ALERT] Root access detected in the log
```

---

## Future Enhancements

* Add timestamps + alert severity levels
* Export alerts to JSON / CSV
* Add log ingestion for Windows event logs
* Real-time monitoring with watchdog
* Add integration with a SIEM (Splunk/Wazuh)

---

## Author

**Twisha**
Cybersecurity Analyst | MS Cybersecurity
GitHub: [@Itstwisha](https://github.com/Itstwisha)

---

## License

MIT License



Just tell me: **Port Scanner or URL Detector?**
```
