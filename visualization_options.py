import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class VisualizationOptions:
    def __init__(self, data):
        self.data = data

    def get_color_choice(self):
        print("\nAvailable Colors: red, blue, green, purple, orange, brown, pink, gray, yellow, cyan")
        color = input("Enter your desired color: ").lower()
        label = input("Enter what this color represents: ")
        return color, label

    def scatterplot(self, x_col, y_col):
        color, label = self.get_color_choice()
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x=x_col, y=y_col, color=color)
        plt.title(f'Scatterplot of {y_col} vs {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(f'{y_col} ({label})')
        plt.show()

    def boxplot(self, x_col, y_col):
        color, label = self.get_color_choice()
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.data, x=x_col, y=y_col, color=color)
        plt.title(f'Boxplot of {y_col} by {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(f'{y_col} ({label})')
        plt.show()

    def pairplot(self, columns):
        sns.pairplot(self.data[columns], hue=columns[0])  # Using the first column as hue by default
        plt.title('Pairplot for Selected Columns')
        plt.show()

    def heatmap(self, columns):
        plt.figure(figsize=(12, 8))
        sns.heatmap(self.data[columns].corr(), annot=True, cmap='coolwarm')
        plt.title('Heatmap of Correlations')
        plt.show()

    def select_columns(self):
        print("\nAvailable columns:")
        for i, column in enumerate(self.data.columns, 1):
            print(f"{i}. {column}")
        
        selected_indices = input("Enter the numbers of columns to visualize (comma-separated): ")
        selected_indices = [int(i.strip()) - 1 for i in selected_indices.split(",")]
        selected_columns = [self.data.columns[i] for i in selected_indices if i in range(len(self.data.columns))]
        return selected_columns

    def run_visualization(self):
        print("\nVisualization Options:")
        print("1. Scatterplot")
        print("2. Boxplot")
        print("3. Pairplot")
        print("4. Heatmap")
        choice = input("Choose the type of visualization (1-4): ")

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please try again.")
            return

        columns = self.select_columns()
        if not columns:
            print("No valid columns selected. Please try again.")
            return

        if choice == "1":
            self.scatterplot(columns[0], columns[1] if len(columns) > 1 else columns[0])
        elif choice == "2":
            self.boxplot(columns[0], columns[1] if len(columns) > 1 else columns[0])
        elif choice == "3":
            self.pairplot(columns)
        elif choice == "4":
            self.heatmap(columns)
