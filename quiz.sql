-- phpMyAdmin SQL Dump
-- version 4.5.0.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 11, 2016 at 10:37 AM
-- Server version: 10.0.17-MariaDB
-- PHP Version: 5.6.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quiz`
--

-- --------------------------------------------------------

--
-- Table structure for table `studentAnswer`
--

CREATE TABLE `studentAnswer` (
  `StudentId` int(11) NOT NULL,
  `questionId` varchar(25) NOT NULL,
  `answer` varchar(250) NOT NULL,
  `points` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `studentAnswer`
--
ALTER TABLE `studentAnswer`
  ADD KEY `stuid` (`StudentId`),
  ADD KEY `queid` (`questionId`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `studentAnswer`
--
ALTER TABLE `studentAnswer`
  ADD CONSTRAINT `queid` FOREIGN KEY (`questionId`) REFERENCES `questionBank` (`questionId`),
  ADD CONSTRAINT `stuid` FOREIGN KEY (`StudentId`) REFERENCES `student` (`StudentId`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
