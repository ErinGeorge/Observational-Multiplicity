# Experiments for Observational Multiplicity paper.

This repository is code for the paper ["Observational Multiplicity" by Erin George, Deanna Needell, and Berk Ustun](https://arxiv.org/pdf/2507.23136).

This contains only code.  To recreate the plots from the paper, the datasets are also needed.  Three of these datasets are publicly available at the following locations:

* [Wisconsin Breast Cancer dataset](https://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original)
* [Bank Marketing dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing)
* [Fannie Mae Single Family Loan dataset](https://capitalmarkets.fanniemae.com/credit-risk-transfer/single-family-credit-risk-transfer/fannie-mae-single-family-loan-performance-data).  This includes code to generate summary statistics, which is necessary to generate the data used in our paper.

For the first two datasets, we use preprocessed versions of `breast-cancer-wisconsin.data` and `bank-additional-full.csv` in our experiments, respectively.  These can be obtained from the original datasets with the `process_bc.py` and `process_bank.py` files.

To obtain the other dataset in the paper, please look at the cited paper.
