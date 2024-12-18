import yfinance as yf
import csv
import pandas as pd


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """Вычисляет и выводит среднюю цену закрытия акций за заданный период."""
    print(data['Close'].mean(axis=0))


def notify_if_strong_fluctuations(data, threshold=2):
    """Анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.
        """
    aver_price = data['Close'].mean(axis=0)
    difference = data['Close'].max() - data['Close'].min()
    res_percent = difference / (aver_price / 100)
    if res_percent > threshold:
        print(f'Цена акции колеблется более чем {threshold}%')



def export_data_to_csv(data, filename):
    '''Функция принимает DataFrame и название файла затем экспортирует данные в csv-файл'''
    df = pd.DataFrame(data)
    df.to_csv(filename)

