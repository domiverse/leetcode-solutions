--
-- @lc app=leetcode id=175 lang=mysql
--
-- [175] Combine Two Tables
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName, Address.City, Address.State # Chọn các cột cần thiết
FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId; # Thực hiện phép nối bên trái giữa hai bảng Person và Address dựa trên PersonId
-- @lc code=end

