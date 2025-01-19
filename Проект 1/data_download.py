import pandas as pd
import yfinance as yf



def fetch_stock_data(ticker, period=None, start_date=None, end_date=None):
    stock = yf.Ticker(ticker)
    if period:
        data = stock.history(period=period)
    elif start_date and end_date:
        data = stock.history(start=start_date, end=end_date)
    else:
        data = stock.history(period='1mo')
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def std_dev(data, window_size=5):
    data['STD'] = data['Close'].rolling(window=window_size, closed='left').std()

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


def rsi(data, periods=14, ema=True):
    """
    Возвращает pd.Series с индексом относительной силы.
    """
    close_delta = data['Close'].diff()
    # Делаем две серий: одну для низких закрытий и одну для высоких закрытий
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    if ema == True:
        # Использование экспоненциальной скользящей средней
        ma_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
        ma_down = down.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
    else:
        # Использование простой скользящей средней
        ma_up = up.rolling(window=periods, adjust=False).mean()
        ma_down = down.rolling(window=periods, adjust=False).mean()

    rs = ma_up / ma_down
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    return data





