import pandas as pd
import re

df = pd.read_csv('data/news.csv')

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_ftcom_and_after(text):
    index = text.find("FT.com")
    return text[:index] if index != -1 else text

def remove_source_and_after(text) : 
    index  = text.find("Source:")
    return text[:index] if index != -1 else text

df.dropna(subset=['text'], inplace=True)

# Filter the DataFrame using .str.contains()
financial_times_news_df = df[df['text'].str.contains('Financial Times')]
#Remove html tags
financial_times_news_copy_df = financial_times_news_df.copy()
financial_times_news_copy_df['text'] = financial_times_news_copy_df['text'].apply(remove_html_tags)

#Remove FT.com and after
financial_times_news_copy_df['text'] = financial_times_news_copy_df['text'].apply(remove_ftcom_and_after)

#Remove Source: and after
financial_times_news_copy_df['text'] = financial_times_news_copy_df['text'].apply(remove_source_and_after)

#Remove &#xa0; and replace with space
financial_times_news_copy_df['text'] = financial_times_news_copy_df['text'].str.replace('&#xa0;', ' ')

#Remove "Follow @FT" and after
financial_times_news_copy_df['text'] = financial_times_news_copy_df['text'].apply(lambda x: x.split("Follow @FT")[0])

#Remove rows with "Please sign up here
financial_times_news_copy_df = financial_times_news_copy_df[financial_times_news_copy_df['text'] != "Please sign up here"]

#Keep rows that contain "FT"
financial_times_news_copy_df = financial_times_news_copy_df[financial_times_news_copy_df['text'].str.contains('FT')]

df.update(financial_times_news_copy_df)

df.to_csv('data/news_cleaned.csv', index=False)