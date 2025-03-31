---
title: FurniStyle (Furniture Shop API)
classes: wide
header:
  teaser: https://github.com/user-attachments/assets/c7a11092-0f84-45ef-a700-950090d53861
ribbon: MidnightBlue
categories:
  - Back_End_Projects
toc: true
---


> # Furniture Shop API Using ASP.NET Core Web API

### This backend API powers an e-commerce platform for FurniStyle, enabling secure user authentication, browsing furniture collections, managing orders, and handling inventory. Built with ASP.NET Core Web API, it follows RESTful principles and provides role-based authentication for customers and admins.

---

> # **🔹 Key Features:**

### **1. User Authentication & Role Management**
- **Customer Registration & Login:** Secure authentication using **ASP.NET Identity**.  
- **Role-Based Access Control:**  
  - **Customer:**  Can browse furniture, add items to the cart, and place orders.  
  - **Admin:** Can manage products, categories, and orders. 
- **JWT Authentication:** Secure API access with **JSON Web Tokens (JWT)**.  
- **Profile Management:** Allows customers to update personal details and view order history.  

### **2. Furniture & Inventory Management**
- **Product Browsing:**
  - Customers can filter furniture by **category, price range, and material and availability**.  
- **Product Details:**  
  - Each furniture item has a name, description, images, price, stock status, and category  
- **Inventory Management:**  
  - Admins can **add, update, and remove furniture**.  
  - Stock levels are updated automatically upon order placement.  

### **3. Shopping Cart & Order Management**
- **Shopping Cart System:**
  - Customers can add furniture to their cart, and it persists even after logging out.  
- **Order Placement & Tracking:**  
  - Customers can place orders, view order status, and receive confirmation.
  - Admins can update order status (Processing, Shipped, Delivered).

### **4. Admin Control Panel**
- **Manage Customers:** View, edit, or deactivate accounts.  
- **Manage Products & Categories:** Add, update, or remove furniture and categories.
- **Manage Orders:** View and update order statuses.

### **5. API Performance & Optimization**
- **RESTful API Design:** Ensures scalability and easy integration with web & mobile apps.  
- **Caching Mechanism:** Implements **in-memory caching** to reduce database load and speed up responses.  
- **Efficient Querying:** Uses **EF Core with optimized queries** for faster database interactions.  

### **5. Security Features**
- **JWT-Based Authentication:** Protects API endpoints.  
- **Data Validation & Error Handling:** Ensures clean and structured API responses.  
- **Role-Based Authorization:** Restricts access to **sensitive admin operations**.  

---

> # **🔹 Technologies Used**
- **ASP.NET Core Web API** – Provides a **RESTful API**.  
- **Entity Framework Core** – Handles database interactions.  
- **SQL Server** – Stores student, course, and enrollment data.  
- **ASP.NET Identity** – Manages authentication and roles.  
- **JWT Authentication** – Secures API access.  
- **Caching (In-Memory/Redis)** – Enhances response time.  
- **Clean Architecture** – Ensures maintainability and scalability.  

---

---
> # **🔹 Test The API**
> ### **🔹 Furnitures**
#### **✅ Get All Furnitures**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/AllFurniture
```
#### **✅ Get a Furniture By Id**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/1
```
#### **✅ Order Furnitures By Name Ascending**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/SortingFurnitureByNameAscending?sort=NameAscending
```
#### **✅ Order Furnitures By Name Descending**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/SortingFurnitureByNameDescending?sort=NameDescending
```
#### **✅ Order Furnitures By Price Ascending**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/SortingFurnitureByPriceAscending?sort=PriceAscending
```
#### **✅ Order Furnitures By Price Descending**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/SortingFurnitureByPriceDescending?sort=PriceDescending
```
#### **✅ Order Furnitures By Quantity Ascending**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/SortingFurnitureByQuantityAscending?sort=QuantityAscending
```
#### **✅ Order Furnitures By Quantity Descending**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/SortingFurnitureByQuantityDescending?sort=QuantityDescending
```
#### **✅ Search Furniture By Name**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/SearchFurnitureByName?search=Ergonomic Office Chair 2
```
#### **✅ Get All Furnitures In A Category**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/GetAllFurnisInCategoryByRoomName?category=Tables
```
#### **✅ Get All Furnitures In A Room**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/GetAllFurnisInRoomByRoomName?room=BedRoom
```
#### **✅ Filtering Furnitures Between Two Prices**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/GetAllFurnisBetweenTwoPrices?price1=50&price2=75.5
```
#### **✅ Applying Pagination on Furnitures**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/ApplyingPaginationOnFurnis?pageIndex=2&pageSize=5
```
#### **✅ Get All Furnitures In A Category**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/GetAllFurnisInCategoryByRoomName?category=Tables
```
#### **✅ Get All Furnitures In A Category**
```
[Git]      |     https://furnistyle.runasp.net/api/Furniture/GetAllFurnisInCategoryByRoomName?category=Tables
```
---

This **ASP.NET Core Web API project** provides a **secure, scalable, and high-performance student management system** with **role-based access, caching, and a clean architecture** for future enhancements. 🚀
<br>

<img   alt="Coding" width="600" src="https://github.com/user-attachments/assets/b32d8560-79bf-4c9d-babf-73ecea391761"> <br><br>



> # [Check The Code Out ](https://github.com/HusseinAdel7/FurniStyleAPI)
