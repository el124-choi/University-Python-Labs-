def process_data(val_int, data_list):  
	val_int += 10  
	data_list.append("PROCESSED")
	print(id(val_int))
	print(id(data_list))
	data_list = ["NEW", "LIST"]  
	data_list.append("END")
	print(id(data_list))
score = 50  
logs = ["START"] 

process_data(score, logs)  

print(f"{score=}")  
print(f"{logs=}")


robot_name = "waffle"
battery_level = 0.8425 # %
distance_travelled = 12450.8 # meters
error_code = 7

print(f"""
{"ROBOT TELEMETRY REPORT":=^40}
Robot Name : {robot_name.title()}
Battery : {battery_level:.1%}
Distance Travelled : {distance_travelled:,.2f} m
Status Code : [{error_code:0>5}]
{"=":=>40}
""")


print(f"""
current distance = {distance_travelled} 
is distance_travelled > 10000 = {distance_travelled > 10000}
""")

#question 5
readings = [12.4, -999.0, 15.8, -999.0, 22.1, 0.0, 18.6]

filtered_readings = [item for item in readings if item != -999.0]
conditional_reading = [i if i != -999.0 else None for i in readings]

print(filtered_readings)
print(conditional_reading)

sensors = ["lidar", "camera", "imu", "accelerometer"]

status_info = {"active": True, "ping_ms": 0} 

sensor_status = {i: status_info for i in sensors}

print(sensor_status)

#question 6

nodes = {  
101: {"name": "alpha", "battery": 92, "weight": 4.5},  
102: {"name": "beta", "battery": 74},  
103: {"name": "gamma", "battery": None, "weight": None},  
104: {"name": "delta", "battery": 31, "weight": 7.6},  
}

def calculate_average_weight(nodes):
        total = 0
        num = 0 
        for key in nodes.keys():
                d = nodes.get(key, 0)
                w = d.get("weight")
                if w != None:
                        print(w)
                        total += w
                        num += 1
        return total/num
                
print(calculate_average_weight(nodes))

#question 7

logs = [  
{"node": "alpha", "cpu_load": 0.45, "memory_mb": 512, "status": "OK"},  
{"node": "beta", "cpu_load": 0.88, "memory_mb": 1024, "status": "WARNING"},  
{"node": "gamma", "cpu_load": 0.12, "status": "OK"},  
{"node": "delta", "cpu_load": 0.95, "memory_mb": 2048, "status": "CRITICAL"},  
{"node": "epsilon", "status": "OFFLINE"},  
]

def extract_active_nodes(log_list):
        return [i for i in log_list if i.get("status") != "OFFLINE" ]

print(extract_active_nodes(logs))
print(len(logs))


def summarise_system_metrics(log_list):
        total_nodes = len(log_list)
        active_nodes = len(extract_active_nodes(log_list))

        total = 0
        num = 0
        for node in extract_active_nodes(log_list):
                c = node.get("cpu_load")
                if c != None:
                        total += c
                        num += 1
        avg_cpu = total / num

        total_memory = 0
        for node in log_list:
                m = node.get("memory_mb")
                if c != None:
                        total_memory += c
        
        
        summary_dict = {"total_nodes": total_nodes, "active_nodes": active_nodes, "avg_cpu": avg_cpu, "total_memory": total_memory}
        return summary_dict
def generate_report(summary):
        print(f"""
{"=":=>40}
SYSTEM METRICS SUMMARY
{"=":=>40}
Total Nodes Tracked : {summary.get("total_nodes")}
Active Nodes : {summary.get("active_nodes")}
Average CPU Load : {summary.get("avg_cpu"):.1%}
Total Memory Alloc. : {summary.get("total_memory"):,.2f} MB
{"=":=>40}
        """)

summary = summarise_system_metrics(logs)
print(summary)

generate_report(summary) 

