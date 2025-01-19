from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Finviz URL and tickers
finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AMZN', 'GOOG', 'TSLA']

news_data = {}

# Fetch news for each ticker
for ticker in tickers:
    url = finviz_url + ticker
    req = Request(url=url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})
    
    response = urlopen(req)
    html = BeautifulSoup(response, 'html.parser')  # Use 'html.parser' for parsing
    
    news_table = html.find(id='news-table')
    
    if news_table:  # Only process if the news table is found
        news_data[ticker] = news_table
    else:
        print(f"News table not found for {ticker}")

# Parse the data
parsed_data = []

for ticker, news_table in news_data.items():  # Use 'news_data' dictionary
    rows = news_table.findAll('tr')
    previous_date = None  # To handle rows with only time
    
    for row in rows:
        # Get the title
        title = row.a.text if row.a else 'No Title'
        
        # Get the date and time
        date_time = row.td.text.strip()
        date_time_split = date_time.split(' ')
        
        if len(date_time_split) == 1:  # Only time provided, reuse previous date
            time = date_time_split[0]
            date = previous_date  # Use the last known date
        else:  # Both date and time provided
            date = date_time_split[0]
            time = date_time_split[1]
            
            # Handle "Today" and "Yesterday"
            if date.lower() == "today":
                date = datetime.now().strftime('%Y-%m-%d')
            elif date.lower() == "yesterday":
                date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
            else:
                try:
                    date = pd.to_datetime(date).strftime('%Y-%m-%d')  # Standard date format
                except Exception as e:
                    print(f"Date parsing error for {date}: {e}")
                    date = None
            
            previous_date = date  # Update the previous date
        
        parsed_data.append([ticker, date, time, title])

# Create DataFrame
df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])
df = df.dropna(subset=['date'])  # Drop rows with invalid dates

# Sentiment Analysis
vader = SentimentIntensityAnalyzer()
df['compound'] = df['title'].apply(lambda title: vader.polarity_scores(title)['compound'])

print("Sample Data:")
print(df.head())

# Data Visualization
df['date'] = pd.to_datetime(df.date).dt.date

plt.figure(figsize=(10, 8))

# # Select only numeric columns for aggregation
numeric_df = df[['ticker', 'date', 'compound']]

# # Group by 'ticker' and 'date', and calculate mean
mean_df = numeric_df.groupby(['ticker', 'date']).mean()

# # Unstack and transpose the DataFrame for plotting
mean_df = mean_df.unstack()
mean_df = mean_df.xs('compound', axis="columns").transpose()

# # Plot the data
mean_df.plot(kind='bar')
plt.title('Average Sentiment Compound Score by Date')
plt.xlabel('Date')
plt.ylabel('Average Compound Score')
plt.legend(title='Ticker')
plt.show()


# one_month_ago = datetime.now().date() - timedelta(days=30)
# df_last_month = df[df['date'] >= one_month_ago]

# # Data Visualization
# plt.figure(figsize=(10, 8))

# # Select only numeric columns for aggregation
# numeric_df_last_month = df_last_month[['ticker', 'date', 'compound']]

# # Group by 'ticker' and 'date', and calculate mean
# mean_df_last_month = numeric_df_last_month.groupby(['ticker', 'date']).mean()

# # Unstack and transpose the DataFrame for plotting
# mean_df_last_month = mean_df_last_month.unstack()
# mean_df_last_month = mean_df_last_month.xs('compound', axis="columns").transpose()

# # Plot the data
# mean_df_last_month.plot(kind='bar')
# plt.title('Average Sentiment Compound Score by Date (Last 1 Month)')
# plt.xlabel('Date')
# plt.ylabel('Average Compound Score')
# plt.legend(title='Ticker')
# plt.show()