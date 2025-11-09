SELECT 
    l.City,
    COUNT(b.Booking_ID) AS Total_Bookings,
    ROUND(AVG(r.Rating), 2) AS Average_Rating
FROM Bookings b
JOIN Locations l 
    ON b.Location_ID = l.Location_ID
JOIN Reviews r 
    ON b.Booking_ID = r.Booking_ID
GROUP BY l.City
HAVING 
    AVG(r.Rating) >= 4.0
    AND COUNT(b.Booking_ID) >= 10
ORDER BY Total_Bookings DESC;
