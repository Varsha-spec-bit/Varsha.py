import yfinance as yf

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol] += shares
        else:
            self.stocks[symbol] = shares
        print(f"Added {shares} shares of {symbol}.")

    def remove_stock(self, symbol, shares):
        if symbol in self.stocks and self.stocks[symbol] >= shares:
            self.stocks[symbol] -= shares
            if self.stocks[symbol] == 0:
                del self.stocks[symbol]
            print(f"Removed {shares} shares of {symbol}.")
        else:
            print(f"Insufficient shares of {symbol} to remove.")
    
    def view_portfolio(self):
        print("Current portfolio:")
        for symbol, shares in self.stocks.items():
            current_price = self.get_stock_price(symbol)
            total_value = current_price * shares
            print(f"{symbol}: {shares} shares, Current Price: {current_price:.2f}, Total Value: {total_value:.2f}")

    def get_stock_price(self, symbol):
        stock = yf.Ticker(symbol)
        current_price = stock.history(period='1d')['Close'][0]
        return current_price

# Example usage:
portfolio = Portfolio()
portfolio.add_stock('AAPL', 10)
portfolio.add_stock('GOOGL', 5)
portfolio.view_portfolio()
