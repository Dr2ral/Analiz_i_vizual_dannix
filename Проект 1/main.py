
import data_download as dd
import data_plotting as dplt
from data_download import *


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    start_date = input('Введите начальную дату (например гггг-мм-дд):')
    end_date = input('Введите конечную дату (например гггг-мм-дд):')
    style_param = input('Введите название стиля (например (classic, ggplot):')

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period, start_date, end_date)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    #Добавление RSI
    rsi(stock_data, 14)

    # Реализация функции статистического индикатора (стандартного отклонения цены закрытия)
    std_dev(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, start_date, end_date, style_param)

    # Вычисляет среднее значение 'Close' и выводит в консоль
    calculate_and_display_average_price(stock_data)

    # Выводит в консоль уведомление о сильных колебаниях
    threshold = int(input())
    notify_if_strong_fluctuations(stock_data, threshold)

    # Экспортирует данные в файл в CSV формате
    filename = 'df.csv'
    export_data_to_csv(stock_data, filename)










if __name__ == "__main__":
    main()
