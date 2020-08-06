### Business Problem Description
The dataset contains the written reviews of restaurants. Our mission is to make some machine learning models that will predict if the review is positive or negative. This is simple for NLP. But the algorithm in this part will be very well applicable to other kinds of text even when the purpose is very different. We should be able to do the followings as well,
1. Apply on books, for example, to predict the genre of a book (i.e., whether the book is a thriller/a comedy/a romance)
2. Apply on HTML webpages to do whatever kind of analysis 
3. Apply on newspaper to predict in which category an article belongs to <br/>

We'll make a general model that you'll be able to apply to most of the texts.

### Dataset Description
The dataset contains 1000 reviews and the two columns of the dataset are **Review** and **Liked** respectively. <br/>
**Review** - Review of a restaurent. <br/>
**Liked** - This column can contain two values 1 or 0. 1 means that it's a positive review and 0 means a negative review. <br/>

**Note:** The file contains the dataset is in .tsv format meaning the columns are separated by **tabs**. <br/>

**Question**: Do we need a dataset where the columns are separated by a comma or by a tab? <br/>
**Ans**: tab separated dataset is ideal for the machine learning algorithms. The text(reviews) itself might contain commas which is also true in our case. It's way better to take tabs here because when people write reviews, they don't put tabs in the review. That would be very rare. Putting commas in the review is very natural. Besides if you press on tab when someone is writing a review, it will take him/her to next button/input field. So we'll never find a tab in the review which will solve the problem of getting these anomalies due to duplicate delimiters in one specific review. It's recommended to prepare the text dataset with a tab separator to eliminate that kind of problem. <br/>
Another solution if it's needed to use a csv file would be to include some double quotes in the review texts. This might also create problems, in case the original review have some double quotes itself which is also present in our **Restaurent Review.tsv** dataset.

