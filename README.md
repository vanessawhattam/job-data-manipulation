[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Yv0gFShj)
# Advanced Data Manipulation THA
In this assignment, you will use advanced functions in `Pandas` to query and filter your data. These functions reduce the workload by simplifying and reducing your code.

To submit, please perform the following:
1. Save a script file for Python with the following name: `covid_lastname_firstname.py` where lastname is your last name and firstname is your first name.
1. Save your screenshots of your output to the directory `assets`. This directory exists at the same leve as `data`.
1. Link your screenshots in `submission.md` where appropriate. That is, if you have screenshots supporting your answers, link those screenshots next to your answer.
1. Answer questions in `submission.md`, linking any screenshots as necessary.
1. Push your assignment to GitHub.

## COVID-19 Pandemic in the United States
The COVID-19 pandemic in the United States is the deadliest pandemic in its history. With 842,141 confirmed deaths in [January of 2022](https://ourworldindata.org/covid-deaths), it has wrought many a change including the further polarization of American politics, increase in virtual work environments, manufacturing and supply chain complications, increase in online learning, greater engagement in video streaming and gaming, and many others.

The pandemic has negatively effected the economics of all countries including the [United States](https://en.wikipedia.org/wiki/Economic_impact_of_the_COVID-19_pandemic_in_the_United_States). A table on the linked page presents a [statistical summary](https://en.wikipedia.org/wiki/Economic_impact_of_the_COVID-19_pandemic_in_the_United_States#Statistical_summary) with various data including job levels, unemployment rate, inflation rate. The data is given for February through August.

If you are curious how I scraped the data from Wikipedia, then feel free to look at the R file [scraping_covid_data.R](/scraping_covid_data.R). I have comments embedded within the file, but I am more than happy to talk to explain it if you are curious. I could have performed this task in Python, but chose to use R because the majority of students have experience with R, so the code related to web scraping would should be the only code you are not familiar with.

## Rename Columns (1 pt.)
Import the file `scraped_data.txt`. Once imported, rename columns like so: (1 pt.)
* `jobs_lvl` change to `jobs_lvl_1000`
* `jobs_mth` change to `jobs_month`
* `unemp_rate` change to `unemploy_rate`
* `unemp_mil` change to `unemploy_mil`
* `emp_pop` change to `employ_pop`
* `infl_rate` change to `infl_rate_perc`
* `snp500_mean` change to `snp500_mean_lvl`
* `public_debt` change to `public_debt_tril`
* `month` leave it as is

## Data Wrangling and Manipulation (9 pts.)
It is time to practice your data wrangling skills with Python. Please perform the following tasks. Take a screen capture of your output and link it in `submission.md`. 

Note, some of the tasks ask you to use regular expressions. Since we have not covered it in class, I have provided the regex syntax. If parentheses are included as part of the regex, include it. For example, I provide `(^j)` below. Thus, your code would be `.filter(regex='(^j)')`.

Ready? Let's go!
1. Calculate the mean of `jobs_lvl_1000`. (1 pt.)
1. Calculate the median of `jobs_lvl_1000`. (1 pt.)
1. Select all columns that start with a *j* (i.e., `(^j)`) **or** contain an *a* (i.e., `(a)`). Save it as a new data frame named `jobs_data_alt`. Output the columns to the terminal. (1 pt.)
1. Using your newly created data frame `jobs_data_alt`, select data in which `jobs_lvl_1000` was greater than 135,000. (1 pt.)
1. Using Pandas piping notation, perform the previous two operations together and save it as a new data frame `jobs_data_alt2`. This means you should select columns that start with a *j* or contain an *a* and select months in which `jobs_lvl_1000` was greater than 135,000. (2 pts.)

Please perform the following tasks. *Do not use* `jobs_data_alt` or `jobs_data_alt2`, but use the original data frame you initially created from the text file.
1. Using Pandas piping notation, select all columns that end with the letter *l* (i.e., `l$`) or contain the letter *o* (i.e., `o`). Additionally, select rows in which `snp500_mean_lvl` is greater than or equal to 3000. (2 pts.)
1. Use the query you just performed. You will calculate the mean and median of `jobs_lvl_1000`. How does it compare to the answers above in which you calculated the mean and median? Please provide your answer in `submission.md`. (1 pt.)
