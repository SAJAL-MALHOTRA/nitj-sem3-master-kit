# WEB TECHNOLOGIES (ITDC0205)
## NIT JALANDHAR PYQ MASTER SOLUTION COMPENDIUM & COVERAGE AUDIT
### Fully Solved Examination Papers: End-Sem Exam & Mid-Sem Sept 2025

---

# SECTION 1: 100% SYLLABUS & THEORY COVERAGE AUDIT

| Exam Paper | Q# | Topic / Concept Tested | Covered in Theory Notes |
| :--- | :---: | :--- | :--- |
| **End-Sem Exam** | Q3(b) | Servlet handling GET, POST, PUT, DELETE via `doGet()`, `doPost()`, `doPut()`, `doDelete()` | Unit 6 (§6.1 Java Servlets Lifecycle & HTTP Methods) |
| **End-Sem Exam** | Q4(a) | JavaBeans getters/setters, encapsulation, data integrity, and Bean conventions | Unit 6 (§6.4 JavaBeans & Component Architecture) |
| **End-Sem Exam** | Q4(b) | JDBC MySQL SELECT query with `ResultSet` while loop & 5 core interfaces | Unit 6 (§6.3 Java Database Connectivity JDBC Architecture) |
| **End-Sem Exam** | Q5(a) | JavaScript Event Handling methodology & DOM manipulation example | Unit 3 (§3.7 Event Propagation & Delegation) |
| **End-Sem Exam** | Q5(b) | HTML Contact Form with CSS layout, client-side validation, and JS submission | Unit 1 (§1.6 HTML5 Forms), Unit 3 (§3.6 DOM Manipulation) |
| **Mid-Sem Sept 2025** | Q1(a) | HTML Registration Form with clean semantic layout and styling | Unit 1 (§1.6 HTML5 Forms & Inputs) |
| **Mid-Sem Sept 2025** | Q1(b) | JavaScript Form Validation: Name regex `/^[A-Za-z\s]+$/` & Mobile regex `/^[6-9]\d{9}$/` | Unit 1 (§1.6 Form Validation), Unit 3 (§3.4 JavaScript Strings & Regex) |
| **Mid-Sem Sept 2025** | Q2(a) | Fibonacci sequence in JavaScript with two input/output textboxes and button | Unit 3 (§3.3 JavaScript Functions & Loops) |
| **Mid-Sem Sept 2025** | Q2(b) | HTML Form `method` attribute: GET vs POST in-depth comparative analysis | Unit 1 (§1.5 HTTP/HTTPS Protocol & Methods) |
| **Mid-Sem Sept 2025** | Q3(a) | XML DTD vs XML Schema (XSD): Syntax, Datatypes, Validation, Namespaces | Unit 6 (§6.5 XML Ecosystem, DTD, and Schema) |
| **Mid-Sem Sept 2025** | Q3(b) | `window.alert()`, `window.confirm()`, `window.prompt()` vs `console.log()` | Unit 3 (§3.9 Browser Object Model BOM) |
| **Mid-Sem Sept 2025** | Q4(a) | `getElementById()` vs `getElementsByClassName()` (Element vs HTMLCollection) | Unit 3 (§3.6 DOM Element Selection Methods) |
| **Mid-Sem Sept 2025** | Q4(b) | `let` vs `var` in JavaScript: Scope, Hoisting, Temporal Dead Zone (TDZ) | Unit 3 (§3.2 Execution Context, Scope & Declarations) |
| **Mid-Sem Sept 2025** | Q4(c) | JavaScript Data Types: 7 Primitives vs Non-Primitives with code examples | Unit 3 (§3.2 Primitive vs Reference Types) |
| **Mid-Sem Sept 2025** | Q5(a) | CSS Box Model and `:nth-child(even)` / `:nth-child(odd)` Table Styling | Unit 2 (§2.1 Box Model, §2.2 Selectors & Pseudo-Classes) |
| **Mid-Sem Sept 2025** | Q5(b) | Document Object Model (DOM) tree architecture and hierarchical diagrams | Unit 1 (§1.3 CRP), Unit 3 (§3.6 DOM Architecture) |
| **Mid-Sem Sept 2025** | Q5(c) | Miscellaneous Operators: `typeof`, `delete`, `in`, `instanceof`, Ternary `?:` | Unit 3 (§3.2 JavaScript Operators) |

---

# SECTION 2: PRODUCTION-READY CODE MASTER SOLUTIONS

### 1. Mid-Sem Q1(b): Form Validation (Name & Mobile Number Regex)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Registration Validation</title>
    <script>
        function validateForm(event) {
            event.preventDefault(); // Prevent standard HTTP form submission
            
            const name = document.getElementById("userName").value.trim();
            const mobile = document.getElementById("userMobile").value.trim();

            // Name validation: Only alphabets and spaces allowed
            const namePattern = /^[A-Za-z\s]+$/;
            if (!namePattern.test(name)) {
                alert("INVALID NAME: Name must contain only alphabets and spaces (no digits or special characters).");
                return false;
            }

            // Mobile validation: Exactly 10 digits starting with 6, 7, 8, or 9
            const mobilePattern = /^[6-9]\d{9}$/;
            if (!mobilePattern.test(mobile)) {
                alert("INVALID MOBILE: Mobile Number must be exactly 10 digits and begin with 6, 7, 8, or 9.");
                return false;
            }

            alert("SUCCESS! Both Name and Mobile Number are valid.");
            return true;
        }
    </script>
</head>
<body>
    <h2>User Registration Form</h2>
    <form onsubmit="validateForm(event)">
        <label for="userName">Name:</label><br>
        <input type="text" id="userName" required><br><br>

        <label for="userMobile">Mobile Number:</label><br>
        <input type="text" id="userMobile" required maxlength="10"><br><br>

        <button type="submit">Submit</button>
        <button type="reset">Clear</button>
    </form>
</body>
</html>
```

---

### 2. Mid-Sem Q2(a): Fibonacci Series in Two Textboxes
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fibonacci Generator</title>
    <script>
        function printFibonacci() {
            const inputVal = document.getElementById("numTerms").value;
            const n = parseInt(inputVal, 10);

            if (isNaN(n) || n <= 0) {
                alert("Please enter a positive integer greater than 0.");
                return;
            }

            let fib = [];
            if (n >= 1) fib.push(0);
            if (n >= 2) fib.push(1);

            for (let i = 2; i < n; i++) {
                fib.push(fib[i - 1] + fib[i - 2]);
            }

            document.getElementById("outputSeries").value = fib.join(", ");
        }
    </script>
</head>
<body>
    <h3>Fibonacci Series Generator</h3>
    <label for="numTerms">Enter n (terms):</label>
    <input type="number" id="numTerms" min="1" placeholder="e.g. 10">
    <button type="button" onclick="printFibonacci()">Print</button>
    <br><br>
    <label for="outputSeries">Output Series:</label>
    <input type="text" id="outputSeries" readonly style="width: 450px;">
</body>
</html>
```

---

### 3. End-Sem Q3(b): Java Servlet Handling GET, POST, PUT, DELETE
```java
package com.nitj.web;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/api/resource")
public class RestfulResourceServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // Handles HTTP GET: Read/Retrieve resource
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        resp.setContentType("application/json");
        PrintWriter out = resp.getWriter();
        out.println("{\"status\": \"success\", \"action\": \"GET\", \"message\": \"Fetched resource successfully\"}");
    }

    // Handles HTTP POST: Create new resource
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        resp.setContentType("application/json");
        String name = req.getParameter("name");
        PrintWriter out = resp.getWriter();
        out.println("{\"status\": \"created\", \"action\": \"POST\", \"createdName\": \"" + name + "\"}");
    }

    // Handles HTTP PUT: Update/Replace existing resource
    @Override
    protected void doPut(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        resp.setContentType("application/json");
        // Read body payload for PUT
        StringBuilder sb = new StringBuilder();
        BufferedReader reader = req.getReader();
        String line;
        while ((line = reader.readLine()) != null) sb.append(line);
        
        PrintWriter out = resp.getWriter();
        out.println("{\"status\": \"updated\", \"action\": \"PUT\", \"payloadReceived\": " + sb.toString() + "}");
    }

    // Handles HTTP DELETE: Remove resource
    @Override
    protected void doDelete(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        resp.setContentType("application/json");
        String id = req.getParameter("id");
        PrintWriter out = resp.getWriter();
        out.println("{\"status\": \"deleted\", \"action\": \"DELETE\", \"deletedId\": \"" + id + "\"}");
    }
}
```

---

### 4. End-Sem Q4(b): JDBC MySQL SELECT Query with While Loop
```java
package com.nitj.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class UserRecordsRetriever {
    private static final String URL = "jdbc:mysql://localhost:3306/university_db";
    private static final String USER = "root";
    private static final String PASS = "password123";

    public static void main(String[] args) {
        String sql = "SELECT UserID, Name, Email, Address FROM UserRecords";

        // Using try-with-resources for automatic resource deallocation
        try (Connection conn = DriverManager.getConnection(URL, USER, PASS);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            System.out.println("----------------------------------------------------------------------------------");
            System.out.printf("%-10s %-20s %-30s %-20s%n", "UserID", "Name", "Email", "Address");
            System.out.println("----------------------------------------------------------------------------------");

            // While loop iterating through ResultSet
            while (rs.next()) {
                int userId = rs.getInt("UserID");
                String name = rs.getString("Name");
                String email = rs.getString("Email");
                String address = rs.getString("Address");

                System.out.printf("%-10d %-20s %-30s %-20s%n", userId, name, email, address);
            }
            System.out.println("----------------------------------------------------------------------------------");
        } catch (SQLException e) {
            System.err.println("Database Access Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```
* **5 Core JDBC Classes/Interfaces Used**:
  1. `java.sql.DriverManager`: Factory class for managing database driver implementations and establishing physical connections.
  2. `java.sql.Connection`: Session interface representing the physical network connection socket to the DBMS.
  3. `java.sql.Statement`: Interface used for executing static SQL statements and returning generated results.
  4. `java.sql.ResultSet`: Cursor interface maintaining a tabular cursor pointing to one row of data at a time.
  5. `java.sql.SQLException`: Root exception class providing database access error information, SQLState codes, and vendor-specific error codes.
