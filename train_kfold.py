#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from configs.config import CONFIG
from src.dr_ensemble.utils.seed import set_seed
from src.dr_ensemble.data.datasets import DiabeticRetinopathyAptosDataset
from src.dr_ensemble.data.transforms import get_train_transform
from src.dr_ensemble.training.kfold import run_kfold_training

def main():
    set_seed(CONFIG["seed"])

    dataset = DiabeticRetinopathyAptosDataset(
        csv_file=CONFIG["data"]["aptos"]["csv_file"],
        image_dir=CONFIG["data"]["aptos"]["image_dir"],
        image_col="id_code",     # change if your csv column is different
        label_col="diagnosis",   # change if your csv column is different
        transform=get_train_transform(),
        image_ext=".png"
    )

    fold_metrics = run_kfold_training(dataset, CONFIG)

    print("\nFinal fold metrics:")
    for i, metrics in enumerate(fold_metrics, start=1):
        print(f"Fold {i}: {metrics}")

if __name__ == "__main__":
    main()

