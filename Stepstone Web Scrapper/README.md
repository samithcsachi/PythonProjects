![Python version](https://img.shields.io/pypi/pyversions/Selenium)
![GitHub last commit](https://img.shields.io/github/last-commit/samithcsachi/PythonProjects)
![GitHub repo size](https://img.shields.io/github/repo-size/samithcsachi/PythonProjects)
![License](https://img.shields.io/badge/License-MIT-green)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

Badge [source](https://shields.io/)

# Stepstone Web Scrapper 

In this project we are trying to web scape the most popular job listing platform in germany. We would like to get the Job Title, Company Name, Location, Contract Type, Job Type, Published Days and Verified Status

## Authors

- [Samith Chimminiyan](https://www.github.com/samithcsachi)

## Table of Contents

- [Authors](#Authors)
- [Table of Contents](#table-of-contents)
- [Problem Statement](#problem-statement)
- [Tech Stack](#tech-stack)
- [Lessons learned and recommendation](#lessons-learned-and-recommendation)
- [Limitation and what can be improved](#limitation-and-what-can-be-improved)
- [Run Locally](#run-locally)
- [Explore the notebook](#explore-the-notebook)
- [Contribution](#contribution)
- [License](#license)

## Problem Statement 

By web scrapping the Job Site, Have created a Dataset which contains all details which can be used for machine learning projects. Using classification algorithm can develop a model which can predict the Average Salary of Data Scientist. 


## Tech Stack

- Python (refer to requirement.txt for the packages used in this project)
- Selenium 


## Lessons learned and recommendation
The initial plan was create a simple scraper using Selenium. When i was searching the main page of Stepstone i can get full list of Jobs and there details. But the issue is that the Salary range was only visible once I login. So i have used a dummy email id and password. Then i was trying to scrape from the main page itself all the details but realized that clicking the each link and opening in another tab will give more details such as description and company details. Once the Tab is opened we can scraped the details and then close the Tab and move to over to the main tab. I have set up the no of jobs to 100 so have written code mode to next screen and then continue the scrapping till the jobs are 100. Scraper was running smooth till 12th Page then came the main challenge for me it an error code. When i searched in google it says it is "Akamai Edge error". i was trying different method to tackle the error. So i have refreshed the site in code and also changed the time sleep to random and was able to tackle the error. 

- Learned to Tackle Akamai Edge error
- Can add code to scrape the description columns 


## Limitation and what can be improved

The Dataset can be used for machine learning purpose but if there are more features like programming language requirements , no of years experience required, other technical skills required. Machine learning model can be developed to check the average salary and also another model can be developed which can analyze the prerequisite for each job is as per the standard or not. 




## Run Locally
Initialize git

```bash
git init
```


Clone the project

```bash
git clone https://github.com/samithcsachi/PythonProjects.git
```

enter the project directory

```bash
cd PythonProjects/Stepstone\ Web\ Scrapper

```

Create a conda virtual environment and install all the packages from the environment.yml (recommended)

```bash
conda env create --prefix ./env --file environment.yml

```

Activate the conda environment

```bash
conda activate ./env
```

List all the packages installed

```bash
conda list
```
Run the Scraper

```
python stepstone_scraper.py

```




## Explore the notebook

GitHub :  [https://github.com/samithcsachi/PythonProjects/blob/main/Stepstone%20Web%20Scrapper/stepstone_scrapper.py](https://github.com/samithcsachi/PythonProjects/blob/main/Stepstone%20Web%20Scrapper/stepstone_scrapper.py)

Kaggle : [https://www.kaggle.com/code/samithsachidanandan/stepstone-web-scrapper](https://www.kaggle.com/code/samithsachidanandan/stepstone-web-scrapper)

## Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or contribute.

## License

MIT License

Copyright (c) 2025 Samith Chimminiyan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Learn more about [MIT](https://choosealicense.com/licenses/mit/) license

## Contact
If you have any questions, suggestions, or collaborations in data science, feel free to reach out:
- 📧 Email: [samith.sachi@gmail.com](mailto:samith.sachi@gmail.com)
- 🔗 LinkedIn: [www.linkedin.com/in/samithchimminiyan](https://www.linkedin.com/in/samithchimminiyan)
- 🌐 Website: [www.samithc.com](https://www.samithc.com)
