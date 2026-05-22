import json
from pathlib import Path

from src.ner.extractor import extract_entities
from src.classifier.baseline import classify_threat
from src.classifier.features import build_features

samples_dir = Path("data/samples")
output_dir = Path("data/processed")


for file_path in samples_dir.glob("*.txt"):

    with open(file_path, "r") as f:
        text = f.read()

    entities = extract_entities(text)
    features = build_features(entities)
    severity = classify_threat(features)

    output = {
        "input_file": file_path.name,
        "entities": entities,
        "features": features,
        "severity": severity
    }

    output_file = output_dir / f"{file_path.stem}.json"

    with open(output_file, "w") as f:
        json.dump(output, f, indent=4)

    print(f"Processed: {file_path.name}")