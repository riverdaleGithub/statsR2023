import numpy as np

class nerualNet():

    def __init__(self,title) -> None:
        self.title = title        
    # Activation function: sigmoid
    def sigmoid(self,x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self,x):
        return x * (1 - x)
    # Initialize the network
    def initialize_network(self, input_nodes, hidden_nodes, output_nodes):
        network = {
            'hidden_weights': np.random.rand(input_nodes, hidden_nodes),
            'hidden_bias': np.random.rand(hidden_nodes),
            'output_weights': np.random.rand(hidden_nodes, output_nodes),
            'output_bias': np.random.rand(output_nodes)
        }
        return network

    # Forward propagation
    def forward_propagate(self, network, input_data):
        hidden_layer = self.sigmoid(np.dot(input_data, network['hidden_weights']) + network['hidden_bias'])
        output_layer = self.sigmoid(np.dot(hidden_layer, network['output_weights']) + network['output_bias'])
        return hidden_layer, output_layer

    # Backpropagation
    def backpropagate(self,network, input_data, target, hidden_layer, output_layer, learning_rate):
        output_error = target - output_layer
        output_delta = output_error * self.sigmoid_derivative(output_layer)

        hidden_error = np.dot(output_delta, network['output_weights'].T)
        hidden_delta = hidden_error * self.sigmoid_derivative(hidden_layer)

        # Update weights
        network['output_weights'] += learning_rate * np.outer(hidden_layer, output_delta)
        network['output_bias'] += learning_rate * output_delta
        network['hidden_weights'] += learning_rate * np.outer(input_data, hidden_delta)
        network['hidden_bias'] += learning_rate * hidden_delta

# Train the network
    def train_network(self, network, input_data, targets, learning_rate, epochs):
        for epoch in range(epochs):
            for input_vector, target in zip(input_data, targets):
                hidden_layer, output_layer = self.forward_propagate(network, input_vector)
                self.backpropagate(network, input_vector, target, hidden_layer, output_layer, learning_rate)

    # Make predictions
    def predict(self,network, input_data):
        _, predictions = self.forward_propagate(network, input_data)
        return np.argmax(predictions, axis=1)


if __name__ == '__main__':
    # def generate_stock_prices(days):
    #     prices = np.random.normal(loc=100, scale=5, size=days)
    #     return np.round(prices, 2)

    # def create_stock_dataset(prices, window_size):
    #     input_data = []
    #     targets = []
    #     for i in range(len(prices) - window_size):
    #         input_data.append(prices[i:i + window_size])
    #         targets.append(prices[i + window_size])
    #     return np.array(input_data), np.array(targets)

    # # Create synthetic stock price dataset
    # days = 100
    # window_size = 5
    # prices = generate_stock_prices(days)
    # input_data, targets = create_stock_dataset(prices, window_size)

    # # Initialize and train the neural network
    # input_nodes = window_size
    # hidden_nodes = 10
    # output_nodes = 1
    # learning_rate = 0.01
    # epochs = 1000

    # agent = nerualNet('test')
    # network = agent.initialize_network(input_nodes, hidden_nodes, output_nodes)
    # agent.train_network(network, input_data, targets.reshape(-1, 1), learning_rate, epochs)

    # # Make predictions on the input data
    # predictions = []
    # for input_vector in input_data:
    #     _, output_layer = agent.forward_propagate(network, input_vector)
    #     predictions.append(output_layer[0])

    # print("Predicted closing prices:", predictions[:5])
    # print("Actual closing prices:", targets[:5])




    input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[1, 0], [0, 1], [0, 1], [1, 0]])

    agent = nerualNet('test')
    network = agent.initialize_network(2, 2, 2)  # 2 input nodes, 2 hidden nodes, 2 output nodes
    agent.train_network(network, input_data, targets, learning_rate=0.5, epochs=10000)

    predictions = agent.predict(network, input_data)
    print("Predictions:", predictions)