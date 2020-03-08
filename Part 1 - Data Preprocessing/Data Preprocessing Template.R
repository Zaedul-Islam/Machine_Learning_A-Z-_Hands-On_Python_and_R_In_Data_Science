# Data Preprocessing

# Importing the dataset
dataset = read.csv("E:/WORKSTATION/Machine Learning Training/Machine Learning A-ZT Hands-On Python and R In Data Science/Part 1 - Data Preprocessing/Dataset/Data.csv") 

# Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)
