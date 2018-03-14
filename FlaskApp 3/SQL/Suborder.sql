-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 2018-03-14 02:51:13
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
-- 表的结构 `Suborder`
--

CREATE TABLE `Suborder` (
  `suborder_id` varchar(10) NOT NULL,
  `order_id` varchar(10) NOT NULL,
  `food_id` varchar(10) NOT NULL,
  `order_amount` int(11) NOT NULL,
  `food_score` float NOT NULL,
  `sub_total_price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `Suborder`
--

INSERT INTO `Suborder` (`suborder_id`, `order_id`, `food_id`, `order_amount`, `food_score`, `sub_total_price`) VALUES
('1', '1', '1', 2, 5, 10),
('2', '1', '2', 1, 4, 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Suborder`
--
ALTER TABLE `Suborder`
  ADD PRIMARY KEY (`suborder_id`,`order_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
