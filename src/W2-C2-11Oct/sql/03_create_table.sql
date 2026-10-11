DROP TABLE IF EXISTS payment_tracker;

CREATE TABLE payment_tracker (
    transaction_id VARCHAR(100) PRIMARY KEY,
    transaction_date TIMESTAMP NOT NULL,
    sender_name VARCHAR(100),
    receiver_name VARCHAR(100),
    amount DECIMAL(10,2) NOT NULL,
    payment_mode VARCHAR(50) DEFAULT 'GPay',
    status VARCHAR(20) DEFAULT 'SUCCESS',
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);