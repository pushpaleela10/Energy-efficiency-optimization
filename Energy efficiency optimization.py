import time
from random import randint

# 1. Check AI accuracy (example: energy prediction)
def check_accuracy():
    actual = [100, 120, 130]
    predicted = [102, 118, 128]
    errors = [(a - p) ** 2 for a, p in zip(actual, predicted)]
    mse = sum(errors) / len(errors)
    print("AI Accuracy: MSE =", round(mse, 2))

# 2. Simple chatbot with low latency
def chatbot(user_input):
    start = time.time()
    reply = "Tip: Turn off unused lights to save energy."
    latency = time.time() - start
    print("Chatbot Reply:", reply)
    print("Response Time:", round(latency, 4), "seconds")

# 3. Simulate real-time IoT data (like smart meter)
def read_iot_data():
    print("Reading real-time IoT energy data:")
    for i in range(3):
        data = randint(90, 150)
        print("Device", i+1, "Data:", data, "kWh")
        time.sleep(1)

# Run all
check_accuracy()
chatbot("How to save energy?")
read_iot_data()


