# Quantum-Secured Threat Intelligence NLP Pipeline

## Overview

The Quantum-Secured Threat Intelligence NLP Pipeline is a cybersecurity-focused Natural Language Processing (NLP) project that extracts structured threat intelligence from unstructured security reports.

The system processes incident reports, malware analyses, threat intelligence feeds, and security alerts to identify important cybersecurity entities such as malware families, CVEs, attack techniques, IP addresses, domains, and threat actors. Extracted information is converted into a structured JSON format that can be used for further analysis, visualization, or integration with other security tools.

---

## Features

* Automated threat intelligence extraction
* Malware identification
* CVE extraction
* MITRE ATT&CK technique detection
* IP address extraction
* Domain extraction
* Threat actor identification
* Confidence scoring for extracted entities
* Structured JSON output
* Modular project architecture
* Machine learning-based classification pipeline

---

## Project Structure

```text
project_root/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── samples/
│   └── fake_dataset.txt
│
├── docs/
│
├── models/
│   ├── classifier.pkl
│   ├── vectorizer.pkl
│   ├── train_embeddings.npy
│   └── train_labels.npy
│
├── notebooks/
│
├── src/
│   ├── classifier/
│   ├── data/
│   ├── eval/
│   ├── ner/
│   ├── pipeline/
│   ├── quantum/
│   └── utils/
│
├── tests/
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Pipeline Workflow

### 1. Data Collection

The project uses cybersecurity reports stored in the dataset. Reports may contain:

* Malware activity
* Exploited vulnerabilities
* Threat actor references
* Command-and-control domains
* Suspicious IP addresses
* Attack techniques

### 2. Preprocessing

The text is cleaned and prepared for analysis through:

* Tokenization
* Normalization
* Feature extraction
* Dataset preparation

### 3. Classification

Machine learning models process the reports and generate embeddings and classification outputs.

### 4. Entity Extraction

The NLP extraction module identifies relevant cybersecurity entities including:

* Malware
* CVEs
* Attack Techniques
* Domains
* IP Addresses
* Threat Actors

### 5. JSON Generation

The extracted information is formatted into a standardized JSON structure.

---

## Example Input

```text
Report ID: REP-1042

Analysts observed Emotet malware communicating with
185.73.221.14 through secure-update-check.net.

The intrusion exploited CVE-2025-1879 and was
attributed to APT29.

PowerShell execution techniques aligned with T1059
were identified during analysis.
```

---

## Example Output

```json
{
  "report_id": "REP-1042",
  "entities": {
    "malware": [
      {
        "name": "Emotet",
        "confidence": 0.97
      }
    ],
    "cves": [
      {
        "name": "CVE-2025-1879",
        "confidence": 0.95
      }
    ],
    "attack_techniques": [
      {
        "name": "T1059",
        "confidence": 0.93
      }
    ],
    "ips": [
      {
        "name": "185.73.221.14",
        "confidence": 0.99
      }
    ],
    "domains": [
      {
        "name": "secure-update-check.net",
        "confidence": 0.98
      }
    ],
    "threat_actor": [
      {
        "name": "APT29",
        "confidence": 0.94
      }
    ]
  },
  "metadata": {
    "source": "generated_dataset",
    "timestamp": "2026-05-20T12:44:00"
  }
}
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd threat-intel-pipeline
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Run the Complete Pipeline

```bash
python main.py
```

### Train the Classifier

```bash
python src/classifier/train.py
```

### Run Inference

```bash
python src/pipeline/Xinference.py
```

### Run Evaluation

```bash
python src/eval/metrics.py
```

---

## Machine Learning Components

### Feature Extraction

The project currently uses:

* TF-IDF Vectorization
* Text Embeddings
* Custom NLP Features

### Classification

The classifier is trained on cybersecurity report data to support downstream threat intelligence extraction.

### Evaluation Metrics

The evaluation module supports:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Dataset

The project uses a generated cybersecurity dataset containing realistic-looking incident reports that include:

* Malware campaigns
* Vulnerability exploitation
* Threat actor activity
* Network indicators
* Attack techniques

The dataset is intended for development, experimentation, and testing purposes.

---

## Testing

Run tests using:

```bash
pytest tests/
```

---

## License

This project is intended for educational and research purposes. Use responsibly and ensure compliance with applicable security and organizational policies.
