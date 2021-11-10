# Coursework 1

## Technical information
### Repository URL
[Repository](https://github.com/14113p/-comp0035_cw1_2021-22.git)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!


## Selection of project methodology
### Methodology (or combination) selected
Scrum/TDSP

### Selection criteria and justification of selection
I have chosen this methodology as I already have some experience with Scrum, however as it is a also a data science project I would like to merge it with TDSP, for the benefit of both the project and my knowledge.
I am still relatively inexperienced when it comes to bigger projects so it would be nice to have a quantifiable progress in order to stay motivated and organised. I am also yet to decide the exact course of the project, so choosing an Agile methodology would allow me to work in small increments and change my plans on the fly if needed to do so.

## Definition of the business need
### Problem definition
    A movie's success or failure often seems to be a matter of chance. It especially impoortant for people involved in movie's production. There is a need for an easily available way of seeing current/historical trends in the film industry.
    The purpose is to visualise the relationship between movie's commercial/critical success and other variables such as length, genre, budget. This would allow to better understand tastes of the general public and could be used when making commercial decisions.
    For the casual/semicasual users, the app will serve as a market understanding tool and a reference point in the popculture discussions.
### Target audience
    - Filmmakers looking for commercial success
    - Film industry enthusiasts
    - Movie Journalists
[The_Filmmaker](personas\filmmaker.pdf)
[The_Movie_Enthusiast](personas\m_enthusiast.pdf)
[The_Journalist](personas\journalist.pdf)
### Questions to be answered using the dataset
    - Is there a common attribute that the most succesful movies share?
    - How does the film's popularity change over time? Does the patternt differ by genre?
    - Was there a noticable change in average movie reception at the time of important events (i.e. pandemic)? 
    - Are movies of particular genre/length/release_date more successful than the others?
    - What is the relationship between movie's rating/revenue and budget?
    - Does original language being other than English influence movie's reception?

### Suggested web app

## Data preparation and exploration
### Data preparation
[Data Preparation](data_preparation.py)

### Prepared data set
[Original data set](data\BFI_raw)
[Prepared data set](data\BFI_merged.xlsx)

### Data exploration
[Data Exploration](data_exploration.py)

## Weekly progress reports

### Report 1
What I did in the last week:
- Chosen the methodology and written the justification 
- Setup the IDE, integrated it with GitHub and setup a virtual environment

What I plan to do in the next week:
- solve the problem below
- have an initial look at the data set

Issues blocking my progress (state ‘None’ if there are no issues):
- can't run code using venv, have to test on global python installation. 
    Reason: pip installing packages to wrong directory

### Report 2
What I did in the last week:
- Solved the package installation directory problem - venv was created and active for interpreting, but not properly activated for pip.
- Defined the business need (WIP)
- Downloaded the first batch of raw data, run first overview

What I plan to do in the next week:
- Have a deeper look into the data
- Attempt to merge the datasheets into one
- Have an initial look at the tmdb API

Issues blocking my progress (state ‘None’ if there are no issues):
- None

### Report 3
What I did in the last week:
- Had a look at the additional libraries and APIs that may be useful (tmdb, glob, os)
- Planned the process of data prep (not much code yet)

What I plan to do in the next week:
- Explore the data properly
- Merge xls files into one
- Make use of the tmdb

Issues blocking my progress (state ‘None’ if there are no issues):
- Merging process is imperfect, doesn't work yet
- Still waiting to be attributed a tmdb API key

### Report 4
What I did in the last week:
- Prepared the data
- Merged the files
- Included the API data

What I plan to do in the next week:
- Polish methodology and target audience sections
- Plot some graphs in the exploration part

Issues blocking my progress (state ‘None’ if there are no issues):
- None

## References
Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
used to using in your course.
