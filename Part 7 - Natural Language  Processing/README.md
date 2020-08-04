### Dataset Description
The dataset contains 1000 reviews and the two columns of the dataset are **Review** and **Liked** respectively. <br/>
**Review** - Review of a restaurent. <br/>
**Liked** - This column can contain two values 1 or 0. 1 means that it's a positive review and 0 means a negative review. <br/>

**Note:** The file contains the dataset is in .tsv format meaning the columns are separated by **tabs**. <br/>

**Question**: Do we need a dataset where the columns are separated by a comma or by a tab? <br/>
**Ans**: tab separated dataset is ideal for the machine learning algorithms. The text(reviews) itself might contain commas which is also true in our case. It's way better to take tabs here because when people write reviews, they don't put tabs in the review. That would be very rare. Putting commas in the review is very natural. Besides if you press on tab when someone is writing a review, it will take him/her to next button/input field. So we'll never find a tab in the review which will solve the problem of getting these anomalies due to duplicate delimiters in one specific review. It's recommended to prepare the text dataset with a tab separator to eliminate that kind of problem. <br/>
Another solution if it's needed to use a csv file would be to include some double quotes in the review texts. This might also create problems, in case the original review have some double quotes itself which is also present in our **Restaurent Review.tsv** dataset.

