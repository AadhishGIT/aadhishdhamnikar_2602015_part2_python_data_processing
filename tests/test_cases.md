# Test Cases

## TC01 - Valid Record

Input:
Valid order

Expected:
Record accepted

Reason:
All validations pass

---

## TC02 - Duplicate Order ID

Input:
O001 repeated

Expected:
Rejected

Reason:
Duplicate order ID

---

## TC03 - Missing Customer Name

Input:
Blank customer name

Expected:
Rejected

Reason:
Missing customer name

---

## TC04 - Missing City

Input:
Blank city

Expected:
Rejected

Reason:
Missing city

---

## TC05 - Quantity Zero

Input:
Quantity = 0

Expected:
Rejected

Reason:
Invalid quantity

---

## TC06 - Negative Quantity

Input:
Quantity = -2

Expected:
Rejected

Reason:
Invalid quantity

---

## TC07 - Invalid Product ID

Input:
P999

Expected:
Rejected

Reason:
Product ID not found

---

## TC08 - Invalid Payment Method

Input:
Cheque

Expected:
Rejected

Reason:
Invalid payment method

---

## TC09 - Invalid Order Status

Input:
Shipped

Expected:
Rejected

Reason:
Invalid order status

---

## TC10 - Invalid Date Format

Input:
20-02-2025

Expected:
Rejected

Reason:
Invalid date format

---

## TC11 - Unit Price Mismatch

Input:
45000 instead of 50000

Expected:
Rejected

Reason:
Unit price mismatch

---

## TC12 - Revenue Calculation

Input:
Quantity 2 × Unit Price 20000

Expected:
Total Amount = 40000

Reason:
Correct calculation

---

## TC13 - Rejection Reason Generation

Input:
Multiple invalid fields

Expected:
All rejection reasons listed

Reason:
Assignment requirement
