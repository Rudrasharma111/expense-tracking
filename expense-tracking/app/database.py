import psycopg2 , os ,time
from dotenv import load_dotenv

load_dotenv() #load passwords from env file

def execute_sql(query, parameters=(), fetch_data=False):
    for attempt in range(5) :
        try:
            connection = psycopg2.connect(
                host=os.getenv("DB_HOST", "db"), 
                dbname=os.getenv("POSTGRES_DB", "expense_db"),
                user=os.getenv("POSTGRES_USER", "user"), 
                password=os.getenv("POSTGRES_PASSWORD", "password")
            )
            
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            
            if fetch_data == True :  
                result = cursor.fetchall()
            else:
                connection.commit() 
                result = None
                
            connection.close()
            return result
            
        except Exception:
            time.sleep(2) 
            
    #stop program if conn fails
    raise Exception("Error: Could not connect to the database!")


def clear_old_data():
    execute_sql("DELETE FROM expenses") #clean table bfore adding csv

def save_expense_to_db(expense_item):
    sql_query = "INSERT INTO expenses (expense_date, category, amount, description) VALUES (%s, %s, %s, %s)"
    execute_sql(sql_query, (expense_item.expense_date, expense_item.category, expense_item.amount, expense_item.description))


def get_analytics(month_filter=None):
    
    #chek if user give month to filter
    if month_filter:
        where_condition = "WHERE TO_CHAR(expense_date, 'Month') ILIKE %s"
        query_parameters = (f"%{month_filter}%",)
    else:
        where_condition = ""
        query_parameters = ()

    result = execute_sql(f"SELECT SUM(amount) FROM expenses {where_condition}", query_parameters, fetch_data=True)
    total_spent = result[0][0] #get total spend
    
    if total_spent == None:
        total_spent = 0.0

    category_query = f"SELECT category, SUM(amount), AVG(amount) FROM expenses {where_condition} GROUP BY category ORDER BY SUM(amount) DESC"
    category_summary = execute_sql(category_query, query_parameters, fetch_data=True)

    trend_query = "SELECT TO_CHAR(expense_date, 'YYYY-MM'), SUM(amount) FROM expenses GROUP BY TO_CHAR(expense_date, 'YYYY-MM') ORDER BY TO_CHAR(expense_date, 'YYYY-MM') DESC"
    monthly_summary = execute_sql(trend_query, fetch_data=True)

    return total_spent, category_summary, monthly_summary
    # get total  avg per category
