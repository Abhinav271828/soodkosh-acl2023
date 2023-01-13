#!/bin/bash

cd word_language_model

echo "Training LM."
python3 main.py --data "../data" \
    --model LSTM \
    --emsize 34 \
    --nhid 200 \
    --lr 20 \
    --epochs 4 \
    --bptt 10 \
    --dropout 0.2 \
    --save "../models/reproduce_paper.pt"
echo "Training Complete."
cd ..
