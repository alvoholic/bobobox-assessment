SELECT 
    g.Guest_Name,
    l.Location_Name,
    b.Booking_Date,
    (
        SELECT MAX(b2.Check_In_Date + b2.Duration)
        FROM Bookings b2
        WHERE b2.Guest_ID = b.Guest_ID
          AND (b2.Check_In_Date + b2.Duration) < b.Check_In_Date
    ) AS Previous_Check_Out_Date,
    b.Total_Price,
    r.Rating
FROM Bookings b
JOIN Guests g 
    ON b.Guest_ID = g.Guest_ID
JOIN Locations l 
    ON b.Location_ID = l.Location_ID
JOIN Reviews r 
    ON b.Booking_ID = r.Booking_ID
WHERE l.Type = 'Pod'
  AND r.Rating = 5
ORDER BY g.Guest_Name, b.Booking_Date;
