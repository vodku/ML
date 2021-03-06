import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def basic_stats_cat(df):
    data_ = []
    for i in df.select_dtypes(include='object').columns:
        data_.append({'Unique Values':list(df[i].unique()),'Number of Unique Values': df[i].nunique(), 'Number of Missing Data': df[i].isnull().sum()})
    df_out = pd.DataFrame(data=data_, columns=['Unique Values', 'Number of Unique Values', 'Number of Missing Data'], index=df.select_dtypes(include='object').columns)
    return df_out

def cat_plot(df, target, plot="boxplot", figsize=(80,30)):
    fig = plt.figure(figsize=figsize)
    for index, i in enumerate(df.select_dtypes(include='object').columns, 1):
        index_ = index%3
        if index_ == 0:
            index_ = 3
        elif index!=1 and index_==1:
            fig = plt.figure(figsize=figsize)   
        ax1 = fig.add_subplot(3,3,index_)
        sns.countplot(data=df, x=i, ax=ax1)
        ax2 = fig.add_subplot(3,3,index_+3)
        _switch_plot(plot, df, i, target, ax2)

def _switch_plot(plot, df, i, target, ax):
    if plot=="boxplot":
        return sns.boxplot(data=df, x=i, y=target, ax=ax)
    elif plot=="violinplot":
        return sns.violinplot(data=df, x=i, y=target, ax=ax)
    elif plot=="swarmplot":
        return sns.swarmplot(data=df, x=i, y =target, color = 'k', alpha = 0.4, ax=ax)
    else:
        return 'Invalid plot name.'

# Source DataCamp
def display_plot(cv_scores, cv_scores_std, alpha_space):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(alpha_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel('Alpha')
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale('log')
    plt.show()