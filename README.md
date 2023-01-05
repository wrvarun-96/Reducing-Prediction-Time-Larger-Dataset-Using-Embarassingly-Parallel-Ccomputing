# Reducing-Prediction-Time-Larger-Dataset-Using-Embarassingly-Parallel-Computing

## Overview
With the use of large sizes, dataset time has always been a crunch. This study investigates the use of multiprocessing and how we can reduce the time for large datasets. So for that, we have taken a dataset where we will be predicting the genres of the books. We will be using built-in parallel processing for training the model and comparing it with others. With new data, we will be using embarrassingly parallel computing to predict, and then we will be comparing with serial processes. We will be implementing this process with the help of a supercomputer. Results tell us that training the model in parallel reduced the time. Similarly, prediction time has been reduced with the use of embarrassingly parallel computing. Varied the dataset size for multiple cores and recorded the time.
Overall, parallel computing can be a useful tool for speeding up the processing of large datasets. By distributing the workload across multiple processes, you can potentially reduce the amount of time it takes to process the data and take advantage of the multiple cores on your computer.

## Problem Statement
The project focuses on the embarrassing parallel computing used for large datasets. One potential problem that you might face when working with large datasets is that the processing time can be slow. The burden might be distributed among several processes or machines using multi-processing or parallel processing to solve this issue, potentially reducing the processing time. The methodology will use parallel computing, evaluate performance, and compare results with serial computing.
Firstly, we will train a machine learning algorithm. Then we send the new data to the trained model using parallel computing, which involves utilising the various cores on the system by using multi- processing or parallel processing, which could shorten the time it takes to predict the data.
Compare the performance of parallel computing with serial computing. We will do a few experiments and record the time required. After that, we'll examine these tests' outcomes and discuss the importance of what we learn.

## Architecture

![alt text](images/Arc.png)

## Methodology

The following steps comprise the methodology for employing embarrassingly parallel computing:
### Processes in Step1:
1. Data has been imported, which is in CSV format. The data contained 100k rows and ten columns.
2. Preprocessing has been done by filtering the unwanted features. At last, we are settled on four features. The features are - ‘author_id’, ‘book_rating’, ‘publish_year’, and ‘text_lang’, and the target column is ‘book_genre’. A standard scaler is used to make the mean 0.
3. A random forest classifier is selected. Model training is done in parallel. Training time has been recorded for both with one core and eight cores. This will be shown in the later part of this report.
### Processes in Step2:
1. We are supplying the trained model with the same set of data. Data will be transmitted in parallel, and very quickly, predictions for the entire dataset will be generated.
2. Compare the overall performance of the parallelised with that of a non-parallelised code. This could involve running equal experiments with a non-parallelised code and evaluating the outcomes to the ones acquired with the parallelised code.
This technique offers a general framework for enforcing embarrassingly parallel computing on a large dataset and may be tailored to many datasets.

## Result
Training time:

Using 1 core : 12.488 sec.
Using 8 cores : 2.84 sec

Below screenshots shows the training using 1 core and 8 cores.
![alt text](images/train.png)


