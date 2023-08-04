# Candle Collector

Candle Collector is a simple Django project that allows users to view a list of candles.

## Installation

Clone the repository, navigate to the project directory, and set up a virtual environment:

```bash
git clone https://github.com/your-username/candle-collector.git
cd candle-collector
python3 -m venv venv
```

Activate the environment
macOS and Linux:
```bash
source venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate

```
Install project dependencies:
```bash
pip3 install -r requirements.txt
```
Apply database migrations:
```bash
python3 manage.py migrate
```

## Usage

1. Run the Django development server:
```bash
python3 manage.py runserver
```

2. Open your web browser and go to `http://127.0.0.1:8000/` to access the Candle Collector app. You'll be able to view a list of candles and their details.

## Contributing

Contributions are welcome! Fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
