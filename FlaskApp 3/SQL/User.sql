-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 2018-03-14 02:51:20
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
-- 表的结构 `User`
--

CREATE TABLE `User` (
  `user_id` varchar(10) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `password_hash` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` int(1) NOT NULL,
  `selling_score` float NOT NULL,
  `purchasing_score` float NOT NULL,
  `zipcode` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `User`
--

INSERT INTO `User` (`user_id`, `user_name`, `password_hash`, `email`, `phone_number`, `address`, `gender`, `selling_score`, `purchasing_score`, `zipcode`) VALUES
('1', 'lynn', '123456', 'nyn88@163.com', '123456789', 'champaign', 1, 5, 5, '61820'),
('1234567890', 'hzong2', 'hahaha', 'hzong2@illinois.edu', '1234567890', 'urbana', 0, 0, 0, ''),
('2', 'amy', '1234567', 'amy@gmail.com', '234567890', 'champaign', 2, 4, 5, '61820'),
('3', 'lucy', '3456789', 'lucy@gmail.com', '2178190000', 'urbana', 1, 4.5, 4, '61821'),
('4', 'anna', '12345678', 'anna@gmail.com', '1111111111', 'champaign', 1, 5, 4, '61820'),
('5', 'bob', '123456', 'bob@gmail.com', '2222222222', 'urbana', 0, 0, 5, '61821'),
('6', 'six', '2222222', '666@gmail.com', '666666666', 'urbana', 1, 4.5, 5, '61821'),
('7', 'seven', '77777777', '777@gmail.com', '2345555555', 'urbana', 1, 4, 3, '61821'),
('8', 'mike', '123456', 'mike@163.com', '0000000000', 'champaign', 0, 4, 3, '61820'),
('9', 'aaaaa', '11111111', 'aaa@gmail.com', '233333333', 'urbana', 2, 4, 5, '61821');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
