-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 02, 2025 at 01:19 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` date NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_number`, `msg`, `date`, `email`) VALUES
(1, '', '', '', '2025-07-30', ''),
(2, 'Shani Raj', '6299996489', 'hwljo;sj foasjs;fl aso', '2025-07-30', 'shaniraj4587@gmail.com'),
(3, 'Shani Raj', '6299996489', 'sdfasf sdadfas ', '2025-07-30', 'shsdfl;j@gqasi.com'),
(4, 'sdfas', '324382473', 'dsdfas; asdflasdjfli;as d', '2025-07-30', 'dfsasfas@dfsgfsdf'),
(24, 'Shani Raj', '06299996489', 'hii hello ji', '2025-07-30', 'test@shaniraj.net'),
(25, 'Shani Raj', '06299996489', 'fdgdsf ', '2025-07-30', 'shaniraj45897@gmail.com'),
(26, 'Shani Raj', '06299996489', 'fdgdsf ', '2025-07-30', 'shaniraj45897@gmail.com'),
(27, 'Shani Raj', '06299996489', 'hii hello hii ji', '2025-07-30', 'shaniraj4587@gmail.com'),
(28, 'Shani Raj', '06299996489', 'hi helo ji', '2025-07-30', 'test@shaniraj.net'),
(29, 'Shani Raj', '06299996489', 'hi helo ji', '2025-07-30', 'test@shaniraj.net'),
(30, 'Shani Raj', '06299996489', 'dfasd sdf ', '2025-07-30', 'test@shaniraj.net'),
(31, 'Shani Raj', '06299996489', 'dfasd sdf ', '2025-07-30', 'test@shaniraj.net'),
(32, 'Shani Raj', '06299996489', 'sdfasd ', '2025-07-30', 'test@shaniraj.net'),
(33, 'Shani Raj', '06299996489', 'sdfsad sdfas ', '2025-07-30', 'shaniraj4587@gmail.com'),
(34, 'Shani Raj', '06299996489', 'sdfsad sdfas ', '2025-07-30', 'shaniraj4587@gmail.com'),
(35, 'Shani Raj', '06299996489', 'sdfsad sdfas ', '2025-07-30', 'shaniraj4587@gmail.com'),
(36, 'Shani Raj', '06299996489', 'sdfsad sdfas ', '2025-07-30', 'shaniraj4587@gmail.com'),
(37, 'Shani Raj', '06299996489', 'njkkkhkjl  j', '2025-07-30', 'shaniraj4587@gmail.com'),
(38, 'Shani Raj', '06299996489', 'njkkkhkjl  j', '2025-07-30', 'shaniraj4587@gmail.com'),
(39, 'Shani Raj', '06299996489', 'fdsadas ', '2025-07-30', 'shaniraj4587@gmail.com'),
(40, 'Shani Raj', '06299996489', 'sdfas sadf asfasd asdfdf', '2025-07-30', 'shaniraj4587@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `date` date NOT NULL,
  `img_file` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `content`, `date`, `img_file`) VALUES
(1, 'THis is my first post', 'first-post', 'hello bhai log ye content hai mera kaisa hai batana thoda hamko bhi', '2025-07-31', 'post-bg.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
