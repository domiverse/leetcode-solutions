--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below
SELECT e.Name AS Employee
FROM Employee e JOIN Employee m ON e.ManagerId = m.Id # Thực hiện phép nối giữa hai bảng Employee (e và m) dựa trên ManagerId và Id
WHERE e.Salary > m.Salary; # Lọc các nhân viên có lương cao hơn lương của quản lý
-- @lc code=end

