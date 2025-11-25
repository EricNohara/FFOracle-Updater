import urllib.request

BASE_URL = "https://fforacle-gegydpfvezf5axc5.centralus-01.azurewebsites.net/api"

def call_put(path):
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url, method="PUT")
    with urllib.request.urlopen(req) as res:
        return res.status
    
def call_post(path):
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url, method="POST")
    with urllib.request.urlopen(req) as res:
        return res.status


def lambda_handler(event, context):
    task = event.get("task")

    try:
        if task == "weekly":
            status = call_put("/AutoUpdate/weekly")
            return {"statusCode": status, "body": "Weekly update OK"}

        elif task == "daily":
            status = call_put("/AutoUpdate/daily")
            return {"statusCode": status, "body": "Daily update OK"}

        elif task == "increment":
            status = call_put("/AppState/increment")
            return {"statusCode": status, "body": "AppState increment OK"}
        
        elif task == "email-articles":
            status = call_post("/Espn/emailArticles")
            return {"statusCode": status, "body": "Email article sending OK"}

        else:
            return {"statusCode": 400, "body": f"Unknown task: {task}"}

    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
