# Expense Tracker CLI

This is a data processing application built with Python, Docker, and PostgreSQL. It follows a modular structure and implements a complete ETL pipeline.

## System Architecture


- **Ingestion**: Automatically reads multiple CSV files from the `data/` folder.
- **Validation**: Uses Pydantic to ensure data integrity before database insertion.
- **Storage**: Uses a dockerized PostgreSQL database with environment-based configuration.
- **Analytics**: Provides CLI-triggered reports for total spending, category averages, and monthly trends.

## How to Run
1. Start the system: `docker-compose up --build`
2. Run analytics: `docker-compose run app python app/main.py analyze`
3. Run tests: `pytest`"
