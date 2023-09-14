<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Write a function</h1>
    <p>An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.</p>
    <p>In the Gregorian calendar, three conditions are used to identify leap years:</p>
    <ol>
        <li>The year can be evenly divided by 4, is a leap year, unless:</li>
        <li>The year can be evenly divided by 100, it is NOT a leap year, unless:</li>
        <li>The year is also evenly divisible by 400. Then it is a leap year.</li>
    </ol>
  <p>This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are NOT leap years.</p>
    
<h2>Task</h2>
    <p>Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.</p>
    <p>Note that the code stub provided reads from STDIN and passes arguments to the <code>is_leap</code> function. It is only necessary to complete the <code>is_leap</code> function.</p>

<h3>Input Format</h3>
    <p>Read <strong>year</strong>, the year to test.</p>

<h3>Constraints</h3>
    <ul>
        <li>1900 &le; year &le; 10<sup>5</sup></li>
    </ul>

 <h3>Output Format</h3>
    <p>The function must return a Boolean value (True/False). Output is handled by the provided code stub.</p>
</body>
</html>