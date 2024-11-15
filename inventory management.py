class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value  
        self.weight = weight 

class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [] 
        self.selected_items = [] 
        self.total_value = 0  
        self.total_weight = 0  
    def knapsack_dp(self, items):
        n = len(items)
        dp = [[0] * (self.capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(self.capacity + 1):
                if items[i - 1].weight <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].value)
                else:
                    dp[i][w] = dp[i - 1][w]
        w = self.capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                self.selected_items.append(items[i - 1])
                self.total_value += items[i - 1].value
                self.total_weight += items[i - 1].weight
                w -= items[i - 1].weight
        return dp[n][self.capacity]

    def display_results(self):
        print("\nKnapsack Packing Results:")
        print(f"Total Value of Selected Items: {self.total_value}")
        print(f"Total Weight of Selected Items: {self.total_weight}")
        print("Selected Items for Packing:")
        for item in self.selected_items:
            print(f"- {item.name}: Value = {item.value}, Weight = {item.weight}")

def get_user_input_items():
    items = []
    num_items = int(input("Enter the number of items: "))
    for i in range(num_items):
        name = input(f"\nEnter the name of item {i + 1}: ")
        value = int(input(f"Enter the value of {name}: "))
        weight = int(input(f"Enter the weight of {name}: "))
        items.append(Item(name, value, weight))
    return items

def get_user_input_knapsack():
    capacity = int(input("\nEnter the weight capacity of the knapsack: "))
    return Knapsack(capacity)

def main():
    items = get_user_input_items()
    knapsack = get_user_input_knapsack()
    knapsack.knapsack_dp(items)
    knapsack.display_results()
if __name__ == "__main__":
    main()
