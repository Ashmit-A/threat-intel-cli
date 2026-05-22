import json
from pathlib import Path

from src.ner.extractor import extract_entities
from src.classifier.baseline import classify_threat
from src.classifier.features import build_features
from src.classifier.model import ThreatClassifier

samples_dir = Path("data/samples")
output_dir = Path("data/processed")

classifier = ThreatClassifier()

all_outputs = []
for file_path in samples_dir.glob("*.txt"):

    with open(file_path, "r") as f:
        text = f.read()

    entities = extract_entities(text)
    features = build_features(entities)
    severity = classifier.predict(features)

    output = {
        "input_file": file_path.name,
        "entities": entities,
        "features": features,
        "severity": severity
    }

    all_outputs.append(output)
aggregate_output = output_dir / f"all_reports.json"

with open(aggregate_output, "w") as f:
    json.dump(all_outputs, f, indent=4)

print("craeted aggregate dataset as output")