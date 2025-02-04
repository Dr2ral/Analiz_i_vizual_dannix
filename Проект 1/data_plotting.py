import matplotlib.pyplot as plt
import pandas as pd
import plotly
import plotly.express as px




def create_and_save_plot(data, ticker, period, start_date, end_date, style_param=None):
    plt.figure(figsize=(10, 6))

    if style_param:
        plt.style.use(style_param)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['STD'], label='STD')
            plt.plot(dates, data['RSI'].values, label='RSI_14')
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['RSI'].values, label='RSI_14')
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()


    filename = f"{ticker}_{period}_{start_date}-{end_date}_stock_price_chart.png"


    plt.savefig(filename)
    print(f"График сохранен как {filename}")

def creat_interactive_plot(data):
    dates = data.index.to_numpy()
    fig = px.bar(data, x=dates, y='Moving_Average', title='Moving average of Close')
    fig.show()
    return data

