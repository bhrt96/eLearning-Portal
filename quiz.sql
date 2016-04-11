-- phpMyAdmin SQL Dump
-- version 4.5.0.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 11, 2016 at 10:40 AM
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
-- Table structure for table `questionBank`
--

CREATE TABLE `questionBank` (
  `questionId` varchar(25) NOT NULL,
  `question` text NOT NULL,
  `answer` text NOT NULL,
  `optionA` text NOT NULL,
  `optionB` text NOT NULL,
  `optionC` text NOT NULL,
  `optionD` text NOT NULL,
  `subject` varchar(25) NOT NULL,
  `setBy` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `StudentId` int(11) NOT NULL,
  `subject` varchar(25) NOT NULL,
  `marks` int(4) NOT NULL,
  `max marks` int(4) NOT NULL,
  `percent` float NOT NULL,
  `result` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `StudentId` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `subject` varchar(25) NOT NULL,
  `college` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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

-- --------------------------------------------------------

--
-- Table structure for table `studentRegister`
--

CREATE TABLE `studentRegister` (
  `StudentId` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `TeacherId` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `subject` varchar(25) NOT NULL,
  `college` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `teacherRegister`
--

CREATE TABLE `teacherRegister` (
  `TeacherId` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `questionBank`
--
ALTER TABLE `questionBank`
  ADD PRIMARY KEY (`questionId`);

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD KEY `stunid` (`StudentId`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`StudentId`);

--
-- Indexes for table `studentAnswer`
--
ALTER TABLE `studentAnswer`
  ADD KEY `stuid` (`StudentId`),
  ADD KEY `queid` (`questionId`);

--
-- Indexes for table `studentRegister`
--
ALTER TABLE `studentRegister`
  ADD PRIMARY KEY (`username`),
  ADD KEY `stu_id` (`StudentId`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`TeacherId`);

--
-- Indexes for table `teacherRegister`
--
ALTER TABLE `teacherRegister`
  ADD PRIMARY KEY (`username`),
  ADD KEY `tea_id` (`TeacherId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `StudentId` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `TeacherId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1001;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `result`
--
ALTER TABLE `result`
  ADD CONSTRAINT `stunid` FOREIGN KEY (`StudentId`) REFERENCES `student` (`StudentId`);

--
-- Constraints for table `studentAnswer`
--
ALTER TABLE `studentAnswer`
  ADD CONSTRAINT `queid` FOREIGN KEY (`questionId`) REFERENCES `questionBank` (`questionId`),
  ADD CONSTRAINT `stuid` FOREIGN KEY (`StudentId`) REFERENCES `student` (`StudentId`);

--
-- Constraints for table `studentRegister`
--
ALTER TABLE `studentRegister`
  ADD CONSTRAINT `stu_id` FOREIGN KEY (`StudentId`) REFERENCES `student` (`StudentId`);

--
-- Constraints for table `teacherRegister`
--
ALTER TABLE `teacherRegister`
  ADD CONSTRAINT `tea_id` FOREIGN KEY (`TeacherId`) REFERENCES `teacher` (`TeacherId`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
