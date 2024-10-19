# import seaborn as sns
# import matplotlib.pyplot as plt
# from data_analysis import DataAnalysis
# class Visualization:
#     def __init__(self, data):
#         self.data = data
    
#     def show_boxplot(self, columns):
#         for column in columns:
#             plt.figure(figsize=(10, 5))
#             sns.boxplot(x=self.data[column])
#             plt.title(f'Boxplot for {column}')
#             plt.show()
#             input("Press Enter to view the next plot...")

#     def show_scatterplot(self, columns):
#         for column in columns:
#             plt.figure(figsize=(10, 5))
#             sns.scatterplot(x=self.data.index, y=self.data[column])
#             plt.title(f'Scatterplot for {column}')
#             plt.show()
#             input("Press Enter to view the next plot...")

#     def select_columns(self):
#         available_columns = self.data.select_dtypes(include=["float", "int"]).columns
#         print("\nAvailable numerical columns:")
#         for i, column in enumerate(available_columns, 1):
#             print(f"{i}. {column}")
        
#         selected_indices = input("Enter the numbers of columns to visualize (comma-separated): ")
#         selected_indices = [int(i.strip()) - 1 for i in selected_indices.split(",")]
        
#         selected_columns = [available_columns[i] for i in selected_indices if i in range(len(available_columns))]
#         return selected_columns

#     # def visualizeMain(self):
#     #     print("\nVisualization Options:")
#     #     print("1. Boxplot")
#     #     print("2. Scatterplot")
#     #     plot_choice = input("Choose the type of plot (1 or 2): ")

#     #     if plot_choice not in ["1", "2"]:
#     #         print("Invalid choice! Please try again.")
#     #         return

#     #     print("\n1. Visualize all columns")
#     #     print("2. Visualize selected columns")
#     #     column_choice = input("Do you want to visualize all columns or only selected ones? (1 or 2): ")

#     #     if column_choice == "1":
#     #         columns = self.data.select_dtypes(include=["float", "int"]).columns
#     #     elif column_choice == "2":
#     #         columns = self.select_columns()
#     #         if not columns:
#     #             print("No valid columns selected. Please try again.")
#     #             return
#     #     else:
#     #         print("Invalid choice! Please try again.")
#     #         return

#     #     if plot_choice == "1":
#     #         self.show_boxplot(columns)
#     #     elif plot_choice == "2":
#     #         self.show_scatterplot(columns)


#     def visualizeMain(self):
#         print("\nWould you like to analyze the dataset before visualization? (yes/no)")
#         analyze_choice = input().lower()

#         if analyze_choice == "yes":
#             DataAnalysis(self.data).analyze()

#         print("\nVisualization Options:")
#         print("1. Boxplot")
#         print("2. Scatterplot")
#         plot_choice = input("Choose the type of plot (1 or 2): ")

#         if plot_choice not in ["1", "2"]:
#             print("Invalid choice! Please try again.")
#             return

#         print("\n1. Visualize all columns")
#         print("2. Visualize selected columns")
#         column_choice = input("Do you want to visualize all columns or only selected ones? (1 or 2): ")

#         if column_choice == "1":
#             columns = self.data.select_dtypes(include=["float", "int"]).columns
#         elif column_choice == "2":
#             columns = self.select_columns()
#             if not columns:
#                 print("No valid columns selected. Please try again.")
#                 return
#         else:
#             print("Invalid choice! Please try again.")
#             return

#         if plot_choice == "1":
#             self.show_boxplot(columns)
#         elif plot_choice == "2":
#             self.show_scatterplot(columns)


import seaborn as sns
import matplotlib.pyplot as plt
from data_analysis import DataAnalysis
from visualization_options import VisualizationOptions
class DataVisualization:
    def __init__(self, data):
        self.data = data

    def get_color_choice(self):
        print("\nAvailable Colors: red, blue, green, purple, orange, brown, pink, gray, yellow, cyan")
        color = input("Enter your desired color: ").lower()
        label = input("Enter what this color represents: ")
        return color, label

    def analyze_data(self):
        print("Analyzing the dataset...\n")
        print("Data Types:\n", self.data.dtypes)
        print("\nNull Values:\n", self.data.isnull().sum())
        print("\nBasic Statistics:\n", self.data.describe())

    # def scatterplot(self, x_col, y_col):
    #     color, label = self.get_color_choice()
    #     plt.figure(figsize=(10, 6))
    #     sns.scatterplot(data=self.data, x=x_col, y=y_col, color=color)
    #     plt.title(f'Scatterplot of {y_col} vs {x_col}')
    #     plt.xlabel(x_col)
    #     plt.ylabel(f'{y_col} ({label})')
    #     plt.show()

    def scatterplot(self, x_col, y_col):
        colors = []
        labels = []

        # Ask for colors and labels for both columns
        for column in [x_col, y_col]:
            color, label = self.get_color_choice()
            colors.append(color)
            labels.append(label)

        plt.figure(figsize=(10, 6))
        
        # Plot the first column (x-axis) against the second column (y-axis)
        sns.scatterplot(data=self.data, x=self.data[x_col], y=self.data[y_col], color=colors[1], label=labels[1])
        
        plt.title(f'Scatterplot of {y_col} vs {x_col}')
        plt.xlabel(f'{x_col} ({labels[0]})')
        plt.ylabel(f'{y_col} ({labels[1]})')
        plt.legend()
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
        sns.pairplot(self.data[columns])
        plt.title('Pairplot for Selected Columns')
        plt.show()

    def heatmap(self, columns):
        plt.figure(figsize=(12, 8))
        sns.heatmap(self.data[columns].corr(), annot=True, cmap='coolwarm')
        plt.title('Heatmap of Correlations')
        plt.show()

    def multivariate_analysis(self):
        columns = self.select_columns()
        print("\nMultivariate Analysis Options:")
        print("1. Pairplot")
        print("2. Heatmap")
        choice = input("Choose the type of multivariate analysis (1 or 2): ")

        if choice == "1":
            self.pairplot(columns)
        elif choice == "2":
            self.heatmap(columns)
        else:
            print("Invalid choice! Please try again.")

    def select_columns(self):
        print("\nAvailable columns:")
        for i, column in enumerate(self.data.columns, 1):
            print(f"{i}. {column}")
        
        selected_indices = input("Enter the numbers of columns to visualize (comma-separated): ")
        selected_indices = [int(i.strip()) - 1 for i in selected_indices.split(",")]
        selected_columns = [self.data.columns[i] for i in selected_indices if i in range(len(self.data.columns))]
        return selected_columns

    def run_visualization(self):
        print("\nWould you like to analyze the dataset before visualization? (yes/no)")
        analyze_choice = input().lower()

        if analyze_choice == "yes":
            self.analyze_data()

        print("\nVisualization Options:")
        print("1. Scatterplot")
        print("2. Boxplot")
        print("3. Multivariate Analysis")
        choice = input("Choose the type of visualization (1-3): ")

        if choice not in ["1", "2", "3"]:
            print("Invalid choice! Please try again.")
            return

        if choice == "1":
            columns = self.select_columns()
            if len(columns) < 2:
                print("You need to select at least two columns for a scatterplot.")
                return
            self.scatterplot(columns[0], columns[1])

        elif choice == "2":
            columns = self.select_columns()
            if len(columns) < 2:
                print("You need to select at least two columns for a boxplot.")
                return
            self.boxplot(columns[0], columns[1])

        elif choice == "3":
            self.multivariate_analysis()

