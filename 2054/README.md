## 2054. Two Best Non-Overlapping Events

You are given a **0-indexed** 2D integer array of **events** where **events[i] = [startTime<sub>i</sub>, endTime<sub>i</sub>, value<sub>i,</sub>]**. The **i<sup>th</sup>** event starts at **startTime<sub>i</sub>** and ends at **endTime<sub>i</sub>**, and if you attend this event, you will receive a value of **value<sub>i</sub>**. You can choose **at most two non-overlapping** events to attend such that the sum of their values is **maximized**.

Return *this **maximum** sum*.

Note that the start time and end time is **inclusive**: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time **t**, the next event must start at or after **t + 1**.

https://leetcode.com/problems/two-best-non-overlapping-events