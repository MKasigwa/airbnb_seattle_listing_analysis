import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## A look at the data
#Check rows and columns function
def check_rows_cols(num_rows, num_cols):
    '''
    INPUT:
    num_rows - int the number of rows in dataframe
    num_cols - int the number of columns in dataframe

    This function will print a the number of rows and columns from the dataframe.
    '''
    print("There are {} rows in the dataset!".format(num_rows))
    print("There are {} columns in the dataset!".format(num_cols))

## Import data 
def import_data(data_path):
    '''
    Returns churn dataframe for the csv found at data_path
    INPUT:
    data_path - string the path to the csv file
    OUTPUT:
    df_listing : processed pandas dataframe of input csv file
    '''
    df = pd.read_csv(data_path)
    return df

## Barplot
def generate_barplot(data_frame,column_name):
    '''
    This function provide the counts for the each series in a column and plot it in bar plot from the df
    INPUT:
    data_frame
    colun_name - string
    OUTPUT:
    Plot bar of value counts
    '''
    vals = data_frame[column_name].value_counts()
    (vals/data_frame.shape[0].plot(kind="bar"))
    plt.title(column_name)