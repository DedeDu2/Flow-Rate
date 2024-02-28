def calculate_traffic_flow_rate(avg_speed, road_capacity):
    return avg_speed * road_capacity

# Example usage:
avg_speed = 60
road_capacity = 100
flow_rate = calculate_traffic_flow_rate(avg_speed, road_capacity)
print("Traffic flow rate:", flow_rate)
