<a id='section_6'></a>
<img width="1269" alt="Screen Shot 2020-11-21 at 9 13 05 PM" src="https://user-images.githubusercontent.com/68249276/99892790-5fb19480-2c3e-11eb-81ad-dc26b28e64f3.png">

<br>

<h2><center>Am I Speaking Your Language?</center><h2>
<h3><center>Natural Language Processing Project</center></h3>
<h4><center> Authors: Chris Ortiz, Matthew Knight and Gilbert Noriega </center><h4>

[About the Project](#section_1) || [Data Dictionary](#section_2) ||  [Initial Hypotheses/Thoughts](#section_3) || [Project Plan](#section_4) || [How to Reproduce](#section_5)



<br>

<a id='section_1'></a>
## About the Project
> We are future data scientist testing our knowledge of Natural Language Processing. For this project, we will be scraping data from over nearly 600 GitHub repository READMEs' using a variety of methods and build machine learning models from the data we pooled. 
___

<br>

## Background
> GitHub is a subsidiary of Microsoft which provides hosting for software development and version control using Git. As of January 2020, GitHub reports having over 40 million users and more than 190 million repositories(including at least 28 million public repositories), making it the largest host of source code in the world.
___

<br>

>*Acknowledgement:The dataset was mined from github.com* 

___

<br>

## Goals
> Our goal for this project is to build a model that can predict what programming language a repository is, given the text of the README file. We will deliver the following in a github repository: 
>
> - A clearly named final notebook. This notebook will be what will contain plenty of markdown documentation and cleaned up code.
> - A README that explains what the project is, how to reproduce the work, and our notes from project planning
> - Python modules that automate the data acquisistion and preparation process. These modules will be imported and used in the final notebook.
> - A set of google slides suitable for a general audience that summarize your findings.
  
[back to the top](#section_6)

___

<br>

<a id='section_2'></a>
## Data Dictionary

| Features | Definition |
| :------- | :-------|
| readme | text of the readme file |
| words | data that has been cleaned and seperated by words |
| watchers | users who are watching the repository |
| stars | users who have starred the repository |
| forks | users who have forked the repository |
| commits | number of times the owner has added content to the repository|


<br>

|  Target  | Definition |
|:-------- |:---------- |
|  language | the main programming language used throughout the github repository |

<br>

[back to the top](#section_6)
___

<br>

<a id='section_3'></a>
## Thoughts

>### Thoughts
>
> - We could add a new feature?
> - Should I turn the categorical variables into booleans?

<br>



[back to the top](#section_6)
___

<br>

<a id='section_4'></a>
## Project Plan: Breaking it Down

>- acquire
>    - Web scraped X amount of README’s, watchers, forks, stars and commits from Y topics from request library
>    - Decide on 4 programming languages: 
>       -   C++, Java, Javascript, Python
>   - Use an number of different topics to introduce variety:
>       - Sports, Biology, Artificial Intelligence, Data Engineering
>   - create an acquire.py to automate the process
>   - create a json file for future use
>- prepare
>    - clean language column by removing % number at the end
>    - change columns to numeric types as needed
>    - normalize, tokenize, stem, lemmatize and remove stop words
>   - split into train, validate, and test
>    - create a prepare.py to automate the process
>    - create a csv file for future use
>
>- explore
>    - split words into sets of 1, 2 and 3
>    - determine significance both visually and statistically
>    - document and consider the results for modeling
> 
>- model and evaluation
>    - find which features are most influential
>    - try different algorithms: 
>       - Ridge Classifier
>       - Random Forest
>       - Gradient Boost
>    - evaluate on train
>    - evaluate on validate
>    - select best model and test to verify
>    - create a preprocessing.py and model.py to automate the process
>
>- conclusion
>    - summarize findings
>    - provide next steps


[back to the top](#section_6)

___

<br>

<a id='section_5'></a>
## How to Reproduce

>1. Download data csv from [here](https://raw.githubusercontent.com/NLP-Darden-Project-Team-6/NLP-3/master/data/raw/readmes.json) or use the [acquire.py](https://github.com/NLP-Darden-Project-Team-6/NLP-3/blob/master/src/acquire.py) functions
>2. Prepare the data with the [prepare.py](https://github.com/NLP-Darden-Project-Team-6/NLP-3/blob/master/src/prepare.py) functions or install the prepped csv [here](https://raw.githubusercontent.com/NLP-Darden-Project-Team-6/NLP-3/master/data/prepared/prepared_readmes.csv)
>3. Run a jupyter notebook importing the necessary libraries and functions.
>4. Follow along in the [summary notebook](https://github.com/NLP-Darden-Project-Team-6/NLP-3/blob/master/summary.ipynb) or forge your own exploratory path. 

[back to the top](#section_6)