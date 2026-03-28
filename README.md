# GreenRoute Optimizer
**Building AI course project**

## Summary
GreenRoute is an AI-driven logistics tool designed for small urban delivery businesses. It predicts the most fuel-efficient delivery routes by analyzing historical traffic density, vehicle load weights, and road gradients, moving beyond simple distance-based optimization.

## Background
Standard GPS systems optimize for the shortest time or distance. However, a route that is 2km shorter but involves heavy stop-and-go traffic or steep inclines can consume up to 30% more fuel.
* **Problem 1:** High operational costs for small local couriers.
* **Problem 2:** Unnecessary CO2 emissions from inefficient routing.
* **Motivation:** To provide small businesses with enterprise-level sustainability tools.

## How is it used?
The solution is a dispatcher dashboard and a driver mobile app. 
1. The driver enters the delivery stops and the current payload weight.
2. The AI calculates the "Green Score" for multiple route options.
3. The driver is guided through the route with the lowest predicted fuel consumption.

## Data Sources and AI Methods
* **Data:** OpenStreetMap for road gradients, public city traffic datasets, and historical fuel consumption logs.
* **AI Techniques:** * **Linear Regression:** Used to calculate the relationship between vehicle weight/incline and fuel burn.
    * **K-Nearest Neighbors (KNN):** Used to classify traffic patterns based on similar historical days.

## Challenges
* Real-time accident reporting (requires integration with live APIs like Waze).
* Ethical consideration: Avoiding "quiet" residential streets to prevent noise pollution.

## What next?
The project could evolve into a Reinforcement Learning model where the AI learns from every trip to improve its accuracy.

## Acknowledgments
* Inspired by the Elements of AI / Building AI course.
* Map data provided by OpenStreetMap contributors.
