#!/usr/bin/env python3

"""
This modules contains helpers functions
"""
import numpy as np
import matplotlib.pyplot as plt

def simple_plot(y:np.array):
    """
    This function plot a simple red plot
    Args:
        y:np.array 
    """
    y_coord = [0, 500, 1000]
    plt.plot(y, color="red")
    plt.yticks(y_coord)

def change_scale(x:np.array,y:np.array):
    """
    This function plots x and y
    Args:
        x:np.array representing the x-coordinates
        y:np.array representing the y-coordinates
    """
    plt.plot(x, y)
    plt.yscale("log")
    plt.xlim(0, 28650)
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of C-14")

def scatter_plot(x:np.array, y:np.array):
    """
    This function plot a scatter plot
    Args:
        x:np.array x-coordinates
        y:np.array y-coordinates
    """
    plt.scatter(x, y, marker="o", color="magenta")
    plt.ylabel("Weight (lbs)")
    plt.xlabel("Height (in)")
    plt.title("Men's Height vs Weight")

def plot_2_lines(x:np.array,y1:np.array,y2:np.array):
    """
    plot two lines
    Args:
        x:np.array x-coordinates
        y1:np.array first y-coordinates
        y2:np.array second y-coordinates
    """
    plt.plot(x, y1, "r--", label="C-14")
    plt.plot(x, y2, "darkgreen", label="Ra-226")

    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of Radioactive Elements")
    plt.ylim(0.0, 1.0)
    plt.yticks([0.0, 0.5, 1.0])
    plt.xlim(0, 20000)

    plt.legend()

def plot_frequency(x:np.array):
    """
    Plot histogram showing frequency
    Args:
        x:np.array x-coordinates
    """
    plt.hist(x, bins=10, edgecolor="black", linewidth=2.0)
    plt.title("Project A")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.xlim(0, 100)
    plt.ylim(0, 30)
