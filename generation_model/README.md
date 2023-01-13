# Pseudoword Generation Model

## Reproduce Results

In order to reproduce the model and outputs reported in our paper, follow the instructions given below:

1. Shift to code directory: `cd ./generation_model`
2. Train LM: `bash train.sh`; Trained model will be saved to `models/reproduce_paper.pt`
3. Generate outputs on trained LM: `bash generate.sh`; Generated outputs will be saved to `outputs/reproduce_paper_output.txt`

To train and generate on custom LMs, edit the paramentrs accordingly in `train.sh` and `generate.sh`. 
Refer to `word_language_model/main.py` and `word_language_model/generate.py` for a more detailed parameter set description.
