def calculate_diff(prev, curr):
    return {item: price - prev.get(item, 0) for item, price in curr.items()}


def group_by_department(employees):
    output_dict = {}

    for name, info in employees.items():
        if info["dept"] not in output_dict:
            output_dict[info["dept"]] = []

        output_dict[info["dept"]].append({
            "emp_name": name,
            "salary": info["salary"],
            "role": info["role"],
        })

    return output_dict
