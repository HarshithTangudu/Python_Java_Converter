CREATE DATABASE IF NOT EXISTS code_converter;
USE code_converter;

CREATE TABLE conversions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    python_code TEXT NOT NULL,
    java_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample data
INSERT INTO conversions (python_code, java_code) VALUES 
('def hello():\n    print("Hi")', 'public static void hello() {\n    System.out.println("Hi")\n}'),
('if x > 0:\n    print("Positive")', 'if (x > 0) {\n    System.out.println("Positive")\n}');
