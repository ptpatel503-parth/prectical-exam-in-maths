# Student Scores Analysis

### Mathematics & Advanced Statistics



------------------------------------------------------------------------

## Table of Contents

-   [Project Overview](#project-overview)
-   [Dataset](#dataset)
-   [Analysis Performed](#analysis-performed)
-   [Key Results](#key-results)
-   [Project Screenshots](#project-screenshots)
-   [Technologies Used](#technologies-used)
-   [Installation and Usage](#installation-and-usage)
-   [Repository Structure](#repository-structure)
-   [Notes and Limitations](#notes-and-limitations)

## Project Overview

This practical project applies **Mathematics and Advanced Statistics**
to a student-score dataset. The notebook uses Python to inspect the
data, calculate descriptive statistics and probabilities, visualize
score distributions, and perform basic linear-algebra operations.

## Dataset

The Excel workbook contains **5,000 rows and 7 columns** in the
`Student Scores` worksheet.

  Column            Description
  ----------------- --------------------------------------
  `Student ID`      Student identifier
  `Age`             Student age
  `Math Score`      Mathematics score
  `Science Score`   Science score
  `English Score`   English score
  `Hours Studied`   Hours studied
  `Pass Fail`       Pass/fail outcome (`Pass` or `Fail`)

## Analysis Performed

1.  **Dataset inspection** --- review dataset dimensions, column names,
    and sample records.
2.  **Central tendency and dispersion** --- calculate the Math Score
    mean, median, and mode, along with the Science Score range,
    variance, and standard deviation.
3.  **Probability** --- calculate overall pass probability, a pass/fail
    contingency table, and conditional pass probability for students
    with more than five study hours.
4.  **Distribution analysis** --- calculate Science Score skewness and
    kurtosis.
5.  **Visualizations** --- create a Math Score histogram with a fitted
    normal curve and an English Score Q-Q plot.
6.  **Linear algebra** --- calculate the dot product, vector norms, and
    angle between the first five Math and Science scores.

## Key Results

The following values are reported by the project notebook.

  Metric                                            Result
  ------------------------------------------- ------------
  Students in dataset                                5,000
  Overall probability of passing                **60.64%**
  Math Score mean                                    70.02
  Math Score median                                  70.30
  Math Score mode                                    100.0
  Science Score range                                84.80
  Science Score variance                            191.93
  Science Score standard deviation                   13.85
  Science Score skewness                           -0.1020
  Science Score kurtosis                           -0.3235
  Pass probability when `Hours Studied > 5`     **99.73%**
  Dot product of first-five-score vectors         24890.46
  Angle between first-five-score vectors            11.08°

## Project Screenshots

### Math Score Distribution

The histogram shows the distribution of Math Scores, with a fitted
normal curve for comparison.

![Histogram and normal curve for Math Score](math_score_dist.png)

### English Score Q-Q Plot

The Q-Q plot compares the ordered English Scores with theoretical normal
quantiles. The upper end visibly flattens near 100, indicating a ceiling
effect in the scores.

![Q-Q plot for English Score](english_score_qq.png)

> **Screenshot setup:** Keep `math_score_dist.png` and
> `english_score_qq.png` in the repository root, alongside this README,
> for the images to render on GitHub.

## Technologies Used

-   **Python** --- analysis language
-   **pandas** --- tabular data handling
-   **NumPy** --- numerical and vector calculations
-   **SciPy** --- statistical calculations
-   **Matplotlib** and **Seaborn** --- visualizations
-   **openpyxl** --- Excel workbook support
-   **Jupyter Notebook** --- interactive workflow

## Installation and Usage

### 1. Get the project files

Clone your repository or download the project files. Keep the notebook,
dataset, plot images, and README in the same project directory.

### 2. Install dependencies

``` bash
pip install pandas numpy scipy matplotlib seaborn openpyxl jupyter
```

### 3. Check the dataset filename

The notebook should point to your actual Excel filename. If the code
expects `students_scores.xlsx`, either rename the workbook to that name
or update the notebook's `read_excel` / `file_path` reference. The
worksheet name is `Student Scores`.

### 4. Start Jupyter Notebook

``` bash
jupyter notebook
```

Open `Practical Exam Mathematics & Advanced Statistics.ipynb` and run
the cells from top to bottom.

## Repository Structure

``` text
student-scores-analysis/
├── README.md
├── Practical Exam Mathematics & Advanced Statistics.ipynb
├── students_scores.xlsx
├── math_score_dist.png
└── english_score_qq.png
```

## Notes and Limitations

-   The reported values reflect the calculations recorded in the
    supplied notebook.
-   The conditional pass probability of 99.73% for students with more
    than five study hours is an observed association in this dataset; it
    does **not** by itself prove that studying more than five hours
    causes a student to pass.
-   The Q-Q plot's flattening near 100 is consistent with scores being
    capped at the maximum value.
-   The README image links are relative paths. GitHub will display them
    when the image files are committed at the paths shown above.

------------------------------------------------------------------------
