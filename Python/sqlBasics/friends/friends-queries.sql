SELECT CONCAT(users.first_name, ' ', users.last_name) AS friend_1,friendships.friend_1_id, friendships.friend_2_id, CONCAT(user2.first_name, ' ', user2.last_name) AS friend_2
FROM users
LEFT JOIN friendships ON users.id = friendships.friend_1_id
LEFT JOIN users AS user2 ON friendships.friend_2_id = user2.id;


-- Additional Exercise
-- Please also write the SQL queries needed to perform the following tasks:

-- Return all users who are friends with Kermit, make sure their names are displayed in results.


-- INCOMPLETE
-- SELECT CONCAT(users.first_name, ' ', users.last_name) as kermits_friends
-- FROM users
-- LEFT JOIN friendships ON users.id = friendships.friend_1_id
-- LEFT JOIN users AS user2 ON friendships.friend_2_id = user2.id;


-- Return the count of all friendships

-- SELECT COUNT(friendships.friend_1_id)
-- from friendships;

-- Find out who has the most friends and return the count of their friends.



-- Create a new user and make them friends with Eli Byers, Kermit The Frog, and Marky Mark



-- Return the friends of Eli in alphabetical order



-- Remove Marky Mark from Eli’s friends.



-- Return all friendships, displaying just the first and last name of both friends


