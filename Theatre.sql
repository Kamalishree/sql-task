CREATE TABLE Screen (
    Screen_Id INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    class_type VARCHAR(10) NOT NULL,
    capacity INT NOT NULL
);

INSERT INTO Screen (name, class_type, capacity) VALUES
('A', 'Gold', 100),
('B', 'Silver', 80),
('C', 'Iron', 60),
('D', 'Gold', 120),
('E', 'Silver', 90);
SELECT * FROM Screen;

CREATE TABLE Seat (
    seat_id INT IDENTITY(1,1) PRIMARY KEY ,
    screen_id INT NOT NULL,
    seat_number VARCHAR(10) NOT NULL,
    FOREIGN KEY (screen_id) REFERENCES Screen(screen_id)
); 

INSERT INTO Seat (screen_id, seat_number) VALUES
(1, 'A1'),
(1, 'A2'),
(2, 'B1'),
(2, 'B2'),
(3, 'C1');
SELECT*FROM Seat;

CREATE TABLE Movie (
    movie_Id INT IDENTITY(1,1) PRIMARY KEY ,
   title VARCHAR(255) NOT NULL,
   genre VARCHAR(50) NOT NULL,
   rating DECIMAL(3,1) NOT NULL,
   status VARCHAR(20) NOT NULL
   
   );

   INSERT INTO Movie (title, genre, rating, status) VALUES
('roja', 'com', 4, 'Now Showing'),
('tom n herry', 'cartoon', 5, 'Now Showing'),
('billa', 'Crime', 4, 'Now Showing'),
('mission mangal', 'Sci-Fi', 5, 'Upcoming'),
('kanchana', 'horror', 4, 'Now Showing'),
('conjuring', 'horror', 5, 'Upcoming'),
('Joker 2', 'Drama', 4, 'Upcoming');

SELECT*FROM Movie;

CREATE TABLE MovieCast (
    cast_id INT IDENTITY(1,1) PRIMARY KEY,
    movie_id INT NOT NULL,
    person_name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
); 

INSERT INTO MovieCast (movie_id, person_name, role) VALUES
(1, 'Leonardo DiCaprio', 'Cobb'),
(2, 'Kate Winslet', 'Rose'),
(3, 'Keanu Reeves', 'Neo'),
(4, 'Matthew McConaughey', 'Cooper'),
(5, 'Idina Menzel', 'Elsa');

SELECT*FROM MovieCast;


CREATE TABLE Review (
    review_id INT IDENTITY(1,1) PRIMARY KEY, 
    movie_id INT NOT NULL,
    content TEXT NOT NULL,
    review_date DATETIME NOT NULL,
    reviewer_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

INSERT INTO Review (movie_id, content, review_date, reviewer_name) VALUES
(1, 'Amazing movie with mind-bending plot!', '2025-06-10 10:00:00', 'Alice'),
(2, 'Heart-touching and emotional.', '2025-06-10 11:00:00', 'Bob'),
(3, 'A revolutionary action film.', '2025-06-10 12:00:00', 'Charlie'),
(4, 'Visually stunning and thought-provoking.', '2025-06-10 13:00:00', 'Diana'),
(5, 'Perfect for kids and adults alike.', '2025-06-10 14:00:00', 'Eve');

SELECT*FROM Review;

CREATE TABLE Show (
    show_id INT IDENTITY(1,1) PRIMARY KEY, 
    screen_id INT NOT NULL,
    movie_id INT NOT NULL,
    show_datetime DATETIME NOT NULL,
    FOREIGN KEY (screen_id) REFERENCES Screen(screen_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
) ;

INSERT INTO Show (screen_id, movie_id, show_datetime) VALUES
(1, 1, '2025-06-11 14:00:00'),
(2, 2, '2025-06-11 16:30:00'),
(3, 3, '2025-06-11 19:00:00'),
(4, 4, '2025-06-11 21:30:00'),
(5, 5, '2025-06-12 11:00:00');

SELECT*FROM Show;

CREATE TABLE ShowSeat (
    show_seat_id INT IDENTITY(1,1) PRIMARY KEY,
    show_id INT NOT NULL,
    seat_id INT NOT NULL,
    is_availabl BIT NOT NULL DEFAULT 1,
    FOREIGN KEY (show_id) REFERENCES Show(show_id),
    FOREIGN KEY (seat_id) REFERENCES Seat(seat_id)
); 

INSERT INTO ShowSeat (show_id, seat_id, is_availabl) VALUES
(1, 1, 1),
(1, 2,0),
(2, 3, 1),
(2, 4, 1),
(3, 5,0);

SELECT*FROM ShowSeat;


CREATE TABLE Usertable (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    phone VARCHAR(15) NOT NULL
);

INSERT INTO Usertable  (name, email, phone) VALUES
('John Doe', 'john@example.com', '1234567890'),
('Jane Smith', 'jane@example.com', '2345678901'),
('Alice Brown', 'alice@example.com', '3456789012'),
('Bob White', 'bob@example.com', '4567890123'),
('Charlie Black', 'charlie@example.com', '5678901234');

SELECT*FROM Usertable;

CREATE TABLE Membership (
    membership_id INT  IDENTITY(1,1)PRIMARY KEY,
    user_id INT NOT NULL,
    current_points INT NOT NULL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES Usertable(user_id)
);

INSERT INTO Membership (user_id, current_points) VALUES
(1, 100),
(2, 200),
(3, 150),
(4, 250),
(5, 300);

SELECT*FROM Membership;

CREATE TABLE Booking (
    booking_id INT IDENTITY(1,1) PRIMARY KEY, 
    user_id INT NOT NULL,
    show_id INT NOT NULL,
    booking_datetime DATETIME NOT NULL,
    total_cost DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Usertable(user_id),
    FOREIGN KEY (show_id) REFERENCES Show(show_id)
);
INSERT INTO Booking (user_id, show_id, booking_datetime, total_cost) VALUES
(1, 1, '2025-06-10 10:00:00', 300.00),
(2, 2, '2025-06-10 11:00:00', 250.00),
(3, 3, '2025-06-10 12:00:00', 200.00),
(4, 4, '2025-06-10 13:00:00', 150.00),
(5, 5, '2025-06-10 14:00:00', 100.00);

SELECT*FROM Booking;

CREATE TABLE PaymentGateway (
    gateway_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Payment (
    payment_id INT IDENTITY(1,1) PRIMARY KEY,
    booking_id INT NOT NULL,
    gateway_id INT NOT NULL,
    transaction_amount DECIMAL(10,2) NOT NULL,
    transaction_datetime DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL,
    failure_reason TEXT,
    credit_card_name VARCHAR(100),
    credit_card_number VARCHAR(20),
    expiry_date DATE,
    cvv VARCHAR(4),
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
    FOREIGN KEY (gateway_id) REFERENCES PaymentGateway(gateway_id)
);

CREATE TABLE FoodItem (
    item_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_combo BIT NOT NULL DEFAULT 0
);

CREATE TABLE Payment (
    payment_id INT IDENTITY(1,1) PRIMARY KEY,
    booking_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL, -- e.g., Card, UPI, Cash
    payment_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
);

CREATE TABLE Feedback (
    feedback_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL,
    booking_id INT NOT NULL,
    comment TEXT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    feedback_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (user_id) REFERENCES [Usertable](user_id),
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
);

CREATE TABLE Staff (
    staff_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50), -- e.g., Manager, Cashier, Cleaner
    contact_number VARCHAR(15),
    joined_date DATE DEFAULT GETDATE()
);

CREATE TABLE SeatReservation (
    reservation_id INT IDENTITY(1,1) PRIMARY KEY,
    booking_id INT NOT NULL,
    seat_id INT NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
    FOREIGN KEY (seat_id) REFERENCES Seat(seat_id)
);

CREATE TABLE MovieGenre (
    movie_id INT NOT NULL,
    genre VARCHAR(50) NOT NULL,
    PRIMARY KEY (movie_id, genre),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

UPDATE Screen
SET capacity = 150
WHERE screen_id = 1;

UPDATE Movie
SET status = 'Upcoming'
WHERE movie_id = 1;

UPDATE Show
SET show_datetime = '2025-06-12 14:00:00'
WHERE show_id = 1;

UPDATE Booking
SET total_cost = 300.00
WHERE booking_id = 1;

TRUNCATE TABLE Screen;

TRUNCATE TABLE Seat;

TRUNCATE TABLE MovieCast;


TRUNCATE TABLE Movie;

SELECT * FROM Movie
WHERE status = 'Now Showing';


SELECT * FROM Screen
WHERE capacity > 100;

SELECT * FROM Movie
WHERE rating > 8.0;

SELECT * FROM Screen
WHERE class_type = 'Gold';


SELECT * FROM Movie
WHERE status = 'Now Showing';

SELECT * FROM MovieCast
WHERE role = 'Hero';

SELECT * FROM Screen WHERE capacity > 100;

SELECT * FROM Screen WHERE capacity BETWEEN 50 AND 150;

SELECT * FROM Screen WHERE class_type IN ('Silver', 'Iron');

SELECT * FROM Seat WHERE seat_number = 'A1';


SELECT * FROM Movie
WHERE status = 'Showing';




select distinct capacity from screen;

select distinct *from screen


SELECT DISTINCT person_name, role FROM MovieCast;


SELECT DISTINCT movie_id FROM MovieCast;

SELECT DISTINCT reviewer_name FROM Review;

SELECT DISTINCT movie_id, reviewer_name FROM Review;


SELECT DISTINCT show_datetime FROM Show;


SELECT DISTINCT movie_id, screen_id FROM Show;

--Arithmetic Operators

SELECT TOP 3 total_cost, total_cost + 50 AS increased_cost FROM Booking;

SELECT TOP 3 capacity, capacity - 10 AS reduced_capacity FROM Screen;

SELECT TOP 3 rating, rating * 1.1 AS boosted_rating FROM Movie;

--Comparison Operators

SELECT TOP 3 title FROM Movie WHERE rating >= 8.0;

SELECT TOP 3 name FROM Screen WHERE capacity != 200;

SELECT TOP 3 booking_id FROM Booking WHERE total_cost < 400;

--Logical Operators

SELECT TOP 3 title 
FROM Movie 
WHERE rating > 7.5 AND status = 'Now Showing';


SELECT TOP 3 show_id 
FROM Show
WHERE NOT screen_id = 1;

--order by,fetch,offset

SELECT * 
FROM Show
ORDER BY show_datetime DESC;


SELECT * 
FROM Show
ORDER BY show_datetime;



SELECT  rating
FROM Movie
ORDER BY  rating DESC;


SELECT  rating
FROM Movie
ORDER BY  rating ;

SELECT * 
FROM Usertable
ORDER BY name ASC;

SELECT * 
FROM Usertable
ORDER BY email DESC;

SELECT * 
FROM Movie
ORDER BY movie_id
OFFSET 5 ROWS FETCH NEXT 10 ROWS ONLY;

SELECT * 
FROM Movie
ORDER BY movie_id
OFFSET 10 ROWS;


SELECT * 
FROM Movie
ORDER BY movie_id
OFFSET 10 ROWS;

SELECT * 
FROM Movie
ORDER BY movie_id
OFFSET 5 ROWS FETCH NEXT 10 ROWS ONLY;



SELECT * 
FROM Usertable
ORDER BY user_id
OFFSET 1 ROWS FETCH NEXT 5 ROWS ONLY;

SELECT*
FROM Usertable
ORDER BY user_id
OFFSET 2 ROWS;


SELECT * 
FROM Membership
ORDER BY membership_id
OFFSET 1 ROWS FETCH NEXT 5 ROWS ONLY;


SELECT * 
FROM Membership
ORDER BY membership_id
OFFSET 3 ROWS;


SELECT * 
FROM Booking
ORDER BY booking_id
OFFSET 4 ROWS FETCH NEXT 5 ROWS ONLY;


SELECT * 
FROM Booking
ORDER BY booking_id
OFFSET 2 ROWS;

SELECT * 
FROM User
ORDER BY user_id
LIMIT 3 OFFSET 10;


--Aggregate function

SELECT name, MAX(capacity) AS max_capacity, MIN(class_type) AS class_type
FROM screen
GROUP BY name;

select class_type,sum(capacity) as sums from screen group by class_type;

select class_type,avg(capacity) as average from screen group by class_type;

select class_type,count(capacity) as count1 from screen group by class_type;

select class_type,min(capacity) as minimum from screen group by ;


SELECT screen_id, CONCAT(name, ' - ', class_type) AS screen_description FROM Screen;


SELECT seat_id, REPLACE(seat_number, 'A', 'Z') AS updated_seat FROM Seat;

SELECT seat_id, TRIM(seat_number) AS cleaned_seat FROM Seat;

select class_type,max(capacity) as maximum from screen group by class_type;


SELECT AVG(rating) AS average_rating
FROM Movie;

SELECT AVG(rating)
FROM Movie;


SELECT COUNT(*) AS total_seats FROM Seat;

SELECT LEFT(seat_number, 1) AS prefix, COUNT(*) AS count_by_prefix
FROM Seat
GROUP BY LEFT(seat_number, 1);


SELECT MAX(seat_id) AS max_seat_id FROM Seat;


SELECT MIN(seat_id) AS min_seat_id FROM Seat;


SELECT is_availabl, COUNT(*) AS seat_count
FROM ShowSeat
GROUP BY is_availabl;

SELECT show_id, COUNT(*) AS total_seats
FROM ShowSeat
GROUP BY show_id;

SELECT show_id, MAX(seat_id) AS max_seat
FROM ShowSeat
GROUP BY show_id;

--joins
--inner join right join ,left join

SELECT 
    s.screen_id,
    s.name AS screen_name,
    s.capacity,
    st.seat_id,
    st.seat_number
FROM Screen s
INNER JOIN Seat st ON s.screen_id = st.screen_id;

SELECT 
    s.screen_id,
    s.name AS screen_name,
    s.class_type,
    s.capacity,
    st.seat_id,
    st.seat_number
FROM Screen s
LEFT JOIN Seat st ON s.screen_id = st.screen_id;

SELECT 
    s.screen_id,
    s.name AS screen_name,
    s.class_type,
    s.capacity,
    st.seat_id,
    st.seat_number
FROM Screen s
RIGHT JOIN Seat st ON s.screen_id = st.screen_id;

SELECT *
FROM Seat s
INNER JOIN Movie m ON s.seat_id = m.movie_id;

SELECT *
FROM Seat s
LEFT JOIN Movie m ON s.seat_id = m.movie_id;

SELECT *
FROM Seat s
RIGHT JOIN Movie m ON s.seat_id = m.movie_id;

SELECT 
    s.seat_id,
    s.seat_number,
    sh.show_id,
    m.title,
    m.genre
FROM Seat s
JOIN ShowSeat ss ON s.seat_id = ss.seat_id
JOIN Show sh ON ss.show_id = sh.show_id
JOIN Movie m ON sh.movie_id = m.movie_id;

SELECT 
    s.seat_id,
    s.seat_number,
    sh.show_id,
    sh.show_datetime,
    m.movie_id,
    m.title,
    m.genre
FROM Seat s
LEFT JOIN ShowSeat ss ON s.seat_id = ss.seat_id
LEFT JOIN Show sh ON ss.show_id = sh.show_id
LEFT JOIN Movie m ON sh.movie_id = m.movie_id;

SELECT 
    s.seat_id,
    s.seat_number,
    sh.show_id,
    sh.show_datetime,
    m.movie_id,
    m.title,
    m.genre
FROM Seat s
RIGHT JOIN ShowSeat ss ON s.seat_id = ss.seat_id
RIGHT JOIN Show sh ON ss.show_id = sh.show_id
RIGHT JOIN Movie m ON sh.movie_id = m.movie_id;

SELECT 
    s.seat_id,
    s.seat_number,
    m.title AS movie_title,
    sh.show_datetime
FROM Seat s
LEFT JOIN ShowSeat ss ON s.seat_id = ss.seat_id
LEFT JOIN Show sh ON ss.show_id = sh.show_id
LEFT JOIN Movie m ON sh.movie_id = m.movie_id;

SELECT 
    s.seat_id,
    s.seat_number,
    m.title AS movie_title,
    sh.show_datetime
FROM Seat s
RIGHT JOIN ShowSeat ss ON s.seat_id = ss.seat_id
RIGHT JOIN Show sh ON ss.show_id = sh.show_id
RIGHT JOIN Movie m ON sh.movie_id = m.movie_id;

SELECT 
    s.seat_id,
    s.seat_number,
    m.movie_id,
    m.title AS movie_title
FROM Seat s
CROSS JOIN Movie m;

SELECT 
    s.seat_number,
    m.title
FROM Seat s
CROSS JOIN Movie m
WHERE s.seat_number LIKE 'A%';

SELECT 
    sc.screen_id,
    sc.name AS screen_name,
    m.movie_id,
    m.title AS movie_title
FROM Screen sc
CROSS JOIN Movie m;

SELECT 
    s.seat_id,
    s.seat_number,
    sh.show_id,
    sh.show_datetime,
    scr.name AS screen_name
FROM Seat s
INNER JOIN ShowSeat ss ON s.seat_id = ss.seat_id
INNER JOIN Show sh ON ss.show_id = sh.show_id
INNER JOIN Screen scr ON sh.screen_id = scr.screen_id;

SELECT 
    m.title AS movie_title,
    sc.name AS screen_name,
    sh.show_datetime
FROM Movie m
INNER JOIN Show sh ON m.movie_id = sh.movie_id
INNER JOIN Screen sc ON sh.screen_id = sc.screen_id;

SELECT 
    b.booking_id,
    u.name AS user_name,
    sh.show_datetime,
    b.total_cost
FROM Booking b
INNER JOIN Usertable u ON b.user_id = u.user_id
INNER JOIN Show sh ON b.show_id = sh.show_id;

SELECT 
    u.name AS user_name,
    b.booking_id,
    sh.show_datetime
FROM Usertable u
LEFT JOIN Booking b ON u.user_id = b.user_id
LEFT JOIN Show sh ON b.show_id = sh.show_id;

SELECT 
    u.name AS user_name,
    b.booking_id,
    sh.show_datetime
FROM Usertable u
RIGHT JOIN Booking b ON u.user_id = b.user_id
RIGHT JOIN Show sh ON b.show_id = sh.show_id;


SELECT capacity,
       CASE 
         WHEN capacity > 100 THEN 'bigger'  
         WHEN capacity <= 100 THEN 'smaller'
       END AS type_capacity 
FROM screen;

SELECT * 
FROM screen 
WHERE capacity IN (
    SELECT capacity 
    FROM screen 
    WHERE capacity = 120
);

SELECT * 
FROM Review 
WHERE movie_id IN (
    SELECT movie_id 
    FROM Movie 
    WHERE status = 'Showing'
);

SELECT * 
FROM Usertable 
WHERE user_id IN (
    SELECT user_id 
    FROM Membership
);

SELECT * 
FROM Review 
WHERE movie_id IN (
    SELECT movie_id 
    FROM Movie 
    WHERE genre = 'horror'
);

SELECT * 
FROM Review 
WHERE reviewer_name IN ('Alice', 'Bob', 'Charlie');

SELECT * 
FROM Review 
WHERE movie_id IN (
    SELECT movie_id 
    FROM Movie 
    WHERE rating > 4.5





SELECT * 
FROM screen s1 
WHERE EXISTS (
    SELECT 1 
    FROM screen s2 
    WHERE s2.capacity = 90
);

SELECT * 
FROM screen s 
WHERE EXISTS (
    SELECT 1 
    FROM Show sh 
    WHERE sh.screen_id = s.screen_id
);

SELECT * 
FROM screen s1 
WHERE NOT EXISTS (
    SELECT 1 
    FROM screen s2 
    WHERE s2.capacity = 170
);

SELECT * 
FROM screen 
WHERE capacity > ANY (
    SELECT capacity 
    FROM screen 
    WHERE class_type = 'Silver'
);

SELECT * 
FROM screen 
WHERE capacity > ANY (
    SELECT capacity 
    FROM screen 
    WHERE class_type = 'gold'
);

SELECT * 
FROM screen 
WHERE capacity > ALL (
    SELECT capacity 
    FROM screen 
    WHERE class_type = 'Silver'
);

SELECT * 
FROM screen 
WHERE capacity > ANY (
    SELECT capacity 
    FROM screen 
    WHERE class_type = 'Gold'
);

SELECT * 
FROM screen 
WHERE capacity > ALL (
    SELECT capacity 
    FROM screen 
    WHERE class_type = 'Iron'
);

SELECT *
FROM Show
WHERE CAST(show_datetime AS DATE) = CURRENT_DATE;

SELECT 
  review_id,
  review_date,
  YEAR(review_date) AS review_year,
  MONTH(review_date) AS review_month,
  DAY(review_date) AS review_day
FROM Review;

GRANT SELECT ON Movie TO admin_user;



GRANT SELECT, INSERT ON Booking TO admin_user;


REVOKE SELECT ON Movie FROM admin_user;



--day 6 practice
SELECT 
    s.name, 
    s.capacity, 
    v.seat_number 
FROM screen s 
INNER JOIN seat v ON s.screen_id = v.screen_id;

SELECT 
    s.screen_id, 
    s.name AS screen_name, 
    s.class_type, 
    se.seat_id, 
    se.seat_number 
FROM Screen s
INNER JOIN Seat se 
    ON s.screen_id = se.screen_id;

    SELECT DISTINCT s.name
FROM Screen s
JOIN Seat se ON s.screen_id = se.screen_id;

    
SELECT s.name AS screen_name, m.title AS movie_title
FROM Screen s
JOIN Show sh ON s.screen_id = sh.screen_id
JOIN Movie m ON sh.movie_id = m.movie_id;

SELECT 
    sc.name AS screen_name,
    COUNT(se.seat_id) AS total_seats
FROM Screen sc
JOIN Seat se ON sc.screen_id = se.screen_id
GROUP BY sc.name;

-- highest revenue

SELECT 
    m.title AS movie_title, 
    SUM(b.total_cost) AS total_revenue
FROM Booking b
JOIN Show s ON b.show_id = s.show_id
JOIN Movie m ON s.movie_id = m.movie_id
GROUP BY m.title
ORDER BY total_revenue DESC
LIMIT 1;


---Calculate the average order value per customer.

SELECT 
    u.name AS customer_name, 
    AVG(b.total_cost) AS avg_order_value
FROM UserTable u
JOIN Booking b ON u.user_id = b.user_id
GROUP BY u.name;


SELECT 
    u.name AS customer_name, 
    AVG(b.total_cost) AS avg_order_value
FROM [Usertable] u
JOIN Booking b ON u.user_id = b.user_id
GROUP BY u.name;

SELECT 
    m.title AS movie_title, 
    COUNT(r.review_id) AS total_reviews
FROM Review r
JOIN Movie m ON r.movie_id = m.movie_id
GROUP BY m.title;


SELECT 
    m.title AS movie_title, 
    AVG(m.rating) AS avg_rating
FROM Movie m
GROUP BY m.title
ORDER BY avg_rating DESC
LIMIT 1;


SELECT 
    m.title AS movie_title, 
    AVG(m.rating) AS average_rating
FROM Movie m
GROUP BY m.title;


SELECT DISTINCT mc.person_name
FROM MovieCast mc
JOIN Movie m ON mc.movie_id = m.movie_id
JOIN Review r ON r.movie_id = m.movie_id
WHERE LEN(CAST(r.content AS VARCHAR(MAX))) > 100;



--Day 7 practice

--Stored Procedure Queries

CREATE PROCEDURE GetUsersByCity
    @City NVARCHAR(50)
AS
BEGIN
    SELECT user_id, name, email, city, created_at
    FROM [Usertable]
    WHERE city = @City;
END;

EXEC GetUsersByCity @City = 'Chennai';

CREATE PROCEDURE GetUserBookingCount
    @UserID INT,
    @BookingCount INT OUTPUT
AS
BEGIN
    SELECT @BookingCount = COUNT(*)
    FROM Booking
    WHERE user_id = @UserID;
END;

DECLARE @Count INT;
EXEC GetUserBookingCount @UserID = 1, @BookingCount = @Count OUTPUT;
PRINT @Count;

CREATE PROCEDURE GetUserBookingCount
    @UserID INT,
    @BookingCount INT OUTPUT
AS
BEGIN
    SELECT @BookingCount = COUNT(*)
    FROM Booking
    WHERE user_id = @UserID;
END;

DECLARE @Count INT;

EXEC GetUserBookingCount 
    @UserID = 1,               -- Replace 1 with the actual user_id
    @BookingCount = @Count OUTPUT;

PRINT 'Booking Count: ' + CAST(@Count AS VARCHAR);

--sub queries

SELECT name, email
FROM [Usertable]
WHERE user_id IN (
    SELECT user_id
    FROM Booking
    WHERE total_cost > 500
);

SELECT 
    u.user_id, 
    u.name, 
    u.email, 
    (SELECT COUNT(*)
     FROM Booking b
     WHERE b.user_id = u.user_id) AS total_bookings
FROM Usertable u;

SELECT name
FROM FoodItem
WHERE food_id NOT IN (
    SELECT DISTINCT food_id
    FROM FoodOrderItem
);

SELECT name, email
FROM [Usertable]
WHERE user_id IN (
    SELECT user_id
    FROM Booking
    GROUP BY user_id
    HAVING SUM(total_cost) > (
        SELECT AVG(total_cost)
        FROM Booking
    
);

SELECT 
    u.name, 
    t.total_spent
FROM [Usertable] u
JOIN (
    SELECT 
        user_id, 
        SUM(total_cost) AS total_spent
    FROM Booking
    GROUP BY user_id
) t ON u.user_id = t.user_id;

SELECT 
    u.name, 
    t.total_spent
FROM [Usertable] u
JOIN (
    SELECT 
        user_id, 
        SUM(total_cost) AS total_spent
    FROM Booking
    GROUP BY user_id
) t ON u.user_id = t.user_id;

--1. Find the Second Highest Booking Amount

SELECT MAX(total_cost) AS second_highest_booking_amount
FROM Booking
WHERE total_cost < (SELECT MAX(total_cost) FROM Booking);

--2. Find Bookings With Amounts Above Their User’s Average 

SELECT b.booking_id, u.name, b.user_id, b.total_cost
JOIN [Usertable] u ON u.user_id = b.user_id
WHERE b.total_cost > (
    SELECT AVG(b2.total_cost)
    FROM Booking b2
    WHERE b.user_id = b2.user_id
);

 --3. List Food Items That Haven’t Been Ordered

 SELECT food_id, name
FROM FoodItem
WHERE food_id NOT IN (
    SELECT DISTINCT food_id
    FROM FoodOrderItem
);

-- 4. Users Who Made More Bookings Than the Average User

SELECT user_id, COUNT(booking_id) AS total_bookings
FROM Booking
GROUP BY user_id
HAVING COUNT(booking_id) > (
    SELECT AVG(total_bookings)
    FROM (
        SELECT COUNT(booking_id) AS total_bookings
        FROM Booking
        GROUP BY user_id
    ) AS sub
);

--Find Users Who Ordered the Most Expensive Food Item

SELECT u.user_id, b.booking_id, foi.food_id
FROM [Usertable] u
JOIN Booking b ON u.user_id = b.user_id
JOIN FoodOrder fo ON b.booking_id = fo.booking_id
JOIN FoodOrderItem foi ON fo.order_id = foi.order_id
JOIN FoodItemSize fis ON foi.size_id = fis.size_id
WHERE fis.rate = (
    SELECT MAX(rate)
    FROM FoodItemSize
);

--Delete Duplicates in a Table

SELECT user_id, COUNT(*)
FROM [Usertable]
GROUP BY user_id
HAVING COUNT(*) > 1;

--Users Who Gave Better Reviews Than Movie Avg Rating

SELECT r.review_id, r.user_id, r.movie_id, r.rating
FROM Review r
WHERE r.rating > (
    SELECT AVG(r2.rating)
    FROM Review r2
    WHERE r.movie_id = r2.movie_id
);

--Day 8 practice
CREATE TABLE Wallet (
    wallet_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT NOT NULL,
    balance DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES [Usertable](user_id)
);

INSERT INTO Wallet (user_id, balance)
VALUES 
(1, 1000.00),
(2, 200.00);

BEGIN TRANSACTION;

-- Debit Rs. 500 from User with user_id = 1
UPDATE Wallet
SET balance = balance - 500
WHERE user_id = 1 AND balance >= 500;

-- Credit Rs. 500 to User with user_id = 2
UPDATE Wallet
SET balance = balance + 500
WHERE user_id = 2;

-- ROLLBACK; -- Uncomment this to simulate an error
COMMIT;

BEGIN TRANSACTION;

-- Insert into the parent table (User)
INSERT INTO [Usertable] (user_id, name, email, phone)
VALUES (100, 'Alice Test', 'alice@example.com', '9999999999');

-- Insert into the child table (Booking), referencing user_id
INSERT INTO Booking (booking_id, user_id, screen_id, booking_datetime, total_cost)
VALUES (200, 100, 1, GETDATE(), 500);

COMMIT;

-- Attempt to violate consistency (invalid user_id)
INSERT INTO Booking (booking_id, user_id, screen_id, booking_datetime, total_cost)
VALUES (201, 999, 1, GETDATE(), 600);  -- 999 does not exist in User table

-- Transaction A
BEGIN TRANSACTION;
UPDATE Wallet SET balance = balance - 100 WHERE user_id = 1;

-- Transaction B (in a separate session)
SELECT balance FROM Wallet WHERE user_id = 1; 
-- Will not see the update from Transaction A if isolation level is set appropriately

-- Commit Transaction A
COMMIT;

BEGIN TRANSACTION;

-- Full ACID with Balance Transfer (Wallet Table)
-- Ensure sufficient balance
IF EXISTS (
    SELECT 1 FROM Wallet WHERE user_id = 1 AND balance >= 1000
)
BEGIN
    -- Debit
    UPDATE Wallet SET balance = balance - 1000 WHERE user_id = 1;

    -- Credit
    UPDATE Wallet SET balance = balance + 1000 WHERE user_id = 2;

    COMMIT;
END
ELSE
BEGIN
    ROLLBACK;
END

--day 9

-- 1NF Equivalent (From Usertable and simple attributes)
CREATE TABLE User_Subscriptions (
    user_id INT,
    subscription_type VARCHAR(50),
    PRIMARY KEY (user_id, subscription_type),
    FOREIGN KEY (user_id) REFERENCES Usertable(user_id)
);

-- 2NF: Splitting booking and items from a single structure
CREATE TABLE Bookings (
    booking_id INT PRIMARY KEY,
    user_id INT,
    booking_datetime DATETIME,
    FOREIGN KEY (user_id) REFERENCES Usertable(user_id)
);

CREATE TABLE Booking_Seats (
    booking_id INT,
    seat_id INT,
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id),
    FOREIGN KEY (seat_id) REFERENCES Seat(seat_id),
    PRIMARY KEY (booking_id, seat_id)
);

-- 3NF: Normalize screen and movie relationship
CREATE TABLE Screens_Normalized (
    screen_id INT PRIMARY KEY,
    name VARCHAR(100),
    capacity INT
);

CREATE TABLE Movies_Normalized (
    movie_id INT PRIMARY KEY,
    title VARCHAR(100),
    language VARCHAR(50),
    release_year INT
);