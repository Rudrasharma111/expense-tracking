@echo off
docker exec -it expense-tracking-db-1 psql -U user -d expense_db %*
exit /b

#".\db.bat"

#".\db.bat -c 'SELECT * FROM expenses;'"
#".\db.bat -c ''"
#".\db.bat -c 'SELECT * FROM expenses ORDER BY amount DESC LIMIT 1;'"
#".\db.bat -c 'SELECT category, COUNT(*) FROM expenses GROUP BY category;'"
#".\db.bat -c "SELECT category, SUM(amount) FROM expenses WHERE category IN ('Food', 'Shopping') GROUP BY category;""