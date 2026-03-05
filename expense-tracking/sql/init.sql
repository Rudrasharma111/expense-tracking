CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    expense_date DATE NOT NULL,
    category VARCHAR(50) NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    description TEXT
);