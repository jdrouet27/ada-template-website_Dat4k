---
layout: default
title: And if we were in a time loop ?
---


#  And if we were in a time loop ?


As the holiday season begins, the need to get cozy and watch a comforting sentimental Christmas movie suddenly appears. There is by chance a new Christmas movie at the box office which looks perfectly cheesy!

Mmh… do you also feel this lingering sense of déjà vu? The Christmas movie last year had almost the same poster, and the same type of actors were starring. 
But when you think more deeply, you also realize that two months ago, you absolutely wanted to get in a spooky mood, and watch the scariest movie, as well as last October and all the years before!

![Pole express](assets/img/pole_express.jpg){:width="500px" class="center-image"}

You might have just found out the most disturbing observation: maybe it is not just a personal feeling, maybe most movies in each season share the same features. 
The evolution of an industry is always seen through its yearly graduation, but striking results could appear if time evolution was considered as a cycle. 
Most importantly, tendencies of the movie industry give insights about our whole society, as it is a mirror of our state of mind.
You are then just about to find that our mood is stuck in a time loop, which controls our entertainment desires! 

But as you are not into conspiracy theories, you might not be that easily convinced…
This study is then here to give you proper answers to your intuition. 
The tools of data sciences learned in ADA will be of great use to deepen the following lines of research: 
Is there a statistically significant recurrence of specific film genres during particular seasons or months of the year? 
Are there discernible patterns in the box office performance of specific film genres throughout the year, and do these patterns correlate with particular months?
Is there a relation between the connotation of the words and the season of release?
Can we predict the release season of a movie by looking at its main features?

In a first part the main genres will be extracted from the data, and their tendency over months will be enhanced. (plots of the main genres over months, analysis of pics, and importance of years. T-test to validate the hypothesis)
In a second part, a causal analysis will find if the reason why movies of a certain genre are more successful in terms of revenue is due to the fact that they are released during their season of predilection. (Très mal expliqué, mais faire causal analysis pour horror et family)
Then, using machine learning tools, the final goal is to determine if it is possible to predict the season of release of a movie, given its main features.



## I. Are there redundancies over months?

This question will be answered through the spectrum of genre and box office revenue. The goal is to determine if there are significant peaks in certain months for specific genres, and also to get an overview of the monthly box office revenue distribution.
### 1. The monthly distribution of genres
There are over 351 different genres in the movie metadata, which seems difficult to study at first sight! But their occurrence decays as a power law, which means that taking into account only the first genres will still describe most of the data. Moreover, many genres have slightly different names but can be grouped in main ones.
8 main genres are then chosen, because they define a high proportion of data, and also because they are the ones which will be relevant further in our monthly study:
- Drama
- Comedy
- Romance
- Thriller
- Action
- Family film
- Horror
- Informative
Let’s look at the overall monthly distribution of these main genres.





<iframe src="distrib_over_season_combined.html" width="800" height="850"></iframe>


The first histogram lets us compare each genre with itself for every month. 
It is clear that most of the genres have less movies in summer than in other seasons, except for Action, Horror and Family film movies.
On the second plot, it is easier to compare each genre to other genres throughout the months.
There are indeed more informative movies than horror movies in Spring but the tendency is the opposite in Summer.
It seems clear the Drama, Comedy, and Action genres are the most present, and this for all seasons.
No striking results appear in this first plot, it would be too easy right? 
Maybe some tendencies will appear by looking at genres individually…
We indeed found 3 genres with noticeable peaks: Horror, Family, and Romance movies.



<style>
    .center-iframe {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
</style>

<iframe src="combined_plots_Horror.html" width="1000" height="380" class="center-iframe"></iframe>


<div style="text-align: center;">
    <iframe src="combined_plots_Romance.html" width="1000" height="380"></iframe>
</div>

<div style="text-align: center;">
    <iframe src="combined_plots_Family film.html" width="1000" height="380"></iframe>
</div>


As can be seen in these plots, the spooky season is clearly during October, while family movies are more released during holidays periods (July, November, December), and a small peak can be seen in February for Romance movies.
However, these results need to be nuanced by stronger analysis, like hypothesis testing. For each of these three genres, a null hypothesis is built, to test the validity of the peaks seen in the previous plots:
H0: "Mean of movies per year and per month for peak months == Mean of movies per year and per month for all the other months."

<iframe src="ttest.html" width="1000" height="380" class="center-iframe"></iframe>



The null hypothesis is rejected under the significance level of 0.05 for the Horror movies in October, and for the Family films in July, November, and December, but not for the Romance movies in February.
This means that it is most likely that there will be more Horror movies in October, while there will be more Family films in July, November and December. 
Our time loop seems to be verified for some main genres!
### 2. The monthly distribution of box office revenue

**Need to do something**


## II. Is the box office affected by a particular release season for a particular movie genre?

We concluded previously that for some genres, there was a clear seasonal redundancy in terms of number of movies released. 
If it is true that for some genres, the number of movies increases a lot during a certain month, then does it mean that the movies released during this particular period are more successful in terms of box office revenue? In other words, will a Horror movie be more successful if released in October? 
This question goes even further than only looking at the movie redundancies, it asks the question of economic success, which can be very interesting for the cinema industry…

Because we obtained significant results only for Horror and Family movies, let’s perform a causal analysis on these genres. This observational study aims to determine if the economic success of Horror/Family movies is caused by a release month in October/July, November, December.
### 1. Hunt down the confounders!

There is a need to balance our control and treatment groups, so that the comparison of their mean box office revenue makes sense. 

The first main confounder would be the movie budget.  Indeed, box office is influenced by when the big franchise movies are released. We’re interested in the success of movies regardless of how big the franchise is.

Secondly, an important bias is the continent of release. In fact, Halloween is celebrated at different degrees of popularity. For example, Russian people don't even celebrate it, whereas It is a big event in the USA. For the case of Family movies, the holiday season also clearly depends on the country of release.
For that reason we might want to match movies with the same continent of release. 

Finally, we take into account the release year of the movie, to eliminate the influence of inflation over the years.
To balance these confounders, a propensity score is used to match the datasets, while an exact matching is performed on the country of release.



### 2. Contradictory results
* Horror movies
Idea of interactive plot-> box plots of treat/control box office revenue before and after the matching 

Regarding Horror movies, it was found that after matching, the movies released in October (treatment group) were showing better average box office revenue than in other months. 

* Family movies
Idea of interactive plot-> box plots of treat/control box office revenue before and after the matching

Regarding Family movies, it was found that after matching, the movies released in July/November/December (treatment group) were showing lower average box office revenue than in other months. 

Comment this part and justify contradictory results

## III. Is a movie release season predictable?






