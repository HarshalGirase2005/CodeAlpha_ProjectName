# Stock Portfolio Tracker

# Hardcoded stock prices (USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

portfolio = {}

# Step 1: User input
print("📈 Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not available. Please choose from:", ", ".join(stock_prices.keys()))
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("⚠ Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Step 2: Calculate total investment
total_value = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock} ({qty} shares @ ${price}) = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Step 3 (Optional): Save results to file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = "portfolio.csv"
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            f.write(f"{stock},{qty},{price},{value}\n")
        f.write(f"Total,,,{total_value}\n")
    print(f"✅ Portfolio saved to {filename}")
