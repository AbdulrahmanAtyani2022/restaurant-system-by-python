
# 🥙 Restaurant Orders Summary Script  

## 📌 Overview  
This project is a **Python-based reporting tool** that processes multiple text files containing restaurant orders and generates a **daily sales summary**. It automatically distinguishes between **In-Restaurant** and **Takeaway** orders, validates the input format, aggregates item quantities, and outputs a clean summary report both to the terminal and to an `Output.txt` file.  

## ⚙️ Features  
- ✅ Reads all `.txt` files in the current directory  
- ✅ Differentiates between **In-Restaurant** and **Takeaway** orders  
- ✅ Tracks total orders and item quantities (Hummous, Fool, Falafel, Tea, Cola, Water)  
- ✅ Validates order input format and logs invalid entries  
- ✅ Generates a **Daily Sales Summary** with item counts and units  
- ✅ Saves the report to `Output.txt` for record keeping  

## 📂 Input Format  
Each order file must follow this structure:  
```
In
Falafel,2,extra
Tea,1,hot
```
or  
```
Out
Hummous,3,spicy
Cola,2,cold
```

- The **first line** specifies the order type: `In` (In-Restaurant) or `Out` (Takeaway).  
- Each subsequent line contains:  
  - Item name (must match predefined items)  
  - Quantity (integer)  
  - Extra details (ignored in summary but required for format validation)  

## 📊 Output Example  
```
Daily Sales Summary:
--------------------
Total orders: 5
Orders In-Restaurant: 3
    Hummous (dishes): 4
    Fool (dishes): 2
    Falafel (portions): 5
    Tea (cups): 3
    Cola (cans): 1
    Water (bottles): 0

Orders Takeaway: 2
    Hummous (dishes): 2
    Fool (dishes): 0
    Falafel (portions): 1
    Tea (cups): 0
    Cola (cans): 3
    Water (bottles): 1
```


Would you like me to also draft a **short README.md template** with installation instructions and usage steps so you can directly copy it into your GitHub repo?
