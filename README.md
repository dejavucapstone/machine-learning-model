# Gym Equipment Classification

This repository contains resources for a machine learning project focused on classifying gym equipment using TensorFlow. It includes datasets, pre-trained models, and Jupyter notebooks for building, training, fine-tuning, evaluating, and converting models into a format suitable for deployment on mobile devices.

## Project Overview

The aim of this project is to classify 8 different types of gym equipment. The model is built using transfer learning with MobileNetV2, followed by fine-tuning to optimize performance for the specific task. The trained model is then saved in both `.h5` (TensorFlow) and `.tflite` (TensorFlow Lite) formats to allow for deployment on different platforms.

## Repository Structure

``` bash
machine-learning-model
│
├── dataset/
│   ├── test/               # Test dataset
│   ├── train/              # Training dataset
│   ├── validation/         # Validation dataset
│   └── README.md           # Dataset documentation
│
├── model/
│   ├── gym_equip.classifier.tflite  # TensorFlow Lite model
│   ├── model_ft_finetuned.h5       # Fine-tuned TensorFlow model
│   └── model_metadata/
│       ├── gym_equip_classifier.json        # Model metadata in JSON format
│       └── gym_equip_classifier_metadata.tflite  # Metadata-enhanced TFLite model
│
├── notebooks/
│   ├── saved_model/         # Saved model directory
│   ├── evaluation.ipynb     # Model evaluation and testing (H5 and TFLite)
│   ├── exploratory.ipynb    # Exploratory Data Analysis (EDA) and visualization
│   └── modeling.ipynb       # Building, training, fine-tuning, saving, and converting TFLite model
│
├── scripts/
│   ├── README.md            # Scripts documentation
│   ├── labels.txt           # Labels for the classifier
│   └── metadata_writer_for_image_classifier.py  # Script to write metadata
│
├── README.md                # Project documentation
└── requirements.txt         # Required Python packages
```

## Project Scope

- **Classification Task**: The model is designed to classify 8 types of gym equipment.
- **Model Conversion**: The trained model is converted into TensorFlow Lite (TFLite) format for mobile deployment.
- **Transfer Learning**: The project uses MobileNetV2 for transfer learning and applies fine-tuning techniques to improve accuracy on the gym equipment dataset.

## Notebooks Overview

- **exploratory.ipynb**: Used for exploratory data analysis (EDA), data preprocessing, and visualization of the gym equipment dataset.
- **modeling.ipynb**: Contains the steps to build the model, train it using transfer learning (MobileNetV2), perform fine-tuning, and save the model. The model is then converted to TFLite format.
- **Metadata Integration**: Enhance the TFLite model with metadata for improved interpretability on edge devices.
- **evaluation.ipynb**: Used for evaluating and testing the model, both in its original `.h5` (TensorFlow) and `.tflite` (TensorFlow Lite) formats.
  
## Model Details

- **model_ft_finetuned.h5**: The final fine-tuned model saved in the TensorFlow `.h5` format.
- **gym_equip.classifier.tflite**: The converted model in TensorFlow Lite format for edge device deployment.
- **gym_equip_classifier_metadata.tflite**: The TFLite model enhanced with metadata for easier use in applications.
- **gym_equip_classifier.json**: Metadata file describing the model's inputs, outputs, and labels.

## Scripts Overview
- **labels.txt**: File containing the class labels for the gym equipment classifier.
- **metadata_writer_for_image_classifier.py**: Script to add metadata to the TFLite model.

Please refer to the scripts/README.md for more details on the scripts.

## Dataset
The dataset is organized into three main folders:

- **train/**: Contains images used for training the model.
- **test/**: Contains images used for testing the model.
- **validation/**: Contains images used for validating the model during training.

Please refer to the `dataset/README.md` for more details on the dataset.


## Installation

To get started, clone this repository and install the necessary dependencies:

### 1. Clone the repository

```bash
git clone https://github.com/dejavucapstone/machine-learning-model.git
``` 
```bash
cd machine-learning-model
```

## Requirements

To run the code and experiments in this repository, you'll need the following Python packages:

```bash
# Install required packages
pip install -r requirements.txt
```

