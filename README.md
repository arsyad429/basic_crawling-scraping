# Basic Web Crawling & Web Scraping Tutorial

This repository contains a **comprehensive tutorial on web crawling and web scraping using Python**, starting from **basic concepts** to **advanced case studies**, including **building an image dataset from crawling and scraping results**.

The tutorials in this repository use two main libraries that are widely used in both industry and academia:

* **BeautifulSoup** → for scraping static web pages
* **Selenium** → for crawling and scraping dynamic (JavaScript-rendered) web pages

This repository is suitable for:

* Beginners who are new to web scraping
* Computer science / data science students
* Preparing datasets for **Machine Learning / Computer Vision**

---

## 🚀 Topics Covered

The tutorials are structured **step by step from basic to advanced**, including:

### 1️⃣ Introduction to Web Crawling & Web Scraping

* What is web crawling vs web scraping
* Basic HTML structure (tags, attributes, selectors)
* Scraping ethics and robots.txt limitations

### 2️⃣ Basic Web Scraping with BeautifulSoup

* Fetching HTML using `requests`
* Parsing HTML with BeautifulSoup
* Extracting data using:

  * `find()`
  * `find_all()`
  * CSS selectors

### 3️⃣ Web Crawling & Scraping with Selenium

* Using Selenium WebDriver
* Automatically opening websites
* Locating HTML elements using:
  * `By.CSS_SELECTOR`
* Difference between `find_element` and `find_elements`

### 4️⃣ Selenium Headless Mode

* What headless mode is
* When to use headless mode
* Advantages and disadvantages

### 5️⃣ Crawling Dynamic Websites

* Handling infinite scroll
* Waiting for elements (implicit & explicit waits)
* Extracting content loaded by JavaScript

### 6️⃣ Image Scraping & Downloading

* Extracting image URLs from attributes and styles
* Downloading images using `requests`
* Saving image files to a local directory

### 7️⃣ Building an Image Dataset

* Organizing dataset folders
* Assigning labels to each image
* Saving dataset metadata to **CSV (Pandas DataFrame)**
* Avoiding duplicate images

The resulting dataset is **ready to be used for Machine Learning / Deep Learning**.

---

## 📂 File Structure

Some of the main files in this repository:

* `SeleniumSimpleScraping.py`
  → Simple scraping example using Selenium

* `SeleniumAksesWebDriver.py`
  → How to access and use Selenium WebDriver

* `SeleniumCrawlingAndScraping.py`
  → Crawling and scraping dynamic web pages

* `SeleniumCrawlingAndScrapingHeadlessMode.py`
  → Crawling using Selenium Headless Mode

* `SeleniumCrawlingAndScrapingImage.py`
  → Image scraping and downloading from websites

* `SeleniumCrawlingAndScrapingImageHeadlessMode.py`
  → Image downloading using headless mode

* `SeleniumCreateImageDataset.py`
  → Case study: building an **image dataset** from crawling and scraping results

---

## 🛠️ Technologies Used

* Python 3.x
* Selenium
* BeautifulSoup (bs4)
* Requests
* Pandas
* Chrome WebDriver

---

## 📌 Important Notes

* Use this repository **for learning and research purposes only**
* Always check and respect the **Terms of Service** of the target website
* Avoid excessive scraping that may overload servers

---

## 🎯 Learning Outcomes

After completing the tutorials in this repository, you should be able to:

* Understand web crawling and scraping concepts
* Extract text and image data from websites
* Handle both static and dynamic websites
* Build datasets ready for **Data Science & Machine Learning**

---

## ✨ Author

This repository was created as a **learning resource from basic concepts to real-world practice**.

Happy learning and enjoy exploring web scraping 🚀
