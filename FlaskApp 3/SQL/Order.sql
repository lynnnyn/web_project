-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 2018-03-14 02:51:00
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
-- 表的结构 `Order`
--

CREATE TABLE `Order` (
  `order_id` varchar(10) NOT NULL,
  `seller_id` varchar(10) NOT NULL,
  `buyer_id` varchar(10) NOT NULL,
  `address` varchar(3000) NOT NULL,
  `time` date NOT NULL,
  `sellers_score` float NOT NULL,
  `buyers_score` float NOT NULL,
  `total_price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `Order`
--

INSERT INTO `Order` (`order_id`, `seller_id`, `buyer_id`, `address`, `time`, `sellers_score`, `buyers_score`, `total_price`) VALUES
('1', '1', '2', 'champaign', '2018-03-01', 5, 5, 20),
('2', '1', '3', 'champaign', '2018-03-02', 5, 5, 30),
('3', '2', '3', 'champaign', '2018-03-02', 5, 5, 23),
('4', '4', '3', 'champaign', '2018-03-06', 5, 4, 33),
('5', '4', '6', 'champaign', '2018-03-09', 4, 4, 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Order`
--
ALTER TABLE `Order`
  ADD PRIMARY KEY (`order_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
