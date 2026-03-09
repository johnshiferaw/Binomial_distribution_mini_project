# Binomial Proportion Confidence Interval Tool (Python)

This project provides a simple Python function that calculates the ''confidence interval of a sample proportion'' and automatically interprets whether a hypothesized population proportion (p₀) is supported by the data.

It is a practical tool for anyone learning:
- Statistical inference  
- Confidence intervals  
- Hypothesis testing  
- Binomial proportion analysis  
- Z-critical values  
- Sampling distribution of proportions  

---

## 📘 What This Tool Does

Given:
- sample_proportion
- proportion_we_want_to_check (null hypothesis proportion)
- confidence_level (0.80, 0.90, 0.95, 0.98, 0.99)
- sample_size

The function:
1. Computes the confidence interval (CI)  
2. Checks whether the hypothesized proportion (p₀) lies inside the CI  
3. Prints a clear interpretation of the hypothesis result  

This gives both ''numerical'' and ''interpretive'' understanding.

---

## 📌 Example Use Case


binomial_test(
    sample_proportion=0.32,
    proportion_we_want_to_check=0.30,
    confidence_level=0.95,
    sample_size=200
)

Output:

The calculated CI

Whether p₀ lies inside the CI

Interpretation (reject or fail to reject hypothesis)


🧠 Statistical Concepts Used

-Standard error of a proportion

-Z-critical values

-Confidence interval formula

-Hypothesis testing logic:

If p₀ lies inside CI → not enough evidence to reject
If p₀ lies outside CI → enough evidence to reject