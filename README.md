# StocksEmotions - Financial Machine Learning Project

## Overview
StocksEmotions is a comprehensive machine learning project that integrates sentiment analysis on financial news to inform trading strategies. This project explores the intersection of large language models, sentiment analysis, and quantitative finance to create innovative trading strategies.

## Components
- `Colab_Finbert.ipynb`: Implementation of the FinBERT model for sentiment analysis.
- `Colab_Roberta.ipynb`: Implementation of the RoBERTa model for sentiment analysis.
- `data_processing.ipynb`: Notebook for processing and cleaning financial news data.
- `momentum_trading_strategy.ipynb`: Notebook illustrating momentum trading strategies based on MACD and RSI indicators.
- `news_trading_strategy.ipynb`: Notebook demonstrating trading strategies informed by news sentiment.
- `text_to_binary.ipynb`: A notebook converting text data to a binary format for analysis.
- `text_to_text_model.ipynb`: Implementation of Text-to-Text models like T5 for sentiment analysis.

## Project Report
Our project report, `Financial_Machine_Learning_project.pdf`, details the methodology, models used, trading strategies, and comprehensive analysis of results. 

## Motivation
The aim of this project is to leverage advanced machine learning models to decode market sentiments from financial news and assess their impact on trading strategies.

## Dataset
Our dataset comprises financial news articles obtained from various online sources, with the Financial Times being a primary contributor. The data was meticulously cleaned and processed to serve as input for sentiment analysis models.

## Models
We benchmarked traditional text representation methods against advanced models like BERT and RoBERTa, fine-tuned on financial texts.

## Trading Strategies
The project evaluates several trading strategies, including:
- MACD and RSI based strategies
- News sentiment-based strategies (Max Count, Highest Score, Threshold)
- Combined strategies that integrate news sentiment with momentum indicators (MACD and RSI)

## Results
Our analysis demonstrated that sentiment-informed strategies, particularly those that combine news sentiment with traditional momentum indicators, significantly impact trading outcomes.

## Conclusion
Incorporating news sentiment into trading strategies can enhance performance metrics. The project provides insights into the effectiveness of various strategy combinations and the potential of sentiment analysis as a directional signal in trading.

## Further Research
The exploration of Text-to-Text models like T5 for sentiment analysis shows promise, with potential for further improvement and fine-tuning.

## How to Use
Each Jupyter notebook in the repository is self-contained and includes comments to guide you through the processes of data handling, model training, and strategy testing.

## Authors
- Romain Berquet
- Antoine Munier

## Acknowledgements
This project was conducted as part of the FIN-423 course at École Polytechnique Fédérale de Lausanne (EPFL).

---

For more details on methodology, model performances, and trading strategy results, please refer to our detailed project report.
