# Data Wrangling and Manipulation (9 pts.)
# It is time to practice your data wrangling skills with Python. Please perform the following tasks. 
# Take a screen capture of your output and link it in `submission.md`. 

#Import the file scraped_data.txt. Once imported, rename columns like so: (1 pt.)
import pandas as pd

scraped_data = pd.read_table('data/scraped_data.txt')

# Rename the columns
scraped_data = (scraped_data
 .rename(columns={'jobs_lvl':'jobs_lvl_1000',
                  'jobs_mth':'jobs_month',
                  'unemp_rate':'unemploy_rate',
                  'unemp_mil':'unemploy_mil',
                  'emp_pop':'employ_pop',
                  'infl_rate':'infl_rate_perc',
                  'snp500_mean':'snp500_mean_lvl',
                  'public_debt':'public_debt_tril'}))


# 1. Calculate the mean of `jobs_lvl_1000`. (1 pt.)
(scraped_data
 .agg({'jobs_lvl_1000':'mean'}))

# 2. Calculate the median of `jobs_lvl_1000`. (1 pt.)
(scraped_data
 .agg({'jobs_lvl_1000':'median'}))

# 3. Select all columns that start with a *j* (i.e., `(^j)`) **or** contain an *a* (i.e., `(a)`). 
#    Save it as a new data frame named `jobs_data_alt`. Output the columns to the terminal. (1 pt.)
jobs_data_alt = (scraped_data
 .filter(regex = '(^j)|(a)'))

jobs_data_alt

# 4. Using your newly created data frame `jobs_data_alt`, select data in which `jobs_lvl_1000` was greater than 135,000. (1 pt.)
(jobs_data_alt
 .query('jobs_lvl_1000 > 135000'))

# 5. Using Pandas piping notation, perform the previous two operations together and save it as a new data frame `jobs_data_alt2`. 
#    This means you should select columns that start with a *j* or contain an *a* and select months in which `jobs_lvl_1000` was greater than 135,000. (2 pts.)
jobs_data_alt2 = (scraped_data
                  .query('jobs_lvl_1000 > 135000')
                  .filter(regex = '(^j)|(a)'))

# Please perform the following tasks. *Do not use* `jobs_data_alt` or `jobs_data_alt2`, but use the original data frame you initially created from the text file

# 1. Using Pandas piping notation, select all columns that end with the letter *l* (i.e., `l$`) or contain the letter *o* (i.e., `o`). 
#    Additionally, select rows in which `snp500_mean_lvl` is greater than or equal to 3000. (2 pts.)
(scraped_data
 .query('snp500_mean_lvl >= 3000')
 .filter(regex = 'l$|o'))

# 2. Use the query you just performed. You will calculate the mean and median of `jobs_lvl_1000`. 
#    How does it compare to the answers above in which you calculated the mean and median? Please provide your answer in `submission.md`. (1 pt.)
(scraped_data
 .query('snp500_mean_lvl >= 3000')
 .filter(regex = 'l$|o')
 .agg({'jobs_lvl_1000': ['mean', 'median']}))