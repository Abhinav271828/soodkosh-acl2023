#!/bin/bash

cd word_language_model

echo "Generating using LM."
python3 generate.py --data "../data" \
    --checkpoint "../models/reproduce_paper.pt" \
    --outf "../outputs/reproduce_paper_output.txt"

echo "Generation Complete."
cd ..
