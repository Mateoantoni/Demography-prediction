# 🌍 Demography prediction

**A Python-powered tool to simulate and analyze the demographic evolution of a region over time.**  
Designed for curious minds aiming to model population growth and interpret historical trends.

---

## 📜 Description

**Demography prediction** processes CSV data containing population records for various countries across multiple years.  
By selecting one or more country codes, it computes:

- Linear regression models in two forms:  
  - `Y = aX + b` (Fit 1: population over time)  
  - `X = aY + b` (Fit 2: time as a function of population)
- Root Mean Square Deviation (RMSD) for both fits
- Population estimation in the year **2050**
- **Pearson correlation coefficient** between year and population size

It is a compact yet powerful tool to explore demographic trajectories and predict future populations.

---

## 🧠 Features

- 📈 Regression modeling using least squares
- 📊 RMSD calculation to evaluate fit accuracy
- 🔍 Correlation analysis (Pearson)
- 📅 Projection of population values in 2050
- 🏳️ Multi-country selection with cumulative population summing

---

## 🗂️ File Structure

- `data.csv` — input dataset (semicolon-separated CSV)
- `main.py` — main script (executable Python program)

---

## 🛠️ Usage

```bash
python3 main.py <COUNTRY_CODE_1> <COUNTRY_CODE_2> ...
