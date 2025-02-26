---
title: EduTrack (Student Management System API)
classes: wide
header:
  teaser: https://github.com/user-attachments/assets/5b5dfc71-b6f2-4b0b-8295-3d32d1a5a43e
ribbon: MidnightBlue
categories:
  - Back_End_Projects
toc: true
---


> # Student Management System Using ASP.NET Core Web API

### This backend API provides a comprehensive student and course management system, enabling secure student registration, course browsing, and enrollment. It follows RESTful API principles with role-based authentication to ensure efficient and secure access for both students and administrators.

---

> # **🔹 Key Features:**

### **1. User Authentication & Role Management**
- **Student Registration & Login:** Secure authentication using **ASP.NET Identity**.  
- **Role-Based Access Control:**  
  - **Student:** Can browse courses, add courses to cart, and enroll.  
  - **Admin:** Can manage students, courses, and departments.  
- **JWT Authentication:** Secure API access with **JSON Web Tokens (JWT)**.  
- **Profile Management:** Allows students to update personal details and change passwords.  

### **2. Course & Enrollment Management**
- **Course Browsing:** Students can filter courses by **department, availability, and difficulty level**.  
- **Shopping Cart for Courses:**  
  - Students can **add courses** to a cart before enrollment.  
  The cart persists even after logging out.  
- **Enrollment Management:**  
  - Students can **enroll in selected courses** from the cart.  
  - Admins can **approve or reject enrollments**.  

### **3. Admin Control Panel**
- **Manage Students:** View, edit, or deactivate student accounts.  
- **Manage Courses:** Add, update, or remove courses.  
- **Manage Departments:** Organize courses into departments.  

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
