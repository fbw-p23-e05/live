import os

ROOT = os.getcwd()
DATA_ROOT = os.path.join(ROOT, 'src/data/initial')

def create_report():
    # create report directory under work directory
    try:
        os.mkdir(f"{DATA_ROOT}/work/reports")
    except FileExistsError:
        pass
    # open the 2 csv files for reading (jobs, customers)
    # open the file for writing (pending_jobs.csv)
    with open(f"{DATA_ROOT}/work/customers.csv", "r") as customer_file, \
            open(f"{DATA_ROOT}/work/jobs.csv", "r") as jobs_file, \
            open(f"{DATA_ROOT}/work/reports/pending_jobs.csv", "w") as report:
                
        # Read customers data into a list
        customers = []
        for line_number, customer in enumerate(customer_file):
            # We ignore the headers
            if line_number > 0:
                data = customer.split(",")
                customers.append(
                    {"id": data[0],
                     "name": data[1]})
                
                # id, name, _ = customer.split(",")
                # customers.append(
                #     {"id": id,
                #      "name": name})
        
        #TODO Build the report file
        # Create headers for file
        report.write("id,description,client\n")
        for line_number, job in enumerate(jobs_file):
            # Ignore the headers
            if line_number > 0:
                data = job.split(",")
                if data[3].strip("\n") != "done":
                    # get client names from customers if the id's match any of the pending jobs
                    # client_name = [customer["name"] for customer in customers if customer["id"] == data[1]]
                    client_name = ""
                    for customer in customers:
                        if customer["id"] == data[1]:
                            client_name = customer["name"]
                    job_desc = data[2]
                    report.write(f"{data[0]},{job_desc},{client_name}\n")

    
create_report()