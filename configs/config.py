#!/usr/bin/env python
# coding: utf-8

# In[ ]:


CONFIG = {
    "seed": 42,
    "num_classes": 5,
    "n_splits": 5,
    "batch_size": 32,
    "num_epochs": 20,
    "learning_rate": 1e-4,
    "num_workers": 2,

    "device": "cuda",

    "data": {
        "aptos": {
            "image_dir": "data/APTOS/train_images_preprocessed",
            "csv_file": "data/APTOS/train.csv",
        },
        "ddr": {
            "image_dir": "data/DDR/images",
            "csv_file": "data/DDR/labels.csv",
        },
        "idrid": {
            "image_dir": "data/IDRiD/images",
            "csv_file": "data/IDRiD/labels.csv",
        },
    },

    "outputs": {
        "checkpoints_dir": "outputs/checkpoints",
        "figures_dir": "outputs/figures",
        "logs_dir": "outputs/logs",
    },

    "ensemble": {
        "method": "topsis",   # choices: soft_voting, topsis, cost_sensitive_topsis
        "class_weights": [1.0, 1.2, 1.5, 2.0, 2.5],
        "cost_matrix": [
            [0, 1, 2, 4, 5],
            [1, 0, 1, 3, 4],
            [2, 1, 0, 2, 3],
            [4, 3, 2, 0, 2],
            [5, 4, 3, 2, 0],
        ]
    }
}

