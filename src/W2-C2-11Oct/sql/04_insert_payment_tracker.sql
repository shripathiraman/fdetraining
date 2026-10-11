INSERT INTO payment_tracker (
    transaction_id,
    transaction_date,
    sender_name,
    receiver_name,
    amount,
    payment_mode,
    status,
    remarks
)
VALUES
('TXN001', '2026-10-01 09:15:00', 'Shripathi', 'Arthi', 150.00, 'GPay', 'SUCCESS', 'Household expenses'),

('TXN002', '2026-10-02 10:30:00', 'Shripathi', 'Varun', 50.00, 'GPay', 'SUCCESS', 'Badminton fees'),

('TXN003', '2026-10-03 14:45:00', 'Arthi', 'Shripathi', 200.00, 'GPay', 'SUCCESS', 'Grocery reimbursement'),

('TXN004', '2026-10-04 08:20:00', 'Shripathi', 'Electricity Board', 120.50, 'GPay', 'SUCCESS', 'Electricity bill'),

('TXN005', '2026-10-05 18:10:00', 'Shripathi', 'Restaurant XYZ', 75.25, 'GPay', 'SUCCESS', 'Dinner payment'),

('TXN006', '2026-10-06 11:00:00', 'Shripathi', 'Fuel Station', 90.00, 'GPay', 'SUCCESS', 'Fuel refill'),

('TXN007', '2026-10-07 16:35:00', 'Arthi', 'School', 300.00, 'GPay', 'SUCCESS', 'School fees'),

('TXN008', '2026-10-08 13:25:00', 'Shripathi', 'Amazon Seller', 45.99, 'GPay', 'SUCCESS', 'Online purchase'),

('TXN009', '2026-10-09 19:40:00', 'Shripathi', 'Friend Ravi', 500.00, 'GPay', 'PENDING', 'Personal transfer'),

('TXN010', '2026-10-10 21:15:00', 'Shripathi', 'Internet Provider', 65.00, 'GPay', 'SUCCESS', 'Internet bill');