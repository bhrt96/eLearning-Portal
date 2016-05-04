-- phpMyAdmin SQL Dump
-- version 4.5.0.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 04, 2016 at 09:49 AM
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
  `questionId` int(25) NOT NULL,
  `question` text NOT NULL,
  `answer` text NOT NULL,
  `optionA` text NOT NULL,
  `optionB` text NOT NULL,
  `optionC` text NOT NULL,
  `optionD` text NOT NULL,
  `subject` varchar(25) NOT NULL,
  `setBy` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `questionBank`
--

INSERT INTO `questionBank` (`questionId`, `question`, `answer`, `optionA`, `optionB`, `optionC`, `optionD`, `subject`, `setBy`) VALUES
(35, 'what is 2*2?', 'b', '2', '4', '6', '8', 'maths', 'si'),
(36, 'what is 5!?', 'b', '5', '120', '50', '720', 'maths', 'si'),
(37, '21^2 =', 'c', '221', '567', '441', '641', 'maths', 'si'),
(38, '(5+6)-4+2 =', 'a', '9', '8', '11', '7', 'maths', 'si'),
(39, '1/0 =', 'd', 'INF', '-INF', '0', 'Undefined', 'maths', 'si'),
(40, 'Ram ______ to swim.', 'b', 'like', 'likes', 'liking', 'none', 'English', 'steven'),
(42, 'Sun rises in east.', 'b', 'Present continuous tense', 'Present indefinite tense', 'Present perfect tense', 'Present perfect continuous tense', 'English', 'steven'),
(43, 'Antonym of good ?', 'a', 'bad', 'worse', 'worst', 'none', 'English', 'steven'),
(44, 'The pen is __ the table.', 'd', 'in', 'of', 'over', 'on', 'English', 'steven'),
(45, 'Shyam was _______ book.', 'c', 'read', 'reads', 'reading', 'write', 'English', 'steven');

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `StudentId` int(11) NOT NULL,
  `subject` varchar(25) NOT NULL,
  `marks` int(4) NOT NULL,
  `max_marks` int(4) NOT NULL,
  `percent` float NOT NULL,
  `result` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`StudentId`, `subject`, `marks`, `max_marks`, `percent`, `result`) VALUES
(1, 'po', -2, 8, -25, 'fail'),
(1, 'po', 1, 16, 6.25, 'fail'),
(1, 'po', 9, 24, 37.5, 'pass'),
(2, 'po', 3, 8, 37.5, 'pass'),
(2, 'maths', -3, 32, -9.375, 'fail'),
(2, 'maths', -3, 40, -7.5, 'fail'),
(2, 'maths', -3, 48, -6.25, 'fail'),
(2, 'maths', -3, 56, -5.35714, 'fail'),
(2, 'maths', -3, 64, -4.6875, 'fail'),
(2, 'maths', -3, 72, -4.16667, 'fail'),
(1, 'maths', -3, 40, -7.5, 'fail'),
(1, 'maths', 1, 48, 2.08333, 'fail'),
(1, 'maths', 5, 56, 8.92857, 'fail'),
(1, 'maths', 9, 64, 14.0625, 'fail'),
(1, 'maths', 13, 72, 18.0556, 'fail'),
(1, 'maths', 17, 80, 21.25, 'fail'),
(1, 'maths', 21, 88, 23.8636, 'fail'),
(1, 'maths', 25, 96, 26.0417, 'fail'),
(1, 'maths', 29, 104, 27.8846, 'fail'),
(1, 'maths', 33, 112, 29.4643, 'fail'),
(1, 'maths', 37, 120, 30.8333, 'fail'),
(1, 'maths', 41, 128, 32.0312, 'fail'),
(1, 'maths', 45, 136, 33.0882, 'pass'),
(2, 'maths', 0, 80, 0, 'fail'),
(4, 'maths', 11, 20, 55, 'pass'),
(4, 'maths', 22, 40, 55, 'pass'),
(4, 'maths', 33, 60, 55, 'pass'),
(5, 'maths', 10, 20, 50, 'pass'),
(5, 'English', 11, 20, 55, 'pass'),
(6, 'English', 20, 20, 100, 'pass'),
(1, 'English', 0, 20, 0, 'fail'),
(7, 'maths', 15, 20, 75, 'pass'),
(7, 'maths', 35, 40, 87.5, 'pass'),
(8, 'maths', 6, 20, 30, 'fail');

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE `session` (
  `sessionId` int(11) NOT NULL,
  `username` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `session`
--

INSERT INTO `session` (`sessionId`, `username`) VALUES
(79042, 'si'),
(132542, 'hari'),
(220743, 'ashu'),
(255543, 'abc'),
(275671, 'sam'),
(438253, 'steven'),
(501111, 'vipul'),
(580014, 'po'),
(624448, 'john'),
(625758, 'ps'),
(692319, 'bharat_n'),
(774365, 'Ramram');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `StudentId` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `college` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`StudentId`, `name`, `college`) VALUES
(1, 'Parshant', 'ps'),
(2, 'Puli', 'po'),
(3, 'bharat', 'aligarh uni'),
(4, 'ABC ABC', 'IITK'),
(5, 'Hari Prakash', 'iiita'),
(6, 'ashu', 'iiita'),
(7, 'Ram', 'iiita'),
(8, 'sam', 'iitk');

-- --------------------------------------------------------

--
-- Table structure for table `studentAnswer`
--

CREATE TABLE `studentAnswer` (
  `StudentId` int(11) NOT NULL,
  `questionId` int(25) NOT NULL,
  `answer` varchar(250) NOT NULL,
  `points` int(11) DEFAULT '-1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentAnswer`
--

INSERT INTO `studentAnswer` (`StudentId`, `questionId`, `answer`, `points`) VALUES
(3, 35, 'c', -1),
(3, 36, 'c', -1),
(3, 35, 'b', 4),
(3, 36, 'b', 4),
(3, 35, 'b', 4),
(3, 36, 'b', 4),
(1, 35, 'c', -1),
(1, 36, 'c', -1),
(1, 35, 'a', -1),
(1, 36, 'None', 0),
(1, 35, 'None', 0),
(1, 36, 'd', -1),
(1, 35, 'a', -1),
(1, 36, 'a', -1),
(2, 35, 'b', 4),
(2, 36, 'c', -1),
(2, 35, 'd', -1),
(2, 36, 'c', -1),
(2, 35, 'a', -1),
(2, 36, 'c', -1),
(2, 35, 'a', -1),
(2, 36, 'c', -1),
(2, 35, 'None', 0),
(2, 36, 'None', 0),
(2, 35, 'None', 0),
(2, 36, 'None', 0),
(2, 35, 'None', 0),
(2, 36, 'None', 0),
(2, 35, 'None', 0),
(2, 36, 'None', 0),
(2, 35, 'None', 0),
(2, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'c', -1),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(1, 35, 'b', 4),
(1, 36, 'None', 0),
(2, 35, 'b', 4),
(2, 36, 'c', -1),
(4, 35, 'b', 4),
(4, 36, 'c', -1),
(4, 37, 'c', 4),
(4, 38, 'None', 0),
(4, 39, 'd', 4),
(4, 35, 'b', 4),
(4, 36, 'c', -1),
(4, 37, 'c', 4),
(4, 38, 'None', 0),
(4, 39, 'd', 4),
(4, 35, 'b', 4),
(4, 36, 'c', -1),
(4, 37, 'c', 4),
(4, 38, 'None', 0),
(4, 39, 'd', 4),
(5, 35, 'b', 4),
(5, 36, 'b', 4),
(5, 37, 'c', 4),
(5, 38, 'b', -1),
(5, 39, 'c', -1),
(5, 40, 'b', 4),
(5, 42, 'c', -1),
(5, 43, 'None', 0),
(5, 44, 'd', 4),
(5, 45, 'c', 4),
(6, 40, 'b', 4),
(6, 42, 'a', 4),
(6, 43, 'a', 4),
(6, 44, 'd', 4),
(6, 45, 'c', 4),
(1, 40, 'None', 0),
(1, 42, 'None', 0),
(1, 43, 'None', 0),
(1, 44, 'None', 0),
(1, 45, 'None', 0),
(7, 35, 'b', 4),
(7, 36, 'b', 4),
(7, 37, 'c', 4),
(7, 38, 'a', 4),
(7, 39, 'a', -1),
(7, 35, 'b', 4),
(7, 36, 'b', 4),
(7, 37, 'c', 4),
(7, 38, 'a', 4),
(7, 39, 'd', 4),
(8, 35, 'b', 4),
(8, 36, 'b', 4),
(8, 37, 'b', -1),
(8, 38, 'b', -1),
(8, 39, 'None', 0);

-- --------------------------------------------------------

--
-- Table structure for table `studentRegister`
--

CREATE TABLE `studentRegister` (
  `StudentId` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentRegister`
--

INSERT INTO `studentRegister` (`StudentId`, `username`, `password`) VALUES
(4, 'abc', 'abc'),
(6, 'ashu', 'ashu'),
(3, 'bharat_n', 'password'),
(5, 'hari', 'hari'),
(2, 'po', 'po'),
(1, 'ps', 'ps'),
(7, 'Ramram', 'ram'),
(8, 'sam', 'sam');

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

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`TeacherId`, `name`, `subject`, `college`) VALUES
(1, 'parshant singh', 'daa', 'iiita'),
(62, 'vipul', 'science', 'vipul'),
(63, 'Prof. XYZ', 'maths', 'si'),
(64, 'john', 'dbms', 'iiita'),
(65, 'hari', 'VLSI', 'iiita'),
(66, 'Steven', 'English', 'Harvard University');

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
-- Dumping data for table `teacherRegister`
--

INSERT INTO `teacherRegister` (`TeacherId`, `username`, `password`) VALUES
(65, 'hari', 'hari'),
(64, 'john', 'john'),
(63, 'si', 'si'),
(66, 'steven', 'steven'),
(62, 'vipul', 'vipul');

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
-- Indexes for table `session`
--
ALTER TABLE `session`
  ADD PRIMARY KEY (`sessionId`);

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
-- AUTO_INCREMENT for table `questionBank`
--
ALTER TABLE `questionBank`
  MODIFY `questionId` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `StudentId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `TeacherId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
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
