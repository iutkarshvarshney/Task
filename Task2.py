import time
import threading

class AlgoRunner:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("Algorithm started.")
        start_time = time.time()

        while self.running:
            elapsed_time = time.time() - start_time
            if elapsed_time > 600:  # 10 minutes = 600 seconds
                self.stop()

            # Simulate algorithm process here
            print(f"Algorithm running... Elapsed time: {elapsed_time:.2f} seconds")

            time.sleep(1)  # Sleep for 1 second to simulate work being done

    def stop(self):
        self.running = False
        print("Algorithm stopped.")
from flask import Flask, jsonify
import threading

app = Flask(__name__)
algo_runner = AlgoRunner()

@app.route('/start_algo', methods=['GET'])
def start_algo():
    if not algo_runner.running:
        algo_thread = threading.Thread(target=algo_runner.start)
        algo_thread.start()
        return jsonify({"status": "Algorithm started."})
    else:
        return jsonify({"status": "Algorithm is already running."})

@app.route('/stop_algo', methods=['GET'])
def stop_algo():
    if algo_runner.running:
        algo_runner.stop()
        return jsonify({"status": "Algorithm stopped."})
    else:
        return jsonify({"status": "Algorithm is not running."})

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/start_algo
#http://127.0.0.1:5000/stop_algo