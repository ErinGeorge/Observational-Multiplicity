# Experiments for Observational Multiplicity paper.

This repository is code for the paper ["Observational Multiplicity" by Erin George, Deanna Needell, and Berk Ustun](https://arxiv.org/pdf/2507.23136).

This contains only code.  To recreate the plots from the paper, the datasets are also needed.  Three of these datasets are publicly available at the following locations:

* [Wisconsin Breast Cancer dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)
* [Bank Marketing dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing)
* [Fannie Mae Single Family Loan dataset](https://capitalmarkets.fanniemae.com/credit-risk-transfer/single-family-credit-risk-transfer/fannie-mae-single-family-loan-performance-data).  This includes code to generate summary statistics, which is necessary to generate the data used in our paper.

For the Bank Marketing dataset, we use a preprocessed version of `bank-additional-full.csv` in our experiments.  This can be obtained from the original dataset with the `process_bank.py` file.

To obtain the other dataset in the paper, please look at the cited paper.
