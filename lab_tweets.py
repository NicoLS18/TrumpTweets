#!/usr/bin/python3

'''
# Lab: Analyzing Trump Tweets

In this lab, you will analyze all tweets sent by president Trump from 2009-2018.
You will get practice
1. loading datasets stored in JSON files,
2. creating plots in python, and
3. writing "fully open ended" code where I don't give you any starter code/doctests to guide you.

The data we will analyze is used to create the following two websites:
1. [An analysis of which types of tweets Trump is likely to send himself, versus which his staffers send.](http://varianceexplained.org/r/trump-tweets/)
2. [A search engine for all of Trump's tweets.](https://www.thetrumparchive.com/)

> **Note:**
> I am using Markdown formatting within this python docstring.
> This is a *very* common practice.
> Markdown (unlike HTML) is designed to be human readable in it's "uncompiled" form,
> and so programmers write markdown *everywhere*.

## Part 0: Setup Project

You will have to upload files to github to submit this lab.
Complete the following steps to setup your project.

1. Create a new github repo through the github interface.

2. Clone that project onto your computer.

3. Copy this `lab_tweets.py` file into your project folder.

## Part 1: Download the Data

The github repo <https://github.com/bpb27/trump_tweet_data_archive> contains an archive of tweets sent by Donald Trump.

1. Download these files `master_*.json.zip`, where * is a year.
    There should be 10 total files (2009-2018).

    > **Note:**
    > This particular archive stops in 2018 because the maintainer moved their codebase to <https://github.com/bpb27/tta-elastic>.
    > The newer archive has data that goes through the current year (and includes messages sent on Truth Social),
    > but it's a bit more complicated to access the data,
    > so we will use this older archive for this assignment.

2. Unzip these files into the project folder you created in Part 0 above.
    You should get a bunch of files that look like `master_*.json`.

## Part 2: Data Analysis

1. Modify this python file so that it:

    1. Opens each json file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.

    2. Prints the total number of tweets.

    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.

       > **NOTE:**
       > It's important to remember that each of these words can appear with many different capitalizations,
       > and your program should count the word no matter how it is capitalized.
       > For example, `OBAMA`, `obama`, and `ObAmA` all need to count as an occurrence of the word `Obama`.
       > Recall that the easiest way to do this is to use the .lower() function and in keyword.

    4. Prints out a count of each of these words.

        > **Hint:**
        > My program gives the following output:
        > ```
        > len(tweets)= 36307
        > counts= {'trump': 13924, 'obama': 2712 ... }
        > ```
        > You'll know your program is correct if you get the same numbers.

2. Select at least 3 more interesting words/phrases to count in trump's tweets,
    and modify your program to display those words.

3. Calculate the percentage of tweets that contain each word.  (Both your new words and Trump's original tweets.)

4. Display the results nicely in a markdown table.

    The display must have all words right justified and the percents printed with two
    significant figures (on both sides of the decimal) as shown in the example output below.

    ```
    | phrase            | percent of tweets |
    | ----------------- | ----------------- |
    |              daca | 00.17             |
    |         fake news | 00.92             |
    |  mainstream media | 00.06             |
    |            mexico | 00.55             |
    |             obama | 07.47             |
    |            russia | 01.13             |
    |             trump | 38.35             |
    |              wall | 00.91             |
    ```

    There are many ways to achieve this effect in python,
    but I recommend using python's f-string syntax.
    Here is a little cheat sheet using doctests:

    >>> name = "Alice"
    >>> f"{name:<10}"
    'Alice     '
    >>> f"{name:>10}"
    '     Alice'
    >>> f"{name:^10}"
    '  Alice   '
    >>> f"{name:*^10}"
    '**Alice***'

    >>> pi = 3.14159265
    >>> f"{pi:.2f}"
    '3.14'
    >>> f"{pi:.4f}"
    '3.1416'
    >>> f"{pi:8.2f}"
    '    3.14'
    >>> f"{pi:08.2f}"
    '00003.14'

5. Plot the results in a bar graph.

    > HINT:
    > The most common way to plot in python is with the matplotlib library.
    > We won't be covering how to use it in class in order to get you practice figuring things out by yourself.
    > You can find a tutorial here: <https://www.w3schools.com/python/matplotlib_bars.asp>.
    > You are also welcome to ask your favorite AI.

## Submission

Create a properly formatted markdown file `README.md` that contains:
1. the markdown table created by your program
2. the image created by your program
3. a short description (1 sentence is fine) for your table/image above

Ensure that you have uploaded to your github repo:
1. your modified python file
2. your python image

You do not need to pass any github actions for this submission.

Upload your github url to canvas.

## Extra Credit

There are two extra credit opportunities for this lab, worth one point each.

1. If you use the latest version of the data (instead of the files in the github repo) you will get +1 point.
    You can find instructions for accessing the data at <https://www.thetrumparchive.com/faq> under the question "Can I have the data?"

2. If you make a plot of other interesting information in this dataset (that doesn't use the 'text' key).
    For example, you could plot: what time of day does Trump tweet most often? or what state does Trump tweet from most often?
    If you add this to your repo you will get +1 point.
'''

import json
import glob
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend so the script runs without a display
import matplotlib.pyplot as plt

################################################################################
# Part 1: Load all JSON files and concatenate tweets
################################################################################

tweets = []
json_files = glob.glob('master_*.json')

for filename in sorted(json_files):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        tweets.extend(data)

print(f'len(tweets)= {len(tweets)}')

################################################################################
# Part 2: Count keyword occurrences (case-insensitive)
# Required keywords + 3 extra interesting ones
################################################################################

keywords = [
    'obama',
    'trump',
    'mexico',
    'russia',
    'fake news',
    # Extra credit / additional interesting keywords
    'wall',
    'daca',
    'mainstream media',
]

counts = {}
for keyword in keywords:
    count = sum(1 for tweet in tweets if keyword in tweet.get('text', '').lower())
    counts[keyword] = count

print(f"counts= {counts}")

################################################################################
# Part 3: Calculate percentages and display as a markdown table
################################################################################

total = len(tweets)

# Sort keywords alphabetically for the table
sorted_keywords = sorted(counts.keys())

# Determine column widths
phrase_width = max(len(kw) for kw in sorted_keywords)
phrase_width = max(phrase_width, len('phrase'))
pct_label = 'percent of tweets'
pct_width = max(len(pct_label), 5)  # "00.17" is 5 chars

separator = '-' * phrase_width
pct_separator = '-' * pct_width

print()
print(f"| {'phrase':>{phrase_width}} | {pct_label:<{pct_width}} |")
print(f"| {separator:>{phrase_width}} | {pct_separator:<{pct_width}} |")

for keyword in sorted_keywords:
    pct = (counts[keyword] / total) * 100
    pct_str = f"{pct:05.2f}"  # e.g. "07.47"
    print(f"| {keyword:>{phrase_width}} | {pct_str:<{pct_width}} |")

################################################################################
# Part 4: Bar graph of keyword percentages
################################################################################

percentages = [(counts[kw] / total) * 100 for kw in sorted_keywords]

plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_keywords, percentages, color='steelblue', edgecolor='black')

# Label each bar with its percentage
for bar, pct in zip(bars, percentages):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.2,
        f"{pct:.2f}%",
        ha='center',
        va='bottom',
        fontsize=9
    )

plt.xlabel('Keyword / Phrase', fontsize=12)
plt.ylabel('Percent of Tweets (%)', fontsize=12)
plt.title("Percentage of Trump Tweets (2009–2018) Containing Each Keyword", fontsize=13)
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.savefig('tweet_keyword_percentages.png', dpi=150)
print("\nBar graph saved to tweet_keyword_percentages.png")

################################################################################
# Extra Credit Part 2: What hour of the day does Trump tweet most often?
################################################################################

from collections import Counter

hour_counts = Counter()
for tweet in tweets:
    # created_at format: "Mon Jan 01 12:34:56 +0000 2018"
    try:
        created_at = tweet.get('created_at', '')
        # Extract the time portion (HH:MM:SS)
        time_part = created_at.split()[3]
        hour = int(time_part.split(':')[0])
        hour_counts[hour] += 1
    except (IndexError, ValueError):
        pass

hours = list(range(24))
hour_tweet_counts = [hour_counts.get(h, 0) for h in hours]

plt.figure(figsize=(12, 5))
plt.bar(hours, hour_tweet_counts, color='tomato', edgecolor='black')
plt.xlabel('Hour of Day (UTC)', fontsize=12)
plt.ylabel('Number of Tweets', fontsize=12)
plt.title('Trump Tweets by Hour of Day (UTC, 2009–2018)', fontsize=13)
plt.xticks(hours)
plt.tight_layout()
plt.savefig('tweet_by_hour.png', dpi=150)
print("Extra credit chart saved to tweet_by_hour.png")
