SELECT track,
       CASE
           WHEN o.finished THEN '2'
           WHEN o.cancelled THEN '-1'
           WHEN o."inDelivery" THEN '1'
ELSE '0'
       END AS status
FROM "Orders" o;