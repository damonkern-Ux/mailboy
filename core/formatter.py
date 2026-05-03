import json

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def response_formatter(response: dict) -> str:
    status = response["status"]
    status = response["status"]
    body = response["body"]
    response_time = response["response time"]
    total_time = response["total time"]

    status_color = GREEN if 200 <= status < 300 else RED

    output = []
    output.append(f"{status_color}STATUS: {status}{RESET}")
    output.append(f"{CYAN}TIME: {response_time:.4f}s{RESET}")
    output.append(f"{CYAN}TOTAL TIME: {total_time:.4f}s{RESET}")
    output.append(f"{YELLOW}BODY:{RESET}")
    
    if isinstance(body, dict) or isinstance(body, list): # checks if the body is a dict or list..
        output.append(json.dumps(body, indent=2))
    
    else:
        output.append(str(body))

    return "\n".join(output)