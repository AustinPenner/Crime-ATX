# Crime and Nightlife in Austin, TX
## Overview
An investigation into criminal offenses in Austin TX and where they occur relative to Austin's nightlife.

Crime data was utilized thanks to [Austin Open Data](https://data.austintexas.gov/), who made this information publicly available. Information regarding bars in Austin was pulled from the Yelp Fusion API.

## Technologies Used
python, mongodb, pandas, matplotlib, scikit-learn

## Show Me The Data
There are 2,197,125 in the full criminal offense dataset. Because the bars dataset is only a current snapshot of bars in Austin, I only pulled records since 1/1/2016 with a valid (latitude,longitude) coordinate, leaving 421,433 crimes to work with. I scraped the entire city and found 797 bars.

The full EDA can be found under [data_exploration.ipynb](https://github.com/AustinPenner/Crime-ATX/blob/master/data_exploration.ipynb).

## Results
I wanted to know if bars were associated with crime, i.e. if crime occurs more frequently around bars than elsewhere. I considered the top 20 categories from 2016 through 2019. Of these 20, 18 were found to occur more frequently around bars at a statistically significant level (p=.05).
