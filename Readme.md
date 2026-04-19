# Selenium Automation – AdNabu Test Store

## Overview

This project automates a key user flow on a Shopify store:

* Search for a product (**Snowboard**)
* Add the product to the cart
* Verify it is successfully added

Built using:

* Python
* Selenium
* PyTest

---

## Prerequisites

Make sure you have:

* Python (>= 3.8)
* Google Chrome
* ChromeDriver (matching your Chrome version)

---

## Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-link>
cd <repo-folder>
python -m pip install selenium pytest
```

---

## Project Structure

```
.
├── test_Adnab.py        # Test script (This file run with pytest + selenium setup , used for generating report)
└── Adnab.py             # Test script (This file will need only selenium setup to run)
└── chromedriver.exe     # ChromeDriver (or configure path)

```

---

## Configuration

Update ChromeDriver path in the script:

```python
Service(r"C:/DRIVERS/chromedriver-win64/chromedriver.exe")
```

---

## Run the Test

```bash
python -m pytest test_Adnab.py -v
```

---

## Test Scenario

* Open website
* Handle password-protected page
* Search for "Snowboard"
* Select product from results
* Add product to cart
* Verify product is added


Automation Test Assignment
