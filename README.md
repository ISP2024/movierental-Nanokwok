## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## 2.1 What refactoring signs (code smells) suggest this refactoring?
The main code smell suggesting this refactoring is Feature Envy.
- The Rental class is using the price_code attribute more than the Movie class.
- The get_price_code method in Movie is primarily used by Rental.
- This indicates that Rental "envies" the price_code feature of Movie.

## 2.2 What design principle suggests this refactoring? Why?
The design principle suggesting this refactoring is the Single Responsibility Principle (SRP).

- Aligns responsibilities: Rental handles all pricing
- Improves cohesion in Rental
- Reduces coupling between Movie and Rental
- Each class has a more focused purpose