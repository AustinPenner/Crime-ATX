# Crime and Bars in Austin TX
## Overview
An investigation into criminal offenses and bars in Austin TX. This project looks at the location of crimes occurred relative to nearby bars in order to determine if a relationship exists between the two. Spoiler: it does.

Crime data was utilized thanks to [Austin Open Data](https://data.austintexas.gov/), who made this information publicly available. Information regarding bars in Austin was pulled from the Yelp Fusion API.

## Technologies Used
python, mongodb, pandas, matplotlib, scikit-learn

## The Data
There are 2,197,125 crimes in the original dataset, from 2003-2019. I filtered on records from 2016 to 2019 (inclusive) with a valid latitude and longitude coordinate, leaving 421,433 crimes to work with. I used Yelp to pull location and other data for all 797 bars in the city. We only consider crimes since 2016 as the bars considered are only a current snapshot as of December 2019.

Heatmap of bars in the city:

<img src="https://github.com/AustinPenner/Crime-ATX/blob/master/images/Bar%20Heatmap.PNG" width="450" height="450">

Top 20 Criminal Offenses:

<img src="https://github.com/AustinPenner/Crime-ATX/blob/master/images/Top%2020%20Crimes.png" width="650" height="400">

## Analysis
The methodology I used was to grab a small, fixed region around some coordinate point and count how many bars were in the region. I used square regions of 1000x1000 ft to capture a few city blocks. To form a baseline I made a grid and iterated through the city of Austin counting how many bars were in each region. The average number of bars was 0.295.

I then looked at each crime with a lat/long coordinate, counted the number of bars in the region centered at that coordinate point, and compared the two. This was done for each criminal offense type in the top 20. For example, the average bars per region for DWIs is 3.525. This difference is clearly large, but is it statistically significant? To answer this question I did 20 one-tailed t tests at significance level of 0.05. To account for the number of comparisons I used a Bonferroni correction, which brings the significance level to .0025. 

The full EDA can be found under [data_exploration.ipynb](https://github.com/AustinPenner/Crime-ATX/blob/master/data_exploration.ipynb).

## Results
I wanted to know if bars were associated with crime, i.e. if crime occurs more frequently around bars than elsewhere. I considered the top 20 categories from 2016 through 2019. A remarkable 18 of 20 crimes were found to occur more often around bars at a statistically significant level.
