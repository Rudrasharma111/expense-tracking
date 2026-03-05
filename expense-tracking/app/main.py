import os, csv, argparse, logging
from dotenv import load_dotenv
from models import ExpenseModel
from database import clear_old_data, save_expense_to_db, get_analytics
# import my database and model files



load_dotenv()
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"), format='%(message)s')

def ingest_data():
    clear_old_data()
    logging.info("Starting data ingestion...")
    
    # Read all csv files from folder
    for file_name in os.listdir("data"):
        if file_name.endswith(".csv"):
            file_path = os.path.join("data", file_name)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    try:
                        save_expense_to_db(ExpenseModel(**row))
                    except Exception as e:
                        logging.warning(f"Skipped bad row in {file_name}. Error: {e}")
                        
    logging.info("Success: All data saved!")

def show_analytics(month=None):
    # Get data from database
    total, cat_summary, month_summary = get_analytics(month)
    
    report_name = month.upper() if month else "ALL MONTHS"
    print(f"\n=== REPORT: {report_name} ===")
    
   
    print("\n1. CATEGORY BREAKDOWN:")
    print(f"   {'Category':<15} | {'Total (₹)':<12} | {'Avg (₹)':<12}")
    print("   " + "-" * 45)                                                 # print catgory table
    for row in cat_summary:
        print(f"   {row[0]:<15} | {float(row[1]):<12.2f} | {float(row[2]):<12.2f}")

    # Print monthly trend if no Month filter


    if not month:
        print("\n2. MONTHLY TREND:")
        print(f"   {'Month':<15} | {'Total (₹)':<12}")
        print("   " + "-" * 32)
        for row in month_summary:
            print(f"   {row[0]:<15} | {float(row[1]):<12.2f}")

    print(f"\n💰 FINAL TOTAL: ₹{float(total):.2f}\n")

if __name__ == "__main__":
                            # setup  comand line Tool
    parser = argparse.ArgumentParser(description="Expense Tracker")
    parser.add_argument("action", choices=["ingest", "analyze", "all"])
    parser.add_argument("--month", help="Filter by month (e.g., January)")
    args = parser.parse_args()

    
    if args.action in ["ingest", "all"]: 
        ingest_data()                                    # Run code Base on  user  command
    if args.action in ["analyze", "all"]: 
        show_analytics(args.month)