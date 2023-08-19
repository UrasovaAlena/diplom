SELECT c.login,
       count(o.id)
FROM "Couriers" c
INNER JOIN "Orders" o ON c.id=o."courierId"
WHERE o."inDelivery"=TRUE
GROUP BY c.login;