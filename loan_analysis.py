"""
Mathematics & Advanced Statistics - Practical Exam
Loan Default Risk: Statistical & Probability Analysis
Part B - Practical (Python Programming)
"""
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("loan_applications.csv")
R = {}   # results collected for the report
print("Dataset shape:", df.shape)
print(df.head(), "\n")

# ---------------- STEP 1: Central tendency & dispersion ----------------
print("=" * 60, "\nSTEP 1: Central Tendency & Dispersion\n" + "=" * 60)
inc_mean, inc_median = df["Income"].mean(), df["Income"].median()
inc_mode = df["Income"].mode()[0]
print(f"Income  Mean   = {inc_mean:,.2f}\nIncome  Median = {inc_median:,.2f}\nIncome  Mode   = {inc_mode:,.2f}")

la = df["Loan_Amount"]
la_range = la.max() - la.min()
la_var, la_std = la.var(ddof=1), la.std(ddof=1)
print(f"Loan_Amount Range    = {la_range:,.2f} (min {la.min():,.0f}, max {la.max():,.0f})")
print(f"Loan_Amount Variance = {la_var:,.2f}\nLoan_Amount Std Dev  = {la_std:,.2f}")
R["step1"] = dict(inc_mean=inc_mean, inc_median=inc_median, inc_mode=inc_mode,
                  la_min=la.min(), la_max=la.max(), la_range=la_range, la_var=la_var, la_std=la_std)

# ---------------- STEP 2: Probability & events ----------------
print("\n" + "=" * 60, "\nSTEP 2: Probability & Events\n" + "=" * 60)
df["Default_Flag"] = (df["Default_Status"] == "Yes").astype(int)
p_default = df["Default_Flag"].mean()
print(f"P(Default) = {df['Default_Flag'].sum()} / {len(df)} = {p_default:.4f}")

bins = [0, 550, 600, 650, 700, 750, 851]
labels = ["<550", "550-599", "600-649", "650-699", "700-749", "750+"]
df["Credit_Range"] = pd.cut(df["Credit_Score"], bins=bins, labels=labels, right=False)
ct = pd.crosstab(df["Credit_Range"], df["Default_Status"], margins=True)
print("\nContingency table (counts):\n", ct)
ct_pct = pd.crosstab(df["Credit_Range"], df["Default_Status"], normalize="index").round(4)
print("\nRow-wise default rate:\n", ct_pct)

low = df[df["Credit_Score"] < 600]
p_def_low = low["Default_Flag"].mean()
p_low = len(low) / len(df)
p_joint = ((df["Credit_Score"] < 600) & (df["Default_Flag"] == 1)).mean()
print(f"\nP(Credit<600)             = {p_low:.4f}")
print(f"P(Default AND Credit<600) = {p_joint:.4f}")
print(f"P(Default | Credit<600)   = {p_joint:.4f}/{p_low:.4f} = {p_def_low:.4f}")
high = df[df["Credit_Score"] >= 600]
p_def_high = high["Default_Flag"].mean()
print(f"P(Default | Credit>=600)  = {p_def_high:.4f}")
R["step2"] = dict(n=len(df), n_def=int(df["Default_Flag"].sum()), p_default=p_default,
                  p_low=p_low, p_joint=p_joint, p_def_low=p_def_low, p_def_high=p_def_high,
                  n_low=len(low), contingency=ct.reset_index().astype(str).values.tolist(),
                  default_rate=ct_pct["Yes"].tolist(), labels=labels)

# ---------------- STEP 3: Distributions & visualization ----------------
print("\n" + "=" * 60, "\nSTEP 3: Distributions & Visualization\n" + "=" * 60)
# (a) Histogram + Gaussian curve
cs = df["Credit_Score"]
mu, sigma = cs.mean(), cs.std(ddof=1)
plt.figure(figsize=(8, 5))
plt.hist(cs, bins=30, density=True, color="#4C78A8", edgecolor="white", alpha=0.85, label="Credit Score")
x = np.linspace(cs.min(), cs.max(), 300)
plt.plot(x, stats.norm.pdf(x, mu, sigma), "r-", lw=2.5, label=f"Gaussian (μ={mu:.1f}, σ={sigma:.1f})")
plt.axvline(600, color="k", ls="--", lw=1, label="Score = 600")
plt.title("Histogram of Credit Score with Gaussian Curve"); plt.xlabel("Credit Score"); plt.ylabel("Density")
plt.legend(); plt.tight_layout(); plt.savefig("fig1_credit_hist.png", dpi=150); plt.close()
print(f"Credit_Score mean = {mu:.2f}, std = {sigma:.2f}  -> fig1_credit_hist.png")

# (b) Skewness & kurtosis of Loan_Amount
skew = stats.skew(la)
kurt_excess = stats.kurtosis(la)         # Fisher (normal = 0)
print(f"Loan_Amount Skewness       = {skew:.4f}")
print(f"Loan_Amount Excess Kurtosis = {kurt_excess:.4f}  (Pearson kurtosis = {kurt_excess + 3:.4f})")
plt.figure(figsize=(8, 5))
plt.hist(la, bins=40, color="#F58518", edgecolor="white")
plt.title(f"Loan Amount Distribution (skew = {skew:.2f}, excess kurtosis = {kurt_excess:.2f})")
plt.xlabel("Loan Amount"); plt.ylabel("Frequency"); plt.tight_layout()
plt.savefig("fig2_loan_hist.png", dpi=150); plt.close()

# (c) Q-Q plot for Income
plt.figure(figsize=(6, 6))
stats.probplot(df["Income"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Income (vs Normal)"); plt.tight_layout()
plt.savefig("fig3_income_qq.png", dpi=150); plt.close()
# supporting evidence: Q-Q of log(Income)
plt.figure(figsize=(6, 6))
stats.probplot(np.log(df["Income"]), dist="norm", plot=plt)
plt.title("Q-Q Plot of log(Income)"); plt.tight_layout()
plt.savefig("fig4_logincome_qq.png", dpi=150); plt.close()
inc_skew = stats.skew(df["Income"])
r_raw = stats.probplot(df["Income"], dist="norm")[1][2]
r_log = stats.probplot(np.log(df["Income"]), dist="norm")[1][2]
print(f"Income skewness = {inc_skew:.4f}; Q-Q correlation raw = {r_raw:.4f}, log = {r_log:.4f}")
R["step3"] = dict(cs_mean=mu, cs_std=sigma, skew=skew, kurt=kurt_excess, inc_skew=inc_skew,
                  r_raw=r_raw, r_log=r_log)

# ---------------- STEP 4: Linear algebra ----------------
print("\n" + "=" * 60, "\nSTEP 4: Linear Algebra Application\n" + "=" * 60)
V = df[["Income", "Loan_Amount"]].head(5).to_numpy(dtype=float)
print("First 5 customers [Income, Loan_Amount]:\n", V)
a, b = V[0], V[1]
dot = np.dot(a, b)
norm_a, norm_b = np.linalg.norm(a, 2), np.linalg.norm(b, 2)
cos_t = dot / (norm_a * norm_b)
angle = np.degrees(np.arccos(cos_t))
print(f"\nCustomer 1 vector = {a},  Customer 2 vector = {b}")
print(f"Dot product (C1.C2)    = {dot:,.2f}")
print(f"Norm-2 of Customer 1   = {norm_a:,.4f}")
print(f"Norm-2 of Customer 2   = {norm_b:,.4f}")
print(f"cos(theta)             = {cos_t:.6f}\nAngle between C1 & C2  = {angle:.4f} degrees")
R["step4"] = dict(V=V.tolist(), dot=dot, norm_a=norm_a, norm_b=norm_b, cos=cos_t, angle=angle)

# ---------------- BONUS: eigen-analysis (links to Theory Q8) ----------------
print("\n" + "=" * 60, "\nBONUS: Eigenvalues/Eigenvectors of standardized covariance\n" + "=" * 60)
X = df[["Age", "Income", "Loan_Amount", "Credit_Score"]]
Z = (X - X.mean()) / X.std(ddof=1)
C = np.cov(Z.T)
vals, vecs = np.linalg.eigh(C)
order = np.argsort(vals)[::-1]; vals, vecs = vals[order], vecs[:, order]
ev_ratio = vals / vals.sum()
print("Eigenvalues:", np.round(vals, 4)); print("Explained variance ratio:", np.round(ev_ratio, 4))
print("PC1 loadings:", dict(zip(X.columns, np.round(vecs[:, 0], 4))))
R["bonus"] = dict(vals=vals.tolist(), ratio=ev_ratio.tolist(), cols=list(X.columns), pc1=vecs[:, 0].tolist())

json.dump(R, open("results.json", "w"), indent=2, default=float)
print("\nAll calculations complete.")
