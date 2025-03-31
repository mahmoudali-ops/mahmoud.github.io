---
title: FurniStyle (Furniture Shop API)
classes: wide
header:
  teaser: https://github.com/user-attachments/assets/a5f260a6-3946-4d85-825e-5b7a150cd34f
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

### **4. API Performance & Optimization**
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


This **ASP.NET Core Web API project** provides a **secure, scalable, and high-performance student management system** with **role-based access, caching, and a clean architecture** for future enhancements. 🚀
<br>

<img   alt="Coding" width="600" src="https://github.com/user-attachments/assets/9435bec9-6cc8-4343-a772-edb40197f767"> <br><br>
<img   alt="Coding" width="600" src="https://github.com/user-attachments/assets/fa640af0-3add-40d9-bae9-540c6925bfb6"> <br><br>
<img   alt="Coding" width="600" src="https://github.com/user-attachments/assets/95dc1e81-1820-41c3-8ae7-5ab982a3e95a"> <br><br>
<img   alt="Coding" width="600" src="https://github.com/user-attachments/assets/21ec3e8f-438e-4345-aebf-c0c39242dd95"> <br><br>



> # [Check The Code Out ](https://github.com/HusseinAdel7/EduTrack_ASP.NET-Core-API)
