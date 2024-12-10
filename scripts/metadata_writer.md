# Metadata Writer for Image Classifier

This script, `metadata_writer_for_image_classifier.py`, adds metadata and associated label files to TensorFlow Lite (TFLite) image classifier models. The metadata enables developers to better understand and utilize the model by providing details such as input requirements, output formats, and associated labels.

---

## Features

1. **Metadata Generation**:

    - Provides input and output tensor details, including dimensions, normalization information, and label files.
    - Includes model-specific metadata such as name, version, author, and description.

2. **Label File Integration**:

    - Embeds label files directly into the TFLite model, enabling seamless integration with client applications.

3. **Metadata Validation**:
    - Generates a JSON file containing the model metadata for easy inspection.

## Prerequisites

-   `Python 3.x`
-   `TensorFlow` and `TensorFlow Lite Support` Library
-   Install dependencies:
    ```bash
    pip install tensorflow tflite-support absl-py flatbuffers
    ```

## Usage

-   Run the script using the following command:

    ```console
    python ./metadata_writer_for_image_classifier.py \
        --model_file=./model/gym_equip_classifier.tflite \
        --label_file=./labels.txt \
        --export_directory=./model/model_metadata
    ```

Parameters:

-   `--model_file`: Path to the TFLite model file you want to add metadata to.
-   `--label_file`: Path to the label file corresponding to the model categories.
-   `--export_directory`: Path where the output TFLite model (with metadata) and JSON file will be saved.

## Output

-   `Updated TFLite Model`: The model file with metadata embedded.
-   `JSON Metadata File`: A human-readable JSON file describing the metadata.

---
