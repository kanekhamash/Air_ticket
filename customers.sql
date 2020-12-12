-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2020 at 09:13 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `air_ticket28`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `from1` varchar(255) DEFAULT NULL,
  `destination` varchar(255) DEFAULT NULL,
  `date_fly` varchar(255) DEFAULT NULL,
  `time_fly` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `address`, `mobile`, `from1`, `destination`, `date_fly`, `time_fly`, `price`) VALUES
(1, 'James John', '234 abc Ave', '01234567', 'MAKKAH', 'JADAH', '12/02/2021', '03:45 AM', '1700'),
(2, 'Robert  Michael', '123 Green Ave', '02144567', 'AMMAN', 'CAIRO', '25/06/2021', '01:24 PM', '1450'),
(3, 'William David', '5673 Lemon Ave', '47328276', 'CASABLANCA', 'TUNISA', '04/11/2022', '07:25 AM', '350'),
(4, 'Richard Joseph', '63 Orange Ave', '98354672', 'MADINA', 'MAKKAH', '14/10/2021', '06:48 PM', '324'),
(12, 'Shereen Ahemd', '33 Lemon Ave', '65068453', 'London', 'New York', '02/22/2021', '05: 22 AM ', '1600'),
(13, 'Waleed Rami', '25 Orange Ave', '67685009', 'New Jersey', 'Rome', '22/04/2021', '04: 56 PM', '1300');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
