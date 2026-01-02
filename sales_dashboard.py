import tkinter as tk
from tkinter import ttk
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

products = []
quantities = []
totals = []

def load_data():
    products.clear()
    quantities.clear()
    totals.clear()

    with open("sales.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            products.append(row[0])
            quantities.append(int(row[2]))
            totals.append(float(row[3]))

def show_dashboard():
    load_data()

    dashboard = tk.Toplevel(root)
    dashboard.title("Sales Dashboard")
    dashboard.geometry("900x600")

    # ----- Summary -----
    total_revenue = sum(totals)
    best_product = products[quantities.index(max(quantities))]

    summary = tk.Label(
        dashboard,
        text=f"Total Revenue: ₹{total_revenue}\nBest Selling Product: {best_product}",
        font=("Arial", 14, "bold")
    )
    summary.pack(pady=10)

    # ----- Charts -----
    fig, ax = plt.subplots(1, 2, figsize=(9, 4))

    # Bar Chart
    ax[0].bar(products, totals)
    ax[0].set_title("Revenue by Product")
    ax[0].set_xlabel("Product")
    ax[0].set_ylabel("Revenue")

    # Pie Chart
    ax[1].pie(totals, labels=products, autopct="%1.1f%%")
    ax[1].set_title("Sales Distribution")

    canvas = FigureCanvasTkAgg(fig, master=dashboard)
    canvas.draw()
    canvas.get_tk_widget().pack()

# ----- Main Window -----
root = tk.Tk()
root.title("Sales Management System")
root.geometry("400x300")

title = tk.Label(root, text="Sales Management Dashboard", font=("Arial", 16, "bold"))
title.pack(pady=30)

btn = ttk.Button(root, text="Open Dashboard", command=show_dashboard)
btn.pack()

root.mainloop()
