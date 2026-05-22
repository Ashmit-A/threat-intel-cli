import json
from pathlib import Path
import pandas as pd

from src.ner.extractor import extract_entities
from src.classifier.baseline import classify_threat
from src.classifier.features import build_features
from src.classifier.model import ThreatClassifier
from src.utils.logger import logger
from src.ner.prepocess import clean_text

samples_dir = Path("data/samples")
output_dir = Path("data/processed")

classifier = ThreatClassifier()

all_outputs = []
for file_path in samples_dir.glob("*.txt"):
    try:

        with open(file_path, "r") as f:
            text = f.read()

        cleaned_text = clean_text(text)
        entities = extract_entities(cleaned_text)
        features = build_features(entities)
        severity = classifier.predict(cleaned_text)

        output = {
            "input_file": file_path.name,
            "text": cleaned_text,
            "entities": entities,
            "features": features,
            "severity": severity
        }

        all_outputs.append(output)

        logger.info(f"Processed {file_path.name}")

    except Exception as e:

        logger.error(f"Error processing {file_path.name}: {e}")

print(json.dumps(all_outputs, indent=2))    


rows = []

for item in all_outputs:
    row = {
        "input_file": item["input_file"],
        "text": item["text"],
        "num_cves": item["features"]["num_cves"],
        "num_malware": item["features"]["num_malware"],
        "num_ips": item["features"]["num_ips"],
        "num_domains": item["features"]["num_domains"],
        "severity": item["severity"]
    }
    rows.append(row)

df = pd.DataFrame(rows)
csv_output = output_dir / "training_data.csv"
df.to_csv(csv_output, index=False)
logger.info(f"Saved structured dataset to {csv_output}")