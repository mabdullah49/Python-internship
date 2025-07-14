import json

# Function to read and parse client requirements
def read_client_requirements(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    project, timeline, priority = '', '', ''
    features = []

    for line in lines:
        line = line.strip()
        if line.startswith('Project:'):
            project = line.split(':', 1)[1].strip()
        elif line.startswith('Features:'):
            continue
        elif line.startswith('-'):
            features.append(line[1:].strip())
        elif line.startswith('Timeline:'):
            timeline = line.split(':', 1)[1].strip()
        elif line.startswith('Priority:'):
            priority = line.split(':', 1)[1].strip()

    return {
        'Project': project,
        'Features': features,
        'Timeline': timeline,
        'Priority': priority
    }

# Function to print and write project summary
def write_project_summary(data, txt_output, json_output):
    summary = (
        "\n📘 Project Summary Report\n"
        "-------------------------\n"
        f"Project: {data['Project']}\n"
        f"Timeline: {data['Timeline']}\n"
        f"Priority: {data['Priority']}\n"
        "Features to Implement:\n"
    )

    for feature in data['Features']:
        summary += f" - {feature}\n"

    print(summary)

    with open(txt_output, 'w') as txt_file:
        txt_file.write(summary)

    # Export JSON with status
    features_with_status = {feature: 'pending' for feature in data['Features']}
    data['FeaturesWithStatus'] = features_with_status

    with open(json_output, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    requirements = read_client_requirements('client_requirements.txt')
    write_project_summary(requirements, 'project_summary.txt', 'project_summary.json')
