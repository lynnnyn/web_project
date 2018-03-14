-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 2018-03-14 02:50:52
-- 服务器版本： 10.0.33-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foooooodie_program`
--

-- --------------------------------------------------------

--
-- 表的结构 `Food`
--

CREATE TABLE `Food` (
  `food_id` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `area` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `maker_id` varchar(10) NOT NULL,
  `description` varchar(3000) NOT NULL,
  `available_amount` int(11) NOT NULL,
  `food_score` float NOT NULL,
  `category_id` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `Food`
--

INSERT INTO `Food` (`food_id`, `name`, `area`, `price`, `maker_id`, `description`, `available_amount`, `food_score`, `category_id`) VALUES
('1', 'coffee', 'champaign', 3, '1', 'great', 3, 5, 1),
('10', 'cake', 'champaign', 8, '9', 'ok', 8, 5, 3),
('2', 'coffee', 'champaign', 2, '2', 'great', 3, 5, 1),
('3', 'milktea', 'urbana', 4, '3', 'good', 4, 5, 1),
('4', 'milktea', 'champaign', 5, '5', 'ok', 2, 5, 1),
('5', 'milktea', 'champaign', 3, '5', 'ok', 2, 5, 1),
('6', 'bread', 'urbana', 5, '6', 'ok', 3, 5, 2),
('7', 'bread', 'champaign', 6, '7', 'ok', 4, 5, 2),
('8', 'bread', 'urbana', 8, '8', 'ok', 5, 5, 2),
('9', 'cake', 'champaign', 6, '8', 'ok', 5, 5, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Food`
--
ALTER TABLE `Food`
  ADD PRIMARY KEY (`food_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
