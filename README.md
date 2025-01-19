# Sentiment-Analysis-Using-VADER-on-Stock-News
This project performs sentiment analysis on stock-related news articles using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool. It scrapes financial news data, analyzes the sentiment of headlines, and visualizes the results using matplotlib.

#### **Features**
- **Web Scraping**: Retrieves financial news headlines from the Finviz website.
- **Sentiment Analysis**: Uses VADER to calculate sentiment scores (positive, negative, neutral, and compound) for each headline.
- **Visualization**: Outputs bar plots of average compound sentiment scores for specified stock tickers over time.
- **Customizable**: Supports adding new tickers for analysis.

---

#### **How to Use**
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/hemanthreddyaeddulla/Sentiment-Analysis-Using-VADER-on-Stock-News
   ```

2. **Install Dependencies**:  
   Ensure Python is installed, then install the required libraries:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**:  
   Execute the script to scrape data, perform sentiment analysis, and generate visualizations:  
   ```bash
   python vader_sentiment_analysis.py
   ```

4. **View the Output**:  
   The script generates a bar chart (`vader_output.png`) showing the sentiment scores.

---

#### **File Descriptions**
1. **`vader_sentiment_analysis.py`**: The Python script that performs web scraping, sentiment analysis, and visualization.
2. **`vader_output.png`**: A sample output image showing sentiment analysis results.

---

#### **Applications**
- **Investors**: Understand the sentiment trends of financial news for better decision-making.
- **Market Analysts**: Use sentiment insights to complement technical and fundamental analysis.
- **Developers**: Extend the project to include other financial metrics or APIs.

---

#### **Pros**
- Lightweight and quick analysis using pre-trained VADER models.
- Fully automated workflow for scraping, analysis, and visualization.
- Minimal dependencies make it easy to set up and use.

---

#### **Cons**
- Limited to sentiment analysis of headlines; doesn't consider the full article content.
- Relies on Finviz for data, which may change its structure or impose restrictions.
- Sentiment analysis is limited to English-language headlines.

---


### **Output**

The project generates a bar chart (`vader_output.png`) that visualizes the **Average Sentiment Compound Score by Date** for multiple stock tickers (e.g., AMZN, GOOG, META). 

#### **Key Observations from the Output**
1. The **compound score** represents the overall sentiment:
   - **Positive**: Values greater than 0.
   - **Neutral**: Values close to 0.
   - **Negative**: Values less than 0.
2. Sentiment scores are grouped by date and stock ticker, showing trends in news sentiment over time.
3. The chart allows a quick comparison of sentiment trends for different stocks across a range of dates.

---

### **Enhancements for Better Results**

#### **1. Improve Sentiment Analysis:**
   - **Full Article Analysis**: Currently, only headlines are analyzed. Fetching full article content for sentiment analysis would provide a more comprehensive view.
   - **Custom Sentiment Models**: Use advanced models like **BERT** or fine-tuned language models for more accurate domain-specific sentiment analysis.

#### **2. Use Additional Data Sources:**
   - Add APIs like **Google News**, **Yahoo Finance**, or **Alpha Vantage** to fetch more diverse and reliable news data.
   - Incorporate social media platforms like **Twitter** or **Reddit** to analyze public sentiment.

#### **3. Expand Visualization Options:**
   - Use dynamic visualization libraries like **Plotly** or **Dash** for interactive charts.
   - Add line charts or heatmaps to display long-term trends and correlations across multiple tickers.

#### **4. Incorporate Market Data:**
   - Combine sentiment scores with **stock price trends** to identify patterns.
   - Analyze the impact of sentiment changes on stock price movement (e.g., sentiment leading to price spikes or drops).

#### **5. Real-Time Updates:**
   - Set up periodic scraping and sentiment analysis to track real-time sentiment changes.
   - Implement live notifications for significant sentiment shifts.

#### **6. Sentiment Context Analysis:**
   - Identify the specific reasons for positive or negative sentiment using **topic modeling**.
   - Categorize headlines (e.g., earnings reports, product launches, controversies) to understand sentiment drivers.

#### **7. Multi-Language Support:**
   - Expand to analyze news in multiple languages by using models like **Google Translate** or multi-lingual sentiment tools.

#### **8. Historical Analysis:**
   - Add a feature to fetch sentiment data for a longer historical period.
   - Correlate historical sentiment data with market events (e.g., earnings announcements, mergers).

---

#### **Dependencies**
- Python 3.7+
- Libraries:
  - `nltk` (for VADER sentiment analysis)
  - `beautifulsoup4` (for web scraping)
  - `matplotlib` (for visualizing sentiment trends)
  - `pandas` (for data manipulation)

---

By implementing these enhancements, the project can evolve into a more sophisticated sentiment-driven stock analysis tool, offering investors and analysts deeper insights. Let me know if you'd like help with any of these improvements!
