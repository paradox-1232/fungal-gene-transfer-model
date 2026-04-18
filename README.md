# Fungal Gene Transfer Model  
**Comparative analysis under different gene transfer probabilities**

## Overview
This project presents a simple agent-based simulation of horizontal gene transfer in a structured fungal-like network. The model explores how genetic elements spread through local interactions between neighboring units over time.

## Biological Motivation
Horizontal gene transfer plays a critical role in the evolution of microbial and fungal systems. Understanding how genes propagate in spatially structured networks provides insights into pathogen evolution, adaptation, and persistence in both natural and agricultural environments.

## Model Description
- The system is represented as a 2D grid where each cell corresponds to a fungal unit.
- Each unit can either contain (1) or lack (0) a specific gene.
- At each time step, gene transfer occurs between neighboring cells with a defined probability.
- The simulation tracks how gene frequency changes over time.

## Results
The model demonstrates how local interactions drive the spread of genetic material across the network. The outputs include:
- Temporal dynamics of gene spread
- Visualization of gene frequency increase
- Comparative analysis under different gene transfer probabilities

## Tools & Technologies
- Python
- NumPy
- Matplotlib

## Future Improvements
- Incorporating fungal network growth dynamics
- Adding stochastic environmental effects
- Extending to network-based (graph) structures
- Exploring additional evolutionary parameters

## Author
Irshad Ullah
