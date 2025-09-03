# 🛒 E-Commerce Order Insights (v1: Basic Data Structures)

## 📌 Project Overview
This is a **menu-driven mini analytics system** for managing and analyzing e-commerce orders.  
It was built **only with Python fundamentals** (lists, dictionaries, sets, tuples, and loops) — no functions, OOP, or file handling yet.  

The goal: to show how even with the basics, we can simulate real-world analytics dashboards used by businesses.  

---

## 🎯 Features
- ✅ Add new orders dynamically  
- ✅ Display all orders in a well-formatted table  
- ✅ Update order details (product, price, quantity, category, discount)  
- ✅ Remove orders by ID  
- ✅ Input validation (avoids crashes on wrong input)  
- ✅ **Revenue analysis** → total & average revenue  
- ✅ **Best-selling product** by revenue  
- ✅ **Category-wise revenue breakdown**  
- ✅ **Basket analysis** → avg. basket size & product frequency  
- ✅ **Discount simulation** → revenue loss & % impact  

---

## 📂 Data Structure
Each order is stored as a dictionary, and all orders are kept in a list:

```python
order = {
    "id": 101,
    "product": "iPhone 15",
    "category": "Electronics",
    "price": 80000,
    "qty": 2,
    "discount": 10
}

```

This allowed me to practice CRUD operations (Create, Read, Update, Delete) on dictionaries inside lists.

## 🖼️ Sample Menu

```python
========= E-Commerce Order Insights =========
1. Add Order
2. Display Orders
3. Update Order
4. Remove Order
5. Revenue Analysis
6. Best-Selling Product
7. Category-wise Revenue
8. Basket Analysis
9. Discount Simulation
10. Exit
=============================================

```
---

## 📊 Example Insights
- Total Revenue: ₹2,50,000
- Average Revenue per Order: ₹31,250
- Best-Selling Product: iPhone 15 (₹1,60,000 revenue)
- Category-wise Revenue: Electronics → ₹2,10,000 | Fashion → ₹40,000
- Average Basket Size: 1.8 items/order
- Discount Simulation (10%): Revenue Drop = 12.5%

## 🚀 Learning Outcomes
- Strengthened knowledge of lists, dictionaries, sets, tuples
- Practiced real-world DS/AI-style analytics with only fundamentals
- Improved input validation & user-friendly design
- Gained confidence before moving into functions, OOP, and file handling

## 📌 Next Steps
- Add file handling to save/load orders
- Refactor with functions for cleaner code
- Add data visualization (matplotlib, seaborn)
- Extend into ML tasks → sales forecasting, product recommendations
